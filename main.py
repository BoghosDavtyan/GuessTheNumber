from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from random import randint

class GuessTheNumber(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.target_number = randint(1, 100)
        self.attempts = 0

        self.info_label = Label(text="I'm thinking of a number between 1 and 100.")
        self.add_widget(self.info_label)

        self.input = TextInput(multiline=False, input_filter='int', hint_text='Enter your guess')
        self.add_widget(self.input)

        self.guess_button = Button(text='Guess', on_press=self.check_guess)
        self.add_widget(self.guess_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

        self.new_game_button = Button(text='New Game', on_press=self.new_game)
        self.add_widget(self.new_game_button)

    def check_guess(self, instance):
        try:
            guess = int(self.input.text)
            self.attempts += 1

            if guess < self.target_number:
                self.result_label.text = f'Too low! Attempts: {self.attempts}'
            elif guess > self.target_number:
                self.result_label.text = f'Too high! Attempts: {self.attempts}'
            else:
                self.result_label.text = f'Correct! You guessed it in {self.attempts} attempts.'
                self.guess_button.disabled = True

        except ValueError:
            self.result_label.text = 'Please enter a valid number.'

        self.input.text = ''

    def new_game(self, instance):
        self.target_number = randint(1, 100)
        self.attempts = 0
        self.info_label.text = "I'm thinking of a number between 1 and 100."
        self.result_label.text = ''
        self.guess_button.disabled = False
        self.input.text = ''

class GuessTheNumberApp(App):
    def build(self):
        return GuessTheNumber()

if __name__ == '__main__':
    GuessTheNumberApp().run()