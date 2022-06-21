from tkinter import *
import ffmpeg, os
from pytube import YouTube
from tkinter.filedialog import askdirectory

main = Tk()
main.title('YtDownloader')
main.resizable(False, False)

file = 'C:/'

canvas = Canvas(main, width=1000, height=600, bg='#282828')
canvas.grid(rowspan=12)

statusbar = Label(main, text='Path: '+file, relief=SUNKEN, font='Verdana', bg='#282828', fg='#ffffff').grid(row=12, rowspan=3, column=0)

titlabel = Label(main, text='Insert a youtube link', font='Verdana', bg='#282828', fg='#ffffff').grid(row=1, column=0)

linkentry = Entry(main, width=50, bg='#b3b3b3')
linkentry.grid(row=2, column=0)

browselbl = Label(main, text='Select the folder where you want to save the file', font='Verdana', bg='#282828', fg='#ffffff').grid(row=3, column=0)
btntext = StringVar()
btntext.set('Browse')
browsebtn = Button(main, text=btntext.get(), font='Verdana', bg='#404040', fg='#ffffff', command=lambda:open_brws()).grid(row=4, column=0)

namelbl = Label(main, text='Declare a filename', font='Verdana', bg='#282828', fg='#ffffff').grid(row=5, column=0)
filentry = Entry(main, width=50, bg='#b3b3b3')
filentry.grid(row=6, column=0)

selec = StringVar()
selec.set('Select')

dropdwn = OptionMenu(main, selec, 'Video', 'Audio', 'Video Only', )
dropdwn.grid(row=7, column=0)
dropdwn.config(bg='#282828', fg='#ffffff')
dropdwn['menu'].config(bg='#282828', fg='#ffffff')

confbtn = Button(main, text='Confirm',font='Verdana', bg='#404040', fg='#ffffff', command=lambda:callback(selec.get())).grid(row=8, column=0)

def open_brws():
    global file
    file = askdirectory(parent=main, title='Select a folder')
    statusbar = Label(main, text='Path: '+file, relief=SUNKEN, font='Verdana', bg='#282828', fg='#ffffff').grid(row=12, column=0)

def callback(value):
        if value == 'Audio':
            try:
                yt = YouTube(linkentry.get())
                print(yt)
            except:
                print('Connection Error')
            mp3file = yt.streams.get_audio_only().download(file, f'{filentry.get()}.mp3')
            print(mp3file)
        elif value == 'Video':
            try:
                yt = YouTube(linkentry.get())
            except:
                print('Connection Error')
            v = ffmpeg.input(yt.streams.filter(resolution='1080p').first().download(file, 'oiawjkldsnakdhnsak.mp4'))
            a = ffmpeg.input(yt.streams.get_audio_only().download(file, 'auhdwkljsahiluhnwsda.mp4'))

            r = ffmpeg.concat(v, a, v=1, a=1).output(f'{file}/{filentry.get()}.mp4').run()
            print(r)
            if os.path.exists(f'{file}/oiawjkldsnakdhnsak.mp4') and os.path.exists(f'{file}/auhdwkljsahiluhnwsda.mp4'):
                os.remove(f'{file}/oiawjkldsnakdhnsak.mp4')
                os.remove(f'{file}/auhdwkljsahiluhnwsda.mp4')
            else:
                print('The files do not exist')
        elif value == 'Video only':
            try:
                yt = YouTube(linkentry.get())
            except:
                print('Connection Error')
            mp4file = yt.streams.filter(resolution='1080p').first().download(file, f'{filentry.get()}.mp4')
            print(mp4file)
        else:
            print('Invalid')
        top = Toplevel()
        canvas2 = Canvas(top, width=500, height=200, bg='#282828')
        canvas2.grid(rowspan=2)
        if value == 'Audio':
            complete = Label(top, text=f'Download Completed!, saved to: {file}/{filentry.get()}.mp3', bg='#282828', fg='#ffffff').grid(row=0, column=0)
        else:
            complete = Label(top, text=f'Download Completed!, saved to: {file}/{filentry.get()}.mp4', bg='#282828', fg='#ffffff').grid(row=0, column=0)
main.mainloop()
