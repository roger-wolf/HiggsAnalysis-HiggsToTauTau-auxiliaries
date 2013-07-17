#!/usr/bin/env python

import os

prefix = {
    'mt' : 'muTau_',
    'et' : 'eleTau_',
    }
folders = {
    'X'         : '0jet_low'  ,
    '0jet_high' : '0jet_high' ,
    'boost_low' : 'boost_low' ,
    'boost_high': 'boost_high',
    'vbf'       : 'vbf'       ,
    }

for chn in ['et', 'mt'] :
    for per in ['8TeV'] :
        if os.path.exists("htt_{CHN}.inputs-sm-{PER}-inclusive.root".format(CHN=chn, PER=per)) :
            os.system("rm htt_{CHN}.inputs-sm-{PER}-inclusive.root".format(CHN=chn, PER=per))
        for old,new in folders.iteritems() :
            os.system("root -l -q -b renameFolders.C\(\\\"htt_{CHN}.inputs-sm-{PER}.root\\\",\\\"htt_{CHN}.inputs-sm-{PER}-inclusive.root\\\",\\\"{OLD}\\\",\\\"{NEW}\\\"\)".format(
                CHN=chn,
                PER=per,
                OLD=prefix[chn]+old,
                NEW=prefix[chn]+new,
                ))
