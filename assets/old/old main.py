import os
import tkinter as tk
import create

def UseFilePath():
    global path
    path = file.get("1.0", "end-1c")
    print(f"current path: {path}")

def AddQuestion():
    text = question.get("1.0", "end-1c")
    try:
        open(path, "a").write(f"\n{text}")
    except FileNotFoundError:
        open(path, "n").write(f"\n{text}")
    question.delete("1.0", "end")

def DisplayQuestions():
    question_array = open(path, "r").read().splitlines()
    question_list.delete("1.0", "end")
    for i in range(len(question_array)):
        question_list.insert("end", f"{i+1}. {question_array[i]}\n")
    
def DisplayFiles():
    file_list.delete("1.0", "end")
    file_array = os.listdir(".")
    for i in range(len(file_array)):
        file_list.insert("end", f"{file_array[i]}\n")

def GenerateQuestions():
    path = file.get("1.0", "end-1c")
    questions = specified_questions.get("1.0", "end-1c")
    repeats = int(reps.get("1.0", "end-1c"))
    create.createpdf(path, questions, repeats)

# Settings
root = tk.Tk()
root.wm_attributes("-fullscreen", True)
root.title("Title")
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

# Widgets

name = tk.Label(root, text="Problem Generator", font=("Helvetica", 20))
name.place(x=(SCREEN_WIDTH/2), y=0, anchor="n")

file_text = tk.Label(root, text="File Path:", font=("Helvetica", 10))
file_text.place(x=(SCREEN_WIDTH/8), y=50, anchor="n")

file = tk.Text(root, height=1, width=90)
file.place(x=(SCREEN_WIDTH/2), y=50, anchor="n")

file_path_button = tk.Button(root, text="Use File Path", command=UseFilePath)
file_path_button.place(x=((SCREEN_WIDTH/4)*3.125), y=75, anchor="n")

type_question = tk.Label(root, text="Type Question:", font=("Helvetica", 10))
type_question.place(x=(SCREEN_WIDTH/8), y=110, anchor="n")

question = tk.Text(root, height=4, width=90)
question.place(x=(SCREEN_WIDTH/2), y=110, anchor="n")

add_question_button = tk.Button(root, text="Add Question", command=AddQuestion)
add_question_button.place(x=((SCREEN_WIDTH/4)*3.125), y=180, anchor="n")

display_question_button = tk.Button(root, text="Display Questions", command=DisplayQuestions)
display_question_button.place(x=(SCREEN_WIDTH/2), y=210, anchor="n")

question_list = tk.Text(root, height=8, width=90)
question_list.place(x=(SCREEN_WIDTH/2), y=240, anchor="n")

display_file_button = tk.Button(root, text="Display Files", command=DisplayFiles)
display_file_button.place(x=(SCREEN_WIDTH/2), y=380, anchor="n")

file_list = tk.Text(root, height=5, width=90)
file_list.place(x=(SCREEN_WIDTH/2), y=410, anchor="n")

specify_questions_text = tk.Label(root, text="Questions (e.g. 6,9):", font=("Helvetica", 10))
specify_questions_text.place(x=(SCREEN_WIDTH/8), y=520, anchor="n")

specified_questions = tk.Text(root, height=1, width=90)
specified_questions.place(x=(SCREEN_WIDTH/2), y=520, anchor="n")

reps_text = tk.Label(root, text="Repeats:", font=("Helvetica", 10))
reps_text.place(x=(SCREEN_WIDTH/8), y=550, anchor="n")

reps = tk.Text(root, height=1, width=2)
reps.place(x=((SCREEN_WIDTH/16)*3), y=550, anchor="n")

generate_questions_button = tk.Button(root, text="Generate Questions", command=GenerateQuestions)
generate_questions_button.place(x=((SCREEN_WIDTH/4)*3.075), y=550, anchor="n")

root.mainloop()