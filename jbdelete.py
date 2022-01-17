import os

place = input ('')
print (place)
for f in os.listdir(place):
    os.remove(os.path.join(place,f))