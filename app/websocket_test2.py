stream_key = "eyJrIjoiWDlHWnhYMWpFSDNJZzdoTmF6TXpSb3Z3TUllVWdDUlQiLCJuIjoic3RyZWFtX2tleSIsImlkIjoxfQ=="
stream_key2 = "eyJrIjoiMGNYYnJkNEM3NVpLOVp3ajFoM3ZxcEwzbncxR0RKaFgiLCJuIjoic3RyZWFtX2tleTIiLCJpZCI6MX0="

import requests
import time
import math
import random

x1 = 0
x2 = 0
x3 = 0

for i in range(3000) :
    a = random.randint(a=1, b=10)
    response = requests.post('http://localhost:3000/api/live/push/1', data='sma,sma=cpu5,host=smar usage_softirq='+str(x1)+',usage_guest='+str(x2)+',usage_guest_nice='+str(x3), headers={'Authorization':'Bearer ' + stream_key})
    # response = requests.post('ws://localhost:3000/some_id/prefix', data='sma,sma=cpu5,host=smar usage_softirq='+str(x1)+',usage_guest='+str(x2)+',usage_guest_nice='+str(x3), headers={'Authorization':'Bearer ' + stream_key})

    # response = requests.post('http://localhost:3000/api/live/push/some_channel/', data={"val1": math.sin(a), 'val2': a}, headers={'Authorization':'Bearer ' + stream_key})
    # response = requests.post('http://localhost:3000/id1/id2/', data='sma,sma=cpu5,host=smar usage_softirq='+str(x1)+',usage_guest='+str(x2)+',usage_guest_nice='+str(x3), headers={'Authorization':'Bearer ' + stream_key})
    x1+=1
    x2+=2
    x3+=3
    print(response)
    time.sleep(0.4)