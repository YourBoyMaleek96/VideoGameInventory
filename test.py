import tkinter as tk
from tkinter import ttk

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