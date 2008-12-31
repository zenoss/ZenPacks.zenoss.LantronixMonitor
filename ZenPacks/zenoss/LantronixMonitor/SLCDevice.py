######################################################################
#
# Copyright 2007 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from copy import deepcopy


class SLCDevice(Device):
    _relations = Device._relations + (
        ('devports', ToManyCont(ToOne,
            'ZenPacks.zenoss.LantronixMonitor.SLCDevPort', 'slc')),
        )

    factory_type_information = deepcopy(Device.factory_type_information)
    custom_actions = []
    custom_actions.extend(factory_type_information[0]['actions'])
    custom_actions.insert(2,
           { 'id'              : 'lantronixSLCDeviceDetail'
           , 'name'            : 'Ports'
           , 'action'          : 'lantronixSLCDeviceDetail'
           , 'permissions'     : (ZEN_VIEW, ) },
           )
    factory_type_information[0]['actions'] = custom_actions

    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()


InitializeClass(SLCDevice)
