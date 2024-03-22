from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Detecting Cardiovuscular Symptomps")
root.configure(background = "red")
root.geometry("800x800")

question1_radioButton = StringVar(value = "0")
Question1 = Label(root, text = "Do you experience shortness of breath during routine activities?")
Question1.pack()
question1_r1 = Radiobutton(root, text = "Yes", variable = question1_radioButton, value = "Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "No", variable = question1_radioButton, value = "No")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Do you have sweeling in feet/ankle/legs(shoes feel tighter) or abdomen?")
Question2.pack()
question2_r1 = Radiobutton(root, text = "Yes", variable = question2_radioButton, value = "Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "No", variable = question2_radioButton, value = "No")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "Do you feel any of these symptoms:- Confusion, Disorientation or Loss of Memory?")
Question3.pack()
question3_r1 = Radiobutton(root, text = "Yes", variable = question3_radioButton, value = "Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "No", variable = question3_radioButton, value = "No")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")
Question4 = Label(root, text = "Do you experience shortness of breath while at rest/lying down?")
Question4.pack()
question4_r1 = Radiobutton(root, text = "Yes", variable = question4_radioButton, value = "Yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "No", variable = question4_radioButton, value = "No")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")
Question5 = Label(root, text = "Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus?")
Question5.pack()
question5_r1 = Radiobutton(root, text = "Yes", variable = question5_radioButton, value = "Yes")
question5_r1.pack()
question5_r2 = Radiobutton(root, text = "No", variable = question5_radioButton, value = "No")
question5_r2.pack()

def cardiovuscular_score():
    score = 0
    if question1_radioButton.get()=="Yes":
       score = score + 10
       print(score)
    if question2_radioButton.get()=="Yes":
       score = score + 10
       print(score)
    if question3_radioButton.get()=="Yes":
       score = score + 10
       print(score)
    if question4_radioButton.get()=="Yes":
       score = score + 10
       print(score)
    if question5_radioButton.get()=="Yes":
       score = score + 10
       print(score)
       
    if score <= 10:
         messagebox.showinfo("Report", "You don`t need to vist the doctor.")
    elif score > 10 and score <= 30:
         messagebox.showinfo("Report", "You might perhaps visit a doctor")
    else :
         messagebox.showinfo("Report", "I strongly advise you to visit a doctor")
        
btn = Button(root, text = "Click Me", command = cardiovuscular_score, bg = "blue", fg = "white")
btn.pack()

root.mainloop()