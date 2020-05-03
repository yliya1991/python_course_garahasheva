import requests

def astronauts_space():
    r = requests.get('http://api.open-notify.org/astros.json')
        
    return r.json()["number"]
