import requests
import aiohttp
import asyncio
from django.http import JsonResponse
import time

urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
    "https://jsonplaceholder.typicode.com/todos/5",
]

# Create your views here.
def sync_fetch_data(request):
    t = time.time()
    results = []

    for url in urls:
        response = requests.get(url)
        results.append(response.json())

    execution_time = time.time() - t
    return JsonResponse({"results": results, "execution_time": execution_time})


async def fetch_single(session, url):
    async with session.get(url) as response:
        return await response.json()


async def async_fetch_data(request):

    t = time.time()
    results = []

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_single(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    execution_time = time.time() - t
    return JsonResponse({"results": results, "execution_time": execution_time})