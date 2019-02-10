def get_cities():
    raw_data = open('resources/locations.list')

    for i in range(15):
        raw_data.__next__()

    data = set()

    for line in raw_data:
        if '(' in line.split('\t')[-1]:
            first_sign = line.split('\t')[-2].strip().split(',')
            if len(first_sign) >= 3:
                address = first_sign[-3]+','+first_sign[-2]+','+first_sign[-1]
            else:
                address = line.split('\t')[-2].strip()
        else:
            first_sign = line.split('\t')[-1][:-1].strip().split(',')

            if len(first_sign) >= 3:
                address = first_sign[-3]+','+first_sign[-2]+','+first_sign[-1]
            else:
                address = line.split('\t')[-1][:-1].strip()
            if address[0] == ' ':
                address = address[1:]
        if len(address) > 0 and address[0] == ' ':
            address = address[1:]
        data.add(address)
    raw_data.close()

    file_write = open('resources/cities.list', 'w')
    for elem in data:
        file_write.write(elem+'\n')
    file_write.close()
