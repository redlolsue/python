import pytest
from television import Television


@pytest.fixture
def tv() -> Television:
    return Television()


def test_init(tv: Television) -> None:
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_power(tv: Television) -> None:
    # TV on
    tv.power()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # TV off
    tv.power()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_mute(tv: Television) -> None:
    # TV on, volume increased once, then muted
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # TV on and unmuted
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    # TV off and muted (mute does nothing while the TV is off)
    tv.power()
    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'

    # TV off and unmuted
    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'


def test_channel_up(tv: Television) -> None:
    # TV off and channel increased
    tv.channel_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # TV on and channel increased
    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'

    # TV on and channel increased past the maximum
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_channel_down(tv: Television) -> None:
    # TV off and channel decreased
    tv.channel_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # TV on and channel decreased past the minimum
    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'


def test_volume_up(tv: Television) -> None:
    # TV off and volume increased
    tv.volume_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # TV on and volume increased
    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    # TV on, muted, and volume increased
    tv.mute()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

    # TV on and volume increased past the maximum
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'


def test_volume_down(tv: Television) -> None:
    # TV off and volume decreased
    tv.volume_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # TV on and volume decreased (after raising it to the maximum)
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    # TV on, muted, and volume decreased
    tv.mute()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # TV on and volume decreased past the minimum
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'
