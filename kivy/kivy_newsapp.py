from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.clock import Clock

noticias = [
    {"título": "Montenegro desvaloriza sondagem sobre apoio à greve: “Direitos de uns não devem obstaculizar os direitos dos outros”",
     "descricao": "A sondagem a que Montenegro se refere é a publicada esta manhã pelo Diário de Notícias e indica que mais de metade da população apoia a greve geral marcada para esta quinta-feira",
     "detalhes": "O primeiro-ministro Luís Montenegro comentou esta quarta-feira, em Baião, os resultados de uma sondagem do Diário de Notícias, que aponta que mais de metade da população apoia a greve geral marcada para amanhã. Segundo o primiero-ministro, a sondagem “vale o que vale”, mas “não é isso que interessa”.\nMontenegro sublinhou ainda que, em Portugal, os “direitos de uns não devem obstaculizar os direitos dos outros”. Destacou a situação do país, afirmando que existe uma “estabilidade económica e política reconhecida a nível internacional” e criticou a atenção dada às sondagens, referindo que “não vale a pena andar com este jogo”.\nO primeiro-ministro acrescentou que os rendimentos estão a crescer, que os jovens têm mais oportunidades do que nos últimos anos e que a credibilidade e reputação do país são elevadas, concluindo: “Estamos no topo da Europa e do Mundo”."
     },
    {"título": "Julgamento de deputado do Chega por difamação adiado para janeiro",
     "descricao": "Pedro Frazão, a ser julgado por alegada difamação do atual coordenador do BE, José Manuel Pureza, invocou imunidade parlamentar",
     "detalhes": "O julgamento do deputado do Chega Pedro Frazão por ter alegadamente difamado, em 2021, o agora coordenador do BE, José Manuel Pureza, foi adiado para janeiro, depois de o arguido ter invocado a imunidade parlamentar.\nA decisão do juiz surgiu depois de a defesa de Pedro Frazão ter remetido ao Tribunal Local Criminal de Lisboa um ofício datado de terça-feira em que a Comissão de Transparência e Estatuto dos Deputados da Assembleia da República refere que é necessária uma nova autorização parlamentar para que o deputado do Chega seja julgado, apesar de esta ter já sido concedida na legislatura anterior.\nA próxima sessão do julgamento ficou agendada para 12 de janeiro de 2026 e destinar-se-á aos depoimentos de Pedro Frazão, caso este pretenda falar, e de José Manuel Pureza.\nDe acordo com a acusação do Ministério Público, em 2021 o deputado do Chega publicou na rede social Twitter (atual X) um vídeo de uma 'jovem militante/simpatizante do Bloco de Esquerda (BE), em que esta refere, em súmula, ter sido vítima de atos sexuais não consentidos por parte de indivíduo ligado ao referido partido'.\nA acompanhar o vídeo, Pedro Frazão escreveu: 'Já não há Pureza no Bloco de Asquereza? #MeToo', questionando ainda, num comentário, quem seria 'o nojento de 62 anos'.\nÀ data da publicação, José Manuel Pureza, coordenador do BE desde 30 de novembro de 2025, era vice-presidente da Assembleia da República e deputado eleito por aquele partido.\nPara o Ministério Público, Pedro Frazão 'tinha perfeita consciência' de que José Manuel Pureza 'pertencia aos órgãos do Bloco de Esquerda, que havia sido eleito deputado por aquele partido e que tinha 62 anos de idade'."
     },
    {"título": "Catarina Martins certa de que até o rato Mickey ganha na segunda volta à extrema-direita    ",
     "descricao": "“Tenho a certeza absoluta que este país não é um país de fascistas e que até o rato Mickey, numa segunda volta, ganha contra quem tiver essas ideias”, disse a candidata presidencial apoiada pelo Bloco de Esquerda",
     "detalhes": "A candidata presidencial Catarina Martins disse hoje, em Gondomar, ter a certeza absoluta que Portugal não é um país de fascistas e que até o rato Mickey, na segunda volta, ganha contra quem tiver essas ideias.\n'Em primeiro lugar, eu tenho a certeza absoluta que este país não é um país de fascistas e que até o rato Mickey, numa segunda volta, ganha contra quem tiver essas ideias', disse.\nCatarina Martins fez estas afirmações durante o debate organizado pela Frente Cívica sobre 'O papel do Presidente da República no combate à corrupção', quando questionada sobre a prevalência dos valores do Estado de Direito Democrático.\nE dirigindo-se à plateia, acrescentou, 'não creio que estejamos num momento em que isso esteja em causa, porque estou convencida de que nós que estamos aqui, que temos ideias, em que todos são diferentes, também votávamos alegremente no rato Mickey, se essa possibilidade se nos colocasse. Posto isto, o problema é que não é com jogos eleitorais, nem com calculismos, que nós combatemos as ideias que estão a aumentar na nossa sociedade'.\nCatarina Martins prosseguiu o raciocínio acrescentando que 'a ideia de que é tudo aritmética eleitoral e de que é melhor determinadas pessoas não se apresentarem, porque isso pode concentrar votos em não sei quem, é muito distante da vida das pessoas'.\n'Eu tenho a certeza que se não houvesse candidaturas à Esquerda, e eu modestamente acho que tenho feito a minha parte, nós estávamos a discutir burcas em vez de discutir o pacote laboral. E se nós passássemos a campanha a discutir burcas em vez de discutir o pacote laboral, então aí sim o nosso país iria por uma rampa deslizante que eu não sei onde é que acabava', enfatizou a candidata.\nCatarina Martins disse 'que muitas vezes esta ideia de que há uma qualquer moderação num centro de regime que não tem dado resposta às pessoas' e que todos 'têm de aceitar como sendo o menos mau face a outro perigo, na verdade só tem aberto o caminho a outro perigo'.\n'Por muitos jogos eleitorais que a gente tenha, por muito taticismo que haja de última hora, essas ideias só crescem. Acho, aliás, que infelizmente o resto da Europa tem-nos dado provas que assim é. Nós estamos agora a aprender a lidar com o fenómeno e estou a tentar um caminho diferente', acrescentou.\nCatarina Martins concluiu, sobre o tema da escalada da extrema-direita em Portugal que há 'caminho novo do que tem acontecido no resto da Europa que não está a resultar', sublinhando que 'o caminho é mesmo ir à luta'."
     },
]

class TelaPrincipal(Screen):
    lista = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.carregar())

    def carregar(self):
        self.lista.data = []
        for item in noticias:
            noticia = {
                "text" = f"{item['título']}\n{item['descricao']}"
                "on_release" = lambda x=item self.abrir_detalhes(x)
            }
        self.lista.data.append(noticia)

    def abrir_detalhes():
        tela_detalhes = self.manager.get_screen('detalhes')
        tela_detalhes.atualizar_conteudo(noticia)
        self.manager.current = 'detalhes'

class TelaDetalhes(Screen):
    titulo = ObjectProperty(None)
    descricao = ObjectProperty(None)

    def atualizar_conteudo(self, noticia):
        self.titulo.text = noticia['título']
        self.descricao.text = noticia['descricao']

class ListaNoticia(RecycleView): pass

class Gerenciador(ScreenManager): pass

class NoticiasApp(App):
    def build(self): return Gerenciador(

    )

NoticiasApp().run()