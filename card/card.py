from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = """
FloatLayout
    MDCard
        pos_hint: {'center_x':0.500, 'center_y':0.500}
        size_hint: 0.5, 0.5
        border_radius: dp(40)
        radius: [100]
        elevation: 8
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
