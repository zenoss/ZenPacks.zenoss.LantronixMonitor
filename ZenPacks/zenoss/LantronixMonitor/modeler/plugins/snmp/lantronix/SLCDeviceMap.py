##########################################################################
#
#   Copyright 2008 Zenoss, Inc. All Rights Reserved.
#
##########################################################################

import re
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class SLCDeviceMap(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.244.1.1.6.1.0': 'setHWProductKey',
        '.1.3.6.1.4.1.244.1.1.6.2.0': 'setHWSerialNumber',
        '.1.3.6.1.4.1.244.1.1.6.3.0': 'setOSProductKey',
        })
    
    def process(self, device, results, log):
        getdata, tabledata = results
        return self.objectMap(getdata)
