import os
import requests
import re
import urllib
from openpyxl import load_workbook

book = load_workbook('image_links.xlsx')
sheet = book.active

image_dir = os.path.join(os.path.dirname(__file__), 'images')
if not os.path.exists(image_dir):
    os.mkdir(image_dir)

for r_number, row in enumerate(sheet.rows):
    for cell in row:
        if str(cell.value).startswith('http'):
            image = cell.value
            image = image[:-1] + '1'

            file_name_data = re.search(
                '((\w|%)+)(\.\w+)+(?!.*(\w+)(\.(\w|%)+)+)', image
            )
            file_name = urllib.parse.unquote(file_name_data.group(0))

            print(f'Downloading {file_name}')
            image_data = requests.get(image).content
            with open(f'images/{file_name}', 'wb') as file:
                file.write(image_data)
