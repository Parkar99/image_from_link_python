import requests
import re
import urllib
from openpyxl import load_workbook

book = load_workbook("image_links.xlsx")
sheet = book.active
for row in sheet.rows:
    for cell in row:
        if str(cell.value).startswith('http'):
            image = cell.value
            image = image[:-1] + '1'

            file_name_data = re.search(
                '((\w|%)+)(\.\w+)+(?!.*(\w+)(\.(\w|%)+)+)', image)
            file_name = urllib.parse.unquote(file_name_data.group(0))

            image_data = requests.get(image).content
            with open(f'images/{file_name}', 'wb') as file:
                file.write(image_data)
