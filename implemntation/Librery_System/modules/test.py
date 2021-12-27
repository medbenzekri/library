import mysql.connector 
import bcrypt
class Authenticate :
    def __init__(self) -> None:
            Authenticate.session = mysql.connector.connect(
            host="20.111.12.142",
            database="Library",
            user="admin",
            password="6N/SgPy8Q#7c~j/4"
            ) 
            
    def login(self,username,password):
        cursor=Authenticate.session.cursor()
        hashed=bcrypt.hashpw(password, bcrypt.gensalt())
        # print(len(hashed))
        # cursor.execute(f"insert into user (username,password) values ('{username}','{hashed.decode()}')")
        # Authenticate.session.commit()
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")

        result=cursor.fetchall()
        print(result[0][1])
        if(bcrypt.checkpw(password,bytes(result[0][1]))):
            print("yup")
       

a = Authenticate()
a.login("mohammed",b"12345678")
