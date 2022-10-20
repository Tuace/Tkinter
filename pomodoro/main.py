from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button():
    window.after_cancel(reset_button)
    canvas.itemconfig(timer_text, text="00:00")



button=Button(text="Reset") #command= reset_button)
button.grid(column=2, row=3)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button():
    global reps
    reps+=1
    work_sec= WORK_MIN =60
    short_break_sec= SHORT_BREAK_MIN *60
    long_break_sec= LONG_BREAK_MIN*60


    if reps % 8 ==0:
        count_down(long_break_sec)
        label.config(text="Break", bg=YELLOW, fg=PINK)
    elif reps %2==0:
        count_down(short_break_sec)
        label.config(text="Break", bg=YELLOW, fg=RED)
    else:
        count_down(work_sec)
        label.config(text="Work", bg=YELLOW, fg=GREEN)

    #count_down(1*60)

button=Button(text="Start", command= start_button)
button.grid(column=0, row=3)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count % 60

    if count_sec <10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
       window.after(1000, count_down, count-1 )
    else:
        start_button()
        if reps %2==0:
            check = Label(text="✔", bg=YELLOW, fg=GREEN)
            check.grid(column=1, row=3)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
label= Label(text='TIMER', font=(FONT_NAME, 35, "bold"), fg=GREEN)
label.grid(column=1,row=0)
window.title("pomadoro")
window.config(width=100,height=50, bg=YELLOW)

#window.minsize()
canvas=Canvas(width=200,height= 224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text= canvas.create_text(100,130, text ="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=2)

check=Label(text="✔",bg=YELLOW,fg=GREEN)
check.grid(column=1,row=3)




window.mainloop()
