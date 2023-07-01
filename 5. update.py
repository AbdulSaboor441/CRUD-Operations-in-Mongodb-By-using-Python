import pymongo

if __name__== "__main__":
    # print('Welcome to Mongodb')
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    # create harry database
    db = client['harry']
    collection = db['mySampleCollectionForHarry']
 
    # update  a document(record) of collection(table)
    prev = {'name':'Abdus Saboor'}
    next = {"$set":{'name':'Abdullah Saleem'}}
    update_one_document = collection.update_one(prev,next)
    
    # update many(multiple) documents(records)
    prev = {'name':'Abdullah Saleem'}
    next = {"$set":{'name':'Abdur Rehman'}}
    update_multiple_documents = collection.update_many(prev,next)
    print(update_multiple_documents.modified_count)


