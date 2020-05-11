from tkinter import *

root = Tk()
root.title('Regla Cramer')

#Primera ecuacion
labelx = Label(root, text = 'X =', width=10).grid(pady=3, row=0, column=0)
capx = Entry(root, width=5).grid(padx=5, row=0, column=1)

labely = Label(root, text = 'Y =', width=10).grid(pady=5, row=0, column=2)
capy = Entry(root, width=5).grid(padx=5, row=0, column=3)

labelz = Label(root, text = 'Z =', width=10).grid(pady=5, row=0, column=4)
capy = Entry(root, width=5).grid(padx=5, row=0, column=5)

labelt = Label(root, text = 'T.I =', width=10).grid(pady=5, row=0, column=6)
capt = Entry(root, width=5).grid(padx=5, row=0, column=7)

#Segunda ecuacion
labelxu = Label(root, text = 'X =', width=10).grid(pady=3, row=1, column=0)
capxu = Entry(root, width=5).grid(padx=5, row=1, column=1)

labelyu = Label(root, text = 'Y =', width=10).grid(pady=5, row=1, column=2)
capyu = Entry(root, width=5).grid(padx=5, row=1, column=3)

labelzu = Label(root, text = 'Z =', width=10).grid(pady=5, row=1, column=4)
capyu = Entry(root, width=5).grid(padx=5, row=1, column=5)

labeltu = Label(root, text = 'T.I =', width=10).grid(pady=5, row=1, column=6)
captu = Entry(root, width=5).grid(padx=5, row=1, column=7)

#Tercera ecuacion
labelxd = Label(root, text = 'X =', width=10).grid(pady=3, row=2, column=0)
capxd = Entry(root, width=5).grid(padx=5, row=2, column=1)

labelyd = Label(root, text = 'Y =', width=10).grid(pady=5, row=2, column=2)
capyd = Entry(root, width=5).grid(padx=5, row=2, column=3)

labelzd = Label(root, text = 'Z =', width=10).grid(pady=5, row=2, column=4)
capyd = Entry(root, width=5).grid(padx=5, row=2, column=5)

labeltd = Label(root, text = 'T.I =', width=10).grid(pady=5, row=2, column=6)
captd = Entry(root, width=5).grid(padx=5, row=2, column=7)

#Botones
#calcular = Button(root, text='Calcular').grid(row=3, column=3)

root.mainloop()