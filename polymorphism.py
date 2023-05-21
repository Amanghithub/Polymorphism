from tkinter import *

root = Tk()

root.title("tk")
root.geometry("400x400")


percentage_grade_3_label = Label(root)
percentage_grade_5_label = Label(root)
percentage_grade_10_label = Label(root)

class grade3:
    def __init__(self,arts,maths):
        self.arts = arts
        self.maths = maths
        
    def percentage(self):
        totalMarks = self.arts+self.maths
        percent = (totalMarks*100)/200
        percentage_grade_3_label["text"]=percent
        

class grade5:
    def __init__(self,arts,maths,social):
        self.arts = arts
        self.maths = maths
        self.social = social
        
    def percentage(self):
        totalMarks = self.arts+self.maths+self.social
        percent = (totalMarks*100)/300
        percentage_grade_5_label["text"]=percent
        
class grade10:
    def __init__(self,arts,maths,social,science):
        self.arts = arts
        self.maths = maths
        self.social = social
        self.science = science
        
        
    def percentage(self):
        totalMarks = self.arts+self.maths+self.social+self.science
        percent = (totalMarks*100)/400
        percentage_grade_10_label["text"]=percent

grade3_obj = grade3(95,98)
grade3_btn = Button(root,text="Grade3",command=grade3_obj.percentage)
grade3_btn.pack()
percentage_grade_3_label.pack()


grade5_obj = grade5(95,98,100)
grade5_btn = Button(root,text="Grade5",command=grade5_obj.percentage)
grade5_btn.pack()
percentage_grade_5_label.pack()

grade10_obj = grade10(95,98,100,99)
grade10_btn = Button(root,text="Grade10",command=grade10_obj.percentage)
grade10_btn.pack()
percentage_grade_10_label.pack()
root.mainloop()