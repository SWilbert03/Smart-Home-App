import os
import configparser
import Database

from time import sleep


class User:
    def __init__(self):
        self.database = Database

    def login_page(self,user:str,password:str):
        search_user = self.database.login(user,password)
        if search_user == 0:
            return 'WRONG ID OR PASSWORD'
        elif search_user == 1:
            return True

    def check_status(self, name, password):
        return Database.account_type(name, password)

    def guestMode(self):
        pass


class button:
    def __init__(self):
        self.status_auto = None
        self.status_bed_lamp = None
        self.status_bed_ac = None
        self.status_bed_music = None
        self.status_kit_lamp = None
        self.status_kit_ac = None
        self.status_kit_music = None
        self.status_liv_lamp = None
        self.status_liv_ac = None
        self.status_liv_music = None
        self.status_bath_lamp = None
        self.status_bath_music = None


class Room:
    def __init__(self, file):
        self.file = file
        self.room = {
            'BEDROOM': set(),
            'BATHROOM': set(),
            'LIVING_ROOM': set(),
            'KITCHEN': set()
        }
        self.database = Database

    def enter_room(self, room, entity):
        self.room[room].add(entity)
        config = configparser.ConfigParser()
        config.read(self.file)
        # pir = config[room]["pir"]
        config.set(room, "pir", "HIGH")
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def exit_room(self, room, entity):
        self.room[room].discard(entity)
        config = configparser.ConfigParser()
        config.read(self.file)
        # pir = config[room]["pir"]
        config.set(room, "pir", "LOW")
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def auto(self, room):
        # db = Database.Repository("localhost", "root", "sby030302", "smarthome_database")
        config = configparser.ConfigParser()
        config.read(self.file)
        pir = config.get(room, 'pir')
        ldr = config.get(room, 'ldr')
        temp = config[room]["temperature"]
        if pir == "HIGH" and ldr == "HIGH":
            config.set(room, "lamps", "ACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, "lamps")
        else:
        # elif pir == "LOW" and ldr == "LOW":
            config.set(room, "lamps", "INACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, "lamps")
        if temp > "29" and pir == "HIGH":
            config.set(room, "ac", "ACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, "ac")
        else:
        # elif pir == "LOW":
            config.set(room, "ac", "INACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, "ac")
        if pir == "HIGH":
            config.set(room, "speaker", "ACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, "speaker")
        else:
        # elif pir == "LOW":
            config.set(room, "speaker", "INACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, "speaker")

    def turn_light(self, room):
        db = Database
        config = configparser.ConfigParser()
        config.read(self.file)
        light = config.get(room, 'lamps')
        if light == 'INACTIVE':
            config.set(room, "lamps", "ACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, 'Lamps', 'ACTIVE')
        elif light == 'ACTIVE':
            config.set(room, "lamps", "INACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, 'Lamps', 'INACTIVE')

    def turn_ac(self, room):
        db = Database
        config = configparser.ConfigParser()
        config.read(self.file)
        ac = config.get(room, 'ac')
        if ac == 'INACTIVE':
            config.set(room, "ac", "ACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, 'AC', 'ACTIVE')
        elif ac == 'ACTIVE':
            config.set(room, "ac", "INACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(room, 'AC', 'INACTIVE')

    def turn_speaker(self, room):
        db = Database
        config = configparser.ConfigParser()
        config.read(self.file)
        speaker = config.get(room, 'speaker')
        if speaker == 'INACTIVE':
            config.set(room, "speaker", "ACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(Database.db_connect(), room, 'Speaker')
        elif speaker == 'ACTIVE':
            config.set(room, "speaker", "INACTIVE")
            config.write(open(self.file, 'w'))
            self.database.change_properties_status(Database.db_connect(), room, 'Speaker')


class Environment:
    def __init__(self, file):
        self.file = file

    def run_time(self, room):
        global time
        time = 0
        Room('properties.ini').enter_room(room, 'Matthew')
        while True:
            Environment('properties.ini').set_ldr()
            Environment('properties.ini').set_temperature()
            Room('properties.ini').auto(room)
            print("time = {}, ac = {}, lamps = {}, speaker = {}, temp = {}, pir = {}, ldr = {}".format
                  (time, Read('properties.ini').ac(room), Read('properties.ini').lamps(room),
                   Read('properties.ini').speaker(room),Read('properties.ini').temp(room),
                   Read('properties.ini').pir(room),Read('properties.ini').ldr(room)))

            time += 1
            if time == 24:
                time = 0
            sleep(0.2)

    def set_ldr(self):
        config = configparser.ConfigParser()
        config.read(self.file)
        if 18 <= time <= 23 or 0 <= time <= 6:
            config.set('BEDROOM', 'ldr', 'HIGH')
            config.set('BATHROOM', 'ldr', 'HIGH')
            config.set('LIVING_ROOM', 'ldr', 'HIGH')
            config.set('KITCHEN', 'ldr', 'HIGH')
            config.write(open(self.file, 'w'))
        elif 7 <= time <= 17:
            config.set('BEDROOM', 'ldr', 'LOW')
            config.set('BATHROOM', 'ldr', 'LOW')
            config.set('LIVING_ROOM', 'ldr', 'LOW')
            config.set('KITCHEN', 'ldr', 'LOW')
            config.write(open(self.file, 'w'))
        elif config['BEDROOM']['lamps'] == 'ACTIVE':
            config.set('BEDROOM', 'ldr', 'LOW')
            config.write(open(self.file, 'w'))
        elif config['BATHROOM']['lamps'] == 'ACTIVE':
            config.set('BATHROOM', 'ldr', 'LOW')
            config.write(open(self.file, 'w'))
        elif config['LIVING_ROOM']['lamps'] == 'ACTIVE':
            config.set('LIVING_ROOM', 'ldr', 'LOW')
            config.write(open(self.file, 'w'))
        elif config['KITCHEN']['lamps'] == 'ACTIVE':
            config.set('KITCHEN', 'ldr', 'LOW')
            config.write(open(self.file, 'w'))

    def set_temperature(self):
        config = configparser.ConfigParser()
        config.read(self.file)
        if 20 <= time <= 23 or 0 <= time <= 4:
            config.set('BEDROOM', 'temperature', '20')
            config.set('BATHROOM', 'temperature', '20')
            config.set('LIVING_ROOM', 'temperature', '20')
            config.set('KITCHEN', 'temperature', '20')
            config.write(open(self.file, 'w'))
        elif 10 <= time <= 15:
            config.set('BEDROOM', 'temperature', '32')
            config.set('BATHROOM', 'temperature', '32')
            config.set('LIVING_ROOM', 'temperature', '32')
            config.set('KITCHEN', 'temperature', '32')
            config.write(open(self.file, 'w'))

        elif 5 <= time <= 19:
            config.set('BEDROOM', 'temperature', '24')
            config.set('BATHROOM', 'temperature', '24')
            config.set('LIVING_ROOM', 'temperature', '24')
            config.set('KITCHEN', 'temperature', '24')
            config.write(open(self.file, 'w'))

        # elif config['BEDROOM']['ac'] == 'ACTIVE':
        #     config.set('BEDROOM', 'temperature', '20')
        #     config.write(open('properties.ini', 'w'))
        # elif config['BATHROOM']['lac'] == 'ACTIVE':
        #     config.set('BATHROOM', 'temperature', '20')
        #     config.write(open(self.file, 'w'))
        # elif config['LIVING_ROOM']['ac'] == 'ACTIVE':
        #     config.set('LIVING_ROOM', 'temperature', '20')
        #     config.write(open(self.file, 'w'))
        # elif config['KITCHEN']['ac'] == 'ACTIVE':
        #     config.set('KITCHEN', 'temperature', '20')
        #     config.write(open(self.file, 'w'))


class Read:
    def __init__(self, file):
        self.file = file
        
    def ac(self, room):
        config = configparser.ConfigParser()
        config.read(self.file)
        ac = config.get(room, 'ac')
        return ac

    def lamps(self, room):
        config = configparser.ConfigParser()
        config.read(self.file)
        lamps = config.get(room, 'lamps')
        return lamps

    def speaker(self, room):
        config = configparser.ConfigParser()
        config.read(self.file)
        speaker = config.get(room, 'speaker')
        return speaker

    def temp(self, room):
        config = configparser.ConfigParser()
        config.read(self.file)
        temp = config.get(room, 'temperature')
        return temp

    def pir(self, room):
        config = configparser.ConfigParser()
        config.read(self.file)
        pir = config.get(room, 'pir')
        return pir

    def ldr(self, room):
        config = configparser.ConfigParser()
        config.read(self.file)
        ldr = config.get(room, 'ldr')
        return ldr