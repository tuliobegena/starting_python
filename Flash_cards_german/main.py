### Flash cards to train German from Portuguese. 500 words total ###

from tkinter import *
import pandas as pd
from random import randint

random_index = 0
flip_timer = False
words_to_learn = []

#----------------------------- generating words -----------------------------#

def reset():
    """
    Reset the words marked as learned, using the data from initial csv file to create the new dict.
    """
    global words_to_learn
    original_german_words = pd.read_csv("data/Top 500 german words.csv")
    original_german_words.to_csv("data/words_to_learn.csv", index=False)
    df = pd.read_csv("data/words_to_learn.csv")
    words_to_learn = df.to_dict(orient="records")
    counter_label.config(counter_label, text=f"Words to learn: {len(words_to_learn)}")
    new_random_word()

try: 
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    reset() # Create a new file to track the progress in case this file does not exist
else:
    words_to_learn = df.to_dict(orient="records")

def new_random_word():
    """
    Generate a random index to get a new card from the dict.
    Calls the function to flip the card after 3 seconds.
    """
    global random_index, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    random_index = randint(0, len(words_to_learn) - 1)
    random_word = words_to_learn[random_index]["German"]
    canvas.itemconfig(word, text=random_word, fill="black")
    canvas.itemconfig(title_lang, text="German", fill="black")
    canvas.itemconfig(card_image, image=front_image)
    flip_timer = window.after(3000, flip_card, random_index) #parameter inside parentheses caused a bug but didnt show error

#----------------------------- managing words -----------------------------#

def know():
    """
    As a word is marked as known, it is removed from the learning pool and the progress is updated.
    """
    del words_to_learn[random_index]
    update_words_to_learn = pd.DataFrame.from_dict(words_to_learn)
    update_words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    counter_label.config(counter_label, text=f"Words to learn: {len(words_to_learn)}")

#----------------------------- fliping cards -----------------------------#

def flip_card(random_index):
    """
    Flips the card, showing the translation.
    Args:
        random_index (int): uses the index from the current card.
    """
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(title_lang, fill="white", text="English")
    random_word = words_to_learn[random_index]["English"]
    canvas.itemconfig(word, fill="white", text=random_word)

#----------------------------- UI -----------------------------#
# Basic UI built with Tkinter

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash-Karten")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=front_image)
title_lang = canvas.create_text(400, 130, text="German", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=1, columnspan=2, stick=EW)

correct_button = Button(image=correct_image, highlightthickness=0, command=lambda: [know(), new_random_word()])
correct_button.grid(column=1, row=2)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_random_word)
wrong_button.grid(column=0, row=2)
reset_button = Button(text="RESET", highlightthickness=0, command=reset)
reset_button.grid(column=1, row=0)
counter_label = Label(text=f"Words to learn: {len(words_to_learn)}", font=("Arial", 28), fg="white", bg=BACKGROUND_COLOR, highlightthickness=0)
counter_label.grid(column=0, row=0)


new_random_word()

window.mainloop()