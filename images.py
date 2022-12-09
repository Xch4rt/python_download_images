import requests
import csv
import os
import asyncio


async def read_csv():
    with open('PricesmartCr_Juguetes.csv', 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)

async def create_folder():
    if not os.path.exists('images'):
        os.makedirs('images')
    return 'images'

async def download_image():
    for row in await read_csv():
        url = row[6]
        filename = row[0].replace(' ', '_').replace('/', '')
        response = requests.get(url)
        with open(f'{await create_folder()}/{filename}.jpg', 'wb') as f:
            f.write(response.content)

async def create_name():
    filename = os.listdir('images')
    with open('./names.txt', 'w', encoding='utf8') as f:
        for name in filename:
            f.write('%s \n' % name)

async def main():
    await download_image()
    await create_name()

if __name__ == '__main__':
    asyncio.run(main())
