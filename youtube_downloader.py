#YouTube video downloader
import tkinter
import customtkinter
from pytube import YouTube

def Startdownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link is invalid")
    print("Download completed !!")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Sarwottam Youtube video downloader")

#add UI elements
title = customtkinter.CTkLabel(app, text="Insert your youtube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#download button
download = customtkinter.CTkButton(app, text="Download", command=Startdownload)
download.pack()

#run app
app.mainloop()
