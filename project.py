import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game board
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check winner
def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Check draw
def check_draw():
    return all(board[r][c] != "" for r in range(3) for c in range(3))

# Player move
def player_move(r, c):
    if board[r][c] == "":
        board[r][c] = "X"
        buttons[r][c].config(text="X", fg="blue")
        if check_winner("X"):
            messagebox.showinfo("Game Over", "You win!")
            reset_game()
            return
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return
        root.after(300, ai_move)

# AI move
def ai_move():
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = "O"
        buttons[r][c].config(text="O", fg="red")
        if check_winner("O"):
            messagebox.showinfo("Game Over", "AI wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()

# Reset game
def reset_game():
    for r in range(3):
        for c in range(3):
            board[r][c] = ""
            buttons[r][c].config(text="")

# Create buttons
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial", 30), width=4, height=2,
                                  command=lambda r=r, c=c: player_move(r, c))
        buttons[r][c].grid(row=r, column=c)

# Restart button
tk.Button(root, text="Restart", font=("Arial", 14), bg="lightblue", command=reset_game).grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()