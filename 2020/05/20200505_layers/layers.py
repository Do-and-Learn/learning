import abc
import contextlib
import io


class L1Provider(abc.ABC):

    @abc.abstractmethod
    def l1_service(self):
        ...


class L2Provider(abc.ABC):

    @abc.abstractmethod
    def l2_service(self):
        ...

    @abc.abstractmethod
    def set_lower_layer(self, layer: L1Provider):
        ...


class L3Provider(abc.ABC):

    @abc.abstractmethod
    def l3_service(self):
        ...

    @abc.abstractmethod
    def set_lower_layer(self, layer: L2Provider):
        ...


class L1(L1Provider):

    def l1_service(self):
        print("L1 doing its job")


class L2(L2Provider):

    def __init__(self):
        self.l1 = None

    def l2_service(self):
        print("L2 service starting its job")
        self.l1.l1_service()
        print("L2 service finishing its job")

    def set_lower_layer(self, layer: L1Provider):
        self.l1 = layer


class L3(L3Provider):

    def __init__(self):
        self.l2 = None

    def l3_service(self):
        print("L3 service starting its job")
        self.l2.l2_service()
        print("L3 service finishing its job")

    def set_lower_layer(self, layer: L2Provider):
        self.l2 = layer


if __name__ == '__main__':
    l1 = L1()
    l2 = L2()
    l3 = L3()

    l2.set_lower_layer(l1)
    l3.set_lower_layer(l2)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        l3.l3_service()
    assert f.getvalue() == """\
L3 service starting its job
L2 service starting its job
L1 doing its job
L2 service finishing its job
L3 service finishing its job
"""
