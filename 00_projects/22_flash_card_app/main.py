from tkinter import *
import pandas
import random
import time
from tkinter import messagebox
import sys

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("00_projects/22_flash_card_app/data/french_words.csv")
except FileNotFoundError as error_message:
    print(f"No data file was found: {error_message}")
    sys.exit()

french_list = list(data.French)
english_list = list(data.English)




def flashcard():
    global img, random_french_word, english_word, canvas_image, english_text, french_text, timer, french_list, english_list
    if len(french_list) > 0:
        random_french_word = random.choice(french_list)
        english_word = english_list[french_list.index(random_french_word)]

        canvas.delete(canvas_image)

        try:
            canvas.delete(french_text, english_text)
        except NameError:
            pass

        img = PhotoImage(file="00_projects/22_flash_card_app/images/card_front.png")
        canvas_image = canvas.create_image(400, 263, image=img)

        french_text = canvas.create_text((400, 150), font=("Arial", 40, "italic"), text=random_french_word, fill="black")
        timer = window.after(3000, func=flip_card)
    else:
        reset = messagebox.askyesno(title="Game Over", message="You got all correct. Reset everything?")
        if reset:
            french_list = list(data.French)
            english_list = list(data.English)
            flashcard()
        else:
            window.quit()

def flip_card():
    global canvas_image, english_text, img, french_text

    canvas.delete(canvas_image, french_text)

    img = PhotoImage(file="00_projects/22_flash_card_app/images/card_back.png")
    canvas_image = canvas.create_image(400, 263, image=img)

    english_text = canvas.create_text((400, 263), font=("Arial", 40, "italic"), text=english_word, fill="black")
    french_text = canvas.create_text((400, 150), font=("Arial", 40, "italic"), text=random_french_word, fill="black")


    
def right():
    global random_french_word, english_word, french_list, english_list, timer
    french_list.remove(random_french_word)
    english_list.remove(english_word)
    generate_csv()
    window.after_cancel(timer)
    flashcard()

def wrong():
    global timer
    window.after_cancel(timer)
    flashcard()

def generate_csv():
    words_to_learn_dict = {
        "French": french_list,
        "English": english_list
    }
    words_to_learn = pandas.DataFrame(words_to_learn_dict)
    words_to_learn.to_csv("00_projects/22_flash_card_app/data/words_to_learn.csv", index=False)

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="00_projects/22_flash_card_app/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=img)
canvas.grid(row=0, column=0, columnspan=2)
flashcard()

left_image = PhotoImage(file="00_projects/22_flash_card_app/images/wrong.png")
left_button = Button(image=left_image, highlightthickness=0, anchor="center", command=wrong)
left_button.grid(row=1, column=0)

right_image = PhotoImage(file="00_projects/22_flash_card_app/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, anchor="center", command=right)
right_button.grid(row=1, column=1)

window.mainloop()