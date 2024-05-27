import aiohttp, asyncio
from bs4 import BeautifulSoup

async def get_page(session, url):
    async with session.get(url) as page:    # why i take the url from session
        return await page.text()
    
async def get_all_pages(session, urls):
    for url in urls:
        p = await get_page(session, url)
        print(BeautifulSoup(p).find('span', {'class': 'text'}).text.strip())
    
async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        await get_all_pages(session, ['https://quotes.toscrape.com/page/2/', 'https://quotes.toscrape.com/page/3/'])
    
if __name__ == '__main__':
    (asyncio.run(main()))
