from kivy.core.window import Window
from kivy.app import App
from ui import TunerUI, SettingsScreen, LoadingScreen
import pyaudio
import numpy as np
from audio import AudioProcessor  
import time 
from calculations import CHUNK, GREEN, RATE, RED, WHITE, ZERO_PADDING, getCloser, getNote, FORMAT, CHANNELS, BUFFER_TIMES, GRAY, TARGET_FREQUENCY, FREQUENCY_RANGE, ANGLE_RANGE,ORANGE
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

class PitchNavi(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.audio = AudioProcessor(CHUNK, RATE, ZERO_PADDING, BUFFER_TIMES)
        self.time = time

    def build(self):
        Window.size = (320, 480)
        #Window.size=(2360/2,1640/2)
        self.sm = ScreenManager()

        self.loading_screen = LoadingScreen(name='loading')
        
        
        # Add loading screen
        

        self.tuner_screen = TunerUI(self.switch_to_settings)
        self.settings_screen = SettingsScreen(self.switch_to_tuner)
        self.sm.add_widget(self.loading_screen)
        screen1 = Screen(name='tuner')
        screen1.add_widget(self.tuner_screen)
        self.sm.add_widget(screen1)

        screen2 = Screen(name='settings')
        screen2.add_widget(self.settings_screen)
        self.sm.add_widget(screen2)
        #Clock.schedule_once(self.show_loading_screen, 0.1)
        self.sm.current = 'loading'
        Clock.schedule_once(self.start_tuner, 3)
        #self.start_tuner(self)

        return self.sm

    def show_loading_screen(self, dt):
        self.sm.current = 'loading'
        Clock.schedule_once(self.start_tuner, 3)  

    def switch_to_settings(self):
        Window.clearcolor = GRAY
        self.sm.current = 'settings'

    def switch_to_tuner(self):
        self.sm.current = 'tuner'
        Window.clearcolor = GRAY
        
    def start_tuner(self, instance):
        self.stream = self.p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=self.audio_callback)
        self.stream.start_stream()
        self.sm.current = 'tuner'

    def audio_callback(self, data, frame, time, status):
        signal = np.frombuffer(data, dtype=np.int16)
        freq, mag = self.audio.process_audio(signal)
        #print(mag)
        pixel = 10*(Window.width/320)
        note, sharp,octave,noteFreq = getNote(freq)

        #self.tuner_screen.freq_label.color=(0,0,0,1)
        
        if mag > self.settings_screen.MAG_THRESH:

            
            

            if self.settings_screen.language_spinner.text=='JP':
                if note == 'C':
                    note = 'ド'
                elif note == 'C#':
                    note = 'ド#'
                elif note == 'D':
                    note = 'レ'
                elif note == 'D#':
                    note = 'レ#'
                elif note == 'E':
                    note = 'ミ'
                elif note == 'F':
                    note = 'ファ'
                elif note == 'F#':
                    note = 'ファ#'
                elif note == 'G':
                    note = 'ソ'
                elif note == 'G#':
                    note = 'ソ#'
                elif note == 'A':
                    note = 'ラ'
                elif note == 'A#':
                    note = 'ラ#'
                elif note == 'B':
                    note = 'シ'
            else:
                note

            status = getCloser(freq, noteFreq)
            
            freq_difference = freq - noteFreq
            direction = freq_difference * pixel
            window_size = Window.size
            #print(f"Current window size: {window_size}")

            Clock.schedule_once(lambda dt: self.tuner_screen.update_line(direction))
            Clock.schedule_once(lambda dt: self.update_font())
            if self.settings_screen.frequency_label_checkbox.active==True:
                self.tuner_screen.freq_label.text = f"{freq:.2f} Hz"
            else:
                self.tuner_screen.freq_label.text = ""
            
            if self.settings_screen.octave_label_checkbox.active==True:
                self.tuner_screen.octave_label.text = f"{octave}"
            else:
                self.tuner_screen.octave_label.text = ""
            

            #print(mag)

            if status == 1:
                #if sharp=='n':
                    #self.tuner_screen.shownotesharp.text=''
                #elif sharp=='#':
                    #self.tuner_screen.shownotesharp.text='♯'
                    #self.tuner_screen.shownotesharp.color=RED
                
                self.tuner_screen.flat.color = WHITE
                self.tuner_screen.sharp.color = RED  
                self.tuner_screen.note.color = RED 
                self.tuner_screen.freq_label.color = RED
                self.tuner_screen.noteFreq.color = RED
                self.tuner_screen.octave_label.color = RED
            elif status == -1:

                #if sharp=='n':
                    #self.tuner_screen.shownotesharp.text=''
                #elif sharp=='#':
                    #self.tuner_screen.shownotesharp.text='♯'
                    #self.tuner_screen.shownotesharp.color=RED
                self.tuner_screen.sharp.color = WHITE
                self.tuner_screen.flat.color = RED
                self.tuner_screen.note.color = RED
                self.tuner_screen.freq_label.color = RED
                self.tuner_screen.noteFreq.color = RED
                self.tuner_screen.octave_label.color = RED
            elif status == -2:

                #if sharp=='n':
                    #self.tuner_screen.shownotesharp.text=''
                #elif sharp=='#':
                    #self.tuner_screen.shownotesharp.text='♯'
                    #self.tuner_screen.shownotesharp.color=ORANGE
                self.tuner_screen.sharp.color = WHITE
                self.tuner_screen.flat.color = ORANGE
                self.tuner_screen.note.color = ORANGE
                self.tuner_screen.freq_label.color = ORANGE
                self.tuner_screen.noteFreq.color = ORANGE
                self.tuner_screen.octave_label.color = ORANGE
            elif status == 2:
                #if sharp=='n':
                    #self.tuner_screen.shownotesharp.text=''
                #elif sharp=='#':
                    #self.tuner_screen.shownotesharp.text='♯'
                    #self.tuner_screen.shownotesharp.color=ORANGE
                self.tuner_screen.flat.color = WHITE
                self.tuner_screen.sharp.color = ORANGE
                self.tuner_screen.note.color = ORANGE
                self.tuner_screen.freq_label.color = ORANGE
                self.tuner_screen.noteFreq.color = ORANGE
                self.tuner_screen.octave_label.color = ORANGE
            else:
                #if sharp=='n':
                    #self.tuner_screen.shownotesharp.text=''
                #elif sharp=='#':
                    #self.tuner_screen.shownotesharp.text='♯'
                    #self.tuner_screen.shownotesharp.color=GREEN
                self.tuner_screen.sharp.color = WHITE
                self.tuner_screen.flat.color = WHITE
                self.tuner_screen.note.color = GREEN
                self.tuner_screen.freq_label.color = GREEN
                self.tuner_screen.noteFreq.color = GREEN
                self.tuner_screen.octave_label.color = GREEN
            if sharp=='n':
                self.tuner_screen.note.text=f"{note}"
            else:
                self.tuner_screen.note.text = f"{note}{sharp}"
            self.tuner_screen.noteFreq.text = f"{noteFreq:.2f} Hz"
        else:
            mag=0
            freq_difference = 0
            direction = freq_difference * pixel
            Clock.schedule_once(lambda dt: self.tuner_screen.update_line(direction))
            Clock.schedule_once(lambda dt: self.update_font())
            self.tuner_screen.sharp.color = WHITE
            self.tuner_screen.flat.color = WHITE
            self.tuner_screen.note.color = WHITE
            self.tuner_screen.freq_label.color = WHITE
            self.tuner_screen.noteFreq.color = WHITE
            self.tuner_screen.octave_label.color = WHITE
            self.tuner_screen.note.text = f"--"
            self.tuner_screen.noteFreq.text = f"-- Hz"
            if self.settings_screen.frequency_label_checkbox.active==True:
                self.tuner_screen.freq_label.text = f"-- Hz"
            else:
                self.tuner_screen.freq_label.text = ""
            if self.settings_screen.octave_label_checkbox.active==True:
                self.tuner_screen.octave_label.text = f"-"
            else:
                self.tuner_screen.octave_label.text = ""
            
        return data, pyaudio.paContinue
    
    def update_font(self):
        self.settings_screen.setting_title_layout.height=40*Window.height/480
        self.settings_screen.back_button.pos_hint={"center_x":0.9,"center_y": 0.5}
        self.tuner_screen.setting_button.pos_hint={"center_x":0.9,"center_y": 0.5}
        if self.settings_screen.language_spinner.text=='JP':
            self.tuner_screen.note.font_size=60*min(Window.width/400,Window.height/400)
        else:
            self.tuner_screen.note.font_size=90*min(Window.width/400,Window.height/400)
    def stop_tuner(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

    def on_stop(self):
        self.stop_tuner()