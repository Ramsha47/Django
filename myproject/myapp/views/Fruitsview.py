from django.http import JsonResponse
from django.core.cache import cache
from myapp.models import Fruit
import logging

def Fruits(request):
    payload = []
    db = None
    
    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'redis'
        print(f"Cache hit! Data fetched from Redis: {payload}")
        ttl = cache.ttl('fruits')
        print(f"TTL for 'fruits': {ttl} seconds")

    else:
        objs = Fruit.objects.all()
        for obj in objs:
            payload.append(obj.fruit_name)
        cache.set('fruits', payload, timeout=10)
        print(f"Data fetched from PostgreSQL and cached in Redis: {payload}")
    print(f"Returning response: {payload}")
    return JsonResponse({'status': 200, 'db': db, 'data': payload})
    



    