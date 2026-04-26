from curl_cffi import requests

def session() -> requests.Session:
    # config do GET
    ses = requests.Session(impersonate='chrome')
    ses.verify = False
    return ses