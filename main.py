from packages.divar_scaper import url_scaper
from packages.mongo_database import seve_data_to_mongodb, print_data_from_mongodb

def to_do(u):
    n = True

    while(n == True):
        print('You are in {} category !'.format(u))
        item = Scaper(u)
        to_do = input("What to do inside category? \n1:print new data  \n2:print data from data base \n3:save data to database\n4:back to main menu\n5:Exit\n>>>")
        if to_do == '1':
            item.just_show()
            n=True
        elif to_do == '2' :
            n=True
            pass
        elif to_do == '3':
            n=True
            pass
        elif to_do == '4' :
            pass




    

class Scaper:
    def __init__(self,mainurl):
        self.URL = mainurl

    def seve_to_database(self,item_dict, collection_name):
        seve_data_to_mongodb(item_dict, collection_name)

    def show_from_database(self, db_name, collection_name):
        print_data_from_mongodb(db_name, collection_name)
    def just_show(self):
        items = (url_scaper(self.URL))
        print(items)

print ('----wellcom to divar scaper----')
all_page_dict = {'':'', 'real_estate':'real-estate', 'buy_residential':'buy-residential', 'buy_apartment':'buy-apartment', 'buy_villa':'buy-villa', 'buy_old_house':'buy-old-house','rent_residential':'rent-residential', 'rent_apartment':'rent-apartment', 'rent_villa':'rent-villa'}
all_town_dict = {'tehran':'tehran', 'ahvaz':'ahvaz'}
get_town = input("Enter Address To Be Scaper : ")
get_category = input("Enter Category : ")
mian_url = 'https://divar.ir/s/{}/{}'.format(all_town_dict[get_town], all_page_dict[get_category])

print(mian_url)
# to_do(get_address)



# #get data from site
# items = (url_scaper('https://divar.ir/s/tehran/vehicles'))

# #save data to database this get dictionary and collection nmae
# seve_data_to_mongodb(item_dict = items , collection_name = 'boz')

# #print data from database this get database name and collection nmae
# print_data_from_mongodb(db_name='mydatabase', collection_name='boz')