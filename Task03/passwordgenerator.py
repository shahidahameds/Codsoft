from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.uix.popup import Popup
import random
import string

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

class PasswordGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        
        with self.canvas.before:
            Color(0, 0, 1, 1)  # Blue color
            self.blue_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        self.password_label = Label(text="Your generated password will appear here", size_hint=(1, 0.5))
        self.add_widget(self.password_label)
        
        password_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        self.add_widget(password_buttons_layout)
        
        self.generate_button = Button(text="Generate Password", size_hint=(0.7, 1))
        self.generate_button.bind(on_press=self.generate_password)
        password_buttons_layout.add_widget(self.generate_button)
        
        self.copy_button = Button(text="Copy Password", size_hint=(0.3, 1))
        self.copy_button.bind(on_press=self.copy_password)
        password_buttons_layout.add_widget(self.copy_button)
        
        self.length_input = TextInput(hint_text="Enter password length", size_hint=(1, 0.1))
        self.add_widget(self.length_input)
        
        self.popup = None
        
    def _update_rect(self, instance, value):
        self.blue_rect.pos = instance.pos
        self.blue_rect.size = instance.size
        
    def generate_password(self, instance):
        try:
            password_length = int(self.length_input.text)
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for i in range(password_length))
            self.password_label.text = generated_password
        except ValueError:
            self.password_label.text = "Please enter a valid number for password length"

    def copy_password(self, instance):
        password = self.password_label.text
        if password:
            Clipboard.copy(password)
            self.show_popup("Password copied successfully!")

    def show_popup(self, message):
        self.popup = Popup(title='Information', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        self.popup.open()

class PasswordGeneratorApp(App):
    def build(self):
        return PasswordGenerator()

if __name__ == "__main__":
    PasswordGeneratorApp().run()
