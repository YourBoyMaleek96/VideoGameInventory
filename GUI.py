import customtkinter as ctk
from tkinter import * 
from main import calculate_achievement_score
from FriendList import initialize_friend_list
from GameList import initialize_game_list

#Constant for color theme
BLUE = "#1f6aa5"

def create_banner_frame(parent, username, status,total_achievements):
    """Create the banner frame with the given username and status."""
    BannerFrame = ctk.CTkFrame(parent, border_width=2, fg_color=BLUE)
    BannerFrame.pack(side="top", fill="x", padx=10, pady=10)
    create_username_banner(BannerFrame, username, status, total_achievements)

def create_main_page(username, status,total_achievements, friend_list, game_list):
    """Create the main screen after the user has logged in"""
    MainPage = ctk.CTkToplevel(app)
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    MainPage.geometry(f"{width}x{height}")
    MainPage.title(" Video Game Profile")
    create_banner_frame(MainPage, username, status,total_achievements)
    
    display_friend_list(MainPage, friend_list, font_size=12)
    display_game_list(MainPage,game_list, font_size=12)
    
    app.withdraw()

def create_username_banner(parent, username, status, total_achievements):
    """Create the username banner with the given username, status, and total_achievements."""
    UsernameBanner = ctk.CTkLabel(parent, text=f"{username} | Achievement Score: {total_achievements} | Status: {status}")
    UsernameBanner.pack(fill="x")

def display_friend_list(parent, friend_list, font_size=12):
    """This function will print out the Friend List on the Main GUI
    """
    friend_frame = ctk.CTkFrame(parent)
    friend_frame.pack(side="left", padx=10, pady=10)

    for friend in friend_list:
        friend_label = ctk.CTkLabel(friend_frame, text=str(friend), height=10, width=30)
        friend_label.pack()

def display_game_list(parent, game_list, font_size=12):
    """This function will print out the Game List on the Main GUI 
    """
    game_frame = ctk.CTkFrame(parent)
    game_frame.pack(side="right", padx=10, pady=10)

    for game in game_list:
        game_label = ctk.CTkLabel(game_frame, text=str(game), height=10, width=30)
        game_label.pack()

def login():
    """This function explains what happens after you press Login.
       It takes in a username and online status and displays it to the screen.
    """
    status = OnlineDrop.get()

    if status in ["Online", "Offline", "Busy"]:
        username = UsernameTextbox.get()
        total_achievements = calculate_achievement_score()

        friend_list = initialize_friend_list("FriendList/friends.txt")
        game_list = initialize_game_list("GameList/games.txt")

        create_main_page(username, status, total_achievements, friend_list, game_list)


" Creates the login window that displays login button and online status dropdown"
app = ctk.CTk() #main window for gui 
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}")
app.title("Video Game Profile")
ctk.set_appearance_mode("Dark") #Set theme to dark mode 
ctk.set_default_color_theme("blue")
frame = ctk.CTkFrame(master = app)
frame._set_appearance_mode("Dark")
frame.pack(pady=20,padx=40,fill = 'both' ,expand = True)
label = ctk.CTkLabel(master=frame, text = 'Login Page')
label.pack(pady = 12, padx=10)
UsernameTextbox = ctk.CTkEntry(master =frame, placeholder_text = "Enter Username")
UsernameTextbox.pack(pady = 12, padx = 10)

#Drop down for online status 
OnlineDrop = ctk.CTkComboBox(master=frame, values = ["Online", "Offline", "Busy"])
OnlineDrop.pack(pady = 12, padx = 10)


#Login Button
LoginButton = ctk.CTkButton(master=frame, text="Login", command= login)
LoginButton.pack(pady=12, padx=10)



app.mainloop() #end gui window 





