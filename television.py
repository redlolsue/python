class Television:
    """
    A class representing a simple television with power, mute, channel, and volume controls.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Set up a television that is off, unmuted, and at the minimum volume and channel.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the television on if it is off, or off if it is on.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute the television if it is unmuted, or unmute it if it is muted.
        Only works when the television is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by one when the television is on.
        Goes back to the minimum channel after the maximum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by one when the television is on.
        Goes to the maximum channel after the minimum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by one when the television is on, and unmute it.
        The volume stays at the maximum if it is already there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by one when the television is on, and unmute it.
        The volume stays at the minimum if it is already there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return the television's current settings. The volume shows as the minimum while muted.
        :return: A string in the format 'Power = [status], Channel = [channel], Volume = [volume]'.
        """
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
