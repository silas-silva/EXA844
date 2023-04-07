import functions_framework
import pymysql

import json
import time

@functions_framework.http
def hello_http(request):    
    request_json = request.get_json(silent=True)
    #request_args = request.args

    map = {}
    if request_json and 'action' in request_json and request_json['action']=="put":
        try:    
            conn = pymysql.connect(  
                host="35.199.76.148",
                port = 3306,
                user="root",
                password="teste@teste",
                db="blog",
                cursorclass=pymysql.cursors.DictCursor
            )

            with conn:
                with conn.cursor() as cursor:
                    message = request_json['message']
                    autor = request_json['autor']
                    date = time.strftime('%Y-%m-%d %H:%M:%S')                    
                    cursor.execute("insert into Messages (message,autor,date) values ('{}','{}','{}');".format(message, autor, date))
                    conn.commit()
                    map["message"] = "put executed successfully"    
        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))            
   
    elif request_json and 'action' in request_json and request_json['action']=="get":
        ####
        try:    
            conn = pymysql.connect(  
                host="35.199.76.148",
                port = 3306,
                user="root",
                password="teste@teste",
                db="blog",
                cursorclass=pymysql.cursors.DictCursor
            )
           
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("select * from Messages;")
                    messages = cursor.fetchall()                    
            return messages

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

        ####
    else:
        map["message"] = "action missing or with wrong value!"
   
    return json.dumps(map)