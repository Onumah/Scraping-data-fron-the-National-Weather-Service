import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.263690000000054&lon=-89.23509999999999#.YxR1IXbP3IU')
print(page)