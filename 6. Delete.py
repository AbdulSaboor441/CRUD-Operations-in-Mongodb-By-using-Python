import pymongo

if __name__== "__main__":
    # print('Welcome to Mongodb')
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    # create harry database
    db = client['harry']
    collection = db['mySampleCollectionForHarry']
 
    # delete a document(record) of collection(table)
    rec = {"name":"harry"}
    delete_one_document = collection.delete_one(rec)
    
    # delete many(multiple) documents(records)
    rec = {"name":"Abdus Saboor"}
    delete_multiple_documents = collection.delete_many(rec)
    print(delete_multiple_documents.deleted_count)

   

    