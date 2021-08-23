from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
FloatLayout:
    MDTextField:
        hint_text: "Email"
        helper_text: "ex: myaccount@email.com"
        size_hint: 0.80, 0.07
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.500, "center_y":0.600}
    
    MDTextField:
        hint_text: "Password"
        helper_text: "ex: 123456"
        size_hint: 0.80, 0.07
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.500, "center_y":0.400}
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
