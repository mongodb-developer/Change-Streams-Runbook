# Function to watch only insert operations
def watch_inserts():
    pipeline = [{"$match": {"operationType": "insert"}}]
    with collection.watch(pipeline=pipeline) as stream:
        for change in stream:
            print("Insert detected:", change)

# Start the change stream for inserts in a separate thread
change_stream_inserts_thread = threading.Thread(target=watch_inserts)
change_stream_inserts_thread.start()

# Insert a new document to trigger the change stream
collection.insert_one({"_id": 4, "name": "Dave", "age": 40})

# Allow some time for the change stream to capture updates
time.sleep(5)
