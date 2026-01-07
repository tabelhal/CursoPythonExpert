from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

perguntas = [
    {
        "pergunta": "Qual foi a causa de morte do ator James Dean?",
        "respostas": ["Suicídio", "Acidente de carro", "Atropelamento", "Cancro do fígado"],
        "correta": "Acidente de carro"
    },
    {
        "pergunta": "A Playstation 2 é a consola mais vendida. Qual é a segunda?",
        "respostas": ["Xbox 360", "Playstation", "Nintendo DS", "Wii"],
        "correta": "Nintendo DS"
    }
]

class QuizLayout(BoxLayout):
    pergunta_texto = StringProperty("")
    options = ListProperty([])
    pontuacao = NumericProperty(0)
    index = NumericProperty(0)

    def on_kv_post(self, base_widget):
        self.carregar_proxima()

    def carregar_proxima(self):
        if self.index < len(perguntas):
            pergunta_atual = perguntas[self.index]
            self.pergunta_texto = pergunta_atual["pergunta"]
            self.options = pergunta_atual["respostas"]
        else:
            self.pergunta_texto = "Fim do Quiz! :)"
            self.options = []
            for btn in self.ids.values():
                btn.disabled = True

    def responder(self, resposta):
        correta = perguntas[self.index]["correta"]
        if resposta == correta:
            self.pontuacao += 1
            self.mostrar_popup("Certo!", "Resposta correta!")
        else:
            self.mostrar_popup("Errado!", f"A correta era: {correta}")

        self.index += 1
        self.carregar_proxima()

    def mostrar_popup(self, titulo, mensagem):
        popup = Popup(
            title=titulo,
            content=Label(text=mensagem),
            size_hint=(None, None),
            size=(300, 200)
        )
        popup.open()

class QuizApp(App):
    def build(self):
        return QuizLayout()

QuizApp().run()
