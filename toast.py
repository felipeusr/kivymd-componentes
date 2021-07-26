from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast

KV = """
FloatLayout:
    Button:
        on_release: app.toast();
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)

    @staticmethod
    def toast():
        toast("this is my android toast!")


Body().run()
