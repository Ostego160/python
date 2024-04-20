class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2

    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status  = False
        self.__muted   = False
        self.__volume  = 0
        self.__channel = 0

    def power(self):
        """
        Method to toggle television power.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Method to toggle television mute.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Method to increase the channel.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease the channel.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increase the volume.
        """
        if self.__status:
            self.__muted = False
            self.__volume = min(self.MAX_VOLUME, self.__volume + 1)

    def volume_down(self):
        """
        Method to decrease the volume.
        """
        if self.__status:
            self.__muted = False
            self.__volume = max(self.MIN_VOLUME, self.__volume - 1)

    def __str__(self) -> str:
        """
        Method to show TV status.
        :return: tv status
        """
        if self.__muted:
            return f'# Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'# Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'