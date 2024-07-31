from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from random import randint, choice

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

        self.hint_label = Label(text='')
        self.add_widget(self.hint_label)

        self.new_game_button = Button(text='New Game', on_press=self.new_game)
        self.add_widget(self.new_game_button)

    def check_guess(self, instance):
        try:
            guess = int(self.input.text)
            self.attempts += 1

            if guess < self.target_number:
                self.result_label.text = f'Too low! Attempts: {self.attempts}'
                self.provide_hint()
            elif guess > self.target_number:
                self.result_label.text = f'Too high! Attempts: {self.attempts}'
                self.provide_hint()
            else:
                self.result_label.text = f'Correct! You guessed it in {self.attempts} attempts.'
                self.hint_label.text = ''
                self.guess_button.disabled = True

        except ValueError:
            self.result_label.text = 'Please enter a valid number.'

        self.input.text = ''

    def provide_hint(self):
        if self.attempts <= 3:
            self.hint_label.text = self.get_basic_hint()
        elif self.attempts <= 6:
            self.hint_label.text = self.get_medium_hint()
        else:
            self.hint_label.text = self.get_advanced_hint()

    def get_basic_hint(self):
        hints = [
            f"The number {'is' if self.target_number % 2 == 0 else 'is not'} even.",
            f"The number {'is' if self.target_number % 5 == 0 else 'is not'} divisible by 5.",
            f"The number is {'greater' if self.target_number > 50 else 'less'} than 50."
        ]
        return choice(hints)

    def get_medium_hint(self):
        hints = [
            f"The number is in the range {(self.target_number // 10) * 10} to {(self.target_number // 10) * 10 + 9}.",
            f"The sum of the digits is {sum(int(digit) for digit in str(self.target_number))}.",
            f"The number {'can' if self.target_number % 3 == 0 else 'cannot'} be divided by 3 without a remainder."
        ]
        return choice(hints)

    def get_advanced_hint(self):
        hints = [
            f"The last digit of the number is {self.target_number % 10}.",
            f"The number is {'a perfect square' if int(self.target_number ** 0.5) ** 2 == self.target_number else 'not a perfect square'}.",
            f"The number is {self.target_number - randint(1, 5)} plus a small number."
        ]
        return choice(hints)

    def new_game(self, instance):
        self.target_number = randint(1, 100)
        self.attempts = 0
        self.info_label.text = "I'm thinking of a number between 1 and 100."
        self.result_label.text = ''
        self.hint_label.text = ''
        self.guess_button.disabled = False
        self.input.text = ''

class GuessTheNumberApp(App):
    def build(self):
        return GuessTheNumber()

if __name__ == '__main__':
    GuessTheNumberApp().run()