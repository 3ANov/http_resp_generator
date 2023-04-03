import asyncio
import datetime

from http_package import HttpPackage

lock = asyncio.Lock()


async def http_package_generator():
    async with lock:
        package = HttpPackage(
            start_line=['GET', '/hello-world', 'HTTP/1.0'],
            headers={'Host': 'example.org', 'Accept-Language': 'ru'},
            body=f"client time: {str(datetime.datetime.now())}"
        )
        return package.__repr__()


async def http_parser(http_package: str):
    async with lock:
        package_list = http_package.split('\n')
        start_line = package_list.pop(0)
        headers = {}
        while (header_line := package_list.pop(0)) != '':
            name = header_line.split(': ').pop(0)
            headers[name] = header_line.split(': ').pop(1)
        body = package_list.pop(0)
        package = HttpPackage(
            start_line=start_line.split(' '),
            headers=headers,
            body=body
        )
        print('******* parsed ********')
        print(package.__repr__())


async def network_service():
    response = await http_package_generator()
    await http_parser(response)


async def start_services():
    coros = [network_service() for i in range(10)]
    await asyncio.gather(*coros)


asyncio.run(start_services())
