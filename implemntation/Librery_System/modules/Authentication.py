import mysql.connector 
import bcrypt
class Authenticate :
    def __init__(self) -> None:
            Authenticate.session = mysql.connector.connect(
            host="20.111.12.142",
            database="Library",
            user="client",
            password="`n1BmMe,es_M$:64"
            ) 
            
    def login(self,username,password) -> False:
        cursor=Authenticate.session.cursor()
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")
        result=cursor.fetchone()
        if(result==None):return False
        print(result[1])
        if(bcrypt.checkpw(password,bytes(result[1]))):
            cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")
            
a = Authenticate()
a.login("bb",b"12345678")
