import customtkinter as ctk
from tkinter import * 
import tkinter

def login():
    status = OnlineDrop.get()
    if status in ["Online", "Offline", "Busy"]:
        new_window = tkinter.Toplevel(app)
        new_window.geometry("200x200")
        new_window.title("Welcome")
        welcome_label = ctk.Label(new_window, text=f"Welcome, {UsernameTextbox.get()}!\nStatus: {status}")
        welcome_label.pack(padx=10, pady=10)
        app.destroy()

app = tkinter.Tk() #main window for gui 
app.geometry = ("400x400") 
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
LoginButton = ctk.CTkButton(master=frame, text="Login")
LoginButton = ctk.CTkButton(master=frame, text="Login", command= login)
LoginButton.pack(pady=12, padx=10)

app.mainloop() #end gui window