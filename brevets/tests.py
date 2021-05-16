import nose
import arrow
import acp_times as acp_times

sample_time = arrow.get('01/01/2021 00:00:00', 'MM/DD/YYYY HH:mm:ss')


def basic_test_open():
    """
    Example open times from the algorithm description webpage
    """
    assert acp_times.open_time(60, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=1,
                                                                                                           minutes=46)
    assert acp_times.open_time(120, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=3,
                                                                                                            minutes=32)
    assert acp_times.open_time(175, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=5,
                                                                                                            minutes=9)
    assert acp_times.open_time(200, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=5,
                                                                                                            minutes=53)


def basic_test_close():
    """
    Example close times from the algorithm description webpage
    """
    assert acp_times.close_time(60, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=4)
    assert acp_times.close_time(120, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=8)
    assert acp_times.close_time(175, 200, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=11,
                                                                                                             minutes=40)


def longer_distance_open():
    """
    Testing open times at distances farther than 200km, taken from the algorithm description webpage
    """
    assert acp_times.open_time(350, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=10,
                                                                                                             minutes=34)
    assert acp_times.open_time(550, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=17,
                                                                                                             minutes=8)
    assert acp_times.open_time(890, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=29,
                                                                                                             minutes=9)


def longer_distance_close():
    """
    Testing close times at distances farther than 200km, taken from the algorithm description webpage
    """
    assert acp_times.close_time(550, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=36,
                                                                                                              minutes=40)
    assert acp_times.close_time(600, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=40)
    assert acp_times.close_time(890, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=65,
                                                                                                              minutes=23)


def test_controle_close_to_start():
    """
    Tests open/close times for controle locations for 60 km and under
	"""
    assert acp_times.open_time(0, 1000, sample_time).replace(second=0, microsecond=0) == sample_time
    assert acp_times.close_time(0, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=1)

    assert acp_times.open_time(5, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(minutes=9)
    assert acp_times.close_time(5, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=1,
                                                                                                            minutes=15)

    assert acp_times.open_time(20, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(minutes=35)
    assert acp_times.close_time(20, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=2)

    assert acp_times.open_time(30, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(minutes=53)
    assert acp_times.close_time(30, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=2,
                                                                                                             minutes=30)

    assert acp_times.open_time(60, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=1,
                                                                                                            minutes=46)
    assert acp_times.close_time(60, 1000, sample_time).replace(second=0, microsecond=0) == sample_time.shift(hours=4)
