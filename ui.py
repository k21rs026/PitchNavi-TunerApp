from sys import orig_argv
from tkinter.font import BOLD
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle, RoundedRectangle, Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ColorProperty, NumericProperty
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.app import App
from kivy.vector import Vector
from kivy.uix.image import Image
from kivy.metrics import dp
import math
from utils import resource_path

from calculations import GRAY, LBLUE, RED, GREEN,dgray,LIGHT_GRAY

JP = resource_path(r'assets\fonts\NotoSansJP-Regular.ttf')

class ImageButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = GRAY
        with self.canvas:
            self.image_rect = Rectangle(
                source=resource_path(r'assets\img\settingswhite.png'),
                pos=self.pos,
                size=self.size
            )
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.image_rect.pos = self.pos
        self.image_rect.size = self.size

class TunerUI(BoxLayout):
    def __init__(self, switch_to_settings_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 20
        Window.clearcolor = GRAY

        self.switch_to_settings_callback = switch_to_settings_callback
        # ---------------------start header-------------------
        self.tuner_title_layout = FloatLayout(size_hint_y=None, height=40*Window.height/480)
        self.title = Label(text="",size_hint_y=None, height=40*Window.height/480, font_name=JP)
        self.setting_button = ImageButton(size_hint=(None, 0.75), pos_hint={'center_x': 0.9,'center_y': 0.5})
        self.setting_button.bind(on_press=self.on_button_press)
        self.setting_button.bind(on_release=self.on_button_release)
        self.setting_button.bind(on_release=self.switch_to_settings)
        self.tuner_title_layout.add_widget(self.title)
        self.tuner_title_layout.add_widget(self.setting_button)
        self.tuner_title_layout.add_widget(
            Widget(size_hint=(None, 0.5), width=dp(20)))
        self.add_widget(self.tuner_title_layout)
        # ---------------------end header-------------------

        self.tuner_layout = FloatLayout()
        add_rounded_background3(self,self.tuner_layout)
        self.music=resource_path(r'assets\fonts\NotoMusic-Regular.ttf')
        
        self.noteFreq = Label(size_hint=(None,None),halign='center',valign='middle',font_name=JP)
        self.tuner_layout.add_widget(self.noteFreq)
        self.note = Label(size_hint=(None,None), halign='center',valign='middle',font_name=JP)
        self.shownoteflat=Label(size_hint=(None,None), halign='center',valign='middle',font_name=JP)
        self.shownotesharp=Label(size_hint=(None,None), halign='center',valign='middle',font_name=self.music)
        self.tuner_layout.add_widget(self.shownotesharp)
        self.tuner_layout.add_widget(self.note)
        self.freq_label = Label(text='', size_hint=(None, None), font_name=JP, halign='center',valign='middle')
        self.tuner_layout.add_widget(self.freq_label)
        with self.canvas:
            self.rect_color = Color(0.9255, 0.7098, 0.4627, 0.5)
            self.rect = RoundedRectangle(radius=[30])
            #self.rect2 =RoundedRectangle(radius=[30])
            self.marks_color = Color(0, 0, 0, 1)
            self.leftbigmark = Line(points=[], width=1)
            self.rightbigmark = Line(points=[], width=1)
            self.leftfirstmark = Line(points=[], width=1)
            self.rightfirstmark = Line(points=[], width=1)
            self.leftsecondmark = Line(points=[], width=1)
            self.rightsecondmark = Line(points=[], width=1)
            self.leftthirdmark = Line(points=[], width=1)
            self.rightthirdmark = Line(points=[], width=1)
            self.leftfourthmark = Line(points=[], width=1)
            self.rightfourthmark = Line(points=[], width=1)
            
            self.leftbigmark2 = Line(points=[], width=1)
            self.rightbigmark2 = Line(points=[], width=1)
            self.leftfirstmark2 = Line(points=[], width=1)
            self.rightfirstmark2 = Line(points=[], width=1)
            self.leftsecondmark2 = Line(points=[], width=1)
            self.rightsecondmark2 = Line(points=[], width=1)
            self.leftthirdmark2 = Line(points=[], width=1)
            self.rightthirdmark2 = Line(points=[], width=1)
            self.leftfourthmark2 = Line(points=[], width=1)
            self.rightfourthmark2 = Line(points=[], width=1)

            self.leftsecondbigmark = Line(points=[], width=1)
            self.rightsecondbigmark = Line(points=[], width=1)
            self.leftfifthmark = Line(points=[], width=1)
            self.rightfifthmark = Line(points=[], width=1)
            self.leftsixthmark = Line(points=[], width=1)
            self.rightsixthmark = Line(points=[], width=1)
            self.leftseventhmark = Line(points=[], width=1)
            self.rightseventhmark = Line(points=[], width=1)
            self.lefteighthmark = Line(points=[], width=1)
            self.righteighthmark = Line(points=[], width=1)

            self.leftsecondbigmark2 = Line(points=[], width=1)
            self.rightsecondbigmark2 = Line(points=[], width=1)
            self.leftfifthmark2 = Line(points=[], width=1)
            self.rightfifthmark2 = Line(points=[], width=1)
            self.leftsixthmark2 = Line(points=[], width=1)
            self.rightsixthmark2 = Line(points=[], width=1)
            self.leftseventhmark2 = Line(points=[], width=1)
            self.rightseventhmark2 = Line(points=[], width=1)
            self.lefteighthmark2 = Line(points=[], width=1)
            self.righteighthmark2 = Line(points=[], width=1)

            self.middlemark2 = Line(points=[], width=1)
            self.middlemark = Line(points=[], width=1)

            self.line_color = Color(0, 0, 0, 1)
            self.needle_line = Line(points=[], width=2)
            self.needle_line2 = Line(points=[], width=2)
        self.octave_label = Label(size_hint=(None,None), halign='center',valign='middle', font_name=JP)
        self.tuner_layout.add_widget(self.octave_label)
        self.flat = Label(text='♭',font_name=self.music,size_hint=(None, None) , halign='center',valign='middle')
        self.tuner_layout.add_widget(self.flat)
        self.sharp = Label(text='♯', font_name=self.music,size_hint=(None,None), halign='center',valign='middle')
        
        self.tuner_layout.add_widget(self.sharp)
        self.add_widget(self.tuner_layout)
        Window.bind(on_resize=self.update_font_size)
        Clock.schedule_once(self.square, 0)

    def on_button_press(self, instance):
        self.setting_button.pos_hint={'center_y': 0.4}

    def on_button_release(self, instance):
        self.setting_button.pos_hint={'center_y': 0.5}

    def update_line(self, direction):
        self.offset=10*(Window.width/320)
        min_position = Window.width/2-self.offset*10
        max_position = Window.width/2+self.offset*10
        new_x_position = Window.width / 2 + direction
        self.setting_button.pos_hint={'x': 0.8,'center_y': 0.5}
        self.needle_x = max(min_position, min(max_position, new_x_position))
        self.line_start=(Window.height/3+Window.height*0.05)/2+Window.height*0.05/2
        self.big_line_length=20*(Window.height/480)
        self.small_line_length=10
        
        self.tuner_title_layout.height=40*Window.height/480

        self.rect.pos=(Window.width*0.1, 0.1*Window.height)
        self.rect.size=(Window.width*0.9-Window.width*0.1, Window.height/3-Window.height*0.1)

        self.rect_size_multiplier_width=max(Window.height/5,Window.width/5)
        self.rect_size_multiplier_height=min(Window.height/4.5,Window.width/4.5)
        self.size_multiplier=min(Window.height/10,Window.width/10)
        self.font_size_multiplier=min(Window.width/400,Window.height/400)

        self.flat.font_size=40*self.font_size_multiplier
        self.sharp.font_size=40*self.font_size_multiplier
        self.freq_label.font_size=20*self.font_size_multiplier
        
        self.noteFreq.font_size=30*self.font_size_multiplier
        self.octave_label.font_size=40*self.font_size_multiplier
        self.shownoteflat.font_size=40*self.font_size_multiplier
        self.shownotesharp.font_size=60*self.font_size_multiplier

        self.noteFreq.pos_hint={'center_x': .5, 'center_y': .85}
        self.note.pos_hint={'center_x': .5, 'center_y': .65}
        self.freq_label.pos_hint={'center_y': 0.4}
        self.flat.pos_hint={'center_x': .1, 'center_y': .65}
        self.sharp.pos_hint={'center_x': .9, 'center_y': .65}
        self.octave_label.pos_hint={'center_x': .9, 'center_y': .85}
        self.shownoteflat.pos_hint={'center_x': .1, 'center_y': .75}
        self.shownotesharp.pos_hint={'center_x': .65, 'center_y': .675}
        
        self.leftbigmark.points = [Window.width/2-self.offset*5, self.line_start, Window.width/2-self.offset*5, self.line_start-self.big_line_length]
        self.rightbigmark.points = [Window.width/2+self.offset*5, self.line_start, Window.width/2+self.offset*5, self.line_start-self.big_line_length]
        self.leftfirstmark.points = [Window.width/2-self.offset*4, self.line_start, Window.width/2-self.offset*4, self.line_start-self.small_line_length]
        self.rightfirstmark.points = [Window.width/2+self.offset*4, self.line_start, Window.width/2+self.offset*4, self.line_start-self.small_line_length]
        self.leftsecondmark.points = [Window.width/2-self.offset*3, self.line_start, Window.width/2-self.offset*3, self.line_start-self.small_line_length]
        self.rightsecondmark.points = [Window.width/2+self.offset*3, self.line_start, Window.width/2+self.offset*3, self.line_start-self.small_line_length]
        self.leftthirdmark.points = [Window.width/2-self.offset*2, self.line_start, Window.width/2-self.offset*2, self.line_start-self.small_line_length]
        self.rightthirdmark.points = [Window.width/2+self.offset*2, self.line_start, Window.width/2+self.offset*2, self.line_start-self.small_line_length]
        self.leftfourthmark.points = [Window.width/2-self.offset, self.line_start, Window.width/2-self.offset, self.line_start-self.small_line_length]
        self.rightfourthmark.points = [Window.width/2+self.offset, +self.line_start, Window.width/2+self.offset, self.line_start-self.small_line_length]

        self.leftbigmark2.points = [Window.width/2-self.offset*5, self.line_start, Window.width/2-self.offset*5, self.line_start+self.big_line_length]
        self.rightbigmark2.points = [Window.width/2+self.offset*5, self.line_start, Window.width/2+self.offset*5, self.line_start+self.big_line_length]
        self.leftfirstmark2.points = [Window.width/2-self.offset*4, self.line_start, Window.width/2-self.offset*4, self.line_start+self.small_line_length]
        self.rightfirstmark2.points = [Window.width/2+self.offset*4, self.line_start, Window.width/2+self.offset*4, self.line_start+self.small_line_length]
        self.leftsecondmark2.points = [Window.width/2-self.offset*3, self.line_start, Window.width/2-self.offset*3, self.line_start+self.small_line_length]
        self.rightsecondmark2.points = [Window.width/2+self.offset*3, self.line_start, Window.width/2+self.offset*3, self.line_start+self.small_line_length]
        self.leftthirdmark2.points = [Window.width/2-self.offset*2, self.line_start, Window.width/2-self.offset*2, self.line_start+self.small_line_length]
        self.rightthirdmark2.points = [Window.width/2+self.offset*2, self.line_start, Window.width/2+self.offset*2, self.line_start+self.small_line_length]
        self.leftfourthmark2.points = [Window.width/2-self.offset, self.line_start, Window.width/2-self.offset, self.line_start+self.small_line_length]
        self.rightfourthmark2.points = [Window.width/2+self.offset, +self.line_start, Window.width/2+self.offset, self.line_start+self.small_line_length]
        self.middlemark2.points = [Window.width/2, self.line_start, Window.width/2, self.line_start+self.big_line_length]

        self.leftsecondbigmark.points = [Window.width/2-self.offset*10, self.line_start, Window.width/2-self.offset*10, self.line_start-self.big_line_length]
        self.rightsecondbigmark.points = [Window.width/2+self.offset*10, self.line_start, Window.width/2+self.offset*10, self.line_start-self.big_line_length]
        self.leftfifthmark.points = [Window.width/2-self.offset*6, self.line_start, Window.width/2-self.offset*6, self.line_start-self.small_line_length]
        self.rightfifthmark.points = [Window.width/2+self.offset*6, self.line_start, Window.width/2+self.offset*6, self.line_start-self.small_line_length]
        self.leftsixthmark.points = [Window.width/2-self.offset*7, self.line_start, Window.width/2-self.offset*7, self.line_start-self.small_line_length]
        self.rightsixthmark.points = [Window.width/2+self.offset*7, self.line_start, Window.width/2+self.offset*7, self.line_start-self.small_line_length]
        self.leftseventhmark.points = [Window.width/2-self.offset*8, self.line_start, Window.width/2-self.offset*8, self.line_start-self.small_line_length]
        self.rightseventhmark.points = [Window.width/2+self.offset*8, self.line_start, Window.width/2+self.offset*8, self.line_start-self.small_line_length]
        self.lefteighthmark.points = [Window.width/2-self.offset*9, self.line_start, Window.width/2-self.offset*9, self.line_start-self.small_line_length]
        self.righteighthmark.points = [Window.width/2+self.offset*9, self.line_start, Window.width/2+self.offset*9, self.line_start-self.small_line_length]

        self.leftsecondbigmark2.points = [Window.width/2-self.offset*10, self.line_start, Window.width/2-self.offset*10, self.line_start+self.big_line_length]
        self.rightsecondbigmark2.points = [Window.width/2+self.offset*10, self.line_start, Window.width/2+self.offset*10, self.line_start+self.big_line_length]
        self.leftfifthmark2.points = [Window.width/2-self.offset*6, self.line_start, Window.width/2-self.offset*6, self.line_start+self.small_line_length]
        self.rightfifthmark2.points = [Window.width/2+self.offset*6, self.line_start, Window.width/2+self.offset*6, self.line_start+self.small_line_length]
        self.leftsixthmark2.points = [Window.width/2-self.offset*7, self.line_start, Window.width/2-self.offset*7, self.line_start+self.small_line_length]
        self.rightsixthmark2.points = [Window.width/2+self.offset*7, self.line_start, Window.width/2+self.offset*7, self.line_start+self.small_line_length]
        self.leftseventhmark2.points = [Window.width/2-self.offset*8, self.line_start, Window.width/2-self.offset*8, self.line_start+self.small_line_length]
        self.rightseventhmark2.points = [Window.width/2+self.offset*8, self.line_start, Window.width/2+self.offset*8, self.line_start+self.small_line_length]
        self.lefteighthmark2.points = [Window.width/2-self.offset*9, self.line_start, Window.width/2-self.offset*9, self.line_start+self.small_line_length]
        self.righteighthmark2.points = [Window.width/2+self.offset*9, self.line_start, Window.width/2+self.offset*9, self.line_start+self.small_line_length]

        self.middlemark.points = [Window.width/2, self.line_start, Window.width/2, self.line_start-self.big_line_length]
        self.needle_line.points = [self.needle_x, self.line_start, self.needle_x, self.line_start+self.big_line_length*2.25]
        self.needle_line2.points = [self.needle_x, self.line_start, self.needle_x, self.line_start-self.big_line_length*2.25]
        self.freq_label.center_x = float(self.needle_x)

    def update_font_size(self, instance, width, height):
        self.font_size = min(width, height) / 20  
    def square(self, dt):
        self.setting_button.width = self.setting_button.height
        self.setting_button.bind(size=self.update_size)

    def update_size(self, instance, value):
        instance.width = instance.height

    def update_size2(self, instance, value):
        instance.width = instance.height

    def switch_to_settings(self, *args):
        self.switch_to_settings_callback()

    def update_rect(self, *args):
        self.rect.size = self.root.size
        self.rect.pos = self.root.pos

def add_rounded_background3(self,layout, color=LIGHT_GRAY, radius=[15]):
    """
    Add a rounded background to any layout.

    :param layout: The layout to which the background will be added.
    :param color: The background color (default is a dark gray).
    :param radius: The radius for the rounded corners (default is 15).
    """
    with self.canvas.before:
        Color(*color)  
        layout.rect = RoundedRectangle(
            size=layout.size, pos=layout.pos, radius=radius)

    layout.bind(size=update_rect, pos=update_rect)

def add_rounded_background(layout, color=LIGHT_GRAY, radius=[15]):
    """
    Add a rounded background to any layout.

    :param layout: The layout to which the background will be added.
    :param color: The background color (default is a dark gray).
    :param radius: The radius for the rounded corners (default is 15).
    """
    with layout.canvas.before:
        Color(*color)  
        layout.rect = RoundedRectangle(
            size=layout.size, pos=layout.pos, radius=radius)
    layout.bind(size=update_rect, pos=update_rect)

def add_rounded_background2(label, color=GRAY, radius=[15]):
    """
    Add a rounded background to any layout.

    :param layout: The layout to which the background will be added.
    :param color: The background color (default is a dark gray).
    :param radius: The radius for the rounded corners (default is 15).
    """
    with label.canvas.before:
        Color(*color)  
        label.rect = RoundedRectangle(
            size=label.size, pos=label.pos, radius=radius)
    label.bind(size=update_rect, pos=update_rect)


def update_rect(self, *args):
    """
    Update the position and size of the rounded rectangle when layout size or position changes.
    """
    self.rect.size = self.size
    self.rect.pos = self.pos

class SettingsScreen(BoxLayout):
    def __init__(self, switch_to_tuner_callback, **kwargs):
        super().__init__(**kwargs)

        self.MAG_THRESH = 0
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 20
        self.switch_to_tuner_callback = switch_to_tuner_callback
        # ---------------------start header-------------------
        self.setting_title_layout = FloatLayout(size_hint_y=None, height=40)
        add_rounded_background(self.setting_title_layout)
        self.title = Label(text="Settings",
                           size_hint_y=None, height=40, font_name=JP,pos_hint={"center_x":0.5,"center_y": 0.5},bold=True,font_size=30)
        self.back_button = Button(background_normal=resource_path(r'assets\img\forwardarrow.png'),
                                  background_down=resource_path(r'assets\img\forwardarrow.png'), size_hint=(None, 1.25),pos_hint={"center_x":0.9,"center_y": 0.5})
        self.back_button.bind(on_press=self.on_button_press)
        self.back_button.bind(on_release=self.on_button_release)
        self.back_button.bind(on_release=self.switch_to_tuner)
        self.setting_title_layout.add_widget(self.title)
        self.setting_title_layout.add_widget(self.back_button)
        self.add_widget(self.setting_title_layout)
        # ---------------------end header-------------------

        # ---------------------start scrollable area-------------------
        scroll_view = ScrollView(size_hint=(1, 1))
        self.settings_layout = GridLayout(
            cols=1, size_hint_y=None, spacing=20, padding=10)
        self.settings_layout.bind(
            minimum_height=self.settings_layout.setter('height'))
        # ---------------------start sensitivity settings-------------------
        self.sensitivity_label_layout = BoxLayout(
            orientation='horizontal', size_hint_y=None, height=30, padding=10, spacing=20)
        self.sensitivity_label_layout.bind(
            minimum_height=self.sensitivity_label_layout.setter('height'))
        add_rounded_background(self.sensitivity_label_layout)
        self.sensitivity_label = Label(text='Sensitivity', halign='left', valign='center', font_name=JP,
                                       size_hint_x=1, height=50)
        self.sensitivity_label.bind(
            size=self.sensitivity_label.setter('text_size'))
        self.sensitivity_label_layout.add_widget(self.sensitivity_label)
        self.settings_layout.add_widget(self.sensitivity_label_layout)
        self.settings_slider = CustomKnob(
            min=0, max=10, value=0, step=1, size_hint=(1, None), height=50)
        self.settings_slider.bind(value=self.on_slider_value_change)
        self.sensitivity_label_layout.add_widget(self.settings_slider)
        # ---------------------end sensitivity settings-------------------

        # ---------------------start language settings-------------------
        self.language_layout = BoxLayout(
            orientation='horizontal', size_hint_y=None, height=30, padding=10, spacing=20)
        self.language_layout.bind(
            minimum_height=self.language_layout.setter('height'))
        add_rounded_background(self.language_layout)
        self.language_label = Label(text='Language', halign='left', valign='center', font_name=JP,
                                    size_hint_x=1, height=50)
        self.language_label.bind(
            size=self.language_label.setter('text_size'))
        self.language_layout.add_widget(self.language_label)
        self.language_spinner = Spinner(text='EN', values=(
            'EN', 'JP'), size_hint=(1, None), height=44,background_color=[37/255, 150/255, 190/255,1],background_normal = '',background_down = '')
        self.language_spinner.bind(text=self.on_language_select)
        self.language_layout.add_widget(self.language_spinner)
        self.settings_layout.add_widget(self.language_layout)
        # ---------------------end language settings-------------------

        # ---------------------start octave settings-------------------
        self.octave_label_layout = BoxLayout(
            orientation='horizontal', size_hint_y=None, height=30, padding=10, spacing=20)
        self.octave_label_layout.bind(
            minimum_height=self.octave_label_layout.setter('height'))
        add_rounded_background(self.octave_label_layout)
        self.octave_label = Label(
            text='Show octave number', halign='left', valign='center', height=50, font_name=JP)
        self.octave_label.bind(
            size=self.octave_label.setter('text_size'))
        self.octave_label_layout.add_widget(self.octave_label)
        Builder.load_string(KV)
        self.octave_label_checkbox = RoundedSwitch(
            size_hint=(None, None), size=(60, 30), active=True)
        self.octave_label_layout.add_widget(self.octave_label_checkbox)
        self.settings_layout.add_widget(self.octave_label_layout)
        # ---------------------end octave settings-------------------

        # ---------------------start frequency settings-------------------
        self.frequency_label_layout = BoxLayout(
            orientation='horizontal', size_hint_y=None, height=30, padding=10, spacing=20)
        self.frequency_label_layout.bind(
            minimum_height=self.frequency_label_layout.setter('height'))
        add_rounded_background(self.frequency_label_layout)
        self.frequency_label = Label(
            text='Show exact frequency', halign='left', valign='center', height=50, font_name=JP)
        self.frequency_label.bind(
            size=self.frequency_label.setter('text_size'))
        self.frequency_label_layout.add_widget(self.frequency_label)
        Builder.load_string(KV)
        self.frequency_label_checkbox = RoundedSwitch(
            size_hint=(None, None), size=(60, 30), active=True)
        self.frequency_label_layout.add_widget(self.frequency_label_checkbox)
        self.settings_layout.add_widget(self.frequency_label_layout)

        scroll_view.add_widget(self.settings_layout)
        self.add_widget(scroll_view)
        Clock.schedule_once(self.square, 0)
        # ---------------------end frequency settings-------------------

        # ---------------------end scrollable area-------------------

    def update_setting_size(self):
        self.sensitivity_label_layout.height=30*Window.height/480
        self.language_layout.height=30*Window.height/480
        self.octave_label_layout.height=30*Window.height/480
        self.frequency_label_layout.height=30*Window.height/480

    def on_slider_value_change(self, instance, value):
        self.MAG_THRESH = int(value * 500)
        if self.language_spinner.text == 'JP':
            self.sensitivity_label.text = f"感度: {int(value)}"
        else:
            self.sensitivity_label.text = f"Sensitivity: {int(value)}"

    def on_button_press(self, instance):
        self.back_button.pos_hint={"center_y": 0.4}

    def on_button_release(self, instance):
        self.back_button.pos_hint={"center_y": 0.5}

    def on_language_select(self, spinner, text):
        if text == 'JP':
            self.language_label.text = '言語'
            self.sensitivity_label.text = f'感度: {int(self.settings_slider.value)}'
            self.title.text = '設定'
            self.octave_label.text = 'オクターブ番号を表示'
            self.frequency_label.text = '正確な周波数を表示'
        else:
            self.language_label.text = 'Language'
            self.sensitivity_label.text = f'Sensitivity: {int(self.settings_slider.value)}'
            self.title.text = 'Settings'
            self.octave_label.text = 'Show octave number'
            self.frequency_label.text = 'Show exact frequency'

    def switch_to_tuner(self, *args):
        self.switch_to_tuner_callback()

    def square(self, dt):
        self.back_button.width = self.back_button.height
        self.back_button.bind(size=self.update_size)

    def update_size(self, instance, value):
        instance.width = instance.height

    def on_resize(self, window, width, height):
        for widget in self.children:
            widget.width = width
            widget.height = height

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(37/255, 150/255, 190/255)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="PitchNavi", font_size='24sp')
        layout.add_widget(self.label)
        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class CustomCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_rect, size=self.update_rect)
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(pos=self.center, size=(
                self.height * 0.4, self.height * 0.4))

    def update_rect(self, *args):
        checkbox_size = self.height * 0.4
        self.bg_rect.size = (checkbox_size, checkbox_size)
        self.bg_rect.pos = (self.center_x - checkbox_size / 2,
                            self.center_y - checkbox_size / 2)

class CustomKnob(Slider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(value=self.update_knob_position)
        self.bind(pos=self.update_knob_position)
        self.bind(size=self.update_knob_position)

    def update_knob_position(self, *args):
        """Update the music note knob position."""
        self.canvas.after.clear()
        with self.canvas.after:
            knob_radius = self.height * 0.305
            knob_x = self.value_pos[0] - knob_radius
            knob_y = self.center_y - knob_radius

            Color(1, 1, 1, 1)  
            Ellipse(pos=(knob_x, knob_y), size=(knob_radius*2, knob_radius * 2))

            ellipse_x = knob_x+knob_radius*2/3
            ellipse_y = knob_y+knob_radius*2/7
            ellipse_width = knob_radius*2/3
            ellipse_height = knob_radius*2/3
            Color(0,0,0,1)
            Ellipse(pos=(ellipse_x, ellipse_y), size=(ellipse_width, ellipse_height))

            line_x = knob_x+knob_radius*2/3.5 + ellipse_width  
            line_y_start = ellipse_y + ellipse_height / 2.5  
            line_y_end = line_y_start + knob_radius / 2  

            Line(points=[line_x, line_y_start, line_x, ((knob_y + knob_radius*2 / 7) + (knob_radius*2 / 3) / 2) + knob_radius*2 / 2], width=2)

KV = '''
<RoundedSwitch>:
    canvas.before:
        # Background rectangle for the switch
        Color:
            rgba: self.on_color if self.active else self.off_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.height / 2]

    # Knob widget inside the switch
    Label:
        id: knob
        size_hint: None, None
        size: root.height, root.height
        pos: root.x + (root.width - self.height) * int(root.active), root.y
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # White knob color
            Ellipse:
                pos: self.pos
                size: self.size
        
            Color:
                rgba: 0, 0, 0, 1  
            Ellipse:
                pos: (self.x + self.width / 3, self.y + self.height / 7) 
                size: (self.width / 3, self.height / 3) 
            Line:
                points: [(self.x + self.width / 3) + self.width / 3.5,(self.y + self.height / 7) + (self.height / 3) / 2.5,(self.x + self.width / 3) + self.width / 3.5, ((self.y + self.height / 7) + (self.height / 3) / 2) + self.height / 2]
                width: 2
'''

class RoundedSwitch(Widget):
    active = BooleanProperty(False)
    on_color = ColorProperty([37/255, 150/255, 190/255])
    off_color = ColorProperty([0.76, 0.76, 0.78, 1])
    knob_animation_duration = NumericProperty(0.1)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.active = not self.active
            knob = self.ids.knob
            
            Animation.cancel_all(knob, 'pos')
            new_x = self.x + (self.width - self.height) * int(self.active)
            anim = Animation(
                x=new_x, duration=self.knob_animation_duration, t='out_quad')
            anim.start(knob)
            return True
        return super().on_touch_down(touch)

class TitleWithRectangle(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = '40sp'
        with self.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rectangle, pos=self._update_rectangle)

    def _update_rectangle(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size