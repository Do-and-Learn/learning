import abc
import contextlib
import io

import typing


class Reader(abc.ABC):

    @abc.abstractmethod
    def read(self) -> str:
        pass


class Writer(abc.ABC):

    @abc.abstractmethod
    def write(self, data: str):
        pass


class Puller(abc.ABC):

    @abc.abstractmethod
    def set_source(self, reader: Reader):
        pass


class Pusher(abc.ABC):
    @abc.abstractmethod
    def set_target(self, writer: Writer):
        pass


class DataSource(Reader):

    def __init__(self):
        data = ['hello', 'my name', 'teddy!']
        self.iter = iter(data)

    def read(self) -> str:
        return f'"{next(self.iter)}"'


class Filter1(Reader, Puller):

    def __init__(self):
        self.source: typing.Optional[Reader] = None

    def read(self) -> str:
        source = self.source.read()
        processed = self.process(source)
        return processed

    def set_source(self, reader: Reader):
        self.source = reader

    @classmethod
    def process(cls, data: str) -> str:
        return f'filter1({data})'


class Filter2(Pusher, Puller):

    def __init__(self):
        self.source: typing.Optional[Reader] = None
        self.target: typing.Optional[Writer] = None

    def set_target(self, writer: Writer):
        self.target = writer

    def set_source(self, reader: Reader):
        self.source = reader

    @classmethod
    def process(cls, data: str) -> str:
        return f'filter2({data})'

    def loop(self):
        try:
            while True:
                source = self.source.read()
                processed = self.process(source)
                self.target.write(processed)
        except StopIteration:
            pass


class DataSink(Writer):

    def write(self, data: str):
        print(f'Receive: {data}')


if __name__ == '__main__':
    data_source = DataSource()
    data_sink = DataSink()
    filter1 = Filter1()
    filter2 = Filter2()

    filter1.set_source(data_source)
    filter2.set_source(filter1)
    filter2.set_target(data_sink)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        filter2.loop()

    assert f.getvalue() == """\
Receive: filter2(filter1("hello"))
Receive: filter2(filter1("my name"))
Receive: filter2(filter1("teddy!"))
"""
