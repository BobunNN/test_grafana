import asyncio
import websockets
from urllib.parse import urlencode, quote_plus
from time import sleep, time_ns
import math
import random
import json

stream_key = "eyJrIjoiWDlHWnhYMWpFSDNJZzdoTmF6TXpSb3Z3TUllVWdDUlQiLCJuIjoic3RyZWFtX2tleSIsImlkIjoxfQ=="
stream_key2 = "eyJrIjoiMGNYYnJkNEM3NVpLOVp3ajFoM3ZxcEwzbncxR0RKaFgiLCJuIjoic3RyZWFtX2tleTIiLCJpZCI6MX0="

header="access_token=" + stream_key

async def stream():
    async with websockets.connect("ws://localhost:3000/api/live/push/custom_id", extra_headers={'Authorization': 'Bearer eyJrIjoiMGNYYnJkNEM3NVpLOVp3ajFoM3ZxcEwzbncxR0RKaFgiLCJuIjoic3RyZWFtX2tleTIiLCJpZCI6MX0='}) as websocket:
        i = 0
        while True:
            # await websocket.send("test Sinewave":  str((math.sin(math.radians(i))+1)*20+80) +" " + str(time_ns()+1000000000))

            # data = "{\"Value\":" + str(random.randint(a=1, b=100)) + "}"
            data = {"result": {"data":{"value": random.randint(a=1, b=100)}}}
            json_data = json.dumps(data)
            print(data)
            await websocket.send(json_data)
            await asyncio.sleep(1)
asyncio.run(stream())