from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "future-sunrise-313716-8d008a19f384.json"
def buck_cre(my_bucket_name):
    storage_client = storage.Client()
##    my_bucket_name = 'future-sunrise-313716-clone22'
    bucket = storage_client.create_bucket(my_bucket_name)
    msg = f"Bucket with name {bucket.name} has been created"
    print(msg)
    object_generator = storage_client.list_blobs(my_bucket_name)
    for i in object_generator:
        print(i)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name)
        )

buck_cre("future-sunrise-313716-clone234")
##upload_blob("future-sunrise-313716","testdata.csv","test.csv")
