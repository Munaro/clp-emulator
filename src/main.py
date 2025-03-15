from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from utils import randomData
import asyncio

app = FastAPI()

active_connections = {}

@app.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):
    await websocket.accept()
    
    if room not in active_connections:
        active_connections[room] = []
    active_connections[room].append(websocket)
    
    try:
        while True:
            if room == "industrialTreadMill":
                data = randomData.generateContainerData()
                for connection in active_connections[room]:
                    await connection.send_json(data)
            await asyncio.sleep(30)
    except WebSocketDisconnect:
        active_connections[room].remove(websocket)
        if not active_connections[room]:
            del active_connections[room]
        print(f"Cliente desconectado da sala {room}")
