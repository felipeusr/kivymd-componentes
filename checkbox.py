from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
FloatLayout
    orientation: 'horizontal'

    MDCheckbox
        size_hint: 0.1, 0.1
        pos_hint: {'center_x':.500, 'center_y':.700}

    MDCheckbox
        size_hint: 0.1, 0.1
        pos_hint: {'center_x':.500, 'center_y':.600}

    MDCheckbox
        size_hint: 0.1, 0.1
        pos_hint: {'center_x':.500, 'center_y':.500}

    MDCheckbox
        size_hint: 0.1, 0.1
        pos_hint: {'center_x':.500, 'center_y':.400}

    MDCheckbox
        size_hint: 0.1, 0.1
        pos_hint: {'center_x':.500, 'center_y':.300}
'''


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
