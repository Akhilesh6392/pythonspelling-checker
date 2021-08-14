from tkinter import*
from  textblob import TextBlob

def check_spelling():
    a=TextBlob(spell_check.get())
    spell = Label(window,text="the correct spelling is:",font=("Arial",30,"bold"),bg="gray")
    spell.pack()
    correct_text = Label(window,text=str(a.correct()),font=("Arial",45,"bold"),bg="orange")
    correct_text.pack()

window = Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background="lightgreen")
text_heading = Label(window, text = "Spelling Checker",font=("Arial",50,"bold"),width=500,bg="lightblue")
text_heading.pack()
text_check = Label(window, text = "Enter the text",font=("Arial",35,"bold"),bg="Yellow",fg="red")

text_check.pack()
spell_check = Entry(window, font=("Arial",45,"bold"),width=500,bg="lightblue")
spell_check.pack()

chech_button=Button(window, text="check!!",font=("Arial",30,"bold"),bg="red",fg="white",command=check_spelling)
chech_button.pack()
window.mainloop()

