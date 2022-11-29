import ffmpeg, os, yt_dlp
from pytube import YouTube
import customtkinter as ctk
import tkinter as tk
from tkinter.filedialog import askdirectory

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

file = f'C:/Users/{os.getlogin()}/Downloads'

def openDialog(textvar):
    global file
    file = askdirectory(parent=main, title='Select a folder')
    textvar.set(file)
    

main = ctk.CTk()
main.title('Youtube Downloader')
main.geometry(f'{1200}x{800}')
main.resizable(False, False)
main.configure(bg='#1f1f1f')

frame = ctk.CTkFrame(main, 
                   width=1000, 
                   height=600, 
                   bg='#282828',
                   corner_radius=10,)
frame.pack(padx=20, pady=20, expand=True)
frame.pack_propagate(0)

label = ctk.CTkLabel(master=frame, text='Insert a youtube link', text_font='Verdana',)
label.pack(padx=10)

user_var = tk.StringVar()
entry = ctk.CTkEntry(master=frame,
                    placeholder_text='Insert a youtube link',
                    textvariable=user_var,
                    width=500, 
                    bg='#b3b3b3',
                    corner_radius=10,
                    height=5)
entry.pack(padx=10, pady=10)


labeltxt = ctk.CTkLabel(
            text='Select the folder where you want to save the file', 
            master=frame, 
            text_font='Verdana',)
labeltxt.pack(padx=10, pady=10)



opendialog = ctk.CTkButton(master=frame, 
                        text='Browse', 
                        text_font='Verdana', 
                        bg='#404040',
                        command=lambda:openDialog(path_var))
opendialog.pack(padx=10, pady=10)

# declare a filename
labelname = ctk.CTkLabel(
            text='Insert the name of the file',
            master=frame,
            text_font='Verdana',)
labelname.pack(padx=10, pady=10)

name_var = tk.StringVar()
entryname = ctk.CTkEntry(master=frame,
                    placeholder_text='Insert the name of the file',
                    textvariable=name_var,
                    width=500,
                    bg='#b3b3b3',
                    corner_radius=10,
                    height=5)
entryname.pack(padx=10, pady=10)

# if he wants to download the video or the audio

labelaudio = ctk.CTkLabel(
            text='Do you want to download the audio or the video?',
            master=frame,
            text_font='Verdana',)
labelaudio.pack(padx=10, pady=10)

# optionmenu for the audio or the video

audio_var = tk.StringVar()
audio_var.set('Both')
audio = ctk.CTkOptionMenu(master=frame,
                        variable=audio_var,
                        values=['Video', 'Audio', 'Both'],
                        width=500,
                        bg='#b3b3b3',
                        corner_radius=10,
                        height=10)
audio.pack(padx=10, pady=10)

# members only or private video
labelmembers = ctk.CTkLabel(
            text='Is the video a members only or a private video?',
            master=frame,
            text_font='Verdana',)
labelmembers.pack(padx=10, pady=10)
# optionmenu for the members only or private video
members_var = tk.StringVar()
members_var.set('No')
members = ctk.CTkOptionMenu(master=frame,
                        variable=members_var,
                        values=['Yes', 'No'],
                        width=500,
                        bg='#b3b3b3',
                        corner_radius=10,
                        height=10)
members.pack(padx=10, pady=10)

# declare a quality
labelquality = ctk.CTkLabel(
            text='Select the quality of the video',
            master=frame,
            text_font='Verdana',)
labelquality.pack(padx=10, pady=10)

quality_var = tk.StringVar()
quality_var.set('Select the quality of the video')
quality = ctk.CTkOptionMenu(master=frame,
                            variable=quality_var,
                            values=['Select the quality of the video', '144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p'],
                            width=500,
                            bg='#b3b3b3',
                            corner_radius=10,
                            height=10)
quality.pack(padx=10, pady=10)

confbutton = ctk.CTkButton(master=frame,
                        text='Confirm',
                        text_font='Verdana',
                        bg='#404040',
                        height=10,
                        command=lambda:callback(audio_var.get(), quality_var.get(), members_var.get()))
confbutton.pack(padx=10, pady=10)

path_var = tk.StringVar()
path_var.set(file)
statusbar = ctk.CTkLabel(master=frame, 
                        textvariable=path_var,
                        text_font='Verdana', 
                        bg='#282828',)
statusbar.pack(padx=10, pady=10)    

def callback(value, value1, value2):
    if value == 'Audio':
        if value2 == 'Yes':
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': f'{file}/{name_var.get()}.mp3',
                    'cookiefile': 'cookies.txt',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([user_var.get()])
            except:
                print('Connection Error')
        else:
            try:
                yt = YouTube(user_var.get())
            except:
                print('Connection Error')
            mp3file = yt.streams.get_audio_only().download(file, f'{name_var.get()}.mp3')
    elif value == 'Both':
        if value2 == 'Yes':
            try:
                ydl_opts = {
                    'format': 'bestvideo+bestaudio',
                    'outtmpl': f'{file}/{name_var.get()}.mp4',
                    'cookiefile': 'cookies.txt',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([user_var.get()])
            except:
                print('Connection Error')
        else:
            try:
                yt = YouTube(user_var.get())
            except:
                print('Connection Error')

            v = ffmpeg.input(yt.streams.filter(resolution=value1).first().download(file, 'oiawjkldsnakdhnsak.mp4'))
            a = ffmpeg.input(yt.streams.get_audio_only().download(file, 'auhdwkljsahiluhnwsda.mp4'))

            r = ffmpeg.concat(v, a, v=1, a=1).output(f'{file}/{name_var.get()}.mp4').run()
            if os.path.exists(f'{file}/oiawjkldsnakdhnsak.mp4') and os.path.exists(f'{file}/auhdwkljsahiluhnwsda.mp4'):
                os.remove(f'{file}/oiawjkldsnakdhnsak.mp4')
                os.remove(f'{file}/auhdwkljsahiluhnwsda.mp4')
            else:
                print('The files do not exist')
    elif value == 'Video':
        if value2 == 'Yes':
            try:
                ydl_opts = {
                    'format': 'bestvideo',
                    'outtmpl': f'{file}/{name_var.get()}.mp4',
                    'cookiefile': 'cookies.txt',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([user_var.get()])
            except:
                print('Connection Error')
        else:
            try:
                yt = YouTube(user_var.get())
            except:
                print('Connection Error')
            mp4file = yt.streams.filter(resolution=value1).first().download(file, f'{name_var.get()}.mp4')
    else:
        print('Invalid option')
        
    #create a popup window to show the download status
    

    #create a label to show the download status
    popup = tk.Tk()
    popup.title('Download Status')
    popup.geometry('400x100')
    popup.resizable(False, False)
    popup.configure(bg='#282828')
    label = ctk.CTkLabel(master=popup,
                        text='Download completed\n Path: ' + file + "/" + name_var.get(),
                        text_font='Verdana',
                        bg='#282828',)
    label.pack(padx=10, pady=10)

    #create a button to close the popup window
    button = ctk.CTkButton(master=popup,
                        text='Close',
                        text_font='Verdana',
                        bg='#404040',
                        height=10,
                        command=popup.destroy)
    button.pack(padx=10, pady=10)

main.mainloop()