from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.entry = TextInput()
        layout.add_widget(self.entry)
        button = Button(text='Click me!')
        button.bind(on_press=self.show_text)
        layout.add_widget(button)
        self.label = Label(text='')
        layout.add_widget(self.label)
        return layout

    def show_text(self, instance):
        text = self.entry.text
        self.label.text = text

if __name__ == '__main__':
    MyApp().run()
