import os
import asyncio
import logging
import aiohttp_autoreload

from aiohttp import web


async def get_pod_info(request):
    return web.json_response({
        'pod_hostname': os.environ.get('HOSTNAME', 'Unknown hostname'),
        'pod_ip': os.environ.get('POD_IP', 'Unknown IP')
#        'pod_ip': '127.0.0.1' 
    })


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/api/pod_info', get_pod_info)

    logging.info('Backend server started')
    return await loop.create_server(app.make_handler(access_log=None), '0.0.0.0', 8000)

if os.environ.get('HOT_RELOAD', 'false').lower() == 'true':
    aiohttp_autoreload.start()

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
