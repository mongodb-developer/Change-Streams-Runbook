# Function to react to changes
def react_to_changes(change):
    if change['operationType'] == 'update':
        document_id = change['documentKey']['_id']
        updated_fields = change['updateDescription']['updatedFields']
        print(f"Reacting to update on document {document_id}: {updated_fields}")
        # Example: Log the update to another collection
        log_collection = db['update_logs']
        log_collection.insert_one({
            "document_id": document_id,
            "updated_fields": updated_fields,
            "timestamp": change['clusterTime']
        })

# Function to watch changes and react to them
def watch_and_react():
    with collection.watch() as stream:
        for change in stream:
            react_to_changes(change)

# Start the change stream and reaction in a separate thread
change_stream_react_thread = threading.Thread(target=watch_and_react)
change_stream_react_thread.start()
