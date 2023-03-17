import os
from tkinter import *
##from tkinter.ttk import *


from tkinter import Tk

import tkinter.font as TkFont

##from PIL import Image
#                   [type_avion,    nb_rowTOT,      Nb_placeTOT,    nb_row1st,  nb_column1st,   nb_row2nd,  nb_colmn2nd]
AIRCRAFT_CONFIG =   ["Airbus A320", "27",           "168",          "10",      "4",             "17",       "6"]

##### DEFINITION DE COULEUR 
color_BlackGrey = ["#474a59", "#2E2E2E","#000000", "#222222"]
color_white     = "#F0FFFF"
color_grey      = "#E6E6E6"
color_red       = "#a22b41"
color_green     = "#A5DF00"
color_transp    = "#000001"


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

def __init__( master=None):
    Tk.frame.__init__(master, background="grey")


##### CREATION DE L INTERFACE GLOBALE
interface = Tk()

#Adding transparent background property
interface.wm_attributes('-transparentcolor', '#000001')

interface.geometry("1900x1200")
#interface.attributes('-fullscreen', True )
interface.bind('<Escape>',lambda e: interface.destroy() )

interface.title("AirCraft Detection")
interface.iconbitmap('C:\\Users\\mario\\Desktop\\GitHub\\SPI-safety_jacket\\IHM\\files\\SPI_Logo.ico')
## Configurer pour ajouter une image de la fenetre



##### CARACTERISTIQUES GLOBALES
check = BooleanVar()


#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
# Creation de la barre de menu
menu = Menu(interface)    
menubar = Menu(interface, background = color_BlackGrey[0], bd = 0)

policemenu_1 = TkFont.Font( size=50, family='Arial', weight=TkFont.BOLD, slant=TkFont.ITALIC)
policemenu_2 = TkFont.Font( size=10, family='Arial')
# Choix du niveau d'acces --> a configurer

# (ALL RIGHTS) creation du menu "Settings"
menu1 = Menu(menubar, tearoff=0, background = color_BlackGrey[0], foreground = color_white, font = policemenu_1)
menu1.add_command(label = "Lauch detection", command = alert, foreground = color_grey, background = color_BlackGrey[1], font = policemenu_2)
menu1.add_command(label = "Save detection", command = alert, foreground = color_grey, background = color_BlackGrey[1], font = policemenu_2)
menu1.add_checkbutton(label = "Get admin right", onvalue = 1, offvalue = 0,  variable = check, command = get_right, foreground = color_grey, background = color_BlackGrey[1], font = policemenu_2 )
menu1.add_command(label="Exit", command = interface.quit, foreground = color_grey, background = color_BlackGrey[1], font = policemenu_2)
menubar.add_cascade(label="Settings", menu=menu1, foreground = color_grey, background = color_BlackGrey[1], font = policemenu_2)

# (ALL RIGHTS) creation du menu "View"
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="test", command = alert, foreground = color_grey, background = color_BlackGrey[0])
menubar.add_cascade(label="View", menu=menu2, foreground = color_grey, background = color_BlackGrey[0])

# (ALL RIGHTS) Creation du menu "Informations"
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About creators", command = alert, foreground = color_grey, background = color_BlackGrey[0])
menubar.add_cascade(label="Informations", menu = menu3, foreground = color_grey, background = color_BlackGrey[0])

# (ADMIN RIGHTS) Creation du menu "Configuration"
if(user_right == 1):
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Create a configuration", command=alert, foreground = color_grey, background = color_BlackGrey[0])
    menubar.add_cascade(label="Configuration", menu = menu3, foreground = color_grey, background = color_BlackGrey[0])


#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
##### Creation du cadre gauche haut pour les entrees d informations
cadre_info1 =  Canvas(interface, width = 600, height = 325, background = color_BlackGrey[1], borderwidth = 0 ) 
##cadre_info1.create_text( 150, 25, text = "Aircraft Configuration", font = ('Helvetica 20 bold'), justify = "center", fill = color_white)

config_lf       = LabelFrame(cadre_info1, text = " Aircraft Configuration" , width = 550, height = 75, borderwidth = 0, )
config_label    = Label(config_lf, text = "AIRCRAFT MODEL : " + AIRCRAFT_CONFIG[0], background =  color_transp)
config_label.config(font= 'Arial 12')
config_label.pack(ipadx=25, ipady=25)
config_lf.pack()

cadre_info1.place(x = 1275, y = 25)


##### Creation du cadre gauche centre pour les entrees d informations
cadre_info2 =  Canvas(interface, width = 600, height = 325, background = color_BlackGrey[1], borderwidth = 0 )         
cadre_info2.place(x = 1275, y = 375)

##### Creation du cadre gauche bas pour les informations editeurs
cadre_info3 =  Canvas(interface, width = 600, height = 225, background = color_BlackGrey[1], borderwidth = 0)         
cadre_info3.place(x = 1275, y = 725)



#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
##### Creation de la configuration par defaut (image + siege)
aircraft_image = PhotoImage(file = ".\\files\\bord_dessus_front.png", width = 500,height = 10)
aircraft_image_canva = Canvas(interface, width = 1200, height = 925, bg = color_BlackGrey[1], bd = 0)
aircraft_image_canva.create_image(1,1, anchor = "n", image = aircraft_image, )
aircraft_image_canva.place(x = 25, y = 25)

# Configuration de la couleur du background
interface.configure(menu = menubar , bg = color_BlackGrey[3])

interface.update()
interface.update_idletasks()
interface.mainloop()