import mysql.connector as mc

db = mc.connect(host = "connorcloudserver.ddns.net", user = "root", password = "a")
my_cursor = db.cursor()
running = True

while running:
    try:
        my_query = str(input("QUERY: "))
        if my_query == "QUIT":
            running = False
            db.close()
        elif my_query == "SAVE":
            db.commit()
        else:
            my_cursor.execute(my_query)
            for i in my_cursor:
                print(i)
    except mc.Error as error:
        print(error)