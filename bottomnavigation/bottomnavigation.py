from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
FloatLayout:
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: "earth"
            text: "earth"
            icon: "earth"
            
        MDBottomNavigationItem:
            name: "star"
            text: "star"
            icon: "star"
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
