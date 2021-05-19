"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km <= 200:
        offset = control_dist_km/34
    elif control_dist_km <= 400:
        offset = (200/34) + (control_dist_km - 200)/32
    elif control_dist_km <= 600:
        offset = (200/34) + (200/32) + (control_dist_km - 400)/30
    else:
        offset = (200/34) + (200/32) + (200/30) + (control_dist_km - 600)/28
    time = brevet_start_time.shift(hours=offset)
    if time.second >= 30:
        return time.shift(minutes=1)
    return time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
        brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    set_limits = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75, 1200: 90, 1400: 116.4, 2200: 220}
    
    if control_dist_km < 60:
        offset = 1 + control_dist_km/20
    elif control_dist_km <= 600:
        offset = control_dist_km/15
    else:
        offset = 40 + (control_dist_km - 600)/11.428
    if control_dist_km == brevet_dist_km:
        offset = set_limits[brevet_dist_km]
    time = brevet_start_time.shift(hours=offset)
    if time.second >= 30:
        return time.shift(minutes=1)
    return time
