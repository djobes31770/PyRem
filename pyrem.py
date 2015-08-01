#!/usr/bin/env python
#__author__ = 'djobes'

import os, sys, subprocess
import volatility.conf as conf
import volatility.registry as registry
import volatility.commands as commands
import volatility.addrspace as addrspace
import volatility.plugins.taskmods as taskmods
import volatility.plugins.imageinfo as imageinfo
#import volatility.plugins.kdbgscan as image

registry.PluginImporter()
config = conf.ConfObject()

#registry.register_global_options(config, commands.Command)
#registry.register_global_options(config, addrspace.BaseAddressSpace)
config.parse_options()
config.PROFILE="Win8SP1x86"
config.LOCATION = "file:///Users/djobes/case-20150729-101/REMWORKSTATION-20150729-114536.raw"

def image_info():
    #imginfo = os.system(vcmd + ' -f ' + vmem +  '  --profile=' + prof + ' imageinfo')
    info = imageinfo.ImageInfo(__self__, config, *args)
    print info

def proc_count():
    p = taskmods.PSList(config)
    for process in p.calculate():
        print process


image_info()
proc_count()
