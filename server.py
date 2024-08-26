import asyncio
from msilib.schema import Error
import websockets

clients = []

async def transfer(websocket, _):
  my_id = len(clients)
  clients.append(websocket)
  async for message in websocket:
    for id, client in enumerate(clients):
      if id != my_id:
        try:
          await client.send(message)
        except Exception as e:
          print(e)

async def main():
  async with websockets.serve(transfer, "localhost", 8765):
    await asyncio.Future()  # run forever

asyncio.run(main())