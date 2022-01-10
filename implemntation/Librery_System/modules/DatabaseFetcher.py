import requests
class Fetcher:
    def get_books(num=50):
        return requests.get("http://20.111.12.142/home.php?limit="+str(num)).json() 