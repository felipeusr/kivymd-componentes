from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
#:import MDIconButton kivymd.uix.button.MDIconButton
#:import MDFloatingActionButton kivymd.uix.button.MDFloatingActionButton
#:import MDFlatButton kivymd.uix.button.MDFlatButton
#:import MDRectangleFlatButton kivymd.uix.button.MDRectangleFlatButton
#:import MDRectangleFlatIconButton kivymd.uix.button.MDRectangleFlatIconButton
#:import MDRoundFlatButton kivymd.uix.button.MDRoundFlatButton
#:import MDRoundFlatIconButton kivymd.uix.button.MDRoundFlatIconButton
#:import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton
#:import MDFillRoundFlatIconButton kivymd.uix.button.MDFillRoundFlatIconButton
#:import MDTextButton kivymd.uix.button.MDTextButton


BoxLayout:
    orientation: 'vertical'
    spacing: 15
    
    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        user_font_size: "60sp"
        
    MDFloatingActionButton:
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.5}
        elevation_normal: 8
        
    MDFlatButton:
        text: "MDFLATBUTTON"
        font_size: "18sp"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        md_bg_color: 0.5, 0.4, 0.75, 1
        
    MDRectangleFlatButton:
        text: "MDRECTANGLEFLATBUTTON"
        theme_text_color: "Custom"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        
    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRECTANGLEFLATICONBUTTON"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        icon_color: 0, 0, 0, 1
        
    MDRoundFlatButton:
        text: "MDROUNDFLATBUTTON"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        text_color: 0, 0, 0, 1
        
    MDRoundFlatIconButton:
        icon: "android"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        text_color: 0, 0, 0, 1
        text: "MDROUNDFLATICONBUTTON"
        
    MDFillRoundFlatButton:
        text: "MDFILLROUNDFLATBUTTON"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        
    MDFillRoundFlatIconButton:
        text: "MDFILLROUNDFLATICONBUTTON"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        icon: 'home'
        
    MDTextButton:
        text: "MDTEXTBUTTON"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        custom_color: 0, 0, 0, 1
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()
