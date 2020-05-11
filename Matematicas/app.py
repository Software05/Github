import tkinter as tk
import numpy as np
def determinanteS():
    s = np.array([[int(capx.get()), int(capy.get()), int(capz.get())], [int(capxu.get()), int(capyu).get(), int(capzu.get())], [int(capxd.get()), int(capyd.get()), int(capzd.get())]])
    determinanteS = np.linalg.det(s)
    return var.set(determinanteS)

ventana=tk.Tk()
ventana.title('Calculadora Cramer')
ventana.geometry('500x500')
ventana.configure(background='dark turquoise')

var=tk.StringVar()

#Ecuacion 1
el=tk.Label(ventana, text='X 1:', bg='pink', fg='white')
el.pack(side=tk.LEFT)
capx=tk.Entry(ventana, width=5)
capx.pack(side=tk.LEFT)

el1=tk.Label(ventana, text='Y 1:', bg='pink', fg='white')
el1.pack(side=tk.LEFT)
capy=tk.Entry(ventana, width=5)
capy.pack(side=tk.LEFT)

el2=tk.Label(ventana, text='Z 1:', bg='pink',  fg='white')
el2.pack(side=tk.LEFT)
capz=tk.Entry(ventana, width=5)
capz.pack(side=tk.LEFT)

#Ecuacion 2
el3=tk.Label(ventana, text='X 2:', bg='pink',  fg='white')
el3.pack(side=tk.LEFT)
capxu=tk.Entry(ventana, width=5)
capxu.pack(side=tk.LEFT)

el4=tk.Label(ventana, text='Y 2:', bg='pink',  fg='white')
el4.pack(side=tk.LEFT)
capyu=tk.Entry(ventana, width=5)
capyu.pack(side=tk.LEFT)

el5=tk.Label(ventana, text='Z 2:', bg='pink',  fg='white')
el5.pack(side=tk.LEFT)
capzu=tk.Entry(ventana, width=5)
capzu.pack(side=tk.LEFT)

#Ecuacion 3
el6=tk.Label(ventana, text='X 3:', bg='pink',  fg='white')
el6.pack(side=tk.LEFT)
capxd=tk.Entry(ventana, width=5)
capxd.pack(side=tk.LEFT)

el7=tk.Label(ventana, text='Y 3:', bg='pink',  fg='white')
el7.pack(side=tk.LEFT)
capyd=tk.Entry(ventana, width=5)
capyd.pack(side=tk.LEFT)

el8=tk.Label(ventana, text='Z 3:', bg='pink',  fg='white')
el8.pack(side=tk.LEFT)
capzd=tk.Entry(ventana, width=5)
capzd.pack(side=tk.LEFT)

#Boton accion
botdet = tk.Button(ventana, text='suma', fg='blue', command=determinanteS)
botdet.pack(side=tk.TOP)

#Resultado label
res=tk.Label(ventana, textvariable=var, padx=5, pady=5, width=50)
res.pack()

ventana.mainloop()