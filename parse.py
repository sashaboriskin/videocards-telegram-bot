import requests
from bs4 import BeautifulSoup
import time
#import xlms
import pandas as pd

def txt_to_csv(file):
  modeling_txt = open(file, 'r', encoding='UTF-8')
  modeling_txt = modeling_txt.readlines()
  name = str(file[:-3]) + 'csv'
  cards = []
  for i in range(len(modeling_txt)):
    card = modeling_txt[i].split('~')
    if 'Нет в наличии' not in card[1]:
      price_of_card = int(card[1])
      name_of_card = card[0]
      link = card[2]
      link_to_png = card[3]
      model = card[4]
      model = model[:-1]
      cards.append([name_of_card, price_of_card, link, link_to_png, model])

  modeling_csv = pd.DataFrame(cards, columns=('Название', 'Цена', 'Ссылка', 'Ссылка на картинку', 'Характеристики'))

  sorted_modeling_csv = modeling_csv.sort_values(
    by="Цена",
    ascending=True,
    kind="mergesort",
    ignore_index=True
  )
  return sorted_modeling_csv


def motherboard(file):
  modeling_txt = open(file, 'r', encoding='windows-1251')
  modeling_txt = modeling_txt.readlines()
  name = str(file[:-3]) + 'csv'
  cards = []
  for i in range(len(modeling_txt)):
    card = modeling_txt[i].split('~')
    if 'Нет в наличии' not in card[1]:
      price_of_card = int(card[1])
      name_of_card = card[0]
      link = card[2]
      link_to_png = card[3]
      model = card[4]
      chipset = card[5]
      chipset = chipset[:-1]
      cards.append([name_of_card, price_of_card, link, link_to_png, model, chipset])

  modeling_csv = pd.DataFrame(cards, columns=(
  'Название', 'Цена', 'Ссылка', 'Ссылка на картинку', 'Характеристики', 'Чипсет'))

  sorted_modeling_csv = modeling_csv.sort_values(
    by="Цена",
    ascending=True,
    kind="mergesort",
    ignore_index=True
  )
  return sorted_modeling_csv

print('Начинаем парсить!')

while True:
  model = open('model.txt', 'w', encoding='windows-1251')
  gamin = open('gaming.txt', 'w', encoding='windows-1251')
  maining = open('maining.txt', 'w', encoding='windows-1251')
  mother = open('mother.txt', 'w', encoding='windows-1251')

  print('парсим проф видюхи')

  url_video = 'https://brigo.ru/catalog/details/professionalnye-videokarty/?PAGEN_1=1'
  response_video = requests.get(url_video)
  soup_video = BeautifulSoup(response_video.text, 'lxml')
  page_video = soup_video.find('ul', class_='page-nav__list')
  pages_video = []
  pagin_video = page_video.find_all('li', class_='page-nav__item')

  for link in pagin_video:
    pageNum = link.text
    pages_video.append(pageNum)

  urls_video = []

  for i in range(1, int(pages_video[-2])+1):
    urls_video.append(i)

  for slug in urls_video:
    print("Сейчас парситься: " + str(slug) + " страница")
    if slug <= 10:
      url_video = url_video[:-1] + str(slug)
    else:
      url_video = url_video[:-2] + str(slug)
    response_video = requests.get(url_video)
    soup_video = BeautifulSoup(response_video.text, 'lxml')
    items = soup_video.find_all('li', class_='catalog-main__item-wrapper')
    for item in items:
      if item.find('p', class_='catalog-main__status').text == 'Товар распродан' or item.find('p', class_='catalog-main__status').text == 'Снято с производства':
        continue
      itemName = item.find('div', class_='catalog-main__title').find('span', class_='ellip-line').text.strip()
      if itemName == '': continue
      itemPrice = item.find('p', class_='catalog-main__price').text.strip().replace(' ', '')
      itemPrice = itemPrice.replace('руб.', '')
      itemLink = "https://brigo.ru" + item.find('div', class_='catalog-main__title').find('a', class_='catalog-main__link').get('href')
      itemSpecification = item.find('p', class_='catalog-main__code ellip_type').text.strip()
      img_soup = BeautifulSoup(requests.get(itemLink).text, 'lxml')
      itemImg = "https://brigo.ru" + img_soup.find('li', class_="popup-slider__item").find('img', class_='img-lazy').get('data-src')
      model.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpecification + "\n")

  print('Теперь проф процессоры')

  url_proc = 'https://brigo.ru/catalog/servernoe-oborudovanie/processory/?PAGEN_1=1'
  response_proc = requests.get(url_proc)
  soup_proc = BeautifulSoup(response_proc.text, 'lxml')
  page_proc = soup_proc.find('ul', class_='page-nav__list')
  pages_proc = []
  pagin_proc = page_proc.find_all('li', class_='page-nav__item')

  for link in pagin_proc:
    pageNum = link.text
    pages_proc.append(pageNum)

  urls_proc = []

  for i in range(1, int(pages_proc[-2])+1):
    urls_proc.append(i)

  for slug in urls_proc:
    print("Сейчас парситься: " + str(slug) + " страница")
    if slug <= 10:
      url_proc = url_proc[:-1] + str(slug)
    else:
      url_proc = url_proc[:-2] + str(slug)
    response_proc = requests.get(url_proc)
    soup_proc = BeautifulSoup(response_proc.text, 'lxml')
    items = soup_proc.find_all('li', class_='catalog-main__item-wrapper')
    for item in items:
      if item.find('p', class_='catalog-main__status').text == 'Товар распродан' or item.find('p', class_='catalog-main__status').text == 'Снято с производства':
        continue
      itemName = item.find('div', class_='catalog-main__title').find('span', class_='ellip-line').text.strip()
      if itemName == '': continue
      itemPrice = item.find('p', class_='catalog-main__price').text.strip().replace(' ', '')
      itemPrice = itemPrice.replace('руб.', '')
      itemLink = "https://brigo.ru" + item.find('div', class_='catalog-main__title').find('a', class_='catalog-main__link').get('href')
      itemSpecification = item.find('p', class_='catalog-main__code ellip_type').text.strip()
      img_soup = BeautifulSoup(requests.get(itemLink).text, 'lxml')
      itemImg = "https://brigo.ru" + img_soup.find('div', class_='product-left').find('img', itemprop='contentUrl').get('src')
      model.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpecification + "\n")

#СИТИЛИНК
  print('Теперь процессоры с ситилинка')

  url_citilink_proc = 'https://www.citilink.ru/catalog/processory/?p=1'
  response_citilink_proc = requests.get(url_citilink_proc)
  soup_citilink_proc = BeautifulSoup(response_citilink_proc.text, 'lxml')
  pages_citilink_proc = []
  pagin_citilink_proc = soup_citilink_proc.find('div', class_='PaginationWidget__wrapper-pagination')
  pagin_citilink_proc_second = pagin_citilink_proc.find_all('a')

  for link in pagin_citilink_proc_second:
    pages_citilink_proc.append(link.text.strip())

  urls_citilink_proc = list(map(int, range(1, int(pages_citilink_proc[-2]) + 1)))

  for slug in urls_citilink_proc:
    print('Сейчас парситься: ' + str(slug) + ' страница')
    url_citilink_proc = url_citilink_proc[:-1] + str(slug)
    response_citilink_proc = requests.get(url_citilink_proc)
    soup_citilink_proc = BeautifulSoup(response_citilink_proc.text, 'lxml')
    items_proc = soup_citilink_proc.find_all('div',class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
    for item in items_proc:
      itemName = item.find('div', class_='ProductCardHorizontal__header-block').find('a',class_='ProductCardHorizontal__title').text.strip()[10:]
      itemLink = "https://www.citilink.ru" + item.find('div', class_='ProductCardHorizontal__header-block').find(
        'a', class_='ProductCardHorizontal__title').get('href')
      if item.find('div', class_='ProductCardHorizontal__not-available-block'):
        continue
      itemPrice = item.find('div', class_='ProductCardHorizontal__buy-block').find('span',class_='ProductCardHorizontal__price_current-price').text.strip().replace(
        ' ', '')
      itemImg = item.find('div', class_='ProductCardHorizontal__image-block').find('div',class_='ProductCardHorizontal__picture-hover_part js--ProductCardInListing__picture-hover_part').get('data-src')
      itemSpec = ''
      itemSpecification = item.find_all('ul', class_='ProductCardHorizontal__properties')[:5]
      for spec in itemSpecification:
        itemSpec += spec.text.strip().replace('  ', '').replace('\n', '|').replace('||', '|')
      if itemName[:3] == "AMD":
        maining.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpec + "\n")
      elif itemName[:5] == "Intel":\
        gamin.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpec + "\n")
#
#ВИДЮХИ СИТИЛИНК
#
  print('Теперь видюхи с ситилинка')
  url_citilink_video = 'https://www.citilink.ru/catalog/videokarty/?p=1'
  response_citilink_video = requests.get(url_citilink_video)
  soup_citilink_video = BeautifulSoup(response_citilink_video.text, 'lxml')
  items_video = soup_citilink_video.find_all('div',
                                             class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
  pages_citilink_video = []
  pagin_citilink_video = soup_citilink_video.find('div', class_='PaginationWidget__wrapper-pagination')
  pagin_citilink_video_second = pagin_citilink_video.find_all('a')

  for link in pagin_citilink_video_second:
    pages_citilink_video.append(link.text.strip())

  urls_citilink_video = list(map(int, range(1, int(pages_citilink_video[-2]) + 1)))

  for slug in urls_citilink_video:
    print('Сейчас парситься: ' + str(slug) + ' страница')
    url_citilink_video = url_citilink_video[:-1] + str(slug)
    response_citilink_video = requests.get(url_citilink_video)
    soup_citilink_video = BeautifulSoup(response_citilink_video.text, 'lxml')
    items_video = soup_citilink_video.find_all('div',
                                               class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
    for item in items_video:
      itemName = item.find('div', class_='ProductCardHorizontal__header-block').find('a',
                                                                                     class_='ProductCardHorizontal__title').text.strip()[11:]
      itemLink = "https://www.citilink.ru" + item.find('div', class_='ProductCardHorizontal__header-block').find('a',
                                                                                                                 class_='ProductCardHorizontal__title').get(
        'href')
      if item.find('div', class_='ProductCardHorizontal__not-available-block'):
        continue
      itemPrice = item.find('div', class_='ProductCardHorizontal__buy-block').find('span',
                                                                                   class_='ProductCardHorizontal__price_current-price').text.strip().replace(
        ' ', '')
      itemImg = item.find('div', class_='ProductCardHorizontal__image-block').find('div',
                                                                                   class_='ProductCardHorizontal__picture-hover_part js--ProductCardInListing__picture-hover_part').get(
        'data-src')
      itemSpec = ''
      itemSpecification = item.find_all('ul', class_='ProductCardHorizontal__properties')
      for spec in itemSpecification:
        itemSpec += spec.text.strip().replace('  ', '').replace('\n', '|').replace('||', '|')
      gamin.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpec + "\n")
      if itemName.find("NVIDIA") > 0:
        maining.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpec + "\n")

#СИТИЛИНК МАТЕРИНКИ

  print('Теперь материнки с ситилинка')
  url_citilink_mother = 'https://www.citilink.ru/catalog/materinskie-platy/?p=1'
  response_citilink_mother = requests.get(url_citilink_mother)
  soup_citilink_mother = BeautifulSoup(response_citilink_mother.text, 'lxml')
  items_mother = soup_citilink_mother.find_all('div',
                                               class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
  pages_citilink_mother = []
  pagin_citilink_mother = soup_citilink_mother.find('div', class_='PaginationWidget__wrapper-pagination')
  pagin_citilink_mother_second = pagin_citilink_mother.find_all('a')

  for link in pagin_citilink_mother_second:
    pages_citilink_mother.append(link.text.strip())

  urls_citilink_mother = list(map(int, range(1, int(pages_citilink_mother[-2]) + 1)))

  for slug in urls_citilink_mother:
    print('Сейчас парситься: ' + str(slug) + ' страница')
    url_citilink_mother = url_citilink_mother[:-1] + str(slug)
    response_citilink_mother = requests.get(url_citilink_mother)
    soup_citilink_mother = BeautifulSoup(response_citilink_mother.text, 'lxml')
    items_mother = soup_citilink_mother.find_all('div', class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
    for item in items_mother:
      itemName = item.find('div', class_='ProductCardHorizontal__header-block').find('a', class_='ProductCardHorizontal__title').text.strip()
      itemLink = "https://www.citilink.ru" + item.find('div', class_='ProductCardHorizontal__header-block').find('a', class_='ProductCardHorizontal__title').get('href')
      if item.find('div', class_='ProductCardHorizontal__not-available-block'):
        continue
      itemPrice = item.find('div', class_='ProductCardHorizontal__buy-block').find('span', class_='ProductCardHorizontal__price_current-price').text.strip().replace(' ', '')
      itemImg = item.find('div', class_='ProductCardHorizontal__image-block').find('div', class_='ProductCardHorizontal__picture-hover_part js--ProductCardInListing__picture-hover_part').get( 'data-src')
      itemSpec = ''
      itemSpecification = item.find_all('li', class_='ProductCardHorizontal__properties_item')
      for spec in itemSpecification:
        itemSpec += spec.text.strip().replace('  ', '').replace('\n', '|').replace('||', '|') + "|"
      itemChipsep = str(itemSpecification[1].text.strip().replace(' ', '')[8:])
      if itemChipsep[0] != 'A' and itemChipsep[0] != 'I':
        continue
      mother.write(itemName + " ~ " + itemPrice + " ~ " + itemLink + " ~ " + itemImg + " ~ " + itemSpec + " ~" + itemChipsep + "\n")


  maining_csv = txt_to_csv('maining.txt')
  gaming_csv = txt_to_csv('gaming.txt')
  model_csv = txt_to_csv('model.txt')
  mother_csv = motherboard('mother.txt')

  maining_csv.to_csv('для майнинга.csv', header=False, index=False)
  gaming_csv.to_csv('для игр.csv', header=False, index=False)
  model_csv.to_csv('для моделирования.csv', header=False, index=False)
  mother_csv.to_csv('материнская плата.csv', header=False, index=False)

  model.close()
  gamin.close()
  maining.close()
  mother.close()

  print('Парсинг закончен')
  break


