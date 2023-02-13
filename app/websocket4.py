stream_key = "eyJrIjoicTJEYXFGNDBPSVcxRHQydEI2aUsxMU14YjZUa1VNQkIiLCJuIjoic3RyZWFtX2tleSIsImlkIjoxfQ=="


import math
import time
import asyncio
import websockets

# url1 = "ws://localhost:3000/some/prefix-path"  #KO
# url2 = "ws://localhost:3000/api/live/push/some_signal" #OK?
url2 = "ws://localhost:3000/api/live/push/some_signal/subpath" #KO

async def stream():
    async with websockets.connect(url2, extra_headers={'Authorization': 'Bearer ' + stream_key}) as websocket:
        i = 0
        while True:
            data = "test Sinewave=" + str((math.sin(math.radians(i))+1)*20+80) +" " + str(time.time_ns()+1000000000)
            await websocket.send(data)
            if (i == 361):
                i = 0
            else:
                i = i + 15
            print(data)
            await asyncio.sleep(1)

asyncio.run(stream())