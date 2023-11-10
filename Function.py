"""
File: calculator.py
Author: GUNDUZ Maxime
Date: 2023
Description: Contient les Fonction nécessaire pour la calculatrice.
"""


import tkinter 
from tkinter import Label
from tkinter import messagebox

# Fonction creation button
def create_button():
    nb = 1  
    operande = ["0", "=", "+", "-", "/", "*", "C"]
    
    for i in range(3):
        for j in range(3):   
            button = tkinter.Button(
                root,
                text=str(nb),
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda nb=nb: create_calcul(str(nb))
                )
            button.grid(row=2 - i, column=j)

            if nb == 3 : 

                # Bouton C
                btn = tkinter.Button(
                root,
                text=operande[6],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[6]: create_calcul(operand)
                )
               
                btn.grid(row=4, column=i)

                # Bouton *
                btn = tkinter.Button(
                root,
                text=operande[5],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[5]: create_calcul(operand)
                )
                
                btn.grid(row=i, column=3)

                # Bouton 0
                btn = tkinter.Button(
                root,
                text=operande[0],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[0]: create_calcul(operand)
                )
                
                btn.grid(row=4, column=i+1)

            if nb == 6 : 

                # Bouton /
                btn = tkinter.Button(
                root,
                text=operande[4],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[4]: create_calcul(operand)
                )
                
                btn.grid(row=i, column=3)

                # Bouton =
                btn = tkinter.Button(
                root,
                text=operande[1],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[1]: create_calcul(operand)
                )
                
                btn.grid(row=4, column=i+2)
            
            if nb == 9 : 

                # Bouton -
                btn = tkinter.Button(
                root,
                text=operande[3],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[3]: create_calcul(operand)
                )
                
                btn.grid(row=i, column=3)


                # Bouton +
                btn = tkinter.Button(
                root,
                text=operande[2],
                font=("Arial", 50),
                height=2,
                width=2,
                command=lambda operand=operande[2]: create_calcul(operand)
                )
               
                btn.grid(row=4, column=i)
              

            nb += 1
    
def create_text_zone():
    global text_label
    text_label = Label(root, text="Calcul : \n", font=("Arial", 20), height=7, width=10)
    text_label.grid(row=0, column=5, columnspan=4)

def update_text(calcul):

    if len(calcul) >=35:
        messagebox.showinfo("Erreur limite de caractere","Vous avez atteint la limite de caractere qui est de 35")
        calcul=""

    text = "Calcul :\n"
    for i in range(len(calcul)):
        text += calcul[i]
        if (i+1) % 7 == 0:
            text += "\n"
    

    if text[-1] == "C":
        text = "Calcul :\n"

    text_label.config(text=text)



def calculate(symbol):
    global calcul

    try:
        res = "Résultat de {} = {}".format(calcul, eval(calcul))
        messagebox.showinfo("Résulat",res)
    except SyntaxError:
        pass
    calcul = ""
    
    

def create_calcul(symbol):
    global calcul
    calcul += symbol 
    update_text(calcul)
    

    if calcul and calcul[-1] == "C":
        calcul =""

    if calcul and calcul[-1] == "=":
        calcul = calcul[:-1]
        calculate(calcul)


# Fonction principal
def main():
    #Creation fenetre
    
    global root
    root = tkinter.Tk()

    global calcul
    calcul=""
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.33)
    height = int(screen_height * 0.5)
    root.minsize(width, height)
    root.title("Calculatrice")
    root.resizable(False, False)
  
    create_button()
    create_text_zone()

    messagebox.showinfo("Auteur","Ce programme a étais réalisé par :\n- GUNDUZ Maxime \n- Github : https://github.com/MaxiyaG/\n- Date: Novembre 2023")

    root.mainloop()
