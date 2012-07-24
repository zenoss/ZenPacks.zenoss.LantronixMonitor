##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2008, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity

def enStr(value, default="unknown"):
    if value is None:
        return default
    elif value:
        return "enabled"
    else:
        return "disabled"


class SLCDevPort(DeviceComponent, ManagedEntity):
    portal_type = meta_type = 'SLCDevPort'
    
    breakSeq = ""
    telnetState = None
    telnetPort = None
    telnetAuth = None
    sshState = None
    sshPort = None
    sshAuth = None
    tcpState = None
    tcpPort = None
    tcpAuth = None
    ip = ""
    baud = None
    dataBits = None
    stopBits = None
    parity = ""
    flowControl = ""

    _properties = (
        {'id':'breakSeq', 'type':'string', 'mode':'w'},
        {'id':'telnetState', 'type':'boolean', 'mode':'w'},
        {'id':'telnetPort', 'type':'int', 'mode':'w'},
        {'id':'telnetAuth', 'type':'boolean', 'mode':'w'},
        {'id':'sshState', 'type':'boolean', 'mode':'w'},
        {'id':'sshPort', 'type':'int', 'mode':'w'},
        {'id':'sshAuth', 'type':'boolean', 'mode':'w'},
        {'id':'tcpState', 'type':'boolean', 'mode':'w'},
        {'id':'tcpPort', 'type':'int', 'mode':'w'},
        {'id':'tcpAuth', 'type':'boolean', 'mode':'w'},
        {'id':'ip', 'type':'string', 'mode':'w'},
        {'id':'baud', 'type':'int', 'mode':'w'},
        {'id':'dataBits', 'type':'int', 'mode':'w'},
        {'id':'stopBits', 'type':'int', 'mode':'w'},
        {'id':'parity', 'type':'string', 'mode':'w'},
        {'id':'flowControl', 'type':'string', 'mode':'w'},
        )

    _relations = (
        ("slc", ToOne(ToManyCont,
            "ZenPacks.zenoss.LantronixMonitor.SLCDevice", "devports")),
        )
    

    factory_type_information = ( 
        { 
            'id'             : 'SLCDevPort',
            'meta_type'      : 'SLCDevPort',
            'description'    : """Arbitrary device grouping class""",
            'icon'           : 'SLCDevPort_icon.gif',
            'product'        : 'LantronixMonitor',
            'factory'        : 'manage_addSLCDevPort',
            'immediate_view' : 'viewSLCDevPort',
            'actions'        :
            ( 
                { 'id'            : 'status'
                , 'name'          : 'Status'
                , 'action'        : 'viewSLCDevPort'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_SETTINGS, )
                },                
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW, )
                },
            )
          },
        )
        
    def viewName(self):
        return self.id
    name = viewName

    def primarySortKey(self):
        return self.snmpindex

    def device(self):
        return self.slc()
    
    def getTelnetStateString(self): return enStr(self.telnetState)
    def getTelnetPortString(self): return self.telnetPort or "????"
    def getTelnetAuthString(self): return enStr(self.telnetAuth)
    def getSSHStateString(self): return enStr(self.sshState)
    def getSSHPortString(self): return self.sshPort or "????"
    def getSSHAuthString(self): return enStr(self.sshAuth)
    def getTCPStateString(self): return enStr(self.tcpState)
    def getTCPPortString(self): return self.tcpPort or "????"
    def getTCPAuthString(self): return enStr(self.tcpAuth)
    def getBaudString(self): return str(self.baud) or "????"
    def getDataBitsString(self): return str(self.dataBits) or "?"
    def getStopBitsString(self): return str(self.stopBits) or "?"
    def getParityString(self): return self.parity or "unknown"
    def getFlowControlString(self): return self.flowControl or "unknown"
    
    def getTelnetString(self):
        return "%s: %s/%s" % (self.getTelnetPortString(),
            self.getTelnetStateString(), self.getTelnetAuthString())
    
    def getSSHString(self):
        return "%s: %s/%s" % (self.getSSHPortString(),
            self.getSSHStateString(), self.getSSHAuthString())
    
    def getTCPString(self):
        return "%s: %s/%s" % (self.getTCPPortString(),
            self.getTCPStateString(), self.getTCPAuthString())
    
    def getPortString(self):
        return "%s %s,%s,%s" % (self.getBaudString(), self.getDataBitsString(),
            self.getParityString(), self.getStopBitsString())


InitializeClass(SLCDevPort)
