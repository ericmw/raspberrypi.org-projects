from guizero import App, Text, TextBox, PushButton, Slider, Picture

#displays value entered in the textbox
def say_my_name():
    welcome_message.value = my_name.value
#defines what happens when the slider is moved
def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title = "Hello World")
#adds a text widget
welcome_message = Text(app, size = 40, font = "Ravie", color = "lightblue")
#adds a textbox widget
my_name = TextBox(app, width = 30)
#adds a button widget
update_text = PushButton(app, command = say_my_name, text = "Display my name")
#adds a slider widget
text_size = Slider(app, command = change_text_size, start = 10, end = 80)
#adds picture widget
my_cat = Picture(app, image = "coding_meme.gif")

#creates the app
app.display()