from kivy.app import App
from kivy.uix.widget import Widget

class MemeScreen(Widget):
    pass

class MemeApp(App):
    def build(self):
        return MemeScreen()

if __name__ == '__main__':
    MemeApp().run()
