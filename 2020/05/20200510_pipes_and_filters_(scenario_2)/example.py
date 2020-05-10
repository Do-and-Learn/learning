import abc
import contextlib
import io


class Reader(abc.ABC):

    @abc.abstractmethod
    def read(self) -> str:
        ...


class Puller:

    def __init__(self):
        self.source = None

    def set_source(self, source: Reader):
        self.source = source


class FilterPuller(Puller, Reader):

    def read(self) -> str:
        data = self.source.read()
        data = self.process(data)
        return data

    @abc.abstractmethod
    def process(self, data: str) -> str:
        ...


class DataSource(Puller, Reader):

    def __init__(self):
        Reader.__init__(self)
        data = ['hello', 'my name', 'teddy!']
        self.iter = iter(data)

    def read(self) -> str:
        return f'"{next(self.iter)}"'


class Filter1(FilterPuller):

    def process(self, data: str) -> str:
        return f'filter1({data})'


class Filter2(FilterPuller):

    def process(self, data: str) -> str:
        return f'filter2({data})'


class DataSink(Puller):

    def pull_loop(self):
        try:
            while True:
                data = self.source.read()
                print(f'Receive: {data}')
        except StopIteration:
            pass


if __name__ == '__main__':
    data_sink = DataSink()
    filter1 = Filter1()
    filter2 = Filter2()
    data_source = DataSource()

    data_sink.set_source(filter2)
    filter2.set_source(filter1)
    filter1.set_source(data_source)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        data_sink.pull_loop()

    assert f.getvalue() == """\
Receive: filter2(filter1("hello"))
Receive: filter2(filter1("my name"))
Receive: filter2(filter1("teddy!"))
"""
