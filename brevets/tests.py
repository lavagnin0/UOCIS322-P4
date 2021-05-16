import nose
import arrow
import acp_times as acp_times

sample_time = arrow.get('01/01/2021 00:00:00', 'MM/DD/YYYY HH:mm:ss')


def test_close_start_times():
    """
    Tests open/close times for controle locations for 60 km and under
	"""
    assert acp_times.open_time(0, 1000, sample_time).replace(second=0) == sample_time
    assert acp_times.close_time(0, 1000, sample_time).replace(second=0) == sample_time.shift(hours=1)

    assert acp_times.open_time(5, 1000, sample_time).replace(second=0) == sample_time.shift(minutes=9)
    assert acp_times.close_time(5, 1000, sample_time).replace(second=0) == sample_time.shift(hours=1, minutes=15)

    assert acp_times.open_time(20, 1000, sample_time).replace(second=0) == sample_time.shift(minutes=35)
    assert acp_times.close_time(20, 1000, sample_time).replace(second=0) == sample_time.shift(hours=2)

    assert acp_times.open_time(30, 1000, sample_time).replace(second=0) == sample_time.shift(minutes=53)
    assert acp_times.close_time(30, 1000, sample_time).replace(second=0) == sample_time.shift(hours=2, minutes=30)

    assert acp_times.open_time(60, 1000, sample_time).replace(second=0) == sample_time.shift(hours=1, minutes=46)
    assert acp_times.close_time(60, 1000, sample_time).replace(second=0) == sample_time.shift(hours=4)
