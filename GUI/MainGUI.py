import customtkinter as ctk
import tkinter

app = tkinter.Tk() #main window for gui 
app.geometry = ("400x400") 
app.title("Video Game Profile")
ctk.set_appearance_mode("Dark") #Set theme to dark mode 
ctk.set_default_color_theme("blue")
frame = ctk.CTkFrame(master = app)
frame.pack(pady=20,padx=40,fill = 'both' ,expand = True)
label = ctk.CTkLabel(master=frame, text = 'Login Page')
label.pack(pady = 12, padx=10)
username_textbox = ctk.CTkEntry(master =frame, placeholder_text = "Enter Username")
username_textbox.pack(pady = 12, padx = 10)


app.mainloop() #end gui window 





