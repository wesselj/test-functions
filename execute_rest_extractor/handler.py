import os
from rest_extractor import extractor

def handle(secrets, data):
   print("running rest extractor")
   os.environ["COGNITE_CLIENT_SECRET"] = secrets.get("client-secret")
   os.environ["BACKFILL_MIN"] = data.get("backfill_min", "")
   extractor.main()
   print("running rest extractor done")
