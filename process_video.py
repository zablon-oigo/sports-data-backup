import json
import boto3
import requests
from io import BytesIO

from config import (
    S3_BUCKET_NAME,
    AWS_REGION,
    INPUT_KEY,
    OUTPUT_KEY_PREFIX 
)

def process_videos():
    """
    Fetch the highlights JSON file from S3, iterate over all video URLs, download each video,
    and upload them back to S3.
    """
    try:
        s3 = boto3.client("s3", region_name=AWS_REGION)

        # Retrieve the JSON file from S3
        print("Fetching JSON file from S3...")
        response = s3.get_object(Bucket=S3_BUCKET_NAME, Key=INPUT_KEY)
        json_content = response['Body'].read().decode('utf-8')
        highlights = json.loads(json_content)

        # Process each highlight record that has a video URL.
        videos = highlights.get("data", [])
        if not videos:
            print("No video records found in the JSON file.")
            return

if __name__ == "__main__":
    process_videos()