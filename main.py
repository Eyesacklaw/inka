# Python imports
import os
import tkinter as tk

# Internal imports
import create
import probability

# Matplotlib imports
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Pandas imports
import pandas as pd

# Settings
STATS_COLOR = (236/255, 236/255, 236/255)
TKINTER_BRG_C = "#F0F0F0"
BACKGROUND_COLOR = (236/255, 236/255, 236/255)
BUTTON_COLOR = "#E3E3E3"
TEXT_COLOR = "#F0F0F0"

def UseFilePath():
    global path
    path = "files/" + file.get("1.0", "end-1c")
    try:
        open(path, "r").read()
        try:
            open(f"{path}.inka", "r").read()
        except:
            open(f"{path}.inka", "x")
    except:
        open(path, "x")
        open(f"{path}.inka", "x")
    DisplayQuestions()
    DisplayFiles()

def DisplayQuestions():
    question_array = open(path, "r").read().splitlines()
    question_list.delete("1.0", "end")
    for i in range(len(question_array)):
        question_list.insert("end", f"{i+1}. {question_array[i]}\n")

def Save():
    text = question_list.get("1.0", "end-1c").splitlines()
    with open(path, "w") as f:
        for i in range(len(text)):
            try:
                if type(int(text[i][0])) == int:
                    line_of_text = text[i].split(".", 1)[1][1:]
                else:
                    line_of_text = text[i]
            except:
                line_of_text = text[i]
            f.write(f"{line_of_text}\n")
    questions = len(open(path, "r").read().splitlines())
    if len(open(f"{path}.inka").read().splitlines()) < questions: # Add 0s to the list
        with open(f"{path}.inka", "w") as f:
            for i in range(questions - len(open(f"{path}.inka").read().splitlines())):
                f.write("0\n")
    DisplayQuestions()
    DisplayFiles()
    
def Clear():
    file.delete("1.0", "end")
    question_list.delete("1.0", "end")
    file_list.delete("1.0", "end")
    specified_questions.delete("1.0", "end")
    reps.delete("1.0", "end")

def DisplayFiles():
    file_list.delete("1.0", "end")
    file_array = os.listdir("files/")
    for i in range(len(file_array)):
        file_list.insert("end", f"{file_array[i]}\n")

def GenerateQuestions():
    questions = specified_questions.get("1.0", "end-1c")
    repeats = int(reps.get("1.0", "end-1c"))
    create.createpdf(path, questions, repeats)

def GenerateBiasedQuestions():
    questions = int(repeats.get("1.0", "end-1c"))
    create.createpdf(path, probability.probability(f"{path}.inka", questions), 1)

def ShowStats():
    with open("assets/stats.inka", "r") as f:
        temp = f.read().splitlines()
        dates = []
        scores = []
        for i in range(len(temp)):
            temp2 = temp[i].split(":")
            temp2[1] = int(temp2[1])
            dates.append(temp2[0])
            scores.append(temp2[1])
    info = {"Dates": dates, "Questions": scores}
    df1 = pd.DataFrame(info)
    stats = tk.Tk()
    stats.configure(bg=TKINTER_BRG_C)
    stats.iconbitmap('assets/icon.ico')
    stats.title("Inka")
    figure = plt.Figure(figsize=(6,5), dpi=100)
    ax = figure.add_subplot(111)
    ax.axes.xaxis.set_ticks([])
    ax.set_facecolor(BACKGROUND_COLOR)
    chart_type = FigureCanvasTkAgg(figure, stats)
    chart_type.get_tk_widget().pack()
    df1 = df1[['Dates','Questions']].groupby("Dates").sum()
    df1.plot(kind='bar', color=STATS_COLOR, legend=False, ax=ax)
    ax.set_title('Stats')

# Settings
root = tk.Tk()
root.configure(bg=TKINTER_BRG_C)
root.wm_attributes("-fullscreen", True)
root.iconbitmap('assets/icon.ico')
root.title("Inka")
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
DEFAULT_FONT = ("Heveltica", 10)

# Widgets

name = tk.Label(root, text="Inka", bg=TEXT_COLOR, font=("Courier", 20))
name.place(x=(SCREEN_WIDTH/2), y=0, anchor="n")

file_text = tk.Label(root, text="File Path:", bg=TEXT_COLOR, font=DEFAULT_FONT)
file_text.place(x=(SCREEN_WIDTH/8), y=50, anchor="n")

file = tk.Text(root, height=1, width=90, bg=TEXT_COLOR)
file.place(x=(SCREEN_WIDTH/2), y=50, anchor="n")

file_path_button = tk.Button(root, text="Use File Path", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=UseFilePath)
file_path_button.place(x=((SCREEN_WIDTH/4)*3.125), y=75, anchor="n")

question_list = tk.Text(root, height=8, width=90, bg=TEXT_COLOR)
question_list.place(x=(SCREEN_WIDTH/2), y=110, anchor="n")

save_file_button = tk.Button(root, text="Save", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=Save)
save_file_button.place(x=((SCREEN_WIDTH/4)*3.2), y=250, anchor="n")

clear = tk.Button(root, text="Clear", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=Clear)
clear.place(x=((SCREEN_WIDTH/16)*3.2), y=250, anchor="n")

display_file_button = tk.Button(root, text="Display Files", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=DisplayFiles)
display_file_button.place(x=(SCREEN_WIDTH/2), y=280, anchor="n")

file_list = tk.Text(root, height=5, width=90, bg=TEXT_COLOR)
file_list.place(x=(SCREEN_WIDTH/2), y=310, anchor="n")

specify_questions_text = tk.Label(root, text="Questions (e.g. 6,9):", font=DEFAULT_FONT, bg=TEXT_COLOR)
specify_questions_text.place(x=(SCREEN_WIDTH/8), y=410, anchor="n")

specified_questions = tk.Text(root, height=1, width=90, bg=TEXT_COLOR)
specified_questions.place(x=(SCREEN_WIDTH/2), y=410, anchor="n")

reps_text = tk.Label(root, text="Repeats:", font=DEFAULT_FONT, bg=TEXT_COLOR)
reps_text.place(x=(SCREEN_WIDTH/8), y=450, anchor="n")

reps = tk.Text(root, height=1, width=2, bg=TEXT_COLOR)
reps.place(x=((SCREEN_WIDTH/16)*3), y=450, anchor="n")

generate_questions_button = tk.Button(root, text="Generate Questions", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=GenerateQuestions)
generate_questions_button.place(x=((SCREEN_WIDTH/4)*3.075), y=450, anchor="n")

freq_text = tk.Label(root, text="Random Set:", font=DEFAULT_FONT, bg=TEXT_COLOR)
freq_text.place(x=(SCREEN_WIDTH/8), y=490, anchor="n")

repeats = tk.Text(root, height=1, width=2, bg=TEXT_COLOR)
repeats.place(x=((SCREEN_WIDTH/16)*3), y=490, anchor="n")

generate_biased_questions_button = tk.Button(root, text="Generate Questions", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=GenerateBiasedQuestions)
generate_biased_questions_button.place(x=((SCREEN_WIDTH/4)*3.075), y=490, anchor="n")

show_stats_button = tk.Button(root, text="Show Stats", font=DEFAULT_FONT, bg=BUTTON_COLOR, command=ShowStats)
show_stats_button.place(x=(SCREEN_WIDTH/2), y=530, anchor="n")

root.mainloop()