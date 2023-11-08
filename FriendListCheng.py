import tkinter as tk
from tkinter import ttk

#Creates the class "Friend"
class Friend:
    #Initializes members of friend object
    def __init__(self, user_name, real_name, last_online):
        self.user_name = user_name
        self.real_name = real_name
        self.last_online = last_online

    def __str__(self):
        return (f"Username: {self.user_name}\n Name: {self.real_name}\n Last Online: {self.last_online} hours\n")

#method that fills the global friend list array with the data from friends.txt
def initialize_friend_list(file_path):
    friend_list = []
    with open(file_path, 'r') as file:
        for line in file:
            friend_data = line.strip().split(',')
            if len(friend_data) == 3:
                userName = friend_data[0].strip()
                realName = friend_data[1].strip()
                lastOnline = int(friend_data[2].strip())

                friend = Friend(userName, realName, lastOnline)
                friend_list.append(friend)

    return friend_list

def update_friend_list_textbox():
    file_path = 'FriendList/friends.txt'
    friend_list = initialize_friend_list(file_path)
    text_box.delete(1.0, tk.END)
    for friend in friend_list:
        text_box.insert(tk.END, str(friend) + '\n')

# Create a GUI for the Game List
app = tk.Tk()
app.title("Friend List")

# Created a Button in order to Show the Game List on GameList/games.txt
display_button = tk.Button(app, text="Update Friend List", command=update_friend_list_textbox)
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