from PIL import Image 
import os
import time
from time import sleep

downloadsFolder = "/Users/marti/Downloads/"
picturesFolder = "/Users/marti/OneDrive/Imágenes/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".jpg", ".jpeg", ".png", ".raw", ".gif", ".ico"]:
            picture = Image.open(os.path.join(downloadsFolder, filename))
            picture.save(os.path.join(picturesFolder, filename), optimize=True, quality=40)            
            print(name + ": " + extension)

        elif extension.lower() in [".mp3", ".aac", ".wav"]:
            audioFolder = "/Users/marti/Music/"
            os.rename(os.path.join(downloadsFolder, filename), os.path.join(audioFolder, filename))

        elif extension.lower() in [".mp4", ".mov"]:
            videoFolder = "/Users/marti/Videos"
            os.rename(os.path.join(downloadsFolder , filename), os.path.join(videoFolder, filename))
            
        elif extension.lower() in [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx"]:
            documentsFolder = "/Users/marti/OneDrive/Documentos/"
            os.rename(os.path.join(downloadsFolder, filename), os.path.join(downloadsFolder, filename))

