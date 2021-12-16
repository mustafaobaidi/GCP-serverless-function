from google.cloud import storage
def hello_gcs(event, context):
    file = event
    bucket = file['bucket']
    fileName = file['name']
    try:
         storage_client = storage.Client()
         destination_bucket_name = 'backupbucket'
         src_bucket = storage_client.bucket(bucket)
         destination_bucket = storage_client.bucket(destination_bucket_name)
         src_object = src_bucket.blob(fileName)
         destination_object_name = fileName
         try:
              copy_object = src_bucket.copy_blob(src_object,destination_bucket,destination_object_name)
         except: 
              print('failed to copy the file to the destination bucket: ', destination_bucket)
    except:
          print('failed to load the information from the bucket: ',bucket)
