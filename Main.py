from kivy.core.window import Window

from Application import Application


#Define overall app charicteristics
Window.size = (1000, 600)


if __name__ == "__main__":
    Application().run()