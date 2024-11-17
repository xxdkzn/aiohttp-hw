from aiohttp import web
import json
from datetime import datetime

app = web.Application()
advertisements = []

async def create_advertisement(request):
    data = await request.json()
    new_ad = {
        'id': len(advertisements) + 1,
        'title': data['title'],
        'description': data['description'],
        'created_at': datetime.now().isoformat(),
        'owner': data['owner']
    }
    advertisements.append(new_ad)
    return web.json_response(new_ad, status=201)

async def get_advertisements(request):
    return web.json_response(advertisements, status=200)

async def delete_advertisement(request):
    ad_id = int(request.match_info['ad_id'])
    global advertisements
    advertisements = [ad for ad in advertisements if ad['id'] != ad_id]
    return web.json_response({'message': 'Advertisement deleted'}, status=204)

app.router.add_post('/advertisements', create_advertisement)
app.router.add_get('/advertisements', get_advertisements)
app.router.add_delete('/advertisements/{ad_id}', delete_advertisement)

if __name__ == '__main__':
    web.run_app(app, port=8080)  # Запускаем сервер на порту 8080