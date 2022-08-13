def sort_by_last_value_in_each_el(lst: list[list[float]]) -> list[list[float]]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j][-1] > lst[j + 1][-1]:  # needed value are the last one
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def calculate_distance_between_two_points(ra_dec1: tuple, ra_dec2: tuple
                                          ) -> float:
    ra1, dec1 = ra_dec1
    ra2, dec2 = ra_dec2
    distance = (ra1-ra2)**2 + (dec1-dec2)**2
    return distance


def get_n_stars_by_brightness(lst: list, number_of_stars: int
                              ) -> list:
    sorted_by_brightness = sort_by_last_value_in_each_el(lst)
    return sorted_by_brightness[:number_of_stars]


def is_in_fov(
            star_ra: float, star_dec: float,
            given_ra: float, given_dec: float,
            fov_h: float, fov_v: float
                ):
    h_min = given_ra - fov_h/2
    h_max = given_ra + fov_h/2
    v_min = given_dec - fov_v/2
    v_max = given_dec + fov_v/2
    if not (is_valid_border(h_min, v_min) and is_valid_border(h_max, v_max)):
        raise ValueError("FOV_min and FOV_max are INVALID")
    if h_min <= star_ra <= h_max\
            and v_min <= star_dec <= v_max:
        return True
    return False


def is_valid_number(num: int):
    if isinstance(num, int) and num > 0:
        return True
    return False


def is_valid_border(x: float, y: float):
    if 0 <= x <= 360 and -90 <= y <= 90:
        return True
    return False


def is_valid_ra(ra: float):
    if 0 <= ra <= 360:
        return True
    return False


def is_valid_dec(dec: float):
    if -90 <= dec <= 90:
        return True
    return False


def is_valid_fov(h: float, v: float):
    if 0 <= h <= 360 and 0 <= v <= 180:
        return True
    return False
