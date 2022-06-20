from tkinter import *

import pandas as pandas
import random
from pandas import *

try:

    with open("data/words_to_learn.csv", encoding='utf-8') as f:
         list_of_words = pandas.read_csv(f)
         list = list_of_words.to_dict(orient="records")

except FileNotFoundError:

    with open("data/french_words.csv", encoding='utf-8') as f:
         list_of_words = pandas.read_csv(f)
         list = list_of_words.to_dict(orient="records")




print(list)
#dictionary to allow the french/english words to link across functions
word_on_card = {}



def next_card():
    '''function to change to the next card'''
    global word_on_card, flip_timer
    # reset the timer to start another 3 secs
    window.after_cancel(flip_timer)
    word_on_card = (random.choice(list))
    canvas.itemconfigure(upper_word, text="French", fill="black")
    canvas.itemconfigure(lower_word, text=word_on_card["French"], fill="black")
    canvas.itemconfigure(card, image=card_front)
    # start another timer
    flip_timer = window.after(3000, flip)

def flip():
    '''function to show the english version of the word'''
    global word_on_card
    canvas.itemconfigure(upper_word, text="English", fill="white")
    canvas.itemconfigure(lower_word, text=word_on_card["English"], fill="white")
    canvas.itemconfigure(card, image=card_back)

def tick_to_know():
    '''remove the word from the list and update csv'''
    # save words to learn to a csv called word_to_learn.csv
    global word_on_card
    list.remove(word_on_card)
    canvas.itemconfigure(remaining, text=f"words to learn: {len(list)}")
    data = pandas.DataFrame(list)
    print(data)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#--UI

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)
tick = PhotoImage(file="images/right.png")
cross = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#image
card = canvas.create_image(400, round(526/2), image=card_front)
upper_word = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
lower_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
remaining = canvas.create_text(100, 30, text=f"words to learn: {len(list)}", font=("Arial", 12, "normal"))
canvas.grid(row=0, column=0, columnspan=2)

button_cross = Button(image=cross, highlightthickness=0, width=100, height=100, command=next_card)
button_cross.grid(row=1, column=0)

button_tick = Button(image=tick, highlightthickness=0, width=100, height=100, command=tick_to_know)
button_tick.grid(row=1, column=1)

next_card()



window.mainloop()