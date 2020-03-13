# import requests
# req = requests.get('https://www.edureka.co/')
# print(req.status_code)
import requests
# pload = {'username':'olivia','password':'123'}
# r = requests.post('https://httpbin.org/post',data = pload)
# r_dictionary= r.json()
# print(r_dictionary['form'])
import requests
from xml.etree import ElementTree
from xml.dom import minidom
import json
from requests.auth import HTTPBasicAuth

import xml.etree.cElementTree as ET
xml="""<?xml version="1.0" encoding="UTF-8"?>
<tns:SALDeviceQueryRequest xmlns:tns="http://avaya.com/v1/SALConcentrator">
<tns:SEID type="Device">(628)089-5788</tns:SEID>
</tns:SALDeviceQueryRequest>"""
# print(xml)
####Python get request

#response=requests.get('https://ui-svha.gl.avaya.com:8443/devicestatus/sal/fl/0050105872',verify=False,auth=HTTPBasicAuth('atom', 'atompass'))
URL_GenALram='https://services-svha.gl.avaya.com:8443/devicestatus/sal/generateTestAlarm?seid=(628)089-5788'
# Dev_Status='https://services-svha.gl.avaya.com:8443/devicestatus/sal/devices/(628)086-6534/(628)089-7426'
response1=requests.get(URL_GenALram,verify=False,auth=HTTPBasicAuth('atom', 'atompass'))
# response2=requests.get(Dev_Status,verify=False,auth=HTTPBasicAuth('atom', 'atompass'))
# print(response1.status_code)
# assert (response1.status_code==200)
print(response1.content)
# print(response1.content)
# print(response2.content)


import time
######################## python Post request ##################################################
# url='https://ui-svha.gl.avaya.com:8443/devicestatus/sal/status'
# header = {"content-type": "application/xml"}
# response1=requests.post(url,data=xml,headers=header,verify=False,auth=HTTPBasicAuth('atom', 'atompass'))
# print(response1.status_code)
# assert (response1.status_code==200)
# print(response1.content)
###=========================FOR Alram Genration==========================================================================================
response_xml_as_string = response1.content.decode('utf-8')
print(response_xml_as_string)
tree = ET.fromstring(response_xml_as_string)
print("Tree Element Description== " + tree[0][2].text)
print("Tree Element Status== " + tree[0][1].text)
# ================================================================================================
URL_ART='https://art-sv.gl.avaya.com:9002/registration/service/atom/health'
ART_Response=requests.get(URL_ART,verify=False,auth=HTTPBasicAuth('artrestuser', 'Avaya123'))
Health_Status=ART_Response.text
if 'good' in Health_Status:
    print("String present")
# ============================================================================================
# URL_SSO='https://sl1-svha.gl.avaya.com/salws/resources/prdRegistration'
# ART_Response=requests.get(URL_SSO,verify=False,auth=HTTPBasicAuth('vmath','Avaya123'))
# print(ART_Response.content)
# print(ART_Response.status_code)
# assert (ART_Response.status_code==200)
# # print("ART SSO Response= " +ART_Response.text)
# ================================================================
GW_Health='https://10.133.12.188:7443/services-gw/rest/autoRegistration/health'
GW_Response=requests.get(GW_Health,verify=False,auth=HTTPBasicAuth('root','Avaya123'))
print(GW_Response.status_code)
assert (GW_Response.status_code==200)
# ============================================


