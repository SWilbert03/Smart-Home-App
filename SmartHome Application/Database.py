import mysql.connector
import os

db = mysql.connector.connect(
    host= 'localhost', user= '202000679',
    password= 'iee', database='smarthome_database')
    

# Tabel Users
def create_table_user():
    cursor = db.cursor(buffered=True)
    drop_table = "DROP TABLE IF EXISTS USERS;"
    create_table = """
                    CREATE TABLE USERS (
                    ID_USER INT NOT NULL AUTO_INCREMENT,
                    Name            VARCHAR(50),
                    Password        VARCHAR(50),
                    Status          ENUM("ADMIN","PARENT","CHILDREN","GUEST"),
                    Time_Created    TIMESTAMP,
                    PRIMARY KEY (ID_USER)
                    ) ENGINE = InnoDB;
                    """
    insert_table = """
                   INSERT INTO USERS (Name, Password, Status, Time_Created) 
                              VALUES ('Matthew', '12345', 'ADMIN', NOW()),
                                     ('Sean', 'qwert', 'PARENT', NOW()),
                                     ('Anak', 'kecil', 'CHILDREN', NOW()),
                                     ('Guest', 'guest', 'GUEST', NOW());
                   """
    cursor.execute(drop_table)
    cursor.execute(create_table)
    cursor.execute(insert_table)
    db.commit()

def login(name: str, password: str):
    cursor = db.cursor(buffered=True)
    check = """
            SELECT EXISTS(SELECT * FROM USERS 
            WHERE name = "{}" and password = "{}");                       
            """.format(name, password)
    cursor.execute(check)
    result = cursor.fetchone()
    for values in result:
        return values

def guestMode():
    cursor = db.cursor(buffered=True)
    allow_guest = """
                  UPDATE PRIVILEGES SET Lamp = '1', Music = '1', AC = '1'
                  WHERE Status = 'GUEST';
                  """
    forbid_guest = """
                   UPDATE PRIVILEGES SET Lamp = '0', Music = '0', AC = '0'
                   WHERE Status = 'GUEST';
                   """
    select = """
             SELECT Lamp FROM PRIVILEGES WHERE Status = 'GUEST';
             """
    cursor.execute(select)
    result = cursor.fetchone()
    for values in result:
        if values == '0':
            cursor.execute(allow_guest)
        elif values == '1':
            cursor.execute(forbid_guest)
    db.commit()

def account_type(name: str , password: str):
    cursor = db.cursor(buffered=True)
    check = """
            SELECT Status FROM USERS WHERE Name = '{}' and Password = '{}';
            """.format(name, password)
    cursor.execute(check)
    result = cursor.fetchone()
    for values in result:
        if values == 'ADMIN':
            return values
        elif values == 'PARENT':
            return values
        elif values == 'CHILDREN':
            return values
        elif values == 'GUEST':
            return values
        else:
            pass


def add_user(name: str, password: str, status: str):
    cursor = db.cursor(buffered=True)
    insert_user = """
                    INSERT INTO USERS (Name, Password, Status, Time_Created) VALUES
                    ("{}","{}","{}",now());
                  """.format(name, password, status)
    reset_increment_1 = "ALTER TABLE USERS DROP ID_USER;"
    reset_increment_2 = "ALTER TABLE USERS ADD ID_USER INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;"
    prevent_duplicate = "ALTER TABLE USERS ADD UNIQUE INDEX(Name);"
    cursor.execute(insert_user)
    cursor.execute(reset_increment_1)
    cursor.execute(reset_increment_2)
    cursor.execute(prevent_duplicate)
    db.commit()


def delete_user(name: str):
    cursor = db.cursor(buffered=True)
    del_user = """
                DELETE FROM USERS WHERE Name = "{}";
               """.format(name)
    reset_increment_1 = "ALTER TABLE USERS DROP ID_USER;"
    reset_increment_2 = "ALTER TABLE USERS ADD ID_USER INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;"
    cursor.execute(del_user)
    cursor.execute(reset_increment_1)
    cursor.execute(reset_increment_2)
    db.commit()


def change_password(name: str, password: str):
    cursor = db.cursor(buffered=True)
    change_pass = """
                    UPDATE USERS SET Password = %s WHERE Name = %s 
                  """
    cursor.execute(change_pass, (password, name))
    db.commit()

def show_user_status():
    cursor = db.cursor(buffered=True)
    show = "SELECT ID_USER, Name, Status FROM USERS;"
    cursor.execute(show)
    column_name = [i[0] for i in cursor.description]
    print(column_name)
    result = cursor.fetchall()
    for values in result:
        print(values)


def show_users_password():
    cursor = db.cursor(buffered=True)
    show = "SELECT ID_USER, Name, Password FROM USERS;"
    cursor.execute(show)
    result = cursor.fetchall()
    column_name = [i[0] for i in cursor.description]
    print(column_name)
    for values in result:
        print(values)


def show_users():
    cursor = db.cursor(buffered=True)
    select = "SELECT * FROM USERS;"
    cursor.execute(select)
    column_name = [i[0] for i in cursor.description]
    print(column_name)
    result = cursor.fetchall()
    for values in result:
        print(values)

def create_table_properties():
    cursor = db.cursor(buffered=True)
    drop = """DROP TABLE IF EXISTS PROPERTIES;"""
    create = """
             CREATE TABLE PROPERTIES (
             Room   ENUM('BEDROOM','BATHROOM','LIVINGROOM','KITCHEN'),
             Lamp   ENUM('0','1'),
             AC     ENUM('0','1'),
             Music  ENUM('0','1')
             ) ENGINE = InnoDB;
             """
    insert = """
             INSERT INTO PROPERTIES (Room, lamp, AC, Music) 
             VALUES ('BEDROOM', '0', '0', '0'),
                    ('BATHROOM', '0', '0', '0'),
                    ('LIVINGROOM', '0', '0', '0'),
                    ('KITCHEN', '0', '0', '0')             
             """
    cursor.execute(drop)
    cursor.execute(create)
    cursor.execute(insert)
    db.commit()


def properties_status():
    cursor = db.cursor(buffered=True)
    status = "SELECT * FROM PROPERTIES;"
    cursor.execute(status)
    column_name = [i[0] for i in cursor.description]
    print(column_name)
    result = cursor.fetchall()
    for values in result:
        print(values)


def change_properties_status(room, properties):
    cursor = db.cursor(buffered=True)
    select = """
             SELECT {} FROM PROPERTIES WHERE Room = '{}';
             """.format(properties, room)

    update_property_active = """
                             UPDATE PROPERTIES SET {} ='1' 
                             WHERE Room ='{}';
                             """.format(properties, room)
    update_property_inactive = """
                             UPDATE PROPERTIES SET {} ='0' 
                             WHERE Room ='{}';
                             """.format(properties, room)

    cursor.execute(select)
    result = cursor.fetchall()
    for values in result:
        if values[0] == '0':
            cursor.execute(update_property_active)
        elif values[0] == '1':
            cursor.execute(update_property_inactive)
    db.commit()


def change_properties_on(room: str, properties: str):
    cursor = db.cursor(buffered=True)
    update_property_active = """
                             UPDATE PROPERTIES SET Status ='1' 
                             WHERE Property_Room ='{}' AND Property_Name ='{}';
                            """.format(room, properties)
    update_time = """
                  UPDATE PROPERTIES SET Time_Updated = NOW() 
                  WHERE Property_Room ='{}' AND Property_Name ='{}';
                  """.format(room, properties)
    cursor.execute(update_property_active)
    cursor.execute(update_time)
    db.commit()


def change_properties_off(room: str, properties: str):
    cursor = db.cursor(buffered=True)
    update_property_inactive = """
                             UPDATE PROPERTIES SET Status ='0' 
                             WHERE Property_Room ='{}' AND Property_Name ='{}' ;
                            """.format(room, properties)
    update_time = """
                  UPDATE PROPERTIES SET Time_Updated = NOW() 
                  WHERE Property_Room ='{}' AND Property_Name ='{}';
                  """.format(room, properties)
    cursor.execute(update_property_inactive)
    cursor.execute(update_time)
    db.commit()


# Tabel Logss
def create_table_log():
    cursor = db.cursor(buffered=True)
    drop_table = "DROP TABLE IF EXISTS LOGS;"
    create_table = """
                   CREATE TABLE LOGS (
                   ID       INT NOT NULL AUTO_INCREMENT,
                   Mode     ENUM("MANUAL","AUTOMATIC"),
                   Room     ENUM("BEDROOM","BATHROOM","LIVING_ROOM","KITCHEN"),
                   Time     TIMESTAMP,
                   PRIMARY KEY (ID)
                   ) ENGINE = InnoDB;
                   """
    insert_value = """
                   INSERT INTO LOGS(Mode, Room, Time)
                   VALUES   ('MANUAL', 'BEDROOM', now()),
                            ('MANUAL', 'BATHROOM', now()),
                            ('MANUAL', 'LIVING_ROOM', now()),
                            ('MANUAL', 'KITCHEN', now());                                
                   """
    cursor.execute(drop_table)
    cursor.execute(create_table)
    cursor.execute(insert_value)
    db.commit()


def show_log():
    cursor = db.cursor(buffered=True)
    select = "SELECT * FROM LOGS;"
    cursor.execute(select)
    column_name = [i[0] for i in cursor.description]
    print(column_name)
    result = cursor.fetchall()
    for values in result:
        print(values)


def update_log(room):
    cursor = db.cursor(buffered=True)
    latest = "SELECT Mode FROM LOGS WHERE ROOM = '{}' ;".format(room)
    update_mode_auto = """
                  UPDATE LOGS SET Mode = 'AUTOMATIC' 
                  WHERE Room ='{}';                    
                  """.format(room)
    update_mode_manual = """
                      UPDATE LOGS SET Mode = 'MANUAL' 
                      WHERE Room ='{}';                    
                      """.format(room)
    cursor.execute(latest)
    result = cursor.fetchone()
    for values in result:
        if values == 'MANUAL':
            cursor.execute(update_mode_auto)
            db.commit()
        elif values == 'AUTOMATIC':
            cursor.execute(update_mode_manual)
            db.commit()
    update_time = """
                  UPDATE LOGS SET Time = NOW() 
                  WHERE Room ='{}';                    
                  """.format(room)
    cursor.execute(update_time)
    db.commit()


def create_insert_table_privileges():
    cursor = db.cursor(buffered=True)
    drop_table = "DROP TABLE IF EXISTS PRIVILEGES;"
    create_table = """
                 CREATE TABLE PRIVILEGES(
                 Status     ENUM('ADMIN', 'PARENT', 'CHILDREN','GUEST'),
                 Auto       ENUM('1','0'),
                 GuestMode  ENUM('1','0'),       
                 Lamp       ENUM('1','0'),
                 Music      ENUM('1','0'),
                 AC         ENUM('1','0'))
                 """
    insert = """
             INSERT INTO PRIVILEGES(Status, Auto, GuestMode, Lamp, Music, AC )
             VALUES(%s, %s, %s, %s, %s, %s); 
             """
    value = [
             ("PARENT"   , '1', '1', '1', '1', '1'),
             ("CHILDREN" , '0', '0', '1', '1', '1'),
             ("GUEST"    , '0', '0', '1', '1', '1'),
             ("ADMIN"    , '0', '0', '0', '0', '0')
            ]
    cursor.execute(drop_table)
    cursor.execute(create_table)
    cursor.executemany(insert, value)
    db.commit()


def show_privileges():
    cursor = db.cursor(buffered=True)
    select = "SELECT * FROM PRIVILEGES;"
    cursor.execute(select)
    column_name = [i[0] for i in cursor.description]
    print(column_name)
    result = cursor.fetchall()
    for values in result:
        print(values)
