from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDSwitch:
    pos_hint: {'center_x':.500, 'center_y':.400}
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
