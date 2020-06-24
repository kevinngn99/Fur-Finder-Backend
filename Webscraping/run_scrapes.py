from scrapers.petkey_scrap import petkey
from scrapers.fidofinder import fidofind
from scrapers.helpinglostpets_scrap import helpinglostpets
from scrapers.lostmydoggie_scrap import lostmydoggie
from scrapers.pawboost import pawboost
from scrapers.tabbytracker import tabbytracker


def scrape():
    zipcode = '32607'
    print('Scraping fidofind')
    fidofind(zipcode)

    print('Scraping helpinglostpets')
    helpinglostpets()

    print('Scraping lostmydoggie')
    lostmydoggie(zipcode)

    print('Scraping pawboost')
    pawboost(zipcode)

    print('Scraping tabbytracker')
    tabbytracker(zipcode)

    print('Scraping petkey')
    petkey(zipcode)

scrape()