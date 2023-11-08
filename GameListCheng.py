import tkinter as tk
from tkinter import ttk

#Creates the class "Game"
class Game:
    #Initializes members of game object
    def __init__(self, game_title, hours_played, num_achievements):
        self.game_title = game_title
        self.hours_played = hours_played
        self.num_achievements = num_achievements

    def __str__(self):
        return (f"Game Title: {self.game_title}\n Hours Played: {self.hours_played}\n Number of Achievements: {self.num_achievements}\n")

#Method that fills the global games list array with the data from games.txt
def initialize_game_list(file_path):
    game_list = []
    with open(file_path, 'r') as file:
        for line in file:
            game_data = line.strip().split(',')
            if len(game_data) == 3:
                title = game_data[0].strip()
                hours = int(game_data[1].strip())
                achievements = int(game_data[2].strip())

                game = Game(title, hours, achievements)
                game_list.append(game)
    
    return game_list

def update_game_list_textbox():
    file_path = 'GameList/games.txt'
    game_list = initialize_game_list(file_path)
    text_box.delete(1.0, tk.END)
    for game in game_list:
        text_box.insert(tk.END, str(game) + '\n')

# Create a GUI for the Game List
app = tk.Tk()
app.title("Game List")

# Created a Button in order to Show the Game List on GameList/games.txt
display_button = tk.Button(app, text="Update Game List", command=update_game_list_textbox)
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