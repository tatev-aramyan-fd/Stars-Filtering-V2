import calculations_validations as clc_vld
import data_gather_manage_functions as dt_fnc
import configs


def get_inputs() -> tuple:
    try:
        ra = float(input("Enter the RA: "))
        dec = float(input("Enter the DEC: "))
        fov_h = float(input("Enter the Horizontal fov_h: "))
        fov_v = float(input("Enter the Vertical fov_v: "))
        number_of_stars = int(input("Enter number of stars: "))
    except ValueError:
        raise ValueError("INPUT Values CANT CONVERT PROPERLY") from None
    else:
        if not clc_vld.is_valid_ra(ra):
            raise ValueError("RA is not valid point, must be in [0,360].")
        if not clc_vld.is_valid_dec(dec):
            raise ValueError("DEC is not valid point. Must be in [-90,90]")
        if not clc_vld.is_valid_fov(fov_h, fov_v):
            raise ValueError("FOV is not valid.")
        if not clc_vld.is_valid_number(number_of_stars):
            raise ValueError("Number of stars must be positive integer.")

        return ra, dec, fov_h, fov_v, number_of_stars


def get_final_data(filename: str) -> list[list]:
    ra, dec, fov_h, fov_v, number_of_stars = get_inputs()

    data = dt_fnc.read_data_from_tsv(filename)
    data_in_fov = dt_fnc.store_stars_in_fov(ra, dec, fov_v, fov_h, data)
    sorted_by_brightness = clc_vld.get_n_stars_by_brightness(data_in_fov,
                                                             number_of_stars)
    final_data = dt_fnc.update_data_with_distances(sorted_by_brightness,
                                                   ra, dec
                                                   )
    return clc_vld.sort_by_last_value_in_each_el(final_data)


def run_application():
    filename = configs.filename
    header = ['ra', 'dec', 'id', 'brightness', 'distance']

    dt_fnc.write_in_file(header, get_final_data(filename))


if __name__ == "__main__":
    run_application()
