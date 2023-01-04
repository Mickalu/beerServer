def convert_ordeddirect_to_list(data_ordered, field_name):
    list_data: list = []

    list_dict_beer = list(map(dict, data_ordered))

    for element in list_dict_beer:
        list_data.append(element[field_name])

    return list_data
