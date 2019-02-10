import folium
from get_data_dict import get_data_dict

my_map = folium.Map(location=[48.314775, 25.082925], zoom_start=4)

year = input('type the year: ')

marks = folium.FeatureGroup(name="Place marks")

data_dict = get_data_dict(year)
coordinates_dict = {}

coordinates_file = open('resources/coordinates.list')
for line in coordinates_file:
    line = line.split('\t')
    if 'error' in line[1]:
        coordinates_dict[line[0]] = line[1][:-1]
    else:
        coordinates_dict[line[0]] = (line[1], line[2][:-1])
coordinates_file.close()

read_error = 0
value_error = 0
no_error = 0
countries_dict = {}

for elem in data_dict:

    # print(elem)
    # input()
    if ',' in elem:
        if elem.split(',')[-1][1:] in countries_dict:
            countries_dict[elem.split(',')[-1][1:]] += len(data_dict[elem])
        else:
            countries_dict[elem.split(',')[-1][1:]] = len(data_dict[elem])
    else:
        if elem in countries_dict:
            countries_dict[elem] += len(data_dict[elem])
        else:
            countries_dict[elem] = len(data_dict[elem])
    if elem in coordinates_dict:
        try:
            tooltip = str(len(data_dict[elem]))
            popup = ''
            for film in data_dict[elem]:
                popup += film + '</br>'
            folium.Marker([float(coordinates_dict[elem][0]), float(coordinates_dict[elem][1])],
                          popup=popup,
                          tooltip=tooltip).add_to(marks)
            no_error += 1
        except ValueError:
            value_error += 1
    else:
        read_error += 1

# print(countries_dict)

print('successfully added markers: ',no_error,'\nunable to read: ', read_error, '\nwrong format: ', value_error, '\n')

mask = folium.FeatureGroup(name="Number of films filmed per country")

mask.add_child(folium.GeoJson(data=open('resources/world.json', 'r',
                             encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor':'green'
    if x['properties']['NAME'] not in countries_dict
    else 'green' if countries_dict[x['properties']['NAME']] < 100
    else 'orange' if 100 <= countries_dict[x['properties']['NAME']] < 500
    else 'red'}))

my_map.add_child(marks)
my_map.add_child(mask)
my_map.add_child(folium.LayerControl())

my_map.save('Map_'+str(year)+'.html')
