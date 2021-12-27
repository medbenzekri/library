import mysql.connector 
import bcrypt

class Authenticate :
            
    def login(self,username,password) -> bool:
        session = mysql.connector.connect(
            host="20.111.12.142",
            database="Library",
            user="client",
            password="`n1BmMe,es_M$:64",
            auth_plugin='mysql_native_password'
            ) 
            
        cursor = session.cursor()
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")
        
        result = cursor.fetchone()
        
        cursor.close()
        session.close()
        
        return False if result == None else bcrypt.checkpw(password,bytes(result[1]))
