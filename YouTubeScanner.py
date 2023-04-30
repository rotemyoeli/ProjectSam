import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import re

def find_product_mentions(video_link, product_name):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"  # Your Google API credentials file
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Set up the YouTube API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    # Extract the video ID from the link
    video_id = video_link.split("v=")[1]

    # Call the YouTube API to get the video transcript
    request = youtube.captions().list(
        part="snippet",
        videoId=video_id
    )
    response = request.execute()

    # Check if captions are available for the video
    if not response["items"]:
        return "Captions are not available for this video."

    # Get the English captions track
    captions_track = next((item for item in response["items"] if item["snippet"]["language"] == "en"), None)

    # Check if English captions are available for the video
    if not captions_track:
        return "English captions are not available for this video."

    # Call the YouTube API to get the video details
    video_request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    video_response = video_request.execute()

    # Get the video title
    video_title = video_response["items"][0]["snippet"]["title"]

    # Extract the transcript from the captions track
    transcript_request = youtube.captions().download(
        id=captions_track["id"]
    )
    transcript = transcript_request.execute()

    # Find all mentions of the product in the transcript
    product_mentions = []
    for line in transcript.split('\n'):
        if re.search(fr'\b{product_name}\b', line, re.IGNORECASE):
            product_mentions.append(line.strip())

    # Return the list of product mentions
    return product_mentions
