######################################################################
#
# Copyright 2008 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

__doc__ = """SLCDevPorts
Gather Lantronix SecureLinx (SLC) configuration information.
"""

import re

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, \
        GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap


class SLCDevPorts(SnmpPlugin):
    relname = "devports"
    modname = "ZenPacks.zenoss.LantronixMonitor.SLCDevPort"

    snmpGetTableMaps = (
        GetTableMap('slcDevPortCfgTable', '.1.3.6.1.4.1.244.1.1.4.2.2.2.1', {
            '.1': 'snmpindex',
            '.2': 'id',
            '.5': 'breakSeq',
            '.6': 'telnetState',
            '.7': 'telnetPort',
            '.8': 'telnetAuth',
            '.9': 'sshState',
            '.10': 'sshPort',
            '.11': 'sshAuth',
            '.12': 'tcpState',
            '.13': 'tcpPort',
            '.14': 'tcpAuth',
            '.15': 'ip',
            '.16': 'baud',
            '.17': 'dataBits',
            '.18': 'stopBits',
            '.19': 'parity',
            '.20': 'flowControl',
            }),
        )
    
    stateMap = {1:False, 2:True}
    parityMap = {1:'none', 2:'odd', 3:'even'}
    flowControlMap = {1:'none', 2:'Xon/Xoff', 3:'RTS/CTS'}

    def process(self, device, results, log):
        getdata, tabledata = results
        portTable = tabledata.get("slcDevPortCfgTable")
        rm = self.relMap()
        for port in portTable.values():
            om = self.objectMap(port)
            om.id = self.prepId(om.id)
            om.telnetState = self.stateMap[om.telnetState]
            om.telnetAuth = self.stateMap[om.telnetAuth]
            om.sshState = self.stateMap[om.sshState]
            om.sshAuth = self.stateMap[om.sshAuth]
            om.tcpState = self.stateMap[om.tcpState]
            om.tcpAuth = self.stateMap[om.tcpAuth]
            om.parity = self.parityMap[om.parity]
            om.flowControl = self.flowControlMap[om.flowControl]
            rm.append(om)
        return rm
