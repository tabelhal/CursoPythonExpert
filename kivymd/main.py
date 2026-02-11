from kivymd.app import MDApp
from kivy.lang import Builder
from telas import *

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Builder.load_file('main.kv')

MyApp().run()