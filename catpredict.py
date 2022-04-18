import boto3
import requests
from serpapi import GoogleSearch
import os
from pathlib import Path
from io import BytesIO

CAT_BREED = "RAGDOLL"

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIAXLGMIXQGGTLQYBUE',
    aws_secret_access_key='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'
)


params = {
  "api_key": "17aca1fd973616ebee6c6df62d2c85d3e6f305efbaafa4df3d3d9416dcdb8b9e",
  "engine": "google",
  "q": CAT_BREED+" cat",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "location": "Austin, Texas, United States",
  "tbm": "isch"
}

search = GoogleSearch(params)
results = search.get_dict()


imageCount = 1
for image in results["images_results"]:
    imgURL = image["original"]
    suffix = imgURL[-4:]
    img_data = requests.get(imgURL).content
    if(suffix in [".jpg",".jpeg",".png"]):
        with BytesIO(img_data) as f:
            s3.Bucket("catpicpredict").upload_fileobj(f,CAT_BREED+str(imageCount)+suffix)
        imageCount += 1












