import requests
def get_books(num=50,name=""):
    return requests.get("http://20.111.12.142/home.php?limit=" + str(num)+"?name="+str(name)).json()

