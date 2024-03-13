import asyncio
import aiohttp
from aiohttp import FormData
from aiohttp import ClientSession
from aiohttp import ClientTimeout

async def call_upload_api(session: ClientSession, auth_header: str, file) -> None:
    headers = {
        'Authorization': auth_header
    }
    data = FormData()
    data.add_field('file', file.read(), filename=file.filename)
    
    async with session.post('http://localhost:8081/user/singleUpload', headers=headers, data=data) as response:
        print(response.status)

async def async_main(auth_header: str, files) -> None:
    timeout = ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [call_upload_api(session, auth_header, file) for file in files]
        await asyncio.gather(*tasks)
