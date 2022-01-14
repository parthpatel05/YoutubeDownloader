import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from pytube import YouTube
import time
import os
import wget

# this downloads the thumbnail with wget
def downThumb(link):
    image_url = link
    image_filename = wget.download(image_url)

    print('Image Successfully Downloaded: ', image_filename)

class FirstWindow(Screen):
    goodObject = False
    link = ObjectProperty(None)
    yt = None

    # this function is called when link is first entered
    def pressed(self):
        lin = self.link.text 
        print(f'Link {lin}')

        try:
            # creates the yt object
            self.yt = YouTube(lin)
            self.goodObject = True

            # change the vidInfo
            self.manager.get_screen("second").ids.result.text = self.ids.title_label.text = self.yt.title
            self.ids.len_label.text = f'{self.yt.length}'
            downThumb(self.yt.thumbnail_url)
            self.ids.thumbImage.source = "sddefault.jpg"
            self.ids.chan_label.text = self.yt.channel_url
            print(self.yt.thumbnail_url)

            self.ids.btn.disabled = False
        except:
            # if the yt object is not created sucessfully
            # keep the continue button disables
            self.link.text = 'Please Enter A Valid Link'
            self.goodObject = False
            self.ids.btn.disabled = True
            self.ids.title_label.text = ""
            self.ids.len_label.text = ""
            self.ids.chan_label.text = ""


    def confirm(self):
        # change the screen
        if self.goodObject == True:
            # this updates the labels for the itags on the next screen
            audiostreams = self.yt.streams.filter(only_audio=True)
            mp4streams = self.yt.streams.filter(file_extension='mp4')
            streams = self.yt.streams
            for i in audiostreams:
                self.manager.get_screen("second").ids.audioLabel.text = self.manager.get_screen("second").ids.audioLabel.text + f"\n{i} "

            for i in mp4streams:
                self.manager.get_screen("second").ids.mp3Label.text = self.manager.get_screen("second").ids.mp3Label.text + f"\n{i} "

            for i in streams:
                self.manager.get_screen("second").ids.allLabel.text = self.manager.get_screen("second").ids.allLabel.text + f"\n{i} "
            


class SecondWindow(Screen):
    def vidDown(self):
        # get the link and itag
        lin = self.manager.get_screen("first").ids.link1.text
        rawtag = self.ids.itag1.text
        tag = None
        try:
            tag = int(rawtag)
            yt = YouTube(lin)
        except ValueError:
            self.ids.itag1.text = "Enter a vaild num"

        try:
            # create video object and then download
            # also show the updates
            video = yt.streams.get_by_itag(tag)
            self.ids.itag1.text = "Downloading"
            video.download()
            self.ids.itag1.text = "Done Downloading"
        except:
            self.ids.itag1.text = "Enter a vaild itag"

    def downHigh(self):
        # disable buttons and show update
        # THIS NOT WORKING FOR SOME REASON
        self.ids.downBtn.disabled = True
        self.ids.highDownBtn.disabled = True
        self.ids.itag1.text = "Downloading"

        # gets the link and then downloads it
        lin = self.manager.get_screen("first").ids.link1.text
        yt = YouTube(lin)
        video = yt.streams.get_highest_resolution()
        video.download()

        # Able the buttons and show update
        self.ids.itag1.text = "Done Downloading"
        self.ids.downBtn.disabled = False
        self.ids.highDownBtn.disabled = False



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()

    if os.path.exists("sddefault.jpg"):
        os.remove("sddefault.jpg")