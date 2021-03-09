#!/usr/bin/python
import os,glob
import argparse
import sys

script_dir = os.path.dirname(__file__)

def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(description='RootBeer Bypass Tools')
    parser.add_argument('--path',
                    help='Path to the input directory of decompiled folder apps.')
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    #path of decompiled folder
    mypath = parsed_args.path+'/smali/com/scottyab/rootbeer'

    listConst = [
        'com.noshufou.android.su',
        'com.noshufou.android.su.elite',
        'eu.chainfire.supersu',
        'com.koushikdutta.superuser',
        'com.thirdparty.superuser',
        'com.yellowes.su',
        'com.topjohnwu.magisk',
        'com.kingroot.kinguser',
        'com.kingo.root',
        'com.smedialink.oneclickroot',
        'com.zhiqupk.root.global',
        'com.alephzain.framaroot',
        'com.koushikdutta.rommanager',
        'com.koushikdutta.rommanager.license',
        'com.dimonvideo.luckypatcher',
        'com.chelpus.lackypatch',
        'com.ramdroid.appquarantine',
        'com.ramdroid.appquarantinepro',
        'com.android.vending.billing.InAppBillingService.COIN',
        'com.chelpus.luckypatcher',
        'com.devadvance.rootcloak',
        'com.devadvance.rootcloakplus',
        'de.robv.android.xposed.installer',
        'com.saurik.substrate',
        'com.zachspong.temprootremovejb',
        'com.amphoras.hidemyroot',
        'com.amphoras.hidemyrootadfree',
        'com.formyhm.hiderootPremium',
        'com.formyhm.hideroot',
    ]

    listFolderConst = [
        '/data/local/',
        '/data/local/bin/',
        '/data/local/xbin/',
        '/sbin/',
        '/su/bin/',
        '/system/bin/',
        '/system/bin/.ext/',
        '/system/bin/failsafe/',
        '/system/sd/xbin/',
        '/system/usr/we-need-root/',
        '/system/xbin/',
        '/cache/',
        '/data/',
        '/dev/',
        '/system',
        '/system/bin',
        '/system/sbin',
        '/system/xbin',
        '/vendor/bin',
        '/sbin',
        '/etc'
    ]

    # replace const to random const
    for comConst in listConst:
        for filename in glob.glob(os.path.join(mypath, '*.smali')):
            with open(filename,'r') as f:
                newlines = []
                for line in f.readlines():
                    newlines.append(line.replace(comConst, 'com.m1n007'))
            with open(filename, 'w') as f:
                for line in newlines:
                    f.write(line)

    # replace folder const into 
    for sbinFolderConst in listFolderConst:
        for filename in glob.glob(os.path.join(mypath, '*.smali')):
            with open(filename,'r') as f:
                newlines = []
                for line in f.readlines():
                    newlines.append(line.replace(sbinFolderConst, '/m1n007'))
            with open(filename, 'w') as f:
                for line in newlines:
                    f.write(line)

    # replace all return true to false
    for filename in glob.glob(os.path.join(mypath, '*.smali')):
        with open(filename,'r') as f:
            newlines = []
            for line in f.readlines():
                newlines.append(line.replace('const/4 v0, 0x1', 'const/4 v0, 0x0'))
        with open(filename, 'w') as f:
            for line in newlines:
                f.write(line)

    print('Success!!!')

