import requests
import json
import common

def test_home():
    url = "http://localhost:%s" % common.PORT
    headers = {"Content-Type": "application/json" }
    resp = requests.get(url, headers=headers)
    
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body == "API BD Agroflorestas!"
