import GameList
import FriendList
import customtkinter as ctk
from GUI import create_login_page, login_button

#Create and load game array
user_game_list = GameList.initialize_game_list('GameList/games.txt')

#Create and load friend array
user_friend_list = FriendList.initialize_friend_list('FriendList/friends.txt')

# Create the login page
app, login_frame, username_textbox, status_dropdown = create_login_page()

# Create the login button
login_button(login_frame, username_textbox, status_dropdown, app, user_friend_list, user_game_list)

# Main Loop
app.mainloop()

#Debug print statements
for game in user_game_list:
    print(game)
for friend in user_friend_list:
    print(friend)

def calculate_achievement_score():
    total_achievements = 0

    for game in user_game_list:
        total_achievements += game.num_achievements
   
    print(f"Total Achievements: {total_achievements}")
    return total_achievements
calculate_achievement_score()

