# Inka

## Description:

The unofficial complement to the flashcards app "Anki", Inka works by having set questions where variables (such as the numbers, and words chosen from a set) in the question can be varied, and can generate worksheets for practising. Worksheets generated can be question specific (for example, 10 different "question 5s"), or weighted-random (i.e. If one question does not get generated this round, it will increase its chance of being generated next round). It can also be used to create "decks" of questions.

Project Structure:
- main.py
- probability.py
- create.py
- assets
    - old
          - stats
               - scores.png
          - old create open stats.py
          - old create without selection.py
          - old create.py
          - old main open stats.py
          - old main without image.py
          - old main without selection.py
          - old main.py
          - old split_string_with_arrays.py
    - Icon.ico
    - stats.inka
- files
    - Chemistry
    - Chemistry.inka
- fonts
    - NotoSansMath-Regular.cw127.pkl
    - NotoSansMath-Regular.pkl
    - NotoSansMath-Regular.ttf

## Libraries:
Uses os, tkinter, datetime and random from regular python modules (only needed to be imported and not installed).

Uses matplotlib, pandas and fpdf as external imports. 

## Getting Started
Install the necessary libraries. I am using python 3.8 to code this program. 

When the program is run, an interface will show up. 
Type in the "file path" in the space provided to open the question set. Inka uses the relative path in files, so "/files/Chemistry" can be typed as "Chemistry".

If the file does not exist, it will automatically create a new file. In our example, "Chemistry" and "Chemistry.inka" will be created, with "Chemistry" containing the questions and "Chemistry.inka" containing the number of questions that have been generated for that problem.

You can edit the questions in the text box, with the buttons "clear" and "save" to, quite self-explanatory, clear and save the file respectively. Note that to choose a number from 1-10 (i.e. varying the prompts), you simply type "<1,10>". Or choosing from a list, for example, apples, oranges, bananas, type "[apples, oranges, bananas]". 

The "Questions" prompt requires you to type in the questions you want to be generated. It can be either separated with dashes ("1-4") meaning generate questions from 1 to 4, or separated with commas ("6,9") meaning generate questions 6 and 9 only. The repeats mean how many sets of those questions to generated, so if "1-4" and "6" are inputted, then it will generate questions from 1 to 4 six times, equating to a total of 24 questions.

The random set prompt, as its name suggests, generates a random set of all the questions. So if you input "9" and there are 5 questions in the "Chemistry" file, then it will generate 45 questions, 1 through 5 nine times.

The show stats button displays a bar chart of how many questions you have practised by generating worksheets over the past days you have been using this program. 

To exit this program, close the python program or press alt-tab, then hover over the cross button with the mouse, and click it.
