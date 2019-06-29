#!/usr/bin/python3
# -*- coding: utf-8 -*-
eol = '\n'

import pkg_resources
from subprocess import call
from subprocess import check_output
import sys

pVersion = int(sys.version[:1])
print("%s\n%s" % ("Welcome", "searching for outdated modules ..."))
print("%s %s" % ("Python Version:", sys.version[:5]))
packages = [dist.project_name for dist in pkg_resources.working_set]

if pVersion > 2:
    outdated = [check_output(["pip3",  "list",  "--outdated", "--user", "--format=freeze"])]
else:
    outdated = [check_output(["pip2",  "list",  "--outdated", "--user", "--format=freeze"])]

to_update = []

for line in outdated:
    to_update.append(line)

if pVersion > 2:
    print("%s %s" % ("pVersion:", "3"))
    ml = [str(x,'ascii', 'ignore') for x in to_update]
else:
    print("%s %s" % ("pVersion:", "2"))
    ml = [str(x) for x in to_update]

output = [sub.split('==') for sub in ml]

def getList(ml):
    mylist = []
    output = [sub.split('==') for sub in ml[0]]
    flat_list = [item for sublist in output for item in sublist]
    s = ('\n'.join(flat_list[:-1]))
    upgradeList = s.split(eol)[::2]
#    print("%s\n%s" %("Upgrade List:", '\n'.join(upgradeList)))
    return upgradeList

uList = getList(output)

print("%s %s" % (len(uList) - 1, "Updates available"))

if len(uList) > 1:
    for upgrade in getList(output):
        print("%s '%s'" % ("now updating module", upgrade))
#        if pVersion > 2:
#            call(["pip3",  "install",  "--upgrade", "--user", upgrade])
#        else:
#            call(["pip2",  "install",  "--upgrade", "--user", upgrade])
else:
    print("%s\n%s" % ("no upgrade needed", "###################################"))

print("%s\n%s" % ("Upgrade finished", "Goodbye ..."))
