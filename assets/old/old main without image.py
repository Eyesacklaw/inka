import os
import tkinter as tk
import create

def UseFilePath():
    global path
    path = "files/" + file.get("1.0", "end-1c")
    try:
        open(path, "r").read()
    except:
        open(path, "x")
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

# Settings
root = tk.Tk()
root.wm_attributes("-fullscreen", True)
root.iconbitmap('assets/icon.ico')
root.title("Inka")
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
DEFAULT_FONT = ("Heveltica", 10)

# Widgets

name = tk.Label(root, text="Inka - Problem Generator", font=("Courier", 20))
name.place(x=(SCREEN_WIDTH/2), y=0, anchor="n")

file_text = tk.Label(root, text="File Path:", font=DEFAULT_FONT)
file_text.place(x=(SCREEN_WIDTH/8), y=50, anchor="n")

file = tk.Text(root, height=1, width=90)
file.place(x=(SCREEN_WIDTH/2), y=50, anchor="n")

file_path_button = tk.Button(root, text="Use File Path", font=DEFAULT_FONT, command=UseFilePath)
file_path_button.place(x=((SCREEN_WIDTH/4)*3.125), y=75, anchor="n")

question_list = tk.Text(root, height=8, width=90)
question_list.place(x=(SCREEN_WIDTH/2), y=110, anchor="n")

save_file_button = tk.Button(root, text="Save", font=DEFAULT_FONT, command=Save)
save_file_button.place(x=((SCREEN_WIDTH/4)*3.2), y=250, anchor="n")

clear = tk.Button(root, text="Clear", font=DEFAULT_FONT, command=Clear)
clear.place(x=((SCREEN_WIDTH/16)*3.2), y=250, anchor="n")

display_file_button = tk.Button(root, text="Display Files", font=DEFAULT_FONT, command=DisplayFiles)
display_file_button.place(x=(SCREEN_WIDTH/2), y=280, anchor="n")

file_list = tk.Text(root, height=5, width=90)
file_list.place(x=(SCREEN_WIDTH/2), y=310, anchor="n")

specify_questions_text = tk.Label(root, text="Questions (e.g. 6,9):", font=DEFAULT_FONT)
specify_questions_text.place(x=(SCREEN_WIDTH/8), y=410, anchor="n")

specified_questions = tk.Text(root, height=1, width=90)
specified_questions.place(x=(SCREEN_WIDTH/2), y=410, anchor="n")

reps_text = tk.Label(root, text="Repeats:", font=DEFAULT_FONT)
reps_text.place(x=(SCREEN_WIDTH/8), y=450, anchor="n")

reps = tk.Text(root, height=1, width=2)
reps.place(x=((SCREEN_WIDTH/16)*3), y=450, anchor="n")

generate_questions_button = tk.Button(root, text="Generate Questions", font=DEFAULT_FONT, command=GenerateQuestions)
generate_questions_button.place(x=((SCREEN_WIDTH/4)*3.075), y=450, anchor="n")

root.mainloop()