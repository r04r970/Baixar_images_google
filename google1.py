from google_images_download import google_images_download  # importing the library

# class instantiation
response = google_images_download.googleimagesdownload()

arguments = {"keywords": "policia", "limit": 100,
             "print_urls": True, "size": "medium", "format": "png"}  # creating list of arguments

paths = response.download(arguments)  # passing the arguments to the function
print(paths)  # printing absolute paths of the downloaded images
