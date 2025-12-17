from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

DADOS_CLIMA = {
    "Lisboa": {"temp": "22ºC", "condicao": "Sol"},
    "Porto": {"temp": "18ºC", "condicao": "Chuva Forte"},
    "Coimbra": {"temp": "20ºC", "condicao": "Muito Nublado"},
    "Leiria": {"temp": "21ºC", "condicao": "Pouco Nublado"},
    "Faro": {"temp": "26ºC", "condicao": "Sol"}
}

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.entry = TextInput()
        layout.add_widget(self.entry)
        button = Button(text='Ver o tempo')
        button.bind(on_press=self.get_weather)
        layout.add_widget(button)
        self.label = Label(text='Pesquise uma cidade e depois clique em "Ver o tempo"')
        layout.add_widget(self.label)
        return layout

    def get_weather(self, instance):
            city = self.entry.text.strip()
            if city in DADOS_CLIMA:
                temp = DADOS_CLIMA[city]['temp']
                cond = DADOS_CLIMA[city]['condicao']
                self.label.text = f"Em {city} estão {temp} e {cond}."
            else:
                self.label.text = "Cidade não encontrada. Tente novamente."

if __name__ == '__main__':
    MyApp().run()