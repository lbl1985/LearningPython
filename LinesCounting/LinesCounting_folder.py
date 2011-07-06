#!/usr/bin/python

import commands
import os

os.chdir("/git/project/dir")
author = "author@comany"
hist = commands.getoutput("git log --shortstat --reverse --pretty=oneline --since=\"last Saturday\" --author=\"" + author + "\" --no-merges")

hist = hist.split("\n")
totalins = 0

for line in hist:
    if line.startswith(' '):
        ins =  line.split(",")[1]
        totalins = totalins + int(ins.split(" ")[1])


print "Since last Saturday you (" + author + ") wrote " + str(totalins) + " lines of code!"