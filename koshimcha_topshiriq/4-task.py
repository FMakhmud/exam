from django.db import models
from bs4 import BeautifulSoup
import requests

#
# class Country(models.Model):
#     name = models.CharField(max_length=64)


r = requests.get('https://www.flashscore.com/').text
soup = BeautifulSoup(r, 'html.parser')
countries = soup.find('aside', class_="container__myMenu").find_all('a')

pinned_leagues = soup.find('aside')
print(pinned_leagues.find('id', class_='menu leftMenu__list'))

for country in countries:
    print(country.text)
