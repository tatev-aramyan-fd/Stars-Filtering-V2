import csv
from calculations_validations import *
from datetime import date


def get_indexes_of_fields(header_list: list) -> tuple:
    ra_index = header_list.index('ra_ep2000')
    dec_index = header_list.index('dec_ep2000')
    id_index = header_list.index('source_id')
    b_index = header_list.index('b')
    return ra_index, dec_index, id_index, b_index


def get_header_from_file(filename: str) -> tuple:
    with open(filename, newline='') as f:
        f.readline()  # read first line as it is not needed
        header = f.readline().strip().split("\t")
        ra, dec, id_, brightness = get_indexes_of_fields(header)

    return header[ra], header[dec], header[id_], header[brightness]


def store_data_from_tsv(filename: str) -> list[list[float]]:
    data_list = []
    with open(filename) as f:
        f.readline()  # read first line / not needed
        header = f.readline().strip().split("\t")
        ra, dec, id_, brightness = get_indexes_of_fields(header)
        csv_obj = csv.reader(f)

        for i in csv_obj:
            try:
                row = i[0].split('\t')
                data_list.append([float(row[ra]), float(row[dec]), float(row[id_]), float(row[brightness])])
            except ValueError:
                raise ValueError("Some data is Null or not proper to be managed!!!") from None

        return data_list


def store_stars_in_fov(ra: float,  dec: float, fov_v: float, fov_h: float, storage: list[list[float]]):
    data_list = []
    for i in storage:
        star_ra = i[0]
        star_dec = i[1]
        if is_in_fov(star_ra, star_dec, ra,  dec, fov_h, fov_v):
            data_list.append(i)
    del storage
    return data_list


def update_data_with_distances(arr: list[list[float]], ra: float, dec: float) -> list[list[float]]:
    for i in arr:
        ra2 = i[0]
        dec2 = i[1]
        i.append(calculate_distance_between_two_points((ra, dec), (ra2, dec2)))
    return arr


def write_in_file(header: list[str], data: list[list[float]]):
    current_timestamp = str(date.today()) + ".csv"
    with open(current_timestamp, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for i in data:
            writer.writerow(i)
