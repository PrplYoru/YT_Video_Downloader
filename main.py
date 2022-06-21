import ffmpeg, os
from pytube import YouTube
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

path = 'Download/'

class YTToMp3(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.9, 0.8)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.window.spacing = [0, 15]
        self.icon = 'logo.jpg'
        
        self.insert = Label(
            text = 'Insert a youtube video link:',
            font_size = 25,
            color = '#6905F5',
            )

        self.user = TextInput(
            multiline=False,
            padding_y = (13, 13),
            size_hint = (1, 0.6),
            )

        self.filenames = Label(
            text = 'Declare a filename',
            font_size = 20,
            color = '#6905F5'
        )

        self.file = TextInput(
            multiline = False,
            padding_y = (13, 13),
            size_hint = (1, 0.6),
        )

        self.specify = Label(
            text = 'Type "video" if you want to download the whole video, \n"audio" if you want to download only the mp3 file of the video\nor "video only" to download the video without audio:',
            font_size = 20,
            color = '#6905F5'
        )

        self.choose = TextInput(
            multiline = False,
            padding_y = (13, 13),
            size_hint = (1, 0.6),
        )
        
        self.button = Button(
            text = 'Confirm',
            size_hint = (0.3, 0.6),
            bold = True,
            background_color = '#6905F5'
            )
        self.button.bind(on_press = self.callback)
        
        self.window.add_widget(self.insert)
        self.window.add_widget(self.user)
        self.window.add_widget(self.filenames)
        self.window.add_widget(self.file)
        self.window.add_widget(self.specify)
        self.window.add_widget(self.choose)
        self.window.add_widget(self.button)
        
        return self.window

    def callback(self, event):
        if self.choose.text == 'audio' or self.choose.text == 'Audio':
            try:
                yt = YouTube(self.user.text)
            except:
                print('Connection Error')
            mp3file = yt.streams.get_audio_only().download(path, f'{self.file.text}.mp3')
            print(mp3file)

            self.choose.text = f'Download complete, saved as {self.file.text}.mp3'
        elif self.choose.text == 'video' or self.choose.text == 'Video':
            try:
                yt = YouTube(self.user.text)
            except:
                print('Connection Error')
            v = ffmpeg.input(yt.streams.filter(resolution='1080p').first().download(path, 'oiawjkldsnakdhnsak.mp4'))
            a = ffmpeg.input(yt.streams.get_audio_only().download(path, 'auhdwkljsahiluhnwsda.mp4'))

            r = ffmpeg.concat(v, a, v=1, a=1).output(f'{path}{self.file.text}.mp4').run()
            print(r)
            if os.path.exists(f'{path}oiawjkldsnakdhnsak.mp4') and os.path.exists(f'{path}auhdwkljsahiluhnwsda.mp4'):
                os.remove(f'{path}oiawjkldsnakdhnsak.mp4')
                os.remove(f'{path}auhdwkljsahiluhnwsda.mp4')
            else:
                print('The files do not exist')
            self.choose.text = f'Download complete, saved as {self.file.text}.mp4'
        elif self.choose.text == 'video only' or self.choose.text == 'only video' or self.choose.text == 'Video only' or self.choose.text == 'Only video':
            try:
                yt = YouTube(self.user.text)
            except:
                print('Connection Error')
            mp4file = yt.streams.filter(resolution='1080p').first().download(path, f'{self.file.text}.mp4')
            print(mp4file)
            self.choose.text = f'Download complete, saved as {self.file.text}.mp3'
        else:
            self.choose.text = f"{self.choose.text} won't work."
  

if __name__ == '__main__':
    YTToMp3().run()