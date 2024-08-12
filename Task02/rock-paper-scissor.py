from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RockPaperScissorsGame(App):
    def build(self):
        self.player_choice = None
        self.computer_choice = None
        self.result = None

        layout = RelativeLayout()

        self.result_label = Label(text="", font_size='20sp', size_hint=(0.8, None), height='100dp', pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(self.result_label)

        self.yes_button = Button(text="Yes", size_hint=(0.3, None), height='48dp', disabled=True, pos_hint={'x': 0.05, 'center_y': 0.5})
        self.yes_button.bind(on_press=self.yes_pressed)
        self.no_button = Button(text="No", size_hint=(0.3, None), height='48dp', disabled=True, pos_hint={'x': 0.35, 'center_y': 0.5})
        self.no_button.bind(on_press=self.no_pressed)
        layout.add_widget(self.yes_button)
        layout.add_widget(self.no_button)

        rock_button = Button(text="Rock", on_press=self.rock_pressed, size_hint=(0.3, None), height='48dp', pos_hint={'center_x': 0.15, 'y': 0})
        rock_button.background_color = (0, 0, 1, 1) 
        paper_button = Button(text="Paper", on_press=self.paper_pressed, size_hint=(0.3, None), height='48dp', pos_hint={'center_x': 0.5, 'y': 0})
        paper_button.background_color = (0, 0, 1, 1)
        scissors_button = Button(text="Scissors", on_press=self.scissors_pressed, size_hint=(0.3, None), height='48dp', pos_hint={'center_x': 0.85, 'y': 0})
        scissors_button.background_color = (0, 0, 1, 1) 
        layout.add_widget(rock_button)
        layout.add_widget(paper_button)
        layout.add_widget(scissors_button)

        return layout

    def determine_winner(self, player, computer):
        if player == computer:
            return "Tie"
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return "You Win!"
        else:
            return "Computer Wins!"

    def draw(self):
        self.result_label.text = f"You chose: {self.player_choice.capitalize()}\n" \
                                 f"Computer chose: {self.computer_choice.capitalize()}\n" \
                                 f"{self.result}\n\n" \
                                 f"Do you want to play again?"

        self.yes_button.disabled = False
        self.no_button.disabled = False

    def play_next_round(self):
        self.yes_button.disabled = True
        self.no_button.disabled = True

        self.player_choice = None
        self.computer_choice = None
        self.result = None
        self.result_label.text = ""

    def yes_pressed(self, instance):
        self.play_next_round()

    def no_pressed(self, instance):
        App.get_running_app().stop()

    def rock_pressed(self, instance):
        self.player_choice = 'rock'
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.result = self.determine_winner(self.player_choice, self.computer_choice)
        self.draw()

    def paper_pressed(self, instance):
        self.player_choice = 'paper'
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.result = self.determine_winner(self.player_choice, self.computer_choice)
        self.draw()

    def scissors_pressed(self, instance):
        self.player_choice = 'scissors'
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.result = self.determine_winner(self.player_choice, self.computer_choice)
        self.draw()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == "__main__":
    RockPaperScissorsGame().run()
