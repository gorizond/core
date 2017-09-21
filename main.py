import time
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def wshandler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            print("{}, {}".format(time.time(), msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


app = web.Application()
app.router.add_get('/ws', wshandler)
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app)
