import tkinter as tk
screen = tk.Tk()
screen.geometry("500x600")
screen.config(bg="grey")
screen.title("Multiplication Calculator")
def GenerateTable():
    number = int(entry1.get())
    range1 = selection.get()
    l1.delete(0, tk.END)
    for i in range(1, range1+1):
        result= str(number)+"x"+ str(i)+ "=" +str(number*i)
        l1.insert(tk.END, result)
        
    

    


label1 = tk.Label(text="Mulplication Table Generator", width=30, height = 2,bg="grey",font=("Arial", 14) )
label1.place(x= 50, y=50)
label2= tk.Label(text="Enter your number here:", width=30, height=2, bg="grey", font=("Arial",14))
label2.place(x=10,y=120)
entry1 = tk.Entry(width = 30)
entry1.place(x=300, y=120)
button1 = tk.Button(text= "Generate", bg="lightblue", width = 25,height=1, command= GenerateTable)
button1.place(x=100,y=180)

l1 = tk.Listbox(width = 30, height = 30)
l1.place(x=100,y=320)
selection = tk.IntVar()
r1 = tk.Radiobutton(text="10", value=10, variable= selection )
r1.place(x=250, y=280)
r2 = tk.Radiobutton(text="20", value=20, variable = selection)
r2.place(x=350, y=280)
r3 = tk.Radiobutton(text="30", value=30, variable = selection)
r3.place(x=450, y=280)
label3 = tk.Label(text= "Select your range", width=30 ,height=2, font=("Arial", 12), bg="grey")
label3.place(x=-30,y=280)

#create a label select your range 
#greate three radiobuttons infroint of it
#10,20,30
screen.mainloop()