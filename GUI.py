import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from pytube import YouTube

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        
        # making a inside grid for link
        self.inside = GridLayout()
        self.inside.cols = 3
        
        self.inside.add_widget(Label(text="Link: "))
        self.link = TextInput(multiline = False) 
        self.inside.add_widget(self.link)
        self.inside.submit = Button(text= "Submit", font_size=40)
        self.inside.submit.bind(on_press = self.pressed) # the way to bind button to function
        self.inside.add_widget(self.inside.submit)

        #inner des layout
        self.indes = GridLayout()
        self.indes.cols = 2

        self.title, self.vidLen, self.channel = "", "",""
        self.indes.add_widget(Label(text="Title: "))
        self.indes.add_widget(Label(text=self.title))
        self.indes.add_widget(Label(text="Length in seconds: "))
        self.indes.add_widget(Label(text=self.vidLen))
        self.indes.add_widget(Label(text="Channel: "))
        self.indes.add_widget(Label(text=self.channel))
        
        # making the main des layout
        self.vidInfo = GridLayout()
        self.vidInfo.cols = 2

        self.vidInfo.add_widget(self.indes)
        self.vidInfo.add_widget(Label(text="Thumbnail"))

        # making confirmaton layout
        self.conf= GridLayout()
        self.conf.cols = 2

        self.conf.add_widget(Label(text="Continue if this is the desired video"))
        self.confButton = Button(text= "Continue", font_size=40)
        self.confButton.bind(on_press = self.confirm)
        self.conf.add_widget(self.confButton)

        # the outside grid
        self.add_widget(self.inside)

        #self.submit = Button(text= "Submit", font_size=40)
        #self.submit.bind(on_press = self.pressed) # the way to bind button to function
        #self.add_widget(self.submit)
        self.add_widget(self.vidInfo)
        self.add_widget(self.conf)


    def pressed(self, instance):
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

    def confirm(self, instance):
        # change the screen
        # to show the screen with the itags
        print('change screen')

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()