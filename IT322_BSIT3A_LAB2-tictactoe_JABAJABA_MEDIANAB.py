import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        """ Initializes the Tic-Tac-Toe game with an improved UI. """
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.board = [None] * 9
        self.is_x_next = True
        self.buttons = []
        self.score = {"X": 0, "O": 0}

        self.create_board()
    
    def create_board(self):
        """ Creates a stylish, responsive game board with UI improvements. """
        self.root.configure(bg="#2c3e50")  # Dark background

        # Grid buttons
        frame = tk.Frame(self.root, bg="#34495e")  # Dark grey frame
        frame.pack(pady=20)

        for i in range(9):
            btn = tk.Button(frame, text="", font=("Helvetica", 24, "bold"), height=2, width=5,
                            bg="#7f8c8d", fg="white", relief="raised", bd=5,
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            btn.bind("<Enter>", lambda event, btn=btn: btn.config(bg="#95a5a6"))  # Hover effect
            btn.bind("<Leave>", lambda event, btn=btn: btn.config(bg="#7f8c8d"))  # Reset hover effect
            self.buttons.append(btn)

        # Game Status Label
        self.status_label = tk.Label(self.root, text="Next Turn: X", font=("Helvetica", 16, "bold"),
                                     fg="white", bg="#2c3e50")
        self.status_label.pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(self.root, text=f"Score - X: {self.score['X']} | O: {self.score['O']}",
                                    font=("Helvetica", 14, "bold"), fg="white", bg="#2c3e50")
        self.score_label.pack(pady=5)

        # Reset Button
        reset_btn = tk.Button(self.root, text="Reset Game", font=("Helvetica", 14, "bold"),
                              bg="#e74c3c", fg="white", padx=10, pady=5, command=self.reset_game)
        reset_btn.pack(pady=10)

    def handle_click(self, index):
        """ Handles a player's move and updates the UI accordingly. """
        if self.board[index] or self.check_winner():
            return
        
        self.board[index] = "X" if self.is_x_next else "O"
        self.buttons[index].config(text=self.board[index], fg="#e74c3c" if self.board[index] == "X" else "#3498db")
        self.is_x_next = not self.is_x_next

        winner = self.check_winner()
        if winner:
            self.score[winner] += 1
            self.status_label.config(text=f"Winner: {winner}")
            self.score_label.config(text=f"Score - X: {self.score['X']} | O: {self.score['O']}")
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        elif None not in self.board:
            self.status_label.config(text="Draw")
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            self.status_label.config(text=f"Next Turn: {'X' if self.is_x_next else 'O'}")

    def check_winner(self):
        """ Checks for a winner and returns 'X' or 'O' if found. """
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]
        ]
        for a, b, c in lines:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None
    
   

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()