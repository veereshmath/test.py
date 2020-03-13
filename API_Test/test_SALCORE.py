import requests
from requests.auth import HTTPBasicAuth
def test_salore():
    URL_GenALram='https://services-svha.gl.avaya.com:8443/devicestatus/sal/generateTestAlarm?seid=(628)089-5788'
    response1 = requests.get(URL_GenALram, verify=False, auth=HTTPBasicAuth('atom', 'atompass'))
    assert (response1.status_code==200)
    print(response1.content)