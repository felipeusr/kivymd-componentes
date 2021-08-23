from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

KV = """
FloatLayout:
    Button:
        text: "Open Dialog"
        on_release: app.show_exit_dialog();
"""


class Body(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_exit_dialog(self):
        self.dialog = MDDialog(
            title="Close Application",
            text="Are you sure you want to exit?",
            size_hint=(0.35, 0.45),
            radius=[20, 20, 20, 20],
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda _: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="Exit",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.stop
                )
            ]  # buttons component
        )  # dialog widget
        self.dialog.open()


Body().run()
