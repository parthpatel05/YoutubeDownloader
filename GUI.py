import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from pytube import YouTube

class MyGrid(Widget):
        
    link = ObjectProperty(None)

    def pressed(self):
        lin = self.link.text # accessing text from input
        
        print(f'Link {lin}')

        try:
            yt = YouTube(lin)
            print('good')
            self.link.text = ''

            # change the vidInfo
            self.title = yt.title
        except:
            self.link.text = 'Please Enter A Valid Link'

    def confirm(self):
        # change the screen
        # to show the screen with the itags
        print('change screen')

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()