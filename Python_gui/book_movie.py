#Application that lets a user book a movie



from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

#function gives feedback after booking your seat
def do_booking():
    info("Booking","Thank you for booking \n" + "Movie: "+ film_choice.value + "\nSeat type: " + seat_type.value + "\nSeat location: " + row_choice.value)

#adds a text widget
app = App(title = "My Second GUI app", width = 300, height = 200, layout = "grid")

#adds a text widget
film_description = Text(app, text = "Select movie to watch", grid = [0,0], align = "left")
#adds a combo widget
film_choice = Combo(app, options = ["Star Wars","Frozen","Lion King"], grid = [1,0], align = "left")
#adds a text widget
seat_type_label = Text(app, text = "Seat type", grid = [0,1], align = "left")
#adds radio button widget
seat_type = ButtonGroup(app, options = [["VIP seat","vip"],["Regular seat","regular"]], selected = "regular", horizontal = "True", grid = [1,1], align = "left") 
#adds a text widget
seat_location = Text(app, text = "Seat location", grid = [0,2], align = "left")
#adds radio button widget
row_choice = ButtonGroup(app, options = [["Front","front"],["Middle","middle"],["Back","back"]],
selected = "middle", horizontal = "True", grid = [1,2],align = "left")
#adds a button widget
book_seats = PushButton(app, command = do_booking, text = "Book seat", grid = [1,3], align = "left")
#creates the app
app.display()