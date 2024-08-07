# Function to watch changes with aggregation pipeline
def watch_with_aggregation():
    pipeline = [
        {"$match": {"operationType": {"$in": ["insert", "update"]}}},
        {"$project": {"fullDocument": 1, "updateDescription.updatedFields": 1}}
    ]
    with collection.watch(pipeline=pipeline) as stream:
        for change in stream:
            print("Aggregated change detected:", change)

# Start the change stream with aggregation in a separate thread
change_stream_aggregation_thread = threading.Thread(target=watch_with_aggregation)
change_stream_aggregation_thread.start()

# Perform updates to trigger the change stream
collection.insert_one({"_id": 5, "name": "Eve", "age": 45})
collection.update_one({"_id": 5}, {"$set": {"age": 46}})

# Allow some time for the change stream to capture updates
time.sleep(5)
