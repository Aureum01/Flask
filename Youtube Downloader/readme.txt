Guide:

1.	First, you will need to install Flask and the required dependencies. You can do this by running the following command:
pip install flask
2.	Next, you will need to write the code for your Flask application. You can use the requests library to make HTTP requests to the YouTube API and retrieve information about the videos you want to download.
3.	To download the video itself, you can use the pytube library, which provides a convenient interface for downloading videos from YouTube. You will need to import the pytube library and use the YouTube class to create an instance of the video you want to download.
4.	Once you have the video instance, you can use the download method to download the video to a specified location on your device.
5.	Finally, you can use Flask to create an interactive web application that allows users to enter the URL of a YouTube video and download it to their device. You can do this by creating a form in your HTML template and using Flask to handle the form submission and trigger the download process.


Index.html:

The template file called index.html contains a form for entering the URL of the YouTube video. When the form is submitted, 
the download function will be called and will download both the video and audio streams of the video to the specified output path.
You will need to create the HTML template file called index.html that contains the form for entering the URL of the YouTube video. 
This template file should be stored in a directory called templates, which should be located in the same directory as your Flask application code.

