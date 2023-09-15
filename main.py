from tkinter import *
window= Tk()
window.title("BMI Calculator @lockheedist")
window.minsize(400,400)
window.config(padx=50,pady=50)


def bmicalc():
    try:
        heightcm = int(entryheight.get())
        heightmt = heightcm / int(100)
        bmi = float(entryweight.get()) // float(heightmt) ** 2
        if bmi <= 18:
            finallabel.config(text=f"Your BMI Is {bmi} ,You are Underweight! ", font=("Helvetica 13"))
        elif bmi <= 24:
            finallabel.config(text=f"Your BMI Is {bmi} ,You are Healty :)", font=("Helvetica 13"))
        elif bmi <= 29:
            finallabel.config(text=f"Your BMI Is {bmi} ,You are Overweight!", font=("Helvetica 13"))
        elif bmi <= 39:
            finallabel.config(text=f"Your BMI Is {bmi} ,You are Obese!", font=("Helvetica 13"))
        else:
            finallabel.config(text=f"Your BMI Is {bmi} ,You are Extremely Obese!", font=("Helvetica 13"))
    except ValueError:
        finallabel.config(text="Please enter correct values!", font=("Helvetica 13"))


#Height Side
label1= Label(text="Height *cm")
label1.grid(row=0,column=0)
entryheight= Entry()
entryheight.grid(row=0,column=1)


#Weight Side
label2= Label(text="Weight *kg")
label2.grid(row=1,column=0)
entryweight=Entry()
entryweight.grid(row=1,column=1)


#calculate button
button= Button(command=bmicalc,text="Calculate BMI")
button.grid(row=2)


#final label
finallabel =Label(text="", font=('Helvetica 13'))
finallabel.grid(row=3,column=2)



window.mainloop()