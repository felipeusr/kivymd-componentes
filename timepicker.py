from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
from kivy.lang import Builder


KV = '''
MDFloatLayout:
    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
'''


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)

    @staticmethod
    def show_time_picker():
        time_dialog = MDTimePicker()
        time_dialog.open()


Body().run()
