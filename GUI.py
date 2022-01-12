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



class FirstWindow(Screen):
    goodObject = False
    link = ObjectProperty(None)
    yt = None

    def pressed(self):
        lin = self.link.text # accessing text from input
        
        print(f'Link {lin}')

        try:
            self.yt = YouTube(lin)
            print('good')
            self.goodObject = True

            # change the vidInfo
            self.ids.title_label.text = self.yt.title
            self.ids.len_label.text = f'{self.yt.length}'
            self.ids.chan_label.text = self.yt.channel_url
            
            print("Length of video: ", self.yt.length,"seconds")
            print("channel: ",self.yt.channel_url)
            self.ids.btn.disabled = False
        except:
            self.link.text = 'Please Enter A Valid Link'
            self.goodObject = False
            self.ids.btn.disabled = True
            self.ids.title_label.text = ""
            self.ids.len_label.text = ""
            self.ids.chan_label.text = ""


        print(self.ids.btn.text)

    def confirm(self):
        # change the screen
        # to show the screen with the itags
        if self.goodObject == True:
            print('change screen')
            audiostreams = self.yt.streams.filter(only_audio=True)
            mp4streams = self.yt.streams.filter(file_extension='mp4')
            streams = self.yt.streams
            for i in audiostreams:
                self.manager.get_screen("second").ids.audioLabel.text = self.manager.get_screen("second").ids.audioLabel.text + f"\n{i} "

            for i in mp4streams:
                self.manager.get_screen("second").ids.mp3Label.text = self.manager.get_screen("second").ids.mp3Label.text + f"\n{i} "

            for i in streams:
                self.manager.get_screen("second").ids.allLabel.text = self.manager.get_screen("second").ids.allLabel.text + f"\n{i} "
            #self.manager.get_screen("second").ids.mp3Label.text = "Sucess"
            #self.manager.get_screen("second").ids.allLabel.text = "Sucess"


class SecondWindow(Screen):
    def vidDown(self):
        lin = self.manager.get_screen("first").ids.link1.text
        rawtag = self.ids.itag1.text
        tag = None
        try:
            tag = int(rawtag)
            yt = YouTube(lin)
        except ValueError:
            self.ids.itag1.text = "Enter a vaild num"
        print(tag)

        try:
            video = yt.streams.get_by_itag(tag)
            self.ids.itag1.text = "Downloading"
            video.download()
            self.ids.itag1.text = "Done Downloading"
        except:
            self.ids.itag1.text = "Enter a vaild itag"

        




class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        #return FirstWindow()
        return kv

if __name__ == "__main__":
    MyApp().run()