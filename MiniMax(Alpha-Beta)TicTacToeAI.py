import cv2
import numpy as np
import time

# Initialize variables
win = 0
player = None
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
img = np.zeros((600, 600, 3), np.uint8)

def circle(x, y):
    cv2.circle(img, (x, y), 80, (0, 234, 255), 5)

def cross(x, y):
    cv2.line(img, (x - 57, y - 57), (x + 57, y + 57), (0, 234, 255), 5)
    cv2.line(img, (x - 57, y + 57), (x + 57, y - 57), (0, 234, 255), 5)

def position(value, x, y):
    if x < 200 and y < 200:
        draw_marker(value, 0, 0, 100, 100)
    elif x < 400 and y < 200:
        draw_marker(value, 0, 1, 300, 100)
    elif x < 600 and y < 200:
        draw_marker(value, 0, 2, 500, 100)
    elif x < 200 and y < 400:
        draw_marker(value, 1, 0, 100, 300)
    elif x < 400 and y < 400:
        draw_marker(value, 1, 1, 300, 300)
    elif x < 600 and y < 400:
        draw_marker(value, 1, 2, 500, 300)
    elif x < 200 and y < 600:
        draw_marker(value, 2, 0, 100, 500)
    elif x < 400 and y < 600:
        draw_marker(value, 2, 1, 300, 500)
    elif x < 600 and y < 600:
        draw_marker(value, 2, 2, 500, 500)

def draw_marker(value, i, j, cx, cy):
    if arr[i][j] == 0:
        arr[i][j] = value
        if value == 1:
            circle(cx, cy)
        elif value == 2:
            cross(cx, cy)
        global win
        win = checkwin()

def checkwin():
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != 0:  # Rows
            return arr[i][0]
        if arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != 0:  # Columns
            return arr[0][i]
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != 0:  # Diagonal
        return arr[0][0]
    if arr[2][0] == arr[1][1] == arr[0][2] and arr[2][0] != 0:  # Anti-diagonal
        return arr[2][0]
    if all(cell != 0 for row in arr for cell in row):
        return 3  # Draw
    return 0

def minimax(board, depth, is_maximizing):
    winner = checkwin()
    if winner == 1:
        return -1
    elif winner == 2:
        return 1
    elif winner == 3:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    score = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    score = minimax(board, depth + 1, True)
                    board[i][j] = 0
                    best_score = min(best_score, score)
        return best_score

def computer_move():
    global player
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                arr[i][j] = 2
                score = minimax(arr, 0, False)
                arr[i][j] = 0
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        time.sleep(0.2)
        position(2, move[1] * 200 + 100, move[0] * 200 + 100)
    player = 1

def callback(event, x, y, flags, param):
    global player
    if win == 0:
        if event == cv2.EVENT_LBUTTONDOWN:
            # Handle button clicks
            if 10 < x < 190 and 10 < y < 60:  # Human First
                reset_board()
                player = 1
            elif 210 < x < 390 and 10 < y < 60:  # AI First
                reset_board()
                player = 2
                computer_move()
            elif 410 < x < 590 and 10 < y < 60:  # Quit
                cv2.destroyAllWindows()
                exit()
            # Handle player move
            elif player == 1:
                position(1, x, y)
                player = 2

def reset_board():
    global arr, img, win
    arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    img[:] = 0
    draw_grid()
    draw_buttons()
    win = 0

def draw_grid():
    for i in range(1, 3):
        cv2.line(img, (200 * i, 0), (200 * i, 600), (255, 255, 255), 2)
        cv2.line(img, (0, 200 * i), (600, 200 * i), (255, 255, 255), 2)

def draw_buttons():
    cv2.rectangle(img, (10, 3), (190, 30), (0, 255, 0), -1)
    cv2.rectangle(img, (210, 3), (390, 30), (0, 255, 0), -1)
    cv2.rectangle(img, (410, 3), (590, 30), (0, 0, 255), -1)
    cv2.putText(img, "Human First", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(img, "AI First", (220, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(img, "Quit", (450, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

cv2.namedWindow("Tic-Tac-Toe")
cv2.setMouseCallback("Tic-Tac-Toe", callback)

# Draw initial grid and buttons
draw_grid()
draw_buttons()

def draw_winning_line():
    """Draws a red line on the winning path."""
    global win
    if win == 1 or win == 2:
        for i in range(3):
            # Check rows
            if arr[i][0] == arr[i][1] == arr[i][2] != 0:
                cv2.line(img, (0, i * 200 + 100), (600, i * 200 + 100), (0, 0, 255), 2)
                return
            # Check columns
            if arr[0][i] == arr[1][i] == arr[2][i] != 0:
                cv2.line(img, (i * 200 + 100, 0), (i * 200 + 100, 600), (0, 0, 255), 2)
                return
        # Check diagonals
        if arr[0][0] == arr[1][1] == arr[2][2] != 0:
            cv2.line(img, (0, 0), (600, 600), (0, 0, 255), 2)
            return
        if arr[0][2] == arr[1][1] == arr[2][0] != 0:
            cv2.line(img, (600, 0), (0, 600), (0, 0, 255), 2)
            return
    win = 0

while True:
    cv2.imshow("Tic-Tac-Toe", img)
    if win != 0:
        if win == 3:
            print("It's a draw! Press R to continue")
        elif win == 2:
            draw_winning_line() 
            print("AI Wins! Press R to continue")
        else:
            print("Player Wins!")

        cv2.imshow("Tic-Tac-Toe", img)
        cv2.waitKey(1)  # Ensure the UI updates immediately
        time.sleep(3)
    elif player == 2 and win == 0:
        computer_move()

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key != -1:
        if player == 1 or player == 2:
            reset_board()
    elif key == ord('r'):
        reset_board()

cv2.destroyAllWindows()
