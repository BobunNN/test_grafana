import math
import time
import asyncio
import websockets

async def stream():
    async with websockets.connect("ws://localhost:3000/api/live/push/custom_id", extra_headers={'Authorization': 'Bearer eyJrIjoiMGNYYnJkNEM3NVpLOVp3ajFoM3ZxcEwzbncxR0RKaFgiLCJuIjoic3RyZWFtX2tleTIiLCJpZCI6MX0='}) as websocket:
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