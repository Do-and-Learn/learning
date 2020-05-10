import abc
import contextlib
import io


class Writer(abc.ABC):

    @abc.abstractmethod
    def write(self, data: str):
        ...


class Pusher:

    def __init__(self):
        self.target = None

    def set_target(self, target: Writer):
        self.target = target


class FilterPusher(Pusher, Writer):

    def write(self, data):
        data = self.process(data)
        self.target.write(data)

    @abc.abstractmethod
    def process(self, data: str) -> str:
        ...


class DataSource(Pusher):

    def push_loop(self):
        data = ['hello', 'my name', 'teddy!']
        for line in data:
            self.target.write(f'"{line}"')


class Filter1(FilterPusher):

    def process(self, data: str) -> str:
        return f'filter1({data})'


class Filter2(FilterPusher):

    def process(self, data: str) -> str:
        return f'filter2({data})'


class DataSink(Writer):

    def write(self, data: str):
        print(f'Receive: {data}')


if __name__ == '__main__':
    data_source = DataSource()
    filter1 = Filter1()
    filter2 = Filter2()
    data_sink = DataSink()

    data_source.set_target(filter1)
    filter1.set_target(filter2)
    filter2.set_target(data_sink)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        data_source.push_loop()
    assert f.getvalue() == """\
Receive: filter2(filter1("hello"))
Receive: filter2(filter1("my name"))
Receive: filter2(filter1("teddy!"))
"""