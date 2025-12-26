from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
# a layout that stacks items vertically/horizontally
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.popup import Popup 

#the login screen is a type of boxlayout - everything will be laid out neatly
class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation = "vertical", padding = 20, spacing = 10, **kwargs)
        #sets the layout to be vertical (top to bottom)

        self.add_widget(Label(text = "Login", font size = 26))

        self.username = TextInput(hint_text = "Enter your username", multiline = False)
        self.add_widget(self.username)
        #shows grey hint text, allows just one line

        self.password = TextInput(hint_text = "Enter your password", password = True, multiline = False)
        self.add_widget(self.password)
        #password=True hides the text or it would work same as the username

        login_btn = Button(text = "Log in")
        login_btn.bind(on_press = self.login)
        self.add_widget(self.login_btn)
        #when clicked will run the checks the login

        #function that will run once the button has been clicked
        def login(self, instance):
            if self.username.text == "Havilah" and self.password.text = "Cookies123":
                Popup(title = "Success", content = Label(text = "Logged in"), size_hint = (0.6, 0.4)).open()
            else:
                Popup(title = "Error", content = Label (text = "Incorrect details"), size_hint = (0.6, 0.4)).open()
            #shows messge to user confirming login worked


#when the app starts the login screen is showed first
class SleepHaven(App):
    def build (self):
        return LoginScreen()

#runs the program
if __name__ == "__main__":
    SleepHaven().run()
