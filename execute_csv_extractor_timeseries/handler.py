import os
from csv_extractor_simple import extractor

def handle(secrets, data):
   print("running rest extractor")
   os.environ["COGNITE_CLIENT_SECRET"] = secrets.get("client-secret")
   extractor.main()
   print("running rest extractor done")
