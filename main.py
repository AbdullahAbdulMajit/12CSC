from tkinter import * #imports codes from tkinter library
import random
from PIL import ImageTk, Image

names = []
global q_a
asked = []
score = 0



q_a = {
  1 : ["What?", 'A', 'B', 'C', 'D', 'A', 1],
  2 : ["When?", 'A', 'B', 'C', 'D', 'A', 2],
  3 : ["Where?", 'A', 'B', 'C', 'D', 'A', 3],
  4 : ["Why?", 'A', 'B', 'C', 'D', 'A', 4],
  5 : ["Who?", 'A', 'B', 'C', 'D', 'A', 5],
}



#def randomiser():
  #global qnum
  #qnum = random.randint(1,10)
  #if qnum not in asked:
    #asked.append(qnum)
  #elif qnum in asked:
    #randomiser()



class QuizIndex:
    def __init__(self, parent):
 
        background_color="orange"

        #FRAME
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()



        #ADDING IMAGES
        #self.bg_image = Image.open("ADDIMAGE.png")
        #self.bg_image =self.bg_image.resize((450,350) Image.ANTIALIAS)
        #self.bg_image = ImageTk.PhotoImage(self.bg_image)

        #LABEL FOR IMAGE
        #self.image_label = Label(self.quiz_frame, image = self.bg_image)
        #self.image_label.place(x=0, y=0, relwidth = 1, relheight = 1)



        #QUESTIONS
        #self.question_label = Label(self.quiz_frame, text = q_a[qnum][0], font = ("Helvetica", "16"), bg = background_color)
        #self.question_label.grid(row = 1, padx = 10, pady = 10)



        #RADIOBUTTONS
        #elf.var1=IntVar()

        #RADIOBUTTON 1
        #self.rb1 = Radiobutton(self.quiz_frame, text = q_a[qnum][1], font = ("Helvetica", "12"), bg = background_color, value = 1, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
        #self.rb1.grid(row = 2, sticky = W)
        
        #RADIOBUTTON 2
        #self.rb2 = Radiobutton(self.quiz_frame, text = q_a[qnum][2], font = ("Helvetica", "12"), bg = background_color, value = 2, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
        #self.rb2.grid(row = 3, sticky = W)

        #RADIOBUTTON 3
        #self.rb3 = Radiobutton(self.quiz_frame, text = q_a[qnum][3], font = ("Helvetica", "12"), bg = background_color, value = 3, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
        #self.rb3.grid(row = 4, sticky = W)

        #RADIOBUTTON 4
        #self.rb4 = Radiobutton(self.quiz_frame, text = q_a[qnum][4], font = ("Helvetica", "12"), bg = background_color, value = 4, padx = 10, pady = 10, variable = self.var1, indicator = 0, background = "light blue")
        #self.rb4.grid(row = 5, sticky = W)

        #CONFIRM BUTTON
        #self.quiz_instance = Button(self.quiz_frame, text = "confirm", font = )



        #TITLE
        self.heading_label=Label(self.quiz_frame, text="GEOGRAPHY QUIZ", font=("Times","28","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20)

        #USER INFO
        self.user_label=Label(self.quiz_frame, text="Enter your name:", font=("Helvetica","14"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #ENTRY BOX
        self.entry_box=Entry(self.quiz_frame, font=("Arial", "10"))
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #BUTTON
        self.continue_button = Button(self.quiz_frame, text="START", font=("Helvetica", "12", "bold"), bg="white", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20) 
       
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #stores input to the name list variable
        self.quiz_frame.destroy()
        


if __name__ == "__main__": #Makes the file the starter file
    root = Tk() #Creates a pop up window
    root.title("Quiz") 
    quiz_instance = QuizIndex(root)
    root.mainloop() #Keeps the window on