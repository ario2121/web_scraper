import pymongo
import pprint
import datetime


def seve_data_to_mongodb(item_dict,collection_name):
    scaper_dict = item_dict
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['divar_database']
    mycol = mydb[collection_name]

    counter = 0
    
    #لیستی از کلید های دیکشنری که همان اسم کالاها می باشد
    my_index_dict = scaper_dict.keys()

    #بررسی داده های دیتابیس و اضاقه کردن داده های جدید به آن
    for i in my_index_dict:
        item_count = mycol.find({'name' : i }).count()
        if item_count == 1:
            print(' {} is exist! '.format(i))
        elif item_count > 1:
            j=0
            while j < item_count-1:
                mycol.delete_one({'name' : i})
                print('delet duplicat {}'.format(i))
                j+=1
        else:
            dic = {'name' : i , 'details' : scaper_dict[i],'data':datetime.datetime.utcnow()}
            x=mycol.insert_one(dic)
            print('Add {} to database'.format(i))
            counter +=1
    print("Total add {} items.".format(counter))

def print_data_from_mongodb(db_name,collection_name):

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[db_name]
    mycol = mydb[collection_name]

    for i in mycol.find().limit(10):
        pprint.pprint(i)


print(print_data_from_mongodb('divar_database','vehicles'))