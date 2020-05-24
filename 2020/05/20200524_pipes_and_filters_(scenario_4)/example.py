import abc
import contextlib
import io
import queue
import threading

import typing


class Reader(abc.ABC):

    @abc.abstractmethod
    def read(self) -> typing.Optional[str]:
        pass


class Writer(abc.ABC):

    @abc.abstractmethod
    def write(self, data: typing.Optional[str]):
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
        data = ['hello', 'my name', 'teddy!', None]
        self.iter = iter(data)

    def read(self) -> typing.Optional[str]:
        return next(self.iter)


class Filter1(Pusher, Puller):

    def __init__(self):
        self.source: typing.Optional[Reader] = None
        self.target: typing.Optional[Writer] = None

    def set_target(self, writer: Writer):
        self.target = writer

    def set_source(self, reader: Reader):
        self.source = reader

    @classmethod
    def process(cls, data: str) -> str:
        return f'filter1({data})'

    def loop(self):
        while True:
            source = self.source.read()
            if source is None:
                self.target.write(None)
                break
            processed = self.process(source)
            self.target.write(processed)


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
        while True:
            source = self.source.read()
            if source is None:
                break
            processed = self.process(source)
            self.target.write(processed)


class DataSink(Writer):

    def write(self, data: str):
        print(f'Receive: {data}')


class Pipe(Reader, Writer):

    def __init__(self):
        self.q = queue.SimpleQueue()

    def read(self) -> typing.Optional[str]:
        return self.q.get()

    def write(self, data: str):
        self.q.put(data)


if __name__ == '__main__':
    data_source = DataSource()
    data_sink = DataSink()
    pipe = Pipe()
    filter1 = Filter1()
    filter2 = Filter2()

    filter1.set_source(data_source)
    filter1.set_target(pipe)
    filter2.set_source(pipe)
    filter2.set_target(data_sink)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        t1 = threading.Thread(target=lambda: filter1.loop())
        t2 = threading.Thread(target=lambda: filter2.loop())
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    assert f.getvalue() == """\
Receive: filter2(filter1(hello))
Receive: filter2(filter1(my name))
Receive: filter2(filter1(teddy!))
"""
