import csv


name_list = []
street_list = []
district_list = []
bus_stations = {}
with open('../data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        name_list.append(row['Name'])
        street_list.append(row['Street'])
        district_list.append(row['District'])
    bus_stations.update(Name=name_list)

    bus_stations.update(Street=street_list)
    bus_stations.update(District=district_list)
# print(name_list)
print(bus_stations)