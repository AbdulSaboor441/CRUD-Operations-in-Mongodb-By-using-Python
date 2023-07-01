import pymongo

if __name__== "__main__":
    # print('Welcome to Mongodb')
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
 
    # showing all databases present in mongodb database.
    show_all_databases = client.list_database_names()
    print(show_all_databases)

    # use harry database.
    db = client['harry']

    # showing the total number of collections(tables) in harry database. 
    collection = db.list_collection_names()
    print(collection)