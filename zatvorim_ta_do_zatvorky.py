#importovanie modulu
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width=500,height=50)
canvas.pack()

#zadeklarovanie premennej a zoznamu
zatvorky = 0
farbicky = ["blue", "yellow", "green", "orange", "red", "pink", "brown"]

#vlozenie vstupu do premennej
vstup = input("Zadaj výraz: ")

def sherlock_holmes(): #funkcia na vyhodnotovanie uzatvorkovania a vykreslenie
    #zadeklarovanie globalnych premennych
    global vstup
    global zatvorky
    global farbicky

    #zadeklarovanie pomocnych premennych
    x = 50
    pocitadlo = -1
     
    for i in vstup: #cyklus pre znaky vo vstupe
        #ak nastane pripad nespravnej zatvorky, vypise text a skonci
        if zatvorky == -1:
            canvas.create_text(100,15,text=vstup,font="Arial 15")
            return canvas.create_text(350,40,text="Uzátvorkovanie je nesprávne",font="Arial 15")

        #pracovanie s premennou podla typu zatvorky (1=status otvorene, 0=status zatvorene)
        if i == "(":
            zatvorky += 1
        if i == ")":
            zatvorky -= 1
    
    for i in vstup:#cyklus pre znaky vo vstupe
        #pracovanie s premennou podla typu zatvorky a vyber farby podla hodnoty premennej
        if i == "(":
            pocitadlo += 1
            canvas.create_text(x,15,text=i,font="Arial 15",fill=farbicky[pocitadlo])
        if i == ")":
            pocitadlo -= 1
            canvas.create_text(x,15,text=i,font="Arial 15",fill=farbicky[pocitadlo+1])

        #pokial nie je znak zatvorka, iba vypise
        if not i == "(" and not i == ")":
            canvas.create_text(x,15,text=i,font="Arial 15")

        #zmena pomocnej premennej
        x += 10

    #vypise, ze uzatvorkovanie je spravne a ukonci program    
    return canvas.create_text(350,40,text="Uzátvorkovanie je správne",font="Arial 15")

#spustenie funkcie    
sherlock_holmes()
