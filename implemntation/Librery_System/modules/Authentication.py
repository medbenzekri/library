from mysql import connector
import bcrypt

class Authenticate :
    def __init__(self) -> None:
        try:
            Authenticate.session= connector.connect(
            host="20.111.12.142",
            database="Library",
            user="client",
            password="`n1BmMe,es_M$:64",
            ) 
        except :
           Authenticate.session=None 
    def login(username,password) -> bool:

        if Authenticate.session==None : return False
        cursor = Authenticate.session.cursor()
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")
        result = cursor.fetchone()
        cursor.excute(f"SELECT * FROM role WHERE username = '{username}'")
        cursor.close()
        return False if result == None else bcrypt.checkpw(password,bytes(result[1]))

if __name__ == '__main__':
    session= connector.connect(
            host="20.111.12.142",
            database="Library",
            user="client",
            password="`n1BmMe,es_M$:64",
            )
    cursor = session.cursor()
    cursor.execute(f"SELECT * FROM user WHERE username = 'mohammed'")
    result = cursor.fetchone()
    print(result)