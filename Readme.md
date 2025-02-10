# YouTube Video Uploader

A simple Python application for uploading videos to YouTube using the YouTube Data API v3.

## Prerequisites

- Python 3.7 or higher
- A Google Cloud Project with YouTube Data API v3 enabled
- OAuth 2.0 credentials configured for a desktop application

## Installation

1. Clone this repository:
```bash
git clone https://github.com/cschladetsch/youtube-uploader
cd youtube-uploader
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Google Cloud Project:
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select an existing one
   - Enable the YouTube Data API v3
   - Go to Credentials
   - Create OAuth 2.0 Client ID (Desktop Application)
   - Download the client configuration
   - Rename it to `client_secrets.json` and place it in the project directory

## Files

- `setup.py`: Configures YouTube API credentials through OAuth2 flow
- `uploader.py`: Handles video uploads to YouTube
- `requirements.txt`: Lists all Python dependencies
- `client_secrets.json`: Your OAuth 2.0 client configuration (you need to create this)
- `secrets.json`: Generated during setup, contains your authentication tokens

## Usage

1. First-time setup:
```bash
python setup.py
```
Follow the prompts to authenticate with your Google account. This will create a `secrets.json` file with your credentials.

2. Upload a video:
```bash
python uploader.py path/to/video.mp4 "Your video description"
```

### Upload Options

The uploader provides the following default settings:
- Videos are uploaded as private
- Category is set to "People & Blogs"
- Video title is taken from the filename
- Progress is displayed during upload

## Error Handling

The application handles various error cases:
- Missing credential files
- Invalid or expired tokens
- Network errors during upload
- Invalid file paths
- YouTube API errors

## Security Notes

- Never commit `client_secrets.json` or `secrets.json` to version control
- Add both files to your `.gitignore`
- Keep your OAuth 2.0 credentials secure
- The application uses OAuth 2.0 for secure authentication

## Troubleshooting

1. If you get authentication errors:
   - Ensure `client_secrets.json` is in the correct location
   - Run `setup.py` again to refresh credentials
   - Check if the YouTube Data API is enabled in your Google Cloud Project

2. If uploads fail:
   - Check your internet connection
   - Verify the video file exists and is readable
   - Ensure the video format is supported by YouTube
   - Check your quota usage in Google Cloud Console

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
