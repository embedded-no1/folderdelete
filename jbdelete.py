import os,shutil

place = input ('')
for files in os.listdir(place):
    path = os.path.join(place, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
