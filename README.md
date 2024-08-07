Step 1: Install Required Packages
Make sure you have the necessary packages installed. You'll need pymongo to interact with MongoDB.
```
pip3 install pymongo
```
Step 2: Import Libraries and Set Up MongoDB Connection
First, import the required libraries and set up the connection to your MongoDB instance.
```
import pymongo
from pymongo import MongoClient
import threading
import time
```
# Connect to MongoDB (adjust the connection string as needed)
client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']
collection = db['test_collection']
Step 3: Define a Function to Watch Changes
Define a function that will watch for changes in the collection and handle those changes.
```
# Function to watch changes in the collection
def watch_changes():
    with collection.watch() as stream:
        for change in stream:
            print("Change detected:", change)
```
# Start the change stream in a separate thread
```
change_stream_thread = threading.Thread(target=watch_changes)
change_stream_thread.start()
```
Step 4: Insert Sample Documents and Perform Updates
Insert some sample documents into the collection and perform updates to see the change stream in action.

# Insert sample documents
```
collection.insert_many([
    {"_id": 1, "name": "Alice", "age": 30},
    {"_id": 2, "name": "Bob", "age": 25},
    {"_id": 3, "name": "Charlie", "age": 35}
])
```
# Perform updates to trigger the change stream
```
collection.update_one({"_id": 1}, {"$set": {"age": 31}})
collection.update_one({"_id": 2}, {"$set": {"name": "Robert"}})
collection.delete_one({"_id": 3})
```
# Allow some time for the change stream to capture updates
```
time.sleep(5)
```
