from packages.divar_scaper import url_scaper
from packages.mongo_database import seve_data_to_mongodb, print_data_from_mongodb

def to_do(u):
    n = True

    while(n == True):
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
        elif to_do == '5':
            break


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

main_url = input("Enter Address To Be Scaper : ")

to_do(main_url)
