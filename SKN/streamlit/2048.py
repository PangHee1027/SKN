import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Streamlit 2048", page_icon="🎮", layout="centered")


# 게임 로직 함수들
def init_game():
  board = [[0] * 4 for _ in range(4)]
  st.session_state.score = 0
  st.session_state.game_over = False
  st.session_state.won = False
  add_new_tile(board)
  add_new_tile(board)
  return board


def add_new_tile(board):
  empty_cells = [
      (r, c) for r in range(4) for c in range(4) if board[r][c] == 0
  ]
  if empty_cells:
    r, c = random.choice(empty_cells)
    board[r][c] = 4 if random.random() < 0.1 else 2


def compress(row):
  new_row = [i for i in row if i != 0]
  new_row += [0] * (4 - len(new_row))
  return new_row


def merge(row):
  score_added = 0
  for i in range(3):
    if row[i] != 0 and row[i] == row[i + 1]:
      row[i] *= 2
      row[i + 1] = 0
      score_added += row[i]
  return row, score_added


def move_left(board):
  new_board = []
  total_score = 0
  changed = False
  for row in board:
    compressed = compress(row)
    merged, score = merge(compressed)
    final_row = compress(merged)
    if final_row != row:
      changed = True
    new_board.append(final_row)
    total_score += score
  return new_board, total_score, changed


def reverse(board):
  return [row[::-1] for row in board]


def transpose(board):
  return [list(row) for row in zip(*board)]


def move_right(board):
  rev = reverse(board)
  moved, score, changed = move_left(rev)
  return reverse(moved), score, changed


def move_up(board):
  trans = transpose(board)
  moved, score, changed = move_left(trans)
  return transpose(moved), score, changed


def move_down(board):
  trans = transpose(board)
  moved, score, changed = move_right(trans)
  return transpose(moved), score, changed


def check_game_over(board):
  # 빈 칸이 있으면 게임 오버 아님
  for r in range(4):
    for c in range(4):
      if board[r][c] == 0:
        return False
      if c < 3 and board[r][c] == board[r][c + 1]:
        return False
      if r < 3 and board[r][c] == board[r + 1][c]:
        return False
  return True


# 세션 상태 초기화
if "board" not in st.session_state:
  st.session_state.board = init_game()
if "score" not in st.session_state:
  st.session_state.score = 0
if "high_score" not in st.session_state:
  st.session_state.high_score = 0
if "game_over" not in st.session_state:
  st.session_state.game_over = False
if "won" not in st.session_state:
  st.session_state.won = False

# UI 스타일 설정 (타일 색상 및 디자인)
st.markdown(
    """
<style>
.tile {
    display: flex;
    align-items: center;
    justify-content: center;
    aspect-ratio: 1 / 1; 
    font-weight: bold;
    border-radius: 8px;
    margin: 4px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}

/* 반응형 폰트 크기 */
.tile { font-size: 3.5vw; } 
.tile-128, .tile-256, .tile-512 { font-size: 3vw; }
.tile-1024, .tile-2048 { font-size: 2.5vw; }
.tile-super { font-size: 2vw; }

@media (max-width: 600px) {
    .tile { font-size: 26px; }
    .tile-128, .tile-256, .tile-512 { font-size: 22px; }
    .tile-1024, .tile-2048 { font-size: 18px; }
    .tile-super { font-size: 14px; }
}

/* 타일 색상 */
.tile-0 { background-color: #cdc1b4; color: #cdc1b4; }
.tile-2 { background-color: #eee4da; color: #776e65; }
.tile-4 { background-color: #ede0c8; color: #776e65; }
.tile-8 { background-color: #f2b179; color: #f9f6f2; }
.tile-16 { background-color: #f59563; color: #f9f6f2; }
.tile-32 { background-color: #f67c5f; color: #f9f6f2; }
.tile-64 { background-color: #f65e3b; color: #f9f6f2; }
.tile-128 { background-color: #edcf72; color: #f9f6f2; }
.tile-256 { background-color: #edcc61; color: #f9f6f2; }
.tile-512 { background-color: #edc850; color: #f9f6f2; }
.tile-1024 { background-color: #edc53f; color: #f9f6f2; }
.tile-2048 { background-color: #edc22e; color: #f9f6f2; }
.tile-super { background-color: #3c3a32; color: #f9f6f2; }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🎮 Streamlit 2048")
st.markdown("버튼을 눌러 타일을 움직이고 **2048**을 만드세요!")

# 점수판 표시
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label="현재 점수", value=st.session_state.score)
with col2:
  if st.session_state.score > st.session_state.high_score:
    st.session_state.high_score = st.session_state.score
  st.metric(label="최고 점수", value=st.session_state.high_score)
with col3:
  if st.button("🔄새 게임"):
    st.session_state.board = init_game()
    st.rerun()

st.write("---")


# 보드판 렌더링 함수
def render_board(board):
  for r in range(4):
    cols = st.columns(4)
    for c in range(4):
      val = board[r][c]
      val_str = str(val) if val != 0 else ""
      tile_class = f"tile-{val}" if val <= 2048 else "tile-super"
      cols[c].markdown(
          f'<div class="tile {tile_class}">{val_str}</div>',
          unsafe_allow_html=True,
      )


render_board(st.session_state.board)

# 게임 상태 확인
if not st.session_state.won:
  for row in st.session_state.board:
    if 2048 in row:
      st.session_state.won = True
      break

if st.session_state.won:
  st.success("🎉 축하합니다! 2048을 달성하셨습니다! 계속 플레이할 수 있습니다.")

if check_game_over(st.session_state.board):
  st.session_state.game_over = True
  st.error("게임 오버! 더 이상 움직일 수 없습니다. '새 게임'을 눌러주세요.")


# 이동 처리 함수
def handle_move(direction):
  if st.session_state.game_over:
    return

  board = st.session_state.board
  if direction == "left":
    new_board, score_added, changed = move_left(board)
  elif direction == "right":
    new_board, score_added, changed = move_right(board)
  elif direction == "up":
    new_board, score_added, changed = move_up(board)
  elif direction == "down":
    new_board, score_added, changed = move_down(board)

  if changed:
    st.session_state.board = new_board
    st.session_state.score += score_added
    add_new_tile(st.session_state.board)
    st.rerun()


# 조작 버튼 UI 배치
st.write("")
col_left, col_mid, col_right = st.columns([1, 1, 1])

with col_mid:
  if st.button("⬆️ 위", use_container_width=True):
    handle_move("up")

col_l, col_d, col_r = st.columns(3)
with col_l:
  if st.button("⬅️ 왼쪽", use_container_width=True):
    handle_move("left")
with col_d:
  if st.button("⬇️ 아래", use_container_width=True):
    handle_move("down")
with col_r:
  if st.button("➡️ 오른쪽", use_container_width=True):
    handle_move("right")