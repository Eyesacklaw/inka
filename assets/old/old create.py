import random
from fpdf import FPDF
import datetime
import os

def split_string_with_tuples(text):
    result = []
    string = ""
    inside_tuple = ""
    in_tuple = False
    for i in range(len(text)):
        if not in_tuple:
            if text[i] == "<":
                in_tuple = True
                result.append(string)
                string = ""
            else:
                string += text[i]
        else:
            if text[i] == ">":
                in_tuple = False
                a = inside_tuple.split(",")
                try:
                    result.append((int(a[0]), int(a[1])))
                except:
                    result.append((int(a[0]), int(a[1][1:])))
                inside_tuple = ""
            else:
                inside_tuple += text[i]
    if string != "":
        result.append(string)
    if inside_tuple != "":
        result.append(inside_tuple)
    return result

#def split_string_with_arrays(text):
    result = []
    string = ""
    inside_array = ""
    in_array = False
    for i in range(len(text)):
        if type(text[i]) != str:
            result.append(text[i])
        else: # If it is string
            line = text[i]
            for n in range(len(line)):
                if not in_array:
                    if line[n] == "[":
                        in_array = True
                        result.append(string)
                        string = ""
                    else:
                        string += line[n]
                else:
                    if line[n] == "]":
                        in_array = False
                        result.append(inside_array.split(",")) #
                        inside_array = ""
                    else:
                        inside_array += line[n]
    if string != "":
        result.append(string)
    if inside_array != "":
        result.append(inside_array)
    print(result)

def split_string_with_arrays(text):
    result = []
    string = ""
    inside_array = ""
    in_array = False
    for i in range(len(text)):
        if type(text[i]) != str:
            result.append(text[i])
        else:
            line = text[i]
            for n in range(len(line)):
                if not in_array:
                    if line[n] == "[":
                        in_array = True
                        result.append(string)
                        string = ""
                    else:
                        string += line[n]
                else:
                    if line[n] == "]":
                        in_array = False
                        result.append(inside_array.split(","))
                        inside_array = ""
                    else:
                        inside_array += line[n]
            if string != "":
                result.append(string)
            string = "" # Reset the string variable
    if inside_array != "":
        result.append(inside_array)
    return result

def createpdf(path, questions, repeats):
    text = ""
    question_list = open(path, "r").read().splitlines()
    a = []
    temp = questions.split(",")
    # Find questions
    for i in range(len(temp)):
        try:
            a.append(int(temp[i]))
        except:
            try:
                a.append(int(str(temp[i].split(" "))[0]))
            except:
                b = temp[i].split("-")
                b_num = []
                for i in range(len(b)):
                    try:
                        b_num.append(int(b[i]))
                    except:
                        b_num.append(int(str(b_num[i].split(" ")[0])))
                a.append(b_num[0])
                while b_num[0] != b_num[-1]:
                    b_num[0] = b_num[0] + 1
                    a.append(b_num[0])
    index = []
    for i in range(len(a)):
        index.append(a[i]-1)
    count = 1
    for i in range(repeats):
        for n in range(len(index)):
            new_question = ""
            updated_question = split_string_with_tuples(question_list[index[n]])
            updated_question = split_string_with_arrays(updated_question)
            for j in range(len(updated_question)):
                if type(updated_question[j]) != tuple:
                    new_question += updated_question[j]
                else:
                    new_question += str(random.randint(updated_question[j][0], updated_question[j][1]))
            text += f"{count}. {new_question}\n\n"
            count += 1
    pdf = FPDF()
    pdf.add_page()
    now = datetime.datetime.now()
    date = now.strftime("%Y.%m.%d %H.%M")
    pdf.set_font("Arial", size = 18)
    pdf.multi_cell(190, 10, txt = f"Problem Set {date}", align="C")
    pdf.set_font("Arial", size = 10)
    pdf.multi_cell(190, 5, txt = text)
    pdf.output(f"Problem Set {date}.pdf")
    os.startfile(os.path.dirname(f"{os.getcwd()}\Problem Set {date}.pdf"))

createpdf("files/addmaths.q", "1-4", 1)