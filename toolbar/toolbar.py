from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
FloatLayout:
    MDToolbar:
        title: 'Toolbar'
        size_hint: 1, 0.1
        pos_hint: {'top':1}
        left_action_items: [['menu', lambda x: self]]
        right_action_items: [['magnify', lambda x: self], ['dots-vertical', lambda x: self]]
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
