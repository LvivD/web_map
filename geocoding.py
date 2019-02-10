from geopy.geocoders import MapBox
geolocator = MapBox(api_key='pk.eyJ1IjoiZGFuaWswNiIsImEiOiJjanJ3Yzg0czIwYWN3NDNvYWY3OGlxczNsIn0.Ri-3Ig44dA66UZY_evkW8g')

file_read = open('resources/cities.list')
file_write = open('resources/coordinates.list', 'w')
i = 0

for i in range(0):
    file_read.__next__()


# print(file_read.readline())

none_error = 0
name_error = 0

for line in file_read:
    try:
        location = geolocator.geocode(line)
        if location is None:
            print(None)
            none_error += 1
            file_write.write(line + '\t' + 'error\tNone' + '\n')
        else:
            file_write.write(line + '\t' + str(location.latitude) + '\t' + str(location.longitude) + '\n')
        i += 1
    except NameError as err:
        print(err)
        name_error += 1
        file_write.write(line + '\t' + 'error' + '\t' + str(err) + '\n')
    if i % 100 == 0:
        print(i)

file_write.write(str(none_error) + '\t' + str(name_error) + '\n')

file_read.close()
file_write.close()
