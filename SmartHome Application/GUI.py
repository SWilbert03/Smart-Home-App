import Service
from Service import *
import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter.messagebox import showinfo
from tkinter.constants import END


class pages:
    def __init__(self):
        self.user = Service.User()
        self.onoff_auto = None
        self.bed_lamp = None
    #SWITCH
    def switch_to_log(self):
        self.window.destroy()
        self.log()

    def switch_to_bed(self):
        self.window.destroy()
        self.bed()

    def switch_to_bath(self):
        self.window.destroy()
        self.bath()

    def switch_to_liv(self):
        self.window.destroy()
        self.liv()

    def switch_to_kit(self):
        self.window.destroy()
        self.kit()

    def switch_to_adset(self):
        self.window.destroy()
        self.adset()

    def switch_to_sett(self):
        self.window.destroy()
        self.sett()
    #END

    def auto_onoff(self,on,off):
        if self.onoff_auto:
            self.automatic.config(image = off)
            print("Off Automation")
            self.onoff_auto = False
        else :
            self.automatic.config(image = on)
            print("On Automation")
            self.onoff_auto = True
    #ONOFFBEDROOM            
    
    #END

    #CONDITION LOGIN
    def con_log(self,name,password):
        print(name)
        print(password)
        conlog_1 = self.user.login_page(name,password)
        conlog_2 = self.user.check_status(name, password)

        if conlog_1 == True:
            if conlog_2 == 'ADMIN':
                print(conlog_2)
                self.switch_to_adset()
            else:
                self.switch_to_liv()
        else:
            self.window.destroy()

    def log(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("GUI_Project/assets")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        # Clear Submit Box
        def clear_widget(event):
            if username_entry == self.window.focus_get() and username_entry.get() == 'Enter Username':
                username_entry.delete(0, END)
            elif password_entry == self.window.focus_get() and password_entry.get() == '********':
                password_entry.delete(0, END)


        def repopulate_defaults(event):
            if username_entry != self.window.focus_get() and username_entry.get() == '':
                username_entry.insert(0, 'Enter Username')
            elif password_entry != self.window.focus_get() and password_entry.get() == '':
                password_entry.insert(0, '********')

        image_image_1 = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = self.canvas.create_image(
            189.0,
            333.0,
            image=image_image_1
        )

        username_image = PhotoImage(
            file=relative_to_assets("user.png"))
        username_bg = self.canvas.create_image(
            187.0,
            432.5,
            image=username_image

        )
        username_entry = Entry(
            bd=0,
            bg="#E7E7E7",
            highlightthickness=0
        )
        username_entry.place(
            x=66.5,
            y=409.0,
            width=241.0,
            height=45.0
        )
        username_entry.insert(0, 'Enter Username')
        username_entry.bind("<FocusIn>", clear_widget)
        username_entry.bind('<FocusOut>', repopulate_defaults)

        password_image = PhotoImage(
            file=relative_to_assets("pass.png"))
        password_bg = self.canvas.create_image(
            187.0,
            488.5,
            image=password_image
        )
        password_entry = Entry(
            bd=0,
            bg="#E7E7E7",
            highlightthickness=0
        )
        password_entry.place(
            x=66.5,
            y=465.0,
            width=241.0,
            height=45.0
        )
        password_entry.insert(0, '********')
        password_entry.bind("<FocusIn>", clear_widget)
        password_entry.bind('<FocusOut>', repopulate_defaults)

        login_image = PhotoImage(
            file=relative_to_assets("login.png"))
        login_btn = Button(
            image=login_image,
            borderwidth=0,
            highlightthickness=0,
            command =lambda: self.con_log(username_entry.get(),password_entry.get()),
            # command= User(username_entry.get(),password_entry.get()).login_page,
            relief="flat"
        )
        login_btn.place(
            x=97.0,
            y=536.0,
            width=172.0,
            height=46.0
        )


        change_pass = PhotoImage(
            file=relative_to_assets("button_2.png"))
        change_pass_btn = Button(
            image=change_pass,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_adset,
            relief="flat")
        change_pass_btn.place(
            x=143.0,
            y=590.0,
            width=89.0,
            height=11.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def bed(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        OUTPUT_PATH_BEDROOM = Path(__file__).parent
        ASSETS_PATH_BEDROOM = OUTPUT_PATH_BEDROOM / Path("GUI_Project/assets2")

        def relative_to_assets_bedroom(path: str) -> Path:
            return ASSETS_PATH_BEDROOM / Path(path)

        #background
        background_image = PhotoImage(file=relative_to_assets_bedroom("image_1.png"))
        background = self.canvas.create_image(
            187.0,
            333.0,
            image=background_image)

        #title
        title_image = PhotoImage(file=relative_to_assets_bedroom("image_2.png"))
        title = self.canvas.create_image(
            108.0,
            46.0,
            image=title_image)

        #menubar
        menu_image = PhotoImage(file=relative_to_assets_bedroom("button_1.png"))
        menu = Button(
            image= menu_image,
            borderwidth= 0,
            highlightthickness= 0,
            command= self.switch_to_sett,
            relief="flat")
        menu.place(
            x=324.0,
            y=37.0,
            width=22.0,
            height=18.0)

        self.on_auto = PhotoImage(file=relative_to_assets_bedroom("button_2.png"))
        self.off_auto= PhotoImage(file=relative_to_assets_bedroom("button_3.png"))
        self.automatic = Button(
            image=self.off_auto,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.auto_onoff(self.on_auto,self.off_auto),
            bd = 0)
        self.automatic.place(
            x=269.0,
            y=140.0,
            width=37.0,
            height=13.0)

        #roomtitle
        room_image = PhotoImage(file=relative_to_assets_bedroom("image_3.png"))
        room = self.canvas.create_image(
            64.0,
            215.0,
            image=room_image)

        #bedroom
        button_image_4 = PhotoImage(file=relative_to_assets_bedroom("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_bed,
            relief="flat")
        button_4.place(
            x=28.0,
            y=242.0,
            width=74.23343658447266,
            height=74.0)

        #bathroom_off
        button_image_15 = PhotoImage(file=relative_to_assets_bedroom("button_15.png"))
        button_15 = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=  self.switch_to_bath,
            relief="flat")
        button_15.place(
            x=109.0,
            y=242.0,
            width=74.0,
            height=74.0)

        #livingroom_off
        button_image_16 = PhotoImage(file=relative_to_assets_bedroom("button_16.png"))
        button_16 = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_liv,
            relief="flat")
        button_16.place(
            x=191.0,
            y=242.0,
            width=74.0,
            height=74.0)

        #kitchen_off
        button_image_17 = PhotoImage(file=relative_to_assets_bedroom("button_17.png"))
        button_17 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_kit,
            relief="flat")
        button_17.place(
            x=272.0,
            y=242.0,
            width=74.0,
            height=74.0)

            
        #device
        image_image_4 = PhotoImage(file=relative_to_assets_bedroom("image_4.png"))
        image_4 = self.canvas.create_image(
            62.0,
            342.0,
            image=image_image_4)

        #lamp
        image_image_5 = PhotoImage(file=relative_to_assets_bedroom("image_5.png"))
        image_5 = self.canvas.create_image(
            105.0,
            411.0,
            image=image_image_5)

        #ac
        image_image_6 = PhotoImage(file=relative_to_assets_bedroom("image_6.png"))
        image_6 = self.canvas.create_image(
            105.0,
            502.0,
            image=image_image_6)

        #music
        image_image_7 = PhotoImage(file=relative_to_assets_bedroom("image_7.png"))
        image_7 = self.canvas.create_image(
            268.0,
            456.0,
            image=image_image_7)

        #buttonmusic
        # is_play = False
        # def switchmusic():
        #     global is_play
        #     if is_play:
        #         # Service.Room.turn_speaker()
        #         music.config(image = play)
        #         print("Pause Music")
        #         is_play = False
        #     else :
        #         music.config(image = pause)
        #         print("Play Music")
        #         is_play = True
        pause = PhotoImage(file=relative_to_assets_bedroom("button_8.png"))
        play = PhotoImage(file=relative_to_assets_bedroom("button_9.png"))
        music = Button(
            image=play,
            borderwidth=0,
            highlightthickness=0,
            # command=switchmusic,
            relief="flat")
        music.place(
            x=244.0,
            y=432.0,
            width=50.0,
            height=50.0)

        # button_ac
        # is_on_ac = False
        # def switchac():
        #     global is_on_ac
        #     if is_on_ac:
        #         ac.config(image = off_ac)
        #         print("Off Ac")
        #         is_on_ac = False
        #     else :
        #         ac.config(image = on_ac)
        #         print("On Ac")
        #         is_on_ac = True
        on_ac = PhotoImage(file=relative_to_assets_bedroom("button_10.png"))
        off_ac= PhotoImage(file=relative_to_assets_bedroom("button_11.png"))
        ac = Button(
            image=off_ac,
            borderwidth=0,
            highlightthickness=0,
            # command=switchac,
            relief="flat")
        ac.place(
            x=141.0,
            y=470.0,
            width=32.0,
            height=13.0)

        #button_lamp
        # is_light = False
        # def switchlamp():
        #     global is_light
        #     if is_light:
        #         lamp.config(image = off)
        #         print("Off Lamp")
        #         is_light = False
        #     else :
        #         lamp.config(image = on)
        #         print("On Lamp")
        #         is_light = True
        on = PhotoImage(file=relative_to_assets_bedroom("button_12.png"))
        off= PhotoImage(file=relative_to_assets_bedroom("button_13.png"))
        lamp = Button(
            image=off,
            borderwidth=0,
            highlightthickness=0,
            # command=switchlamp,
            relief="flat")
        lamp.place(
            x=141.0,
            y=379.0,
            width=32.0,
            height=13.0)


        


        self.window.resizable(False, False)
        self.window.mainloop()

    def bath(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("GUI_Project/assets2")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        background = self.canvas.create_image(
            187.0,
            333.0,
            image=background_image)

        #title
        title_image = PhotoImage(file=relative_to_assets("image_2.png"))
        title = self.canvas.create_image(
            108.0,
            46.0,
            image=title_image)

        #menubar
        menu_image = PhotoImage(file=relative_to_assets("button_1.png"))
        menu = Button(
            image= menu_image,
            borderwidth= 0,
            highlightthickness= 0,
            command= self.switch_to_sett,
            relief="flat")
        menu.place(
            x=324.0,
            y=37.0,
            width=22.0,
            height=18.0)

        self.on_auto = PhotoImage(file=relative_to_assets("button_2.png"))
        self.off_auto= PhotoImage(file=relative_to_assets("button_3.png"))
        self.automatic = Button(
            image=self.off_auto,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.auto_onoff(self.on_auto,self.off_auto),
            bd = 0)
        self.automatic.place(
            x=269.0,
            y=140.0,
            width=37.0,
            height=13.0)

        #roomtitle
        room_image = PhotoImage(file=relative_to_assets("image_3.png"))
        room = self.canvas.create_image(
            64.0,
            215.0,
            image=room_image)

        #bathroom
        bathroom_image = PhotoImage(
            file=relative_to_assets("button_5.png"))
        bathroom_button = Button(
            image=bathroom_image,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_bath,
            relief="flat"
        )
        bathroom_button.place(
            x=109.25552368164062,
            y=242.0,
            width=74.23343658447266,
            height=74.0
        )

        #device
        image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            62.0,
            342.0,
            image=image_image_4)

        #lamp
        lamp_image = PhotoImage(file=relative_to_assets("image_5.png"))
        lamp = self.canvas.create_image(
            105.0,
            411.0,
            image=lamp_image)

        #music
        image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            268.0,
            456.0,
            image=image_image_7)

        #buttonmusic
        # is_play = False
        # def switchmusic():
        #     global is_play
        #     if is_play:
        #         music.config(image = play)
        #         print("Pause Music")
        #         is_play = False
        #     else :
        #         music.config(image = pause)
        #         print("Play Music")
        #         is_play = True
        pause = PhotoImage(file=relative_to_assets("button_8.png"))
        play = PhotoImage(file=relative_to_assets("button_9.png"))
        music = Button(
            image=play,
            borderwidth=0,
            highlightthickness=0,
            # command=switchmusic,
            relief="flat")
        music.place(
            x=244.0,
            y=432.0,
            width=50.0,
            height=50.0)

        #button_lamp
        # is_light = False
        # def switchlamp():
        #     global is_light
        #     if is_light:
        #         lamp.config(image = off)
        #         print("Off Lamp")
        #         is_light = False
        #     else :
        #         lamp.config(image = on)
        #         print("On Lamp")
        #         is_light = True
        on = PhotoImage(file=relative_to_assets("button_12.png"))
        off= PhotoImage(file=relative_to_assets("button_13.png"))
        lamp = Button(
            image=off,
            borderwidth=0,
            highlightthickness=0,
            # command=switchlamp,
            relief="flat")
        lamp.place(
            x=141.0,
            y=379.0,
            width=32.0,
            height=13.0)

        #bedroom_off
        button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
        button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_bed,
            relief="flat"
        )
        button_14.place(
            x=28.0,
            y=242.0,
            width=74.0,
            height=74.0
        )

        #livingroom_off
        button_image_16 = PhotoImage(file=relative_to_assets("button_16.png"))
        button_16 = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_liv,
            relief="flat")
        button_16.place(
            x=191.0,
            y=242.0,
            width=74.0,
            height=74.0)

        #kitchen_off
        button_image_17 = PhotoImage(file=relative_to_assets("button_17.png"))
        button_17 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_kit,
            relief="flat")
        button_17.place(
            x=272.0,
            y=242.0,
            width=74.0,
            height=74.0)


        self.window.resizable(False, False)
        self.window.mainloop()

    def liv(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("GUI_Project/assets2")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        background = self.canvas.create_image(
            187.0,
            333.0,
            image=background_image)

        #title
        title_image = PhotoImage(file=relative_to_assets("image_2.png"))
        title = self.canvas.create_image(
            108.0,
            46.0,
            image=title_image)

        #menubar
        menu_image = PhotoImage(file=relative_to_assets("button_1.png"))
        menu = Button(
            image= menu_image,
            borderwidth= 0,
            highlightthickness= 0,
            command= self.switch_to_sett,
            relief="flat")
        menu.place(
            x=324.0,
            y=37.0,
            width=22.0,
            height=18.0)    

        self.on_auto = PhotoImage(file=relative_to_assets("button_2.png"))
        self.off_auto= PhotoImage(file=relative_to_assets("button_3.png"))
        self.automatic = Button(
            image=self.off_auto,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.auto_onoff(self.on_auto,self.off_auto),
            bd = 0)
        self.automatic.place(
            x=269.0,
            y=140.0,
            width=37.0,
            height=13.0)

        #roomtitle
        room_image = PhotoImage(file=relative_to_assets("image_3.png"))
        room = self.canvas.create_image(
            64.0,
            215.0,
            image=room_image)


        #livingroom
        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_liv,
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
        image_4 = self.canvas.create_image(
            62.0,
            342.0,
            image=image_image_4)

        #lamp
        image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            105.0,
            411.0,
            image=image_image_5)

        #ac
        image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            105.0,
            502.0,
            image=image_image_6)

        #music
        image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            268.0,
            456.0,
            image=image_image_7)

        #buttonmusic
        # is_play = False
        # def switchmusic():
        #     global is_play
        #     if is_play:
        #         music.config(image = play)
        #         print("Pause Music")
        #         is_play = False
        #     else :
        #         music.config(image = pause)
        #         print("Play Music")
        #         is_play = True
        pause = PhotoImage(file=relative_to_assets("button_8.png"))
        play = PhotoImage(file=relative_to_assets("button_9.png"))
        music = Button(
            image=play,
            borderwidth=0,
            highlightthickness=0,
            # command=switchmusic,
            relief="flat")
        music.place(
            x=244.0,
            y=432.0,
            width=50.0,
            height=50.0)

        #button_ac
        # is_on_ac = False
        # def switchac():
        #     global is_on_ac
        #     if is_on_ac:
        #         ac.config(image = off_ac)
        #         print("Off Ac")
        #         is_on_ac = False
        #     else :
        #         ac.config(image = on_ac)
        #         print("On Ac")
        #         is_on_ac = True
        on_ac = PhotoImage(file=relative_to_assets("button_10.png"))
        off_ac= PhotoImage(file=relative_to_assets("button_11.png"))
        ac = Button(
            image=off_ac,
            borderwidth=0,
            highlightthickness=0,
            # command=switchac,
            relief="flat")
        ac.place(
            x=141.0,
            y=470.0,
            width=32.0,
            height=13.0)

        #button_lamp
        # is_light = False
        # def switchlamp():
        #     global is_light
        #     if is_light:
        #         lamp.config(image = off)
        #         print("Off Lamp")
        #         is_light = False
        #     else :
        #         lamp.config(image = on)
        #         print("On Lamp")
        #         is_light = True
        on = PhotoImage(file=relative_to_assets("button_12.png"))
        off= PhotoImage(file=relative_to_assets("button_13.png"))
        lamp = Button(
            image=off,
            borderwidth=0,
            highlightthickness=0,
            # command=switchlamp,
            relief="flat")
        lamp.place(
            x=141.0,
            y=379.0,
            width=32.0,
            height=13.0)

        #bedroom_off
        button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
        button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_bed,
            relief="flat"
        )
        button_14.place(
            x=28.0,
            y=242.0,
            width=74.0,
            height=74.0
        )

        #bathroom_off
        button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
        button_15 = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_bath,
            relief="flat")
        button_15.place(
            x=109.0,
            y=242.0,
            width=74.0,
            height=74.0)

        #kitchen_off
        button_image_17 = PhotoImage(file=relative_to_assets("button_17.png"))
        button_17 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_kit,
            relief="flat")
        button_17.place(
            x=272.0,
            y=242.0,
            width=74.0,
            height=74.0)


        self.window.resizable(False, False)
        self.window.mainloop()

    def kit(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("GUI_Project/assets2")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        background = self.canvas.create_image(
            187.0,
            333.0,
            image=background_image)

        #title
        title_image = PhotoImage(file=relative_to_assets("image_2.png"))
        title = self.canvas.create_image(
            108.0,
            46.0,
            image=title_image)

        #menubar
        menu_image = PhotoImage(file=relative_to_assets("button_1.png"))
        menu = Button(
            image= menu_image,
            borderwidth= 0,
            highlightthickness= 0,
            command= self.switch_to_sett,
            relief="flat")
        menu.place(
            x=324.0,
            y=37.0,
            width=22.0,
            height=18.0)

        #automatic
        # is_on_auto = False
        # def switchauto():
        #     global is_on_auto
        #     if is_on_auto:
        #         automatic.config(image = off_auto)
        #         print("Off Automation")
        #         is_on_auto = False
        #     else:
        #         automatic.config(image = on_auto)
        #         print("On Automation")
        #         is_on_auto = True
        self.on_auto = PhotoImage(file=relative_to_assets("button_2.png"))
        self.off_auto= PhotoImage(file=relative_to_assets("button_3.png"))
        self.automatic = Button(
            image=self.off_auto,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.auto_onoff(self.on_auto,self.off_auto),
            bd = 0)
        self.automatic.place(
            x=269.0,
            y=140.0,
            width=37.0,
            height=13.0)

        #roomtitle
        room_image = PhotoImage(file=relative_to_assets("image_3.png"))
        room = self.canvas.create_image(
            64.0,
            215.0,
            image=room_image)


        #kitchen
        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_kit,
            relief="flat"
        )
        button_7.place(
            x=271.76654052734375,
            y=242.0,
            width=74.23342895507812,
            height=74.0
        )

        #device
        image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            62.0,
            342.0,
            image=image_image_4)

        #lamp
        image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            105.0,
            411.0,
            image=image_image_5)

        #ac
        image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            105.0,
            502.0,
            image=image_image_6)

        #music
        image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            268.0,
            456.0,
            image=image_image_7)

        #buttonmusic
        # is_play = False
        # def switchmusic():
        #     global is_play
        #     # properties = Service.Room
        #     if is_play:
        #         # properties.turn_speaker()
        #         music.config(image = play)
        #         print("Pause Music")
        #         is_play = False
        #     else :
        #         # properties.t
        #         music.config(image = pause)
        #         print("Play Music")
        #         is_play = True
        pause = PhotoImage(file=relative_to_assets("button_8.png"))
        play = PhotoImage(file=relative_to_assets("button_9.png"))
        music = Button(
            image=play,
            borderwidth=0,
            highlightthickness=0,
            # command=switchmusic,
            relief="flat")
        music.place(
            x=244.0,
            y=432.0,
            width=50.0,
            height=50.0)

        #button_ac
        # is_on_ac = False
        # def switchac():
        #     global is_on_ac
        #     if is_on_ac:
        #         ac.config(image = off_ac)
        #         print("Off Ac")
        #         is_on_ac = False
        #     else :
        #         ac.config(image = on_ac)
        #         print("On Ac")
        #         is_on_ac = True
        on_ac = PhotoImage(file=relative_to_assets("button_10.png"))
        off_ac= PhotoImage(file=relative_to_assets("button_11.png"))
        ac = Button(
            image=off_ac,
            borderwidth=0,
            highlightthickness=0,
            # command=switchac,
            relief="flat")
        ac.place(
            x=141.0,
            y=470.0,
            width=32.0,
            height=13.0)

        #button_lamp
        # is_light = False
        # def switchlamp():
        #     global is_light
        #     if is_light:
        #         lamp.config(image = off)
        #         print("Off Lamp")
        #         is_light = False
        #     else :
        #         lamp.config(image = on)
        #         print("On Lamp")
        #         is_light = True
        on = PhotoImage(file=relative_to_assets("button_12.png"))
        off= PhotoImage(file=relative_to_assets("button_13.png"))
        lamp = Button(
            image=off,
            borderwidth=0,
            highlightthickness=0,
            # command=switchlamp,
            relief="flat")
        lamp.place(
            x=141.0,
            y=379.0,
            width=32.0,
            height=13.0)

        #bedroom_off
        button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
        button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_bed,
            relief="flat"
        )
        button_14.place(
            x=28.0,
            y=242.0,
            width=74.0,
            height=74.0
        )

        #bathroom_off
        button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
        button_15 = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_bath,
            relief="flat")
        button_15.place(
            x=109.0,
            y=242.0,
            width=74.0,
            height=74.0)

        #livingroom_off
        button_image_16 = PhotoImage(file=relative_to_assets("button_16.png"))
        button_16 = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_liv,
            relief="flat")
        button_16.place(
            x=191.0,
            y=242.0,
            width=74.0,
            height=74.0)

        self.window.resizable(False, False)
        self.window.mainloop()

    def adset(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("GUI_Project/assets3")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            187.0,
            333.0,
            image=image_image_1)

        # box
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            187.0,
            338.0,
            image=image_image_2)

        # change
        change_bg = PhotoImage(
            file=relative_to_assets("button_3.png"))
        change_btn = Button(
            image=change_bg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat")
        change_btn.place(
            x=146.0,
            y=423.0,
            width=82.0,
            height=21.0)


        # back
        back_bg = PhotoImage(file=relative_to_assets("button_4.png"))
        back_btn = Button(
            image=back_bg,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_log,
            relief="flat")
        back_btn.place(
            x=27.0,
            y=39.0,
            width=18.0,
            height=18.0)

        # dropdown
        image_image_list = PhotoImage(file=relative_to_assets("image_3.png"))
        image_list = self.canvas.create_image(
            187.0,
            300.0,
            image=image_image_list)
        selected_user = StringVar()
        listuser = ttk.Combobox(self.window, textvariable=selected_user, values=["Jane Doe", "Santa", "Jack", "Ripper"],
                                state='readonly')
        listuser.place(
            x=60.0,
            y=280.0,
            width=253.0,
            height=38.0)


        def user_select(event):
            showinfo(
                title='Result',
                message=f'You selected {selected_user.get()}!')


        listuser.bind('<<ComboboxSelected>>', user_select)

        # background_entry
        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            187.0,
            373.0,
            image=image_image_3)
        change_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0)
        change_entry.place(
            x=60.0,
            y=353.0,
            width=253.0,
            height=38.0)

        self.window.resizable(False, False)
        self.window.mainloop()

    def sett(self):
        self.window = Tk()
        self.window.title("SMARTHOME UI")
        self.window.geometry("375x667")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=667,
            width=375,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("GUI_Project/assets3")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            187.0,
            333.0,
            image=image_image_1
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= self.switch_to_log,
            relief="flat"
        )
        button_2.place(
            x=27.0,
            y=201.0,
            width=320.0,
            height=63.0
        )


        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_bed,
            relief="flat"
        )
        button_4.place(
            x=27.0,
            y=39.0,
            width=18.0,
            height=18.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def run(self):
        self.log()

a = pages()
a.run()