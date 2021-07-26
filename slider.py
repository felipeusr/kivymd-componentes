from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
FloatLayout:
    MDSlider:
        min: 0
        max: 100
        value: 40
'''


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
