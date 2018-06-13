from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width',     '1000')
Config.set('graphics', 'height',    '500')

from kivy.app import App

from kivy.uix.boxlayout     import  BoxLayout
from kivy.uix.floatlayout   import  FloatLayout
from kivy.uix.gridlayout    import  GridLayout
from kivy.uix.label         import  Label
from kivy.uix.textinput     import  TextInput
from kivy.uix.scatter       import  Scatter
from kivy.uix.widget        import  Widget
from kivy.uix.screenmanager import  ScreenManager, Screen, FadeTransition

from kivy.lang import Builder

class LSE(Screen):
    pass

class Lista(Screen):
    pass

class Fila(Screen):
    pass

class Pilha(Screen):
    pass

class ABP(Screen):
    pass

class MainWidget(Widget):
    pass

class MainScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

style = Builder.load_file('visual.kv')

class visualEd(App):
    def build(self):
        return style

if __name__ == "__main__":
    visualEd().run()
