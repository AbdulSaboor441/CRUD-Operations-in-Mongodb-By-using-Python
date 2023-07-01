import pymongo

if __name__== "__main__":
    # print('Welcome to Mongodb')
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    # create harry database
    db = client['harry']
    collection = db['mySampleCollectionForHarry']
    # insert one document
    dictionary = {'_id':'1','name': 'harry','marks':'24'}
    collection.insert_one(dictionary)


    # insert multiple documents
    dictionary1 = [ 
                   {'_id':'2','name':'Abdus Saboor', 'marks':35},
                   {'_id':'3','name':'Abdul Majeed', 'marks':35},
                   {'_id':'4','name':'Abdullah Saleem', 'marks':25},
                   {'_id':'5','name':'Abdul Ghafoor', 'marks':25}
    ]
    
    collection.insert_many(dictionary1)


    # insert multiple documents
    dictionary2 = [ 
                   {'_id':'6','name':'Abdus Saboor', 'marks':34},
                   {'_id':'7','name':'Abdus Saboor', 'marks':33},
                   {'_id':'8','name':'Abdus Saboor', 'marks':32},
                   {'_id':'9','name':'Abdus Saboor', 'marks':31}
    ]
    
    collection.insert_many(dictionary2)

