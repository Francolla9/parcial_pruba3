import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):

        peso = self.txt_peso_articulo.get()
        tipo_peso = self.combobox_tipo_de_peso.get() 
        

        if peso != "" and not peso.isalpha() and float(peso) > 0:
            peso = float(peso) 
            if tipo_peso == "Onzas":
                peso =  peso * 28.3495
            self.lista_pesos.append(peso)
            alert("excelente","el peso ingresado es valido")
        else:
            alert("error","el peso ingresado no es valido")



    
    def btn_mostrar_on_click(self):
        contador_posicion = 0

        for peso in self.lista_pesos:
            peso_onzas = peso * 0.035274
            mensaje = "la posicion es " + str(contador_posicion) + " el peso en gramos es " + str(peso) + " y el peso en onzas es " + str(peso_onzas) 
            print(mensaje) 
            contador_posicion += 1 
        

    def btn_informar_on_click(self):
        contador_pesos = 0
        bandera = True
        peso_maximo = None
        posicion_peso_maximo = None

        for peso in self.lista_pesos:  
            if bandera == True:
                peso_maximo = peso
                posicion_peso_maximo = contador_pesos 
                bandera = False 
                continue
            
            contador_pesos +=1
            if peso_maximo < peso:
                peso_maximo = peso 
                posicion_peso_maximo = contador_pesos 
                

        peso_mas_alto = (peso_maximo * 0.035274)

        print("la posicion del peso maximo es " + str(posicion_peso_maximo) + " y su peso es " +  str(peso_mas_alto))
            
            
    #1 

       

        contador = 0 
        peso_minimo = None 
        bandera = True 
        posicion_peso_minimo = None 


        for peso in self.lista_pesos:

            if bandera == True:
                peso_minimo = peso
                posicion_peso_minimo = contador 
                bandera = False 
                continue 


            contador += 1
            if peso < peso_minimo:
                peso_minimo = peso  
                posicion_peso_minimo = contador 
                 

        

        print("el peso minimo es " + str(peso_minimo) + " y la posicion es " + str(posicion_peso_minimo))



        #2 
        contador_pesos = 0
        acumulador = 0 
        for peso in self.lista_pesos:
        
            acumulador += peso
            contador_pesos += 1


             
        promedio = acumulador / contador_pesos  

        print("el promedio es " + str(promedio * 0.035274 ))   
        

        #3 

        print("el promedio es " + str(promedio)) 


        #4 
        contador_cant_promedio = 0
        for peso in self.lista_pesos: 

            if peso > promedio:
                print(peso)
                contador_cant_promedio += 1 
        
        print("cantidad de pesos que superan al promedio " + str(contador_cant_promedio))

        #5 

        for peso in self.lista_pesos:

            if peso < promedio:
                print(peso * 0.035274)

        


        

            
              

                
                






if __name__ == "__main__":
    app = App()

    app.mainloop()