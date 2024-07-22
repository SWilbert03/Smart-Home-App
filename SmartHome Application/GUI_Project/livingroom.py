from pathlib import Path
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.constants import FLAT, GROOVE


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("SMARTHOME UI")
window.geometry("375x667")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

#background
canvas.place(x = 0, y = 0)
background_image = PhotoImage(file=relative_to_assets("image_1.png"))
background = canvas.create_image(
    187.0,
    333.0,
    image=background_image)

#title
title_image = PhotoImage(file=relative_to_assets("image_2.png"))
title = canvas.create_image(
    108.0,
    46.0,
    image=title_image)

#menubar
def menu():
    window.destroy()
    os.system(r"python setting.py")
menu_image = PhotoImage(file=relative_to_assets("button_1.png"))
menu = Button(
    image= menu_image,
    borderwidth= 0,
    highlightthickness= 0,
    command= menu,
    relief="flat")
menu.place(
    x=324.0,
    y=37.0,
    width=22.0,
    height=18.0)    

#automatic
is_on_auto = False
def switchauto():
    global is_on_auto
    if is_on_auto:
        automatic.config(image = off_auto)
        print("Off Automation")
        is_on_auto = False
    else :
        automatic.config(image = on_auto)
        print("On Automation")
        is_on_auto = True
on_auto = PhotoImage(file=relative_to_assets("button_2.png"))
off_auto= PhotoImage(file=relative_to_assets("button_3.png"))
automatic = Button(
    image=off_auto,
    borderwidth=0,
    highlightthickness=0,
    command=switchauto,
    bd = 0)
automatic.place(
    x=269.0,
    y=140.0,
    width=37.0,
    height=13.0)

#roomtitle
room_image = PhotoImage(file=relative_to_assets("image_3.png"))
room = canvas.create_image(
    64.0,
    215.0,
    image=room_image)


#livingroom
def livingroom_page():
    window.destroy()
    os.system(r"python livingroom.py")
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=livingroom_page,
    relief="flat"
)
button_6.place(
    x=190.51104736328125,
    y=242.0,
    width=74.23342895507812,
    height=74.0
)

#device
image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    62.0,
    342.0,
    image=image_image_4)

#lamp
image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    105.0,
    411.0,
    image=image_image_5)

#ac
image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    105.0,
    502.0,
    image=image_image_6)

#music
image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    268.0,
    456.0,
    image=image_image_7)

#buttonmusic
is_play = False
def switchmusic():
    global is_play
    if is_play:
        music.config(image = play)
        print("Pause Music")
        is_play = False
    else :
        music.config(image = pause)
        print("Play Music")
        is_play = True
pause = PhotoImage(file=relative_to_assets("button_8.png"))
play = PhotoImage(file=relative_to_assets("button_9.png"))
music = Button(
    image=play,
    borderwidth=0,
    highlightthickness=0,
    command=switchmusic,
    relief="flat")
music.place(
    x=244.0,
    y=432.0,
    width=50.0,
    height=50.0)

#button_ac
is_on_ac = False
def switchac():
    global is_on_ac
    if is_on_ac:
        ac.config(image = off_ac)
        print("Off Ac")
        is_on_ac = False
    else :
        ac.config(image = on_ac)
        print("On Ac")
        is_on_ac = True
on_ac = PhotoImage(file=relative_to_assets("button_10.png"))
off_ac= PhotoImage(file=relative_to_assets("button_11.png"))
ac = Button(
    image=off_ac,
    borderwidth=0,
    highlightthickness=0,
    command=switchac,
    relief="flat")
ac.place(
    x=141.0,
    y=470.0,
    width=32.0,
    height=13.0)

#button_lamp
is_light = False
def switchlamp():
    global is_light
    if is_light:
        lamp.config(image = off)
        print("Off Lamp")
        is_light = False
    else :
        lamp.config(image = on)
        print("On Lamp")
        is_light = True
on = PhotoImage(file=relative_to_assets("button_12.png"))
off= PhotoImage(file=relative_to_assets("button_13.png"))
lamp = Button(
    image=off,
    borderwidth=0,
    highlightthickness=0,
    command=switchlamp,
    relief="flat")
lamp.place(
    x=141.0,
    y=379.0,
    width=32.0,
    height=13.0)

#bedroom_off
def bedroom_page():
    window.destroy()
    os.system(r"python bedroom.py")
button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=bedroom_page,
    relief="flat"
)
button_14.place(
    x=28.0,
    y=242.0,
    width=74.0,
    height=74.0
)

#bathroom_off
def bathroom_page():
    window.destroy()
    os.system(r"python bathroom.py")
button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=bathroom_page,
    relief="flat")
button_15.place(
    x=109.0,
    y=242.0,
    width=74.0,
    height=74.0)

#kitchen_off
def kitchen_page():
    window.destroy()
    os.system(r"python kitchen.py")
button_image_17 = PhotoImage(file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=kitchen_page,
    relief="flat")
button_17.place(
    x=272.0,
    y=242.0,
    width=74.0,
    height=74.0)


window.resizable(False, False)
window.mainloop()
