class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2

    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status  = False
        self.__muted   = False
        self.__volume  = 0
        self.__channel = 0

    def power(self) -> None:
        """
        Method to toggle television power.

        :returns:
            None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to toggle television mute.

        :returns:
            None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the channel.

        :returns:
            None
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel.

        :returns:
            None
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume.

        :returns:
            None
        """
        if self.__status:
            self.__muted = False
            self.__volume = min(Television.MAX_VOLUME, self.__volume + 1)

    def volume_down(self) -> None:
        """
        Method to decrease the volume.

        :returns:
            None
        """
        if self.__status:
            self.__muted = False
            self.__volume = max(Television.MIN_VOLUME, self.__volume - 1)

    def __str__(self) -> str:
        """
        Method to show TV status.

        :returns:
            str: tv status
        """
        if self.__muted:
            return f'# Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'# Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'