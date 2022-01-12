def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://tourism:tourism123@cluster0.7tpgg.mongodb.net/Tourism?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Tourism']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
   


    
    # Get the database
    dbname = get_database()
    collection_name = dbname["User_Data"]
    user_2 = {
    "_id" : "003",
    "user_name" : "Maya",
    "type" : ['waterfall','hill station'],
    "pincode" : "413508",
    "group_list" : [1,8,7],
    "cliked_places" :[2,9,3]
    }
    collection_name.insert_one(user_2)