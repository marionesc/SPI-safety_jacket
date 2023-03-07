from tkinter import *
from tkinter.ttk import *
from tkinter import Tk
from PIL import Image


##### DEFINITION DE COULEUR 
color_BlackGrey = ["#474a59", "#2E2E2E"]
color_white     = "#F0FFFF"
color_grey      = "#E6E6E6"
color_red       = "#a22b41"
color_green     = "#A5DF00"

user_right = 1

##### Deffinition des fontions de rappel
def alert():
    print("alerte", "Bravo!")
    
def get_right():
    if(check.get()):
        user_right = 1
        print("administrator rights; user_right :" + str(user_right))
    else : 
        user_right = 0
        print("user rights; user_right :" + str(user_right))
    return user_right

##### CREATION DE L INTERFACE GLOBALE
interface = Tk()
interface.attributes('-zoomed', True)
interface.bind('<Escape>',lambda e: interface.destroy())

interface.title("AirCraft Detection")
## Configurer pour ajouter une image de la fenetre



##### CARACTERISTIQUES GLOBALES
check = BooleanVar()


#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
# Creation de la barre de menu
menu = Menu(interface)    
menubar = Menu(interface, bg = color_BlackGrey[1], bd = 0)

# Choix du niveau d'acces --> a configurer

# (ALL RIGHTS) creation du menu "Settings"
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label = "Lauch detection", command = alert, foreground = color_grey, background = color_BlackGrey[1] )
menu1.add_command(label = "Save detection", command = alert, foreground = color_grey, background = color_BlackGrey[1])
menu1.add_checkbutton(label = "Get admin right", onvalue = 1, offvalue = 0,  variable = check, command = get_right, foreground = color_grey, background = color_BlackGrey[1] )
menu1.add_command(label="Exit", command = interface.quit, foreground = color_grey, background = color_BlackGrey[1])
menubar.add_cascade(label="Settings", menu=menu1, foreground = color_grey, background = color_BlackGrey[1])

# (ALL RIGHTS) creation du menu "View"
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="test", command = alert, foreground = color_grey, background = color_BlackGrey[1])
menubar.add_cascade(label="View", menu=menu2, foreground = color_grey, background = color_BlackGrey[1])

# (ALL RIGHTS) Creation du menu "Informations"
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About creators", command = alert, foreground = color_grey, background = color_BlackGrey[1])
menubar.add_cascade(label="Informations", menu = menu3, foreground = color_grey, background = color_BlackGrey[1])

# (ADMIN RIGHTS) Creation du menu "Configuration"
if(user_right == 1):
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Create a configuration", command=alert, foreground = color_grey, background = color_BlackGrey[1])
    menubar.add_cascade(label="Configuration", menu = menu3, foreground = color_grey, background = color_BlackGrey[1])


#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
##### Creation du cadre gauche pour les entrees d informations
cadre_info =  Canvas(interface, width = 600, height = 950, background = color_white)         
cadre_info.place(x = 1300, y = 25)



# Configuration de la couleur du background
interface.configure(menu = menubar , bg = color_BlackGrey[0])

interface.update()
interface.update_idletasks()
interface.mainloop()