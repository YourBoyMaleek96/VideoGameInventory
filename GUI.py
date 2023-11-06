import customtkinter as ctk
from tkinter import * 

def login():
    """This function explains what happens after you press Login.
       It takes in a username and online staus and display it to screen.
    """
    status = OnlineDrop.get()
    if status in ["Online", "Offline", "Busy"]:
        MainPage = ctk.CTkToplevel(app)
        width = app.winfo_screenwidth()
        height = app.winfo_screenheight()
        MainPage.geometry(f"{width}x{height}")
        MainPage.title(" Video Game Profile")
        BannerFrame = ctk.CTkFrame(MainPage, border_width=2, fg_color= "Blue")
        BannerFrame.pack(side="top", fill="x", padx=10,pady=10)
        UsernameBanner = ctk.CTkLabel(BannerFrame, text=f"{UsernameTextbox.get()} | Achievement Score: | Status: {status}")
        UsernameBanner.pack(fill = "x")
        app.withdraw()



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





