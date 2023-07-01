import pymongo

if __name__== "__main__":
    # welcome mongodb
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    # creating database(harry)
    db = client["harry"]

    # creating collection(table)
    collection = db["mySampleCollectionForHarry"]

    # finding that marks of Abdur Rehman which is greater then or equal to 26
    finding_specific_document = collection.find({"name":"Abdur Rehman", "marks": {"$gt":26}})
    for item in finding_specific_document:
        print(item)

    
