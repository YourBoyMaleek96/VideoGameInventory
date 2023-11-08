import tkinter as tk
import GameListCheng
import FriendListCheng

# Create and load game array
user_game_list = GameListCheng.initialize_game_list('GameList/games.txt')

# Create and load friend array
user_friend_list = FriendListCheng.initialize_friend_list('FriendList/friends.txt')
