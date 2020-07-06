import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class QuestionWindow(Screen):
    pass

class AnswerWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    app = MyApp()
    app.run()
