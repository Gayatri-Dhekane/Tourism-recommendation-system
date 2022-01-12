def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING ="mongodb+srv://tourism:tourism123@cluster0.7tpgg.mongodb.net/Tourism?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Tourism']
    #collection_name = dbname["user_1_items"]
    
    

    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname=get_database()
    #print(dbname)
    collection_name = dbname["User_Data"]

    user_1 = {
    "_id" : "004",
    "user_name" : "Isha",
    "type" : ['beach','park'],
    "pincode" : "415001",
    "group_list" : [0,5,6],
    "cliked_places" :[1,8,3]
    }
    collection_name.insert_many([user_1])
    
    
