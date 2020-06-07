import tkinter as tk
import numpy as np

def determinanteS():
    s = np.array([[int(capx.get()), int(capy.get()), int(capz.get())], 
                  [int(capxu.get()), int(capyu.get()), int(capzu.get())], 
                  [int(capxd.get()), int(capyd.get()), int(capzd.get())]])
    determinanteS = np.linalg.det(s)
    return var.set(round(determinanteS))

def determinanteX():
    x = np.array([[int(capt.get()), int(capy.get()), int(capz.get())], 
                  [int(captu.get()), int(capyu.get()), int(capzu.get())], 
                  [int(captd.get()), int(capyd.get()), int(capzd.get())]])
    determinanteX = np.linalg.det(x)
    return varx.set(round(determinanteX))

def determinanteY():
    y = np.array([[int(capx.get()), int(capt.get()), int(capz.get())], 
                  [int(capxu.get()), int(captu.get()), int(capzu.get())], 
                  [int(capxd.get()), int(captd.get()), int(capzd.get())]])
    determinanteY = np.linalg.det(y)
    return vary.set(round(determinanteY))

def determinanteZ():
    z = np.array([[int(capx.get()), int(capy.get()), int(capt.get())], 
                  [int(capxu.get()), int(capyu.get()), int(captu.get())], 
                  [int(capxd.get()), int(capyd.get()), int(captd.get())]])
    determinanteZ = np.linalg.det(z)
    return varz.set(round(determinanteZ))

ventana=tk.Tk()
ventana.title('Calculadora Cramer')
ventana.geometry('500x500')
ventana.configure(background='dark turquoise')

var=tk.StringVar()
varx=tk.StringVar()
vary=tk.StringVar()
varz=tk.StringVar()

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

l=tk.Label(ventana, text='T 1:', bg='pink',  fg='white')
l.pack(side=tk.LEFT)
capt=tk.Entry(ventana, width=5)
capt.pack(side=tk.LEFT)

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

l9=tk.Label(ventana, text='T 2:', bg='pink',  fg='white')
l9.pack(side=tk.LEFT)
captu=tk.Entry(ventana, width=5)
captu.pack(side=tk.LEFT)

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

l10=tk.Label(ventana, text='T 3:', bg='pink',  fg='white')
l10.pack(side=tk.LEFT)
captd=tk.Entry(ventana, width=5)
captd.pack(side=tk.LEFT)

#Boton Determinantes
botdet = tk.Button(ventana, text='S', fg='blue', command=determinanteS)
botdet.pack(side=tk.TOP)

botdetx = tk.Button(ventana, text='X', fg='blue', command=determinanteX)
botdetx.pack(side=tk.TOP)

botdety = tk.Button(ventana, text='Y', fg='blue', command=determinanteY)
botdety.pack(side=tk.TOP)

botdetz = tk.Button(ventana, text='Z', fg='blue', command=determinanteZ)
botdetz.pack(side=tk.TOP)

#Botones 

#Resultado label
res=tk.Label(ventana, textvariable=var, padx=5, pady=5, width=50)
res.pack()

rex=tk.Label(ventana, textvariable=varx, padx=5, pady=5, width=50)
rex.pack()

rey=tk.Label(ventana, textvariable=vary, padx=5, pady=5, width=50)
rey.pack()

rez=tk.Label(ventana, textvariable=varz, padx=5, pady=5, width=50)
rez.pack()

ventana.mainloop()