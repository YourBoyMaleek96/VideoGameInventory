import tkinter as tk
from tkinter import ttk
class Game:
    def __init__(self, game_title, hours_played, num_achievements):
        self.game_title = game_title
        self.hours_played = hours_played
        self.num_achievements = num_achievements

    def __str__(self):
        return (f"Game Title: {self.game_title}\n Hours Played: {self.hours_played}\n Number of Achievements: {self.num_achievements}")

def load_game_data(file_path):

    game_list = []

    with open('GameList/games.txt', 'r') as file:
        for line in file:
            game_data = line.strip().split(',')
            if len(game_data) == 3:
                title = game_data[0].strip()
                hours = int(game_data[1].strip())
                achievements = int(game_data[2].strip())

                game = Game(title, hours, achievements)
                game_list.append(game)
    return game_list

def display_game_list():
    game_list = load_game_data('GameList/games.txt')
    text_box.delete(1.0, tk.END)
    for game in game_list:
        text_box.insert(tk.END, str(game) + '\n\n')

# Create a GUI for the Window List
app = tk.Tk()
app.title("Game List")

# Created a Button in order to Show the Game List on GameList/games.txt
display_button = tk.Button(app, text = "Update Game List", command = display_game_list)
display_button.pack()

# Creating a scroll bar to look through the game list
scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

# Create a text box to display the game list with a scrollbar
text_box = tk.Text(app, width=60, height=20, yscrollcommand = scrollbar.set)
text_box.pack()

scrollbar.config(command=text_box.yview)

# Run the GUI (Temporary)
app.mainloop()