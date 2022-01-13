import requests
class Fetcher:
    def get_books(num=50,name=""):
        return requests.get(f"http://20.111.12.142/home.php?limit=?name={name}").json()
    def get_blooks(name:str):
        return requests.get(f"http://20.111.12.142/search.php?name={name}").json() 