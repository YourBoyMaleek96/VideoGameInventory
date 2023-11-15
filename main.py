from GameList import initialize_game_list, calculate_achievement_score
from FriendList import initialize_friend_list
from GUI import create_login_page, login_button

#Create and load game array
user_game_list = initialize_game_list('GameList/games.txt')
achievement_score = calculate_achievement_score(user_game_list)
#Create and load friend array
user_friend_list = initialize_friend_list('FriendList/friends.txt')

# Create the login page
app, login_frame, username_textbox, status_dropdown = create_login_page()

# Create the login button
login_button(login_frame, username_textbox, status_dropdown, app, user_friend_list, user_game_list, achievement_score)

# Main Loop
app.mainloop()


