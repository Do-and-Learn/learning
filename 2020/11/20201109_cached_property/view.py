import abc


class View:

    @abc.abstractmethod
    def _wait_for_view(self):
        pass
