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
    
    # Create the friend menu and banner
    friend_menu_frame = ctk.CTkFrame(MainPage, border_width=3, border_color=BLUE)
    friend_banner = ctk.CTkLabel(friend_menu_frame, text="Friends")
    friend_banner.pack()  # Place the friend_banner inside the frame
    friend_menu_frame.place(relx=0.3, rely=0.5, anchor="center")

    # Create the game menu and banner
    game_menu_frame = ctk.CTkFrame(MainPage, border_width=3, border_color=BLUE)
    game_banner = ctk.CTkLabel(game_menu_frame, text="Games")
    game_banner.pack()  # Place the game_banner inside the frame
    game_menu_frame.place(relx=0.7, rely=0.5, anchor="center")

    # Create and place your textboxes (friend_menu and game_menu) here
    friend_menu = ctk.CTkTextbox(MainPage, border_width=3, border_color=BLUE)
    friend_menu.place(relx=0.3, rely=0.6, anchor="center", relwidth=0.2, relheight=0.4) 
    friends = initialize_friend_list("FriendList/friends.txt")
    display_friend_list(friend_menu, friends)

    game_menu = ctk.CTkTextbox(MainPage, border_width=3, border_color=BLUE)
    game_menu.place(relx=0.7, rely=0.6, anchor="center", relwidth=0.2, relheight=0.4)  
    games = initialize_game_list("GameList/games.txt")
    display_game_list(game_menu, games)
    
    app.withdraw()
  
def create_username_banner(parent, username, status, total_achievements):
    """Create the username banner with the given username, status, and total_achievements."""
    UsernameBanner = ctk.CTkLabel(parent, text=f"{username} | Achievement Score: {total_achievements} | Status: {status}")
    UsernameBanner.pack(fill="x")

def display_friend_list(parent, friend_list, font_size=12):
    """This function will print out the Friend List on the Main GUI"""
    for friend in friend_list:
        parent.insert(END, str(friend) + "\n")

def display_game_list(parent, game_list, font_size=12):
    """This function will print out the Game List on the Main GUI"""
    for game in game_list:
        parent.insert(END, str(game) + "\n")

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





