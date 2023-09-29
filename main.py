import cx_Oracle
import json

# create connection object
print('Connecting to db..')
con = cx_Oracle.connect('username/password@localhost')

try:
    
    cur = con.cursor()
    # Reading data from db in single query. Can be modelled to execute multiple queries. However this method is better in case the volume of data < 150000
    cur.execute('select * from employee')
    rows = cur.fetchall()

    print("Reading data from json")
    f = open('data.json')
    json_data = json.load(f)

    for i in rows:
        if (i[1] != json_data[i[0]]):
            print("Flagging value for item: ", i[0])
    
    print("Completed")

except Exception as e:
    print(e)
