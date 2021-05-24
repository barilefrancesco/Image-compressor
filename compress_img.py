from PIL import Image
import PIL
import os
import glob


def compress_images(directory=False, quality=30):
    try:
        os.makedirs(directory + '\\Compressed')
    except:
        print('Compressed dir exist')

    # 1. If there is a directory then change into it, else perform the next operations inside of the 
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png', 'JPEG', 'jpeg'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save(directory+ "\\Compressed\\"+image, optimize=True, quality=quality)

if __name__ == "__main__":

    print("Inserisci il percorso della cartella (es. C:\\Users\\nomeutente\\Documents\Fotos ):")
    path = input()

    while True:
        print("Inserisci la qualità delle immagini compresse (0-100):")
        q = input()
        if 0 <= int(q) <= 100:
            break


    compress_images(path, int(q))
