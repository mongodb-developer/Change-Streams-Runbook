# Function to watch changes with resume token
def watch_with_resume_token():
    resume_token = None
    try:
        with collection.watch() as stream:
            for change in stream:
                print("Change detected:", change)
                resume_token = stream.resume_token
    except Exception as e:
        print(f"Stream interrupted: {e}")
    
    # Resume from the last known resume token
    if resume_token:
        with collection.watch(resume_after=resume_token) as stream:
            for change in stream:
                print("Resumed change detected:", change)

# Start the change stream with resume token in a separate thread
change_stream_resume_thread = threading.Thread(target=watch_with_resume_token)
change_stream_resume_thread.start()

# Perform updates to trigger the change stream
collection.update_one({"_id": 2}, {"$set": {"age": 26}})
collection.delete_one({"_id": 1})

# Allow some time for the change stream to capture updates
time.sleep(5)
