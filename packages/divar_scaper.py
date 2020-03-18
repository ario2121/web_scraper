import requests
from bs4 import BeautifulSoup
import re
def url_scaper(main_url):
    #scraping main url
    # main_url = 'https://divar.ir/s/tehran/vehicles'
    sub_url_list = []
    payload = {}
    res = requests.get(url = main_url)
    print(res)
    soup = BeautifulSoup(res.content, 'lxml')
    # print(soup.prettify())

    cars = soup.findAll(attrs='post-card__content')
    link = soup.findAll(attrs='col-xs-12 col-sm-6 col-xl-4 p-tb-large p-lr-gutter post-card')
    price = soup.findAll(attrs="body-12 post-card__description")

    #search sub url and seve to list
    # for i in link :
    #     sub = (re.search(r'href=([\"\'].+?[\"\'])',str(i)))
    #     sub_url_list.append(sub.group(1))
    for i in link:
        sub_url_list.append(i.get('href'))

    # print(sub_url_list)
    item_scapred_dict = {}
    main_dict = {}
    #scraping sub url and save to list
    try:
        for x in sub_url_list:
            sub_url = "https://divar.ir{}".format(x.replace('\"',''))
            sub_res = requests.get(url = sub_url)
            sub_soup = BeautifulSoup(sub_res.content, 'lxml')
            item_name = sub_soup.find(id='app').find(attrs='post-header__title')
            item_detials = sub_soup.find(id='app').findAll(attrs='post-fields-item')
            
            item_scapred_list = []
            item_scapred_dict = {}
            
            # print(item_name.text)

            for i in item_detials:

                item_scapred_dict[i.contents[0].text] = i.contents[1].text
                # print(i.contents[0].text,i.contents[1].text)

            #ایجاد لیستی شامل جزيیات شی به صورت دیکشنری
            item_scapred_list.append(item_scapred_dict)
            main_dict[item_name.text] = item_scapred_list
            
            # print("---------------------------------------")  

    except (requests.exceptions.ChunkedEncodingError):
        print("errrrrrrrrrrrrrrrrrrorrrrrrrrrrrrrr")
        pass


    return main_dict
