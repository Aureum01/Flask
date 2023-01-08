import requests
import os

def download_video(url, file_name):
  # Send an HTTP request to the URL of the video
  response = requests.get(url)
  
  # Check if the response is successful
  if response.status_code == 200:
    # Write the contents of the response to a local file
    with open(file_name, 'wb') as f:
      f.write(response.content)
  else:
    print(f"Failed to download video: {response.status_code}")

# Test the function
download_video("https://www.youtube.com/watch?v=<video_id>", "video.mp4")
