# GCP-serverless-function

GCP Cloud Functions:

Steps to test the functionality:
------------------------------------
1- Go to the GCP console and click on Cloud Storage from the navigation menu. Click on create bucket and create two buckets, 
the first one is going to be your main bucket and the second one will be your backup bucket.

2- Go back to the navigation menu and click on Cloud Functions. Click create function,
and chooce the bucket that you want to set the trigger on. Go to the code and make sure the Runtime is python 3.7.

3- copy the code from the gcp.py file to the cloud function. Also, copy the file dependencies to the requirment.txt 
that is located inside your cloud function. Click deploy and wait until the function is ready.

4- Go to the navigation menu and click on cloud storage. 
From there click on your main bucket that you set as a trigger to the cloud function. Add a file, then check your backup bucket to see if the file have been copied there.
