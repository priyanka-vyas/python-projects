BACKGROUND_COLOR = "#B1DDC6"

'''1. Download the starting files from the course resources.

2. Use the images in the image folder, to create the following user interface. The ❌ and ✅ are buttons. You can add images to buttons like this:

my_image = PhotoImage(file="path/to/image_file.png")
button = Button(image=my_image, highlightthickness=0)

3. Here are some hints for the fonts, measurements and positioning.


HINTS:

1. You will need a 2 X 2 grid, with the flash card taking up 2 columns.

2. The flash card is a Canvas with 1 image and 2 pieces of text.

3. The image is card_front.png, created from the PhotoImage class. Be careful about the full image path as the image is inside the image folder.'''
# UI


# reading data
import pandas
import random

file = pandas.read_csv("data/french_words.csv")
list_of_french_words = file.values.tolist()
current_card = []
flip_timer = 0
from tkinter import *


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list_of_french_words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card[0], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card[1], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    print(type(current_card))
    len(current_card)
    if current_card in list_of_french_words:
        print(1)
    list_of_french_words.remove(current_card)
    data = pandas.DataFrame(list_of_french_words)
    data.to_csv("words_to_learn.csv")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, columnspan=2, column=0)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
button_right.grid(row=1, column=1, padx=50)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(row=1, column=0, padx=50)

next_card()
window.mainloop()
