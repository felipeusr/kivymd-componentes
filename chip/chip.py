from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
FloatLayout:
    MDChip:
        text: 'Facebook'
        icon: 'facebook'
        pos_hint: {"center_x":0.5, "center_y":0.5}
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
