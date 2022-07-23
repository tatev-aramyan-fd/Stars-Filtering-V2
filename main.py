from data_gather_manage_functions import *
import configs


def get_inputs() -> tuple:
    print("BE CAREFUL !!!\nRA is in range [0, 360]\nDEC is in range [-90,90]")
    ra = float(input("Enter the RA: "))
    dec = float(input("Enter the DEC: "))
    if not is_valid_points(ra, dec):
        raise ValueError("RA DEC is not valid points.")

    print("h is in range [0, 360]\nv is in range [-90,90]")
    fov_h = float(input("Enter the Horizontal fov_h: "))
    fov_v = float(input("Enter the Vertical fov_v: "))
    if not is_valid_points(fov_h, fov_v):
        raise ValueError("FOV is not valid. ")

    number_of_stars = int(input("Enter number of stars: "))
    if not is_valid_number(number_of_stars):
        raise ValueError("Number of stars must be positive integer. ")

    return ra, dec, fov_h, fov_v, number_of_stars


def get_final_data(filename: str) -> list[list]:
    ra, dec, fov_h, fov_v, number_of_stars = get_inputs()

    data = store_data_from_tsv(filename)
    data_in_fov = store_stars_in_fov(ra, dec, fov_v, fov_h, data)
    sorted_by_brightness = sort_n_stars_by_brightness(data_in_fov, number_of_stars)
    final_data = update_data_with_distances(sorted_by_brightness, ra, dec)

    return sort_by_last_value_in_each_el(final_data)


def run_application():
    # filename = configs.test_file
    filename = configs.get_filename()
    header = [*get_header_from_file(filename), 'distance']
    write_in_file(header, get_final_data(filename))


if __name__ == "__main__":
    run_application()
