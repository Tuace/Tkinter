from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
window= Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)
canvas=Canvas(width=800, height=526)
records=pandas.read_csv("C:/Users/pravi/Downloads/flash-card-project-start/data/french_words.csv")
new_record=records.to_dict(orient='records')
print(new_record)
#df=pd.DataFrame.to_dict("french_words.csv")
#DataFrame.to_dict()
def right():
    current_card= random.choice(new_record)
    canvas.itemconfig(english_title, text="French", font=("Arial", 20, "bold"))
    canvas.itemconfig(word, text=f"{current_card['French']}", font=("Arial", 30, "bold"))
    #french_title = canvas.create_text(400, 150, )
    #french_word = canvas.create_text(400, 230, t)


    #(current_card["French"])

def countdown(current_card):
    card_front_image = PhotoImage(file="C:/Users/pravi/Downloads/flash-card-project-start/images/card_back.png")

    canvas.itemconfig(english_title, text="English", font=("Arial", 20, "bold"))
    canvas.itemconfig(word, text=f"{current_card['English']}", font=("Arial", 30, "bold"))



card_front_image=PhotoImage(file="C:/Users/pravi/Downloads/flash-card-project-start/images/card_front.png")
canvas.create_image(400,263,image=card_front_image)
canvas.grid(row=0,column=1)
window.after(3000,func)
left_image=PhotoImage(file="C:/Users/pravi/Downloads/flash-card-project-start/images/wrong.png")
left_button=Button(image=left_image, highlightthickness=0, command=right)
left_button.grid(row=3,column=0, columnspan=1)
right_image=PhotoImage(file="C:/Users/pravi/Downloads/flash-card-project-start/images/right.png")
right_button=Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(row=3,column=2, columnspan=2)
english_title= canvas.create_text(400,150,text="Title",font=("Arial", 20, "bold"))
word=canvas.create_text(400,230,text="word",font=("Arial", 30, "bold"))
right()
window.mainloop()
