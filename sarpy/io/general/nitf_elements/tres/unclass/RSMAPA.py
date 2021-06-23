
from ..tre_elements import TREExtension, TREElement

__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


class PAR(TREElement):
    def __init__(self, value):
        super(PAR, self).__init__()
        self.add_field('PARVAL', 's', 21, value)


class RSMAPAType(TREElement):
    def __init__(self, value):
        super(RSMAPAType, self).__init__()
        self.add_field('IID', 's', 80, value)
        self.add_field('EDITION', 's', 40, value)
        self.add_field('TID', 's', 40, value)
        self.add_field('NPAR', 'd', 2, value)
        self.add_field('XUOL', 's', 21, value)
        self.add_field('YUOL', 's', 21, value)
        self.add_field('ZUOL', 's', 21, value)
        self.add_field('XUXL', 's', 21, value)
        self.add_field('XUYL', 's', 21, value)
        self.add_field('XUZL', 's', 21, value)
        self.add_field('YUXL', 's', 21, value)
        self.add_field('YUYL', 's', 21, value)
        self.add_field('YUZL', 's', 21, value)
        self.add_field('ZUXL', 's', 21, value)
        self.add_field('ZUYL', 's', 21, value)
        self.add_field('ZUZL', 's', 21, value)
        self.add_field('IR0', 's', 2, value)
        self.add_field('IRX', 's', 2, value)
        self.add_field('IRY', 's', 2, value)
        self.add_field('IRZ', 's', 2, value)
        self.add_field('IRXX', 's', 2, value)
        self.add_field('IRXY', 's', 2, value)
        self.add_field('IRXZ', 's', 2, value)
        self.add_field('IRYY', 's', 2, value)
        self.add_field('IRYZ', 's', 2, value)
        self.add_field('IRZZ', 's', 2, value)
        self.add_field('IC0', 's', 2, value)
        self.add_field('ICX', 's', 2, value)
        self.add_field('ICY', 's', 2, value)
        self.add_field('ICZ', 's', 2, value)
        self.add_field('ICXX', 's', 2, value)
        self.add_field('ICXY', 's', 2, value)
        self.add_field('ICXZ', 's', 2, value)
        self.add_field('ICYY', 's', 2, value)
        self.add_field('ICYZ', 's', 2, value)
        self.add_field('ICZZ', 's', 2, value)
        self.add_field('GX0', 's', 2, value)
        self.add_field('GY0', 's', 2, value)
        self.add_field('GZ0', 's', 2, value)
        self.add_field('GXR', 's', 2, value)
        self.add_field('GYR', 's', 2, value)
        self.add_field('GZR', 's', 2, value)
        self.add_field('GS', 's', 2, value)
        self.add_field('GXX', 's', 2, value)
        self.add_field('GXY', 's', 2, value)
        self.add_field('GXZ', 's', 2, value)
        self.add_field('GYX', 's', 2, value)
        self.add_field('GYY', 's', 2, value)
        self.add_field('GYZ', 's', 2, value)
        self.add_field('GZX', 's', 2, value)
        self.add_field('GZY', 's', 2, value)
        self.add_field('GZZ', 's', 2, value)
        self.add_loop('PARs', self.NPAR, PAR, value)


class RSMAPA(TREExtension):
    _tag_value = 'RSMAPA'
    _data_type = RSMAPAType
