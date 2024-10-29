import asyncio
import json
import os
import sys
import websockets

# you can get ready to run this by `cd`ing into this folder (folder_chat) in a
# terminal and running the following commands:
#
# $ python3 -m venv env
# $ . env/bin/activate
# $ pip install websockets
# 
# When you re-open a terminal to this same folder in the future, you can just
# run the following command to set it back up:
#
# $ . env/bin/activate
# 
# Then, use this command to run the server (and Ctrl+C to stop it), with
# whatever folder you want to use:
#
# $ python server.py ~/folder_chat_folder

folder = os.path.abspath(sys.argv[1])

async def serve_ws(websocket, _):
    file = None
    try:
        while True:
            data = json.loads(await websocket.recv())
            filename = data['filename'] + '.txt'
            if not file or os.path.basename(file.name) != filename:
                new_path = os.path.join(folder, data['filename'] + '.txt')
                actual_filename = os.path.basename(new_path)
                if actual_filename != filename:
                    break
                if file:
                    os.rename(file.name, new_path)
                if file:
                    file.close()
                file = open(new_path, 'w')
            file.seek(0)
            file.truncate(0)
            file.write(data['contents'])
            file.flush()
    except websockets.exceptions.ConnectionClosedOK:
        if file:
            os.unlink(file.name)
            file.close()

async def main():
    async with websockets.serve(serve_ws, "127.0.0.1", 10008):
        await asyncio.Future()
asyncio.run(main())
