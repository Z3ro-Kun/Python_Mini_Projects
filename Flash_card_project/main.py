import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


data = pd.read_csv("./data/words_to_learn.csv")
french_words = data.to_dict(orient="records")



window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width= 800, height=528, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 265, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=6)


random_number = 0


def change_word():
    global random_number, timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    random_number = random.randint(0, 100)
    canvas.itemconfig(word_text, text=french_words[random_number]["French"], fill="black")
    timer = window.after(3000, english_word)
    window.after(3005, remove_words)


def change_word2():
    global random_number, timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    random_number = random.randint(0, 100)
    canvas.itemconfig(word_text, text=french_words[random_number]["French"], fill="black")
    timer = window.after(3000, english_word)


def english_word():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=french_words[random_number]["English"], fill="white")

def remove_words():
    global random_number
    french_words.pop(random_number)
    df = pd.DataFrame(french_words)
    df.to_csv("./data/words_to_learn.csv", sep=",", index=False)






cross_img = PhotoImage(file="./images/wrong.png")
tick_img = PhotoImage(file="./images/right.png")


wrong_button = Button(highlightthickness=0, image=cross_img, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=change_word2)
wrong_button.grid(row=1, column= 1)

right_button = Button(highlightthickness=0, image=tick_img, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=change_word)
right_button.grid(row=1, column= 4)



timer = window.after(3000, english_word)
change_word()










window.mainloop()