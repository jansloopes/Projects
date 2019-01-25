from os import getenv
import pymysql as mariadb

def create_employee(cursor):
    sql_command = """
    CREATE TABLE employee ( 
    staff_number INTEGER PRIMARY KEY, 
    firstname VARCHAR(20), 
    lastname VARCHAR(30),  
    joining DATE);"""
    cursor.execute(sql_command)


def create_investigation(cursor):
    sql_command = """
    CREATE TABLE `Investigation` (
    `name` VARCHAR(50) NULL,
    `joining` DATE NULL,
    `investigation_number` INT UNSIGNED NULL,
    INDEX `investigation_number` (`investigation_number`)
    )
    COMMENT='onderzoek'
    COLLATE='utf8_general_ci'
    ;
    """
    cursor.execute(sql_command)

def create_employee_investigation(cursor):
    sql_command = """
    CREATE TABLE employee_investigation( 
    investigation_number INTEGER, 
    staff_number INTEGER);"""
    cursor.execute(sql_command)

def open_db_connectie() -> file:
    # Open database connection
    try:
        db = mariadb.connect('127.0.0.1', 'Python', 'Pythontje', 'nfir')
    except mariadb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        exit(1)
# prepare a cursor object using cursor() method
    cursor = db.cursor()
    return(db)
# disconnect from server
db.close()

def main():
    open_db_connectie()
    db = open_db_connectie()
    cursor = db.cursor()
    create_employee(cursor)

# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
