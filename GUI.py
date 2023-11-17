import customtkinter as ctk
from tkinter import *
from GameList import calculate_achievement_score, Game

#Constant for color theme
BLUE = "#1f6aa5"
DARK = "gray14"

def create_banner_frame(parent):
    """Create the banner frame with the given username and status."""
    BannerFrame = ctk.CTkFrame(parent, border_width=2, fg_color=BLUE)
    BannerFrame.pack(side="top", fill="x", padx=10, pady=10)

def create_main_page(app, username, status, user_friend_list, user_game_list, score):
    """Create the main screen after the user has logged in"""
    MainPage = ctk.CTkToplevel()
    width = MainPage.winfo_screenwidth()
    height = MainPage.winfo_screenheight()
    MainPage.geometry(f"{width}x{height}")
    MainPage.title(" Video Game Profile")
    
    BannerFrame = ctk.CTkFrame(MainPage, border_width=2, fg_color=BLUE)
    BannerFrame.pack(side="top", fill="x", padx=10, pady=10)
    UsernameBanner = create_username_banner(BannerFrame, username, status, score)
    
    create_friends_banner(MainPage)
    friend_menu = friends_menu(MainPage, user_friend_list)
    
    create_games_banner(MainPage)
    game_menu = games_menu(MainPage, user_game_list)

    button_frame = ctk.CTkFrame(MainPage,fg_color= DARK)
    button_frame.pack(pady=10)

    friend_menu_widget = friends_menu(MainPage, user_friend_list)
    add_friend_button = ctk.CTkButton(button_frame, text="Add Friend", command=lambda: add_friend_function(friend_menu_widget))
    add_friend_button.pack(side=ctk.LEFT, padx=10)

    remove_friend_button = ctk.CTkButton(button_frame, text="Remove Friend", command=lambda: remove_friend_function(friend_menu_widget, user_friend_list))
    remove_friend_button.pack(side=ctk.LEFT, padx=10)

    # In create_main_page function
    add_game_button = ctk.CTkButton(button_frame, text="Add Game", command=lambda: add_game_function(app, game_menu, user_game_list, calculate_achievement_score, UsernameBanner, username, status))
    add_game_button.pack(side=ctk.LEFT, padx=10)

    remove_game_button = ctk.CTkButton(button_frame, text="Remove Game", command=lambda: remove_game_function(game_menu, user_game_list, calculate_achievement_score, UsernameBanner, username, status))
    remove_game_button.pack(side=ctk.LEFT, padx=10)

    logout_button = ctk.CTkButton(button_frame, text="Logout", command=app.destroy)
    logout_button.pack(side=ctk.LEFT, padx=10)

    app.withdraw()
    return MainPage, UsernameBanner
    
def create_friends_banner(parent):
    """Create the Friends List Label above the Friends List"""
    friend_menu_frame = ctk.CTkFrame(parent, border_width=3, fg_color= DARK)
    friend_banner = ctk.CTkLabel(friend_menu_frame, text="Friends List", padx=8, pady=5, font=("Helvetica", 16))
    friend_banner.pack()
    friend_menu_frame.place(relx=0.3, rely=0.15, anchor="center")  

def create_games_banner(parent):
    """Create the Games List Label above the Friends List"""
    game_menu_frame = ctk.CTkFrame(parent, border_width=3,fg_color= DARK)
    game_banner = ctk.CTkLabel(game_menu_frame, text="Game List", padx=8, pady=5, font=("Helvetica", 16))  # Adjust font size
    game_banner.pack()
    game_menu_frame.place(relx=0.7, rely=0.15, anchor="center")

def friends_menu(parent, friend_list):   
    """create menu to display  friends""" 
    friend_menu = ctk.CTkTextbox(parent, border_width=3, border_color=BLUE)
    friend_menu.place(relx=0.3, rely=0.4, anchor="center", relwidth=0.3, relheight=0.45)
    friend_menu._textbox.configure(state="normal", wrap="none", insertoff=1) 
    display_friend_list(friend_menu, friend_list)
    friend_menu._textbox.configure(state="disabled", wrap="none", insertoff=1)
    return friend_menu

def games_menu(parent, game_list):
    """create menu to display games"""
    game_menu = ctk.CTkTextbox(parent, border_width=3, border_color=BLUE)
    game_menu.place(relx=0.7, rely=0.4, anchor="center", relwidth=0.3, relheight=0.45)
    game_menu._textbox.configure(state="normal", wrap="none", insertoff=1)
    display_game_list(game_menu, game_list)
    game_menu._textbox.configure(state="disabled", wrap="none", insertoff=1)
    return game_menu    
  
def create_username_banner(parent, username, status, score):
    """Create the username banner with the given username, status, and total_achievements."""
    UsernameBanner = ctk.CTkLabel(parent, text=f"{username} | Achievement Score: {score} | Status: {status}")
    UsernameBanner.pack(fill="x")
    return UsernameBanner

def display_friend_list(parent, friend_list, font_size=12):
    """This function will print out the Friend List on the Main GUI"""
    for friend in friend_list:
        parent.insert(END, str(friend) + "\n")

def display_game_list(parent, game_list, font_size=12):
    """This function will print out the Game List on the Main GUI"""
    for game in game_list:
        parent.insert(END, str(game) + "\n")


def get_game_details(title_prompt, value_prompt):
    input_dialog = ctk.CTkInputDialog(text=title_prompt,title=value_prompt)
    value = input_dialog.get_input()
    return value

def login(username_textbox, status_dropdown, app, user_friend_list, user_game_list, score, error_label):

    """This function explains what happens after you press Login.
       It takes in a username and online status and displays it to the screen.
    """
    username = username_textbox.get()
    if username.strip() == "":
        error_label.configure(text="Username cannot be empty.")
        error_label.pack()
        return
    else:
        error_label.pack_forget()

        status = status_dropdown.get()
    if status in ["Online", "Offline", "Busy"]:
        MainPage, UsernameBanner = create_main_page(app, username, status, user_friend_list, user_game_list, score)

def create_login_page():
    """ Creates the login window that displays login button and online status dropdown"""
    app = ctk.CTk()  # main window for GUI
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    app.geometry(f"{width}x{height}")
    app.title("Video Game Profile")
    ctk.set_appearance_mode("Dark")  # Set theme to dark mode
    
    ctk.set_default_color_theme("blue")
    login_frame = ctk.CTkFrame(master=app)
    login_frame.pack(pady=20, padx=40, fill='both', expand=True)
    label = ctk.CTkLabel(master=login_frame, text='Login Page')
    UsernameTextbox = ctk.CTkEntry(master=login_frame, placeholder_text="Enter Username")
    UsernameTextbox.pack(pady=12, padx=10)
    OnlineDrop = ctk.CTkComboBox(master=login_frame, values=["Online", "Offline", "Busy"])
    OnlineDrop.pack(pady=12, padx=10)
    error_label = ctk.CTkLabel(master=login_frame, text="", fg_color="red")
    error_label.pack(pady=5)
    error_label.pack_forget()
    return app, login_frame, UsernameTextbox, OnlineDrop, error_label

def login_button(master, username_textbox, status_dropdown, app, user_friend_list, user_game_list, score, error_label):
    LoginButton = ctk.CTkButton(master=master, text="Login", command=lambda: login(username_textbox, status_dropdown, app, user_friend_list, user_game_list, score, error_label))
    LoginButton.pack(pady=12, padx=10)
    return LoginButton

def add_game_function(app, game_menu, user_game_list, calculate_score_func, username_banner, username, status):
     
    title = get_game_details("Enter Game Title:", "Game Title")
    
    if title is None:
        return
    
    hours_played = get_game_details("Enter Hours Played:", "Hours Played")
    
    if hours_played is None:
        return
    
    achievements = get_game_details("Enter Achievements:", "Achievements")
    
    if achievements is None:
        return
    if title:
       game_details = f"Game Title: {title}\nHours Played: {hours_played}\nNumber of Achievements: {achievements}\n"
    
    # Update the game list
    user_game_list.append(Game(title, hours_played, achievements))

    new_score = calculate_score_func(user_game_list)
    username_banner.configure(text=f"{username} | Achievement Score: {new_score} | Status: {status}")
    app.update()  # Refresh the app
    # Update the display in the GUI
    game_menu._textbox.configure(state="normal")
    game_menu.insert(END, game_details + "\n")
    game_menu._textbox.configure(state="disabled")


def get_friend_details(title_prompt, value_prompt):
    input_dialog = ctk.CTkInputDialog(text=title_prompt, title=value_prompt)
    value = input_dialog.get_input()
    return value


def add_friend_function(friends_menu):
    username = get_friend_details("Enter Friend's Username:", "Friend's Username")
    
    if username is None:
        return
    
    real_name = get_friend_details("Enter Friend's Real Name:", "Friend's Real Name")
    
    if real_name is None:
        return
    
    last_online = get_friend_details("Enter Last Online:", "Hours since Last Online:")
    
    if last_online is None:
        return
    
    if username:
        friend_details = f"Username: {username}\nReal Name: {real_name}\nHours since Last Online: {last_online}\n"
    
    # Update the display in the GUI
    friends_menu._textbox.configure(state="normal")
    friends_menu.insert(END, friend_details + "\n")
    friends_menu._textbox.configure(state="disabled")

def remove_game_function(game_menu, user_game_list, calculate_score_func, username_banner, username, status):
    # Extract game titles from the list of games
    game_titles = [game.game_title for game in user_game_list]

    # Create a toplevel window for game removal
    remove_game_window = ctk.CTkToplevel()
    remove_game_window.title("Remove Games")
    remove_game_window.grab_set()

    # Create a list to store the games and its contents for each checkbox
    selected_games_vars = []

    def remove_selected_games():
        nonlocal user_game_list, game_menu, selected_games_vars

        # Identify selected games
        selected_indices = [i for i, var in enumerate(selected_games_vars) if var.get() == 1]

        # Remove the selected games from both the list and the display
        for index in sorted(selected_indices, reverse=True):
            game_menu.configure(state="normal")

            # Identify the start and end indices for the game in the GUI display
            start_index = game_menu.search(game_titles[index], "1.0", END)
            end_index = game_menu.search("\n\n", start_index, END)
            
             # Check if both indices are valid
            if start_index and end_index: 
                game_menu.tag_remove("sel", start_index, end_index)
                game_menu.delete(start_index, end_index)

            game_menu.configure(state="disabled")

            del user_game_list[index]
            new_score = calculate_score_func(user_game_list)
            username_banner.configure(text=f"{username} | Achievement Score: {new_score} | Status: {status}")

        # Update the Game List Textbox and Remove Empty Entries
        updated_game_menu_text = "\n\n".join([
            f"Game Title: {game.game_title}\n"
            f"Hours Played: {game.hours_played if hasattr(game, 'hours_played') else 'N/A'}\n"
            f"Number of Achievements: {game.num_achievements if hasattr(game, 'num_achievements') else 'N/A'}"
            for game in user_game_list if hasattr(game, 'game_title') and game.game_title.strip()
        ])

        game_menu.configure(state="normal")
        game_menu.delete(1.0, END)
        game_menu.insert(END, updated_game_menu_text + '\n\n')
        game_menu.configure(state="disabled")

        remove_game_window.destroy()

    # Create a checkbox for each game
    for game_title in game_titles:
        var = IntVar()
        selected_games_vars.append(var)
        checkbox = ctk.CTkCheckBox(remove_game_window, text=game_title, variable=var, bg_color=DARK, fg_color=BLUE)
        checkbox.pack(anchor=W)

    # Add a button to remove selected games
    remove_button = ctk.CTkButton(remove_game_window, text="Remove Selected Games", command=remove_selected_games)
    remove_button.pack()

    # Add a button to close GUI without removing a game
    cancel_button = ctk.CTkButton(remove_game_window, text="Cancel", command=remove_game_window.destroy)
    cancel_button.pack()

# THIS WORKS EXCEPT FOR ADDED FRIENDS - Remove Friend will Remove Added Friends
def remove_friend_function(friend_menu, user_friend_list):
    # Extract friend usernames from the list of friends
    user_names = [friend.user_name for friend in user_friend_list]

    print("Usernames:", user_names)

    # Create a toplevel window for game removal
    remove_friend_window = ctk.CTkToplevel()
    remove_friend_window.title("Remove Friends")
    remove_friend_window.grab_set()

    # Create a list to store the friends and their contents for each checkbox
    selected_friends_vars = []

    def remove_selected_friends():
        nonlocal user_friend_list, friend_menu, selected_friends_vars

        # Identify selected friends
        selected_indices = [i for i, var in enumerate(selected_friends_vars) if var.get() == 1]
        print("Selected Indices:", selected_indices)

        #Remove the selected friends from both the list and the display
        for index in sorted(selected_indices, reverse=True):
            friend_menu.configure(state="normal")

            # Identify the start and end indices for the friend in the GUI display
            user_name = user_names[index]
            start_index = friend_menu.search(user_name, "1.0", END)
            end_index = friend_menu.search("\n\n", start_index, END)

            print("Start Index:", start_index)
            print("End Index:", end_index)

            # Check if both indices are valid
            if start_index and end_index:
                friend_menu.tag_remove("sel", start_index, end_index)
                friend_menu.delete(start_index, end_index)

            friend_menu.configure(state="disabled")

            del user_friend_list[index]

        # Update the Friends List Textbox and Remove Empty Entries
        updated_friend_menu_text = "\n\n".join([
            f"Username: {friend.user_name}\n"
            f"Real Name: {friend.real_name if hasattr(friend, 'real_name') else 'N/A'}\n"
            f"Hours since Last Online: {friend.last_online if hasattr(friend, 'last_online') else 'N/A'}\n"
            for friend in user_friend_list if hasattr(friend, 'user_name') and friend.user_name.strip()
        ])

        friend_menu.configure(state="normal")
        friend_menu.delete(1.0, END)
        friend_menu.insert(END, updated_friend_menu_text + '\n\n')
        friend_menu.configure(state="disabled")

        remove_friend_window.destroy()

    # Create a checkbox for each friend
    for user_name in user_names:
        var = IntVar()
        selected_friends_vars.append(var)
        checkbox = ctk.CTkCheckBox(remove_friend_window, text=user_name, variable=var, bg_color=DARK, fg_color=BLUE)
        checkbox.pack(anchor=W)

    # Add a button to remove selected friends
    remove_button = ctk.CTkButton(remove_friend_window, text="Remove Selected Friends", command=remove_selected_friends)
    remove_button.pack()

    # Add a button to close the GUI without removing a friend
    cancel_button = ctk.CTkButton(remove_friend_window, text="Cancel", command=remove_friend_window.destroy)
    cancel_button.pack()


