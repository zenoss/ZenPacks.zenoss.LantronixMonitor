##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2008, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


__doc__ = """SLCDeviceMap
Gather model number, serial number and OS information from a 
Lantronix device.
"""

import re
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs

class SLCDeviceMap(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.244.1.1.6.1.0': 'setHWProductKey',
        '.1.3.6.1.4.1.244.1.1.6.2.0': 'setHWSerialNumber',
        '.1.3.6.1.4.1.244.1.1.6.3.0': 'setOSProductKey',
        })
    
    def process(self, device, results, log):
        getdata, tabledata = results
        om = self.objectMap(getdata)
        om.setHWProductKey = MultiArgs(om.setHWProductKey, "Lantronix")
        om.setOSProductKey = MultiArgs(om.setOSProductKey, "Lantronix")
        return om
