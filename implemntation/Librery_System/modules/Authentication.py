import requests


def login(username, password) -> bool:
    return requests.get("http://20.111.12.142/login.php?username=" + username + "&&password=" + password).text != ""
