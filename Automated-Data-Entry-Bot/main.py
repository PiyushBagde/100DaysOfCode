from fillGform import FillGform
from scrapedata import ScrapeData

scrapper = ScrapeData()
print(scrapper.links)
print(scrapper.addresses)
print(scrapper.prices)

bot = FillGform()
bot.fill_form()
