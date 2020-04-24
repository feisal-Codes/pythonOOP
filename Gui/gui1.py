from tkinter import Tk,Label,PhotoImage,BOTTOM,RIGHT,LEFT,RIDGE

root=Tk()


peace=Label(
   master=root,
   font=('Helvetica',16,'bold italic'),
   foreground='white',
   background='black',
   padx=25,
   pady=10,
   text='Peace Begins with a smile '

   

)
peace.pack(side=BOTTOM)

Hello=Label(
   master=root,
   font=('Helvetica',16,'bold italic'),
   foreground='white',
   background='black',
   padx=25,
   pady=10,
   text='Hello ,GUI World '
)
Hello.pack(side=RIGHT)
root.mainloop()
