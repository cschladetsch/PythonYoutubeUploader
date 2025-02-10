#!/usr/bin/env python3
import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

def setup_youtube_credentials():
    """
    Set up YouTube API credentials by walking through OAuth2 flow
    and saving the resulting credentials to secrets.json
    """
    # OAuth 2.0 scopes required for uploading videos
    SCOPES = [
        'https://www.googleapis.com/auth/youtube.upload',
        'https://www.googleapis.com/auth/youtube'
    ]

    try:
        # Check if client_secrets.json exists
        if not os.path.exists('client_secrets.json'):
            print("Error: client_secrets.json not found!")
            print("\nPlease follow these steps:")
            print("1. Go to Google Cloud Console (https://console.cloud.google.com)")
            print("2. Create a new project or select an existing one")
            print("3. Enable the YouTube Data API v3")
            print("4. Go to Credentials")
            print("5. Create OAuth 2.0 Client ID (Desktop Application)")
            print("6. Download the client configuration")
            print("7. Rename it to client_secrets.json and place it in this directory")
            return False

        # Create the flow using client secrets file
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=SCOPES
        )

        # Run the OAuth flow
        credentials = flow.run_local_server(port=0)

        # Save the credentials
        with open('secrets.json', 'w') as f:
            json.dump({
                'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes
            }, f)

        print("\nCredentials successfully saved to secrets.json!")
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    setup_youtube_credentials()
