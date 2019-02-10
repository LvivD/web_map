def get_data_dict(year_to_get):
    raw_data = open('resources/locations.list')

    for i in range(15):
        raw_data.__next__()

    data_dict = {}


    for line in raw_data:

        first_sign = line.split('\t')[0].strip('"').find('(')
        title = line.split('\t')[0].strip('"')[:first_sign-1]

        first_sign = line.find('(')
        second_sign = line.find(')')
        year = line[first_sign + 1: second_sign]

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
        if len(address) > 0 and address[0] == ' ':
            address = address[1:]


        if year in data_dict:
            if address in data_dict[year]:
                data_dict[year][address].add(title)
            else:
                data_dict[year][address] = {title}
        else:
            data_dict[year] = {address: {title}}
        i+=1
    raw_data.close()
    # print(get_data_dict(year_to_get))
    if year_to_get in data_dict:
        return data_dict[year_to_get]
    else:
        print('no films were filmed that year')
        return {}