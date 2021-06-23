"""
The security tags definitions, which are used in each NITF subheader element.
"""

import logging
from .base import NITFElement, _StringDescriptor, _StringEnumDescriptor, _parse_str

__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


#########
# NITF 2.1 version


class NITFSecurityTags(NITFElement):
    """
    The NITF security tags object for NITF version 2.1 - see standards document
    MIL-STD-2500C for more information.

    In the NITF standard, this object is simply redefined (is an identical way)
    for each of the main header and subheader objects. This object is intended to
    be flexibly used for any and all of these.
    """

    _ordering = (
        'CLAS', 'CLSY', 'CODE', 'CTLH', 'REL', 'DCTP', 'DCDT', 'DCXM',
        'DG', 'DGDT', 'CLTX', 'CAPT', 'CAUT', 'CRSN', 'SRDT', 'CTLN')
    _lengths = {
        'CLAS': 1, 'CLSY': 2, 'CODE': 11, 'CTLH': 2,
        'REL': 20, 'DCTP': 2, 'DCDT': 8, 'DCXM': 4,
        'DG': 1, 'DGDT': 8, 'CLTX': 43, 'CAPT': 1,
        'CAUT': 40, 'CRSN': 1, 'SRDT': 8, 'CTLN': 15}
    CLAS = _StringEnumDescriptor(
        'CLAS', True, 1, {'U', 'R', 'C', 'S', 'T'}, default_value='U',
        docstring='The classification level.')  # type: str
    CLSY = _StringDescriptor(
        'CLSY', True, 2, default_value='',
        docstring='Security Classification System. This field shall contain valid values '
                  'indicating the national or multinational security system used to classify this element. '
                  'Country Codes per FIPS PUB 10-4 shall be used to indicate national security systems. '
                  'The designator :code:`XN` is for classified data generated by a component using NATO security '
                  'system marking guidance. This code is outside the FIPS 10-4 document listing, and was '
                  'selected to not duplicate existing codes.')  # type: str
    CODE = _StringDescriptor(
        'CODE', True, 11, default_value='',
        docstring='Codewords. This field shall contain a valid indicator of the security '
                  'compartments associated. Valid values include one or more of the digraphs found '
                  'in table A-4. Multiple entries shall be separated by a single ECS spaces (0x20). '
                  'The selection of a relevant set of codewords is application '
                  'specific.')  # type: str
    CTLH = _StringDescriptor(
        'CTLH', True, 2, default_value='',
        docstring='Control and Handling. This field shall contain valid additional security control '
                  'and/or handling instructions (caveats) associated with this element.')  # type: str
    REL = _StringDescriptor(
        'REL', True, 20, default_value='',
        docstring='Releasing Instructions. This field shall contain a valid list of country and/or '
                  'multilateral entity codes to which countries and/or multilateral entities this element'
                  'is authorized for release. Valid items in the list are one or more country codes as '
                  'found in FIPS PUB 10-4 and/or codes identifying multilateral entities.')  # type: str
    DCTP = _StringEnumDescriptor(
        'DCTP', True, 2, {'', 'DD', 'DE', 'GD', 'GE', 'O', 'X'}, default_value='',
        docstring='Declassification Type. This field shall contain a valid indicator of the type of '
                  'security declassification or downgrading instructions which apply '
                  'to this element.')  # type: str
    DCDT = _StringDescriptor(
        'DCDT', True, 8, default_value='',
        docstring='Declassification Date. This field shall indicate the date on which this element '
                  'is to be declassified if the value in Declassification '
                  'Type is :code:`DD`.')  # type: str
    DCXM = _StringEnumDescriptor(
        'DCXM', True, 4,
        {'', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8',
         '25X1', '25X2', '25X3', '25X4', '25X5', '25X6', '25X7', '25X8', '25X9',
         'DN10', 'DNI'}, default_value='',
        docstring='Declassification Exemption. This field shall indicate the reason this element is '
                  'exempt from automatic declassification if the value in Declassification '
                  'Type is :code:`X`.')  # type: str
    DG = _StringEnumDescriptor(
        'DG', True, 1, {'', 'S', 'C', 'R'}, default_value='',
        docstring='Downgrade. This field shall indicate the classification level to which this element is to '
                  'be downgraded if the values in Declassification Type are '
                  ':code:`GD` or :code:`GE`.')  # type: str
    DGDT = _StringDescriptor(
        'DGDT', True, 8, default_value='',
        docstring='Downgrade Date. This field shall indicate the date on which this element is to be downgraded '
                  'if the value in Declassification Type is :code:`GD`.')  # type: str
    CLTX = _StringDescriptor(
        'CLTX', True, 43, default_value='',
        docstring='Classification Text. This field shall be used to provide additional information about '
                  'classification to include identification of a declassification or downgrading event if the '
                  'values in Declassification Type are DE or GE. It may also be used to identify multiple '
                  'classification sources and/or any other special handling rules. '
                  'Values are user defined free text.')  # type: str
    CAPT = _StringEnumDescriptor(
        'CAPT', True, 1, {'', 'O', 'D', 'M'}, default_value='',
        docstring='Classification Authority Type. This field shall indicate the type of authority '
                  'used to classify this element.')  # type: str
    CAUT = _StringDescriptor(
        'CAUT', True, 40, default_value='',
        docstring='Classification Authority. This field shall identify the classification authority '
                  'for this element dependent upon the value in Classification Authority Type. Values are user '
                  'defined free text which should contain the following information: original classification '
                  'authority name and position or personal identifier if the value in Classification Authority '
                  'Type is O; title of the document or security classification guide used to classify this element '
                  'if the value in Classification Authority Type is D; and Derive-Multiple if the classification '
                  'was derived from multiple sources. In the latter case, the originator will maintain a record '
                  'of the sources used in accordance with existing security directives. One of the multiple '
                  'sources may also be identified in Classification Text if desired')  # type: str
    CRSN = _StringEnumDescriptor(
        'CRSN', True, 1, {'', 'A', 'B', 'C', 'D', 'E', 'F', 'G'}, default_value='',
        docstring='Classification Reason. This field shall contain values indicating the reason for '
                  'classifying the graphic. Valid values are A to G. These correspond to the reasons for '
                  'original classification per E.O. 12958, Section 1.5.(a) to (g).')  # type: str
    SRDT = _StringDescriptor(
        'SRDT', True, 8, default_value='',
        docstring='Security Source Date. This field shall indicate the date of the source used to derive '
                  'the classification of the graphic. In the case of multiple sources, the date of the '
                  'most recent source shall be used.')  # type: str
    CTLN = _StringDescriptor(
        'CTLN', True, 15, default_value='',
        docstring='Security Control Number. This field shall contain a valid security control number '
                  'associated with the graphic. The format of the security control number shall be in '
                  'accordance with the regulations governing the appropriate '
                  'security channel(s).')  # type: str


#########
# NITF 2.0 version

class NITFSecurityTags0(NITFElement):
    """
    The NITF security tags object for NITF version 2.0 - see standards document
    MIL-STD-2500A for more information.

    In the NITF standard, this object is simply redefined (is an identical way)
    for each of the main header and subheader objects. This object is intended to
    be flexibly used for any and all of these.
    """

    _ordering = (
        'CLAS', 'CODE', 'CTLH', 'REL', 'CAUT', 'CTLN', 'DWNG', 'DEVT')
    _lengths = {
        'CLAS': 1, 'CODE': 40, 'CTLH': 40, 'REL': 40, 'CAUT': 20,
        'CTLN': 20, 'DWNG': 6, 'DEVT': 40}
    CLAS = _StringEnumDescriptor(
        'CLAS', True, 1, {'U', 'R', 'C', 'S', 'T'}, default_value='U')  # type: str
    CODE = _StringDescriptor('CODE', True, 40)  # type: str
    CTLH = _StringDescriptor('CTLH', True, 40)  # type: str
    REL = _StringDescriptor('REL', True, 40)  # type: str
    CAUT = _StringDescriptor('CAUT', True, 20)  # type: str
    CTLN = _StringDescriptor('CTLN', True, 20)  # type: str
    DWNG = _StringDescriptor('DWNG', True, 6)  # type: str

    def __init__(self, **kwargs):
        self._DEVT = None
        super(NITFSecurityTags0, self).__init__(**kwargs)

    @property
    def DEVT(self):
        return self._DEVT

    @DEVT.setter
    def DEVT(self, value):
        self._DEVT = _parse_str(value, 40, None, 'DEVT', self)

    def _get_attribute_length(self, fld):
        if fld == 'DEVT':
            return 0 if self.DWNG != '999998' else self._lengths[fld]
        else:
            return super(NITFSecurityTags0, self)._get_attribute_length(fld)

    @classmethod
    def minimum_length(cls):
        # DEVT may not be there
        return super(NITFSecurityTags0, cls).minimum_length() - 40

    @classmethod
    def _parse_attribute(cls, fields, attribute, value, start):
        if attribute == 'DEVT':
            if fields['DWNG'] == b'999998':
                fields['DEVT'] = value[start:start+40].decode('utf-8')
                return start+40
            else:
                fields['DEVT'] = None
                # nothing to be done
                return start
        else:
            return super(NITFSecurityTags0, cls)._parse_attribute(fields, attribute, value, start)
