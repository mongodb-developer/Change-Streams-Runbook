# Function to watch changes with error handling
def watch_with_error_handling():
    try:
        with collection.watch() as stream:
            for change in stream:
                print("Change detected:", change)
    except pymongo.errors.PyMongoError as e:
        print(f"Error watching change stream: {e}")
        # Retry or log the error as needed

# Start the change stream with error handling in a separate thread
change_stream_error_thread = threading.Thread(target=watch_with_error_handling)
change_stream_error_thread.start()

# Perform updates to trigger the change stream
collection.update_one({"_id": 2}, {"$set": {"name": "Bobby"}})
collection.delete_one({"_id": 4})

# Allow some time for the change stream to capture updates
time.sleep(5)
