from tkinder import*



#crear las funciones

def calcular():

  horas.set(int(numeroSeg.get())//3600)

  numeros=(int(numeroSeg.get())%3600)

  minuto.set(int(numeros)//60)

  segundo.set(int(numeros.get())%60)

  

def limpiar():

    horas.set("")

    numeros.set("")

    minuto.set("")

    segundo.set("")

    

def salir():

    exit()

    

ventana = "tk"

ventana.title("conversor de segundos a horas y minutos")

ventana.geometry("380*150")

ventana.iconbitmap("818149.ico")

ventana.config("bg=#aff522")

    

#declarar las variables

numeroSeg = stringVar()

horas = stringVar()

minuto = strinVar()

segundo = stringVar()

numeros = stringVar()



#etiquetas

lblNum = label(ventana, text="ingrese el numero en segundos", font=("Arial", 10,"bold"),bg="#22eef5")

lblNum.place(x=10,y=10)



lblhrs = label(ventana, text="Horas", font=("Arial", 10,"bold"),bg="#22eef5")

lblhrs.place(x=10,y=70)



lblmin = label(ventana, text="Minutos", font=("Arial", 10,"bold"),bg="#22eef5")

lblmun.place(x=120,y=70)



lblseg = label(ventana, text="Segundos", font=("Arial", 10,"bold"),bg="#22eef5")

lbl.place(x=230,y=70)



#casillero de textos

txtnumseg = entry(ventana, textvariable=numeroSeg, font=("Arial",10,"bold"), width=40)

txtNumseg.place(x=10,y=35)

txtNemseg.focus()





txthoras = Entry(ventana, txtvariable=horas, font=("Arial",10,"bold"), width=13)  

txthoras.place(x=120,y=90)   



txtmin = Entry(ventana, txtvariable=minuto, font=("Arial",10,"bold"), width=13)  

txtmin.place(x=120,y=90)

    

txtseg = Entry(ventana, txtvariable=segundo, font=("Arial",10,"bold"), width=13)  

txtseg.place(x=230,y=90)

    

#botones

btncalcular = Button(ventana, text="calcular", command=calcular, width=8,height=3,bg= "blue")

btncalcular.place(x=300,y=20)



btnlimp = Button(ventana, text="limpiar", command=limpiar, width=10, heigth=1,bg="green", fg="black", font=("Arial",10,"bold"))

btnlimp.place(x=100,y=115)



btnsalir = Button(ventana, text="salir", command=salir, width=10, heigth=1,bg="green", fg="black", font=("Arial",10,"bold"))

btnlimp.place(x=200,y=115)

ventana.mainloop()






