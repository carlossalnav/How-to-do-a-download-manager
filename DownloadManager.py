import os
import shutil
import time

# 1.
downloadPath = '/Users/Username/Downloads/'

# 2.
textExt = ('.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf','.xlsx')
videoExt = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv')
audioExt = ('.mp3', '.wma', '.wav', '.flac')
imageExt = ('.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg')
compressedExt = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
executableExt = ('.exe', '.msi','.run','.cmd','.apk','.jar','.bat','.app')
codeExt = ('.py','.css','.sass','.html','.jsp','.js','.rb','.php','.xml','.dll')

# 3.
def getOption():
    print('¿Do you want the download manager create the missing folders? \n')
    option = input('Write an "S" for YES, or a "N" for NO: \n>> ').strip().lower()

    attempts = 0

    while option != 's' and option != 'n':

        if attempts == 4:
            print('\nNo more attempts remaining.')
            exit()

        print('\nInvalid option, enter "S" or "N"')
        option = input('>> ').strip().lower()

        attempts += 1

    return option

# 4.
def checkFolders():
    necessary = ('Text','Video', 'Audio','Image', 'Compressed', 'Executable','Programming','Other')

    allFiles = os.listdir(downloadPath)
    missingFolders = []

    for n in necessary:

        lenFiles = len(allFiles)
        progress = 0

        for f in allFiles:
            if f != n:
                progress += 1

            else:
                pass

        if progress == lenFiles:
            missingFolders.append(n)

    if len(missingFolders) == 0:
        pass

    else:
        print('An error has occurred in your directory {} - the following folders are missing: '.format(downloadPath))

        for c in missingFolders:
            print('* {}'.format(c))

        print('')

        option = getOption()

        if option == 'n':
            print('\nExiting...')
            exit()

        else:
            try:
                for mf in missingFolders:
                    os.mkdir(downloadPath + mf)

                print('\nFolders created successfully!')

            except:
                print('\nAn unexpected error has occurred!')

#5
def order(file, extention):
    for ext in textExt:
        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Text')

    for ext in videoExt:

        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Video')

    for ext in audioExt:

        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Audio')

    for ext in imageExt:

        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Image')

    for ext in compressedExt:

        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Compressed')

    for ext in executableExt:

        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Executable')

    for ext in codeExt:

        if extention == ext:
            shutil.move(downloadPath + file, downloadPath + 'Programming')

    if extention != '':
        try:
            shutil.move(downloadPath + file, downloadPath + 'Other')

        except:
            pass

#6
def main():

    print('\nStarting...\n')
    checkFolders()
    counter = 0
    for file in os.listdir(downloadPath):
        try:
            ext = os.path.splitext(file)[1]
            order(file, ext)
            counter = counter + 1

        except:
            print('The file could not be moved {}\n'.format(file))

    print('{} Files ordered successfully in {}!\n'.format(counter - 8,downloadPath))
    print('The process has finished...')
    time.sleep(3)

if __name__ == '__main__':
    main()