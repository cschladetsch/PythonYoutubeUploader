#!/usr/bin/env python3
import os
import json
import argparse
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

def load_credentials():
    """Load credentials from secrets.json"""
    try:
        with open('secrets.json', 'r') as f:
            creds_data = json.load(f)
            
        credentials = Credentials(
            token=creds_data['token'],
            refresh_token=creds_data['refresh_token'],
            token_uri=creds_data['token_uri'],
            client_id=creds_data['client_id'],
            client_secret=creds_data['client_secret'],
            scopes=creds_data['scopes']
        )
        
        # Refresh token if expired
        if credentials.expired:
            credentials.refresh(Request())
            
        return credentials
    except FileNotFoundError:
        print("Error: secrets.json not found! Please run setup.py first.")
        return None
    except Exception as e:
        print(f"Error loading credentials: {str(e)}")
        return None

def upload_video(file_path, description):
    """
    Upload a video to YouTube
    
    Args:
        file_path (str): Path to the video file
        description (str): Video description
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            return False

        # Load credentials
        credentials = load_credentials()
        if not credentials:
            return False

        # Create YouTube API client
        youtube = build('youtube', 'v3', credentials=credentials)

        # Get the filename without extension as default title
        title = os.path.splitext(os.path.basename(file_path))[0]

        # Prepare the video upload request
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': [],
                'categoryId': '22'  # Default to 'People & Blogs' category
            },
            'status': {
                'privacyStatus': 'private',  # Default to private
                'selfDeclaredMadeForKids': False
            }
        }

        # Create media file upload
        media = MediaFileUpload(
            file_path,
            chunksize=1024*1024,
            resumable=True
        )

        # Create the video insert request
        insert_request = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )

        print("Starting upload...")
        response = None
        while response is None:
            status, response = insert_request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%")

        print(f"\nUpload Complete!")
        print(f"Video ID: {response['id']}")
        print(f"Title: {response['snippet']['title']}")
        print(f"URL: https://youtu.be/{response['id']}")
        return True

    except HttpError as e:
        print(f"An HTTP error occurred: {str(e)}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Upload a video to YouTube')
    parser.add_argument('file', help='Path to the video file')
    parser.add_argument('description', help='Video description')
    
    args = parser.parse_args()
    upload_video(args.file, args.description)

if __name__ == "__main__":
    main()
