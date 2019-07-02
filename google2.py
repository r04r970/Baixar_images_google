from google_images_download import google_images_download  # importing the library

end = 5
response = google_images_download.googleimagesdownload()

for i in range(end):
    arguments = {"keywords": "gato", "limit": 1,
                 "print_urls": True, "size": "medium", "format": "png"}  # creating list of arguments

    # passing the arguments to the function
    paths = response.download(arguments)
    print(paths)  # printing absolute paths of the downloaded images
