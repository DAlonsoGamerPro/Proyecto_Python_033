from tkinter import *
import random
root = Tk()
root.title("Juego de Colores")
root.geometry("500x400")
root.config(bg="CadetBlue1")

label_score = Label(root,text="Puntos: 0",font=("Bahnschrift Light",15,"bold"),bg="CadetBlue1")
label_score.place(relx=0.1,rely=0.1,anchor=CENTER)

label_name = Label(root,font=("Arial",40),bg="CadetBlue1")
label_name.place(relx=0.5,rely=0.3,anchor=CENTER)

input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5,anchor=CENTER)

class game:
    def __init__(self):
        self.__score = 0
    
    def update_game(self):
        self.text = ["NEGRO","ROSA","VERDE","AZUL","AMARILLO","ROJO"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black","pink","green","blue","yellow","red"]
        self.random_number_for_color = random.randint(0,5)
        
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
    
    def __update_score(self,input_value):
        
        if(input_value == self.color[self.random_number_for_color]):
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(0,10)
            label_score["text"] = "Puntos: " + str(self.__score)
    
    def get_user_value(self,input_value):
        self.__update_score(input_value)
        
obj1 = game()
def get_input():
    value = input_value.get()
    obj1.get_user_value(value)
    obj1.update_game()
    input_value.delete(0,END)

btn = Button(root,text="Verificar",bg="firebrick2",padx=10,pady=1,font=("Arial",15),command=get_input)
btn.place(relx=0.35,rely=0.65,anchor=CENTER)

btn1 = Button(root,text="Iniciar",bg="goldenrod1",padx=10,pady=1,font=("Arial",15),command=obj1.update_game)
btn1.place(relx=0.65,rely=0.65,anchor=CENTER)

root.mainloop()