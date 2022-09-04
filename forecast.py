#import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#extract website content
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.263690000000054&lon=-89.23509999999999#.YxR1IXbP3IU')
soup = BeautifulSoup(page.content, 'html.parser')

container = soup.find(id= 'seven-day-forecast-list')
items = container.find_all(class_ = 'tombstone-container')
period_names = [item.find(class_ = 'period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures = [item.find(class_ = 'temp').get_text() for item in items]

df = pd.DataFrame(
    {
        'period names': period_names,
        'short descriptions': short_descriptions,
        'temperatures': temperatures,
    }
)

df.to_csv('Forecast.csv')