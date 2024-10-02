import tkinter as tk
from tkinter import messagebox
import random

class TrikiGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Trikki Game")
        self.window.geometry("300x300")
        self.player_vs_player = False
        self.current_player = "X"
        self.board = [" "] * 9
        self.create_widgets()

    def create_widgets(self):
        self.mode_label = tk.Label(self.window, text="Seleccione el modo de juego:")
        self.mode_label.pack()

        self.mode_buttons_frame = tk.Frame(self.window)
        self.mode_buttons_frame.pack()

        self.pvp_button = tk.Button(self.mode_buttons_frame, text="Jugador vs Jugador", command=self.set_pvp_mode)
        self.pvp_button.pack(side=tk.LEFT)

        self.pvm_button = tk.Button(self.mode_buttons_frame, text="Jugador vs Máquina", command=self.set_pvm_mode)
        self.pvm_button.pack(side=tk.LEFT)

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.board_frame, text="", command=lambda i=i: self.click(i), height=3, width=6)
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def set_pvp_mode(self):
        self.player_vs_player = True
        self.start_game()

    def set_pvm_mode(self):
        self.player_vs_player = False
        self.start_game()

    def start_game(self):
        self.mode_label.pack_forget()
        self.mode_buttons_frame.pack_forget()
        self.board_frame.pack()

    def click(self, i):
        if self.board[i] == " ":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                self.game_over()
            elif self.player_vs_player:
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                self.computer_move()

    def computer_move(self):
        possible_moves = [i for i, x in enumerate(self.board) if x == " "]
        move = random.choice(possible_moves)
        self.board[move] = "O"
        self.buttons[move].config(text="O")
        if self.check_winner():
            self.game_over()

    def check_winner(self):
        winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]
        if " " not in self.board:
            return "Empate"
        return False

    def game_over(self):
        winner = self.check_winner()
        if winner == "Empate":
            messagebox.showinfo("Resultado", "Es un empate!")
        else:
            messagebox.showinfo("Resultado", "El ganador es el jugador " + winner + "!")
        self.window.quit()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TrikiGame()
    game.run()