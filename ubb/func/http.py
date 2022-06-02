import httpx


async def get(url: str):
    async with httpx.AsyncClient() as client:
             r = await client.get(url, follow_redirects=True)
    return r


async def post(url: str, pdata):
    async with httpx.AsyncClient() as client:
             r = await client.post(url,
                                   data=pdata
                                   )
    return r
