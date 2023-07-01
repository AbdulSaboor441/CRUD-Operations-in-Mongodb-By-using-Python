import pymongo

if __name__== "__main__":
    # print('Welcome to Mongodb')
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    db = client['harry']
    collection = db['mySampleCollectionForHarry']
    
    # find only one document and hide the marks and id of that document.
    # one_document = collection.find_one({'name':'Abdus Saboor'}, {'marks':0, '_id':0})
    # print(one_document)

    
    # find multiple documents and hide the marks of those documents. 
    all_Docs = collection.find({'marks':35},{'marks':0})
    for item in all_Docs:
        print(item)
    

  