#!/usr/bin/python

import commands
import os
import subprocess

#os.chdir("/git/project/dir")
##os.chdir("C:\CProjects\Kinect_OpenNI\RGBDemo-0.5.0-Source\RGBDemo-0.5.0-Source\mysuperdemo")
##os.chdir("C:\CProjects\LearningBoost")
os.chdir("C:\CProjects\LearningPython")
#author = "author@comany"
author = "herbert19lee@gmail.com"

#print os.popen("dir").read()
##output=os.popen("dir").read()
##print output
##
##(stat, output) = commands.getstatusoutput(pipe)
##
##if (stat == 0):
##    print "Command succeeded, here is the output: %s" % output
##else:
##    print "Command failed, here is the output:%s" % output
        
#hist = commands.getoutput("git log --shortstat --reverse --pretty=oneline --since=07/06/2011 --author=\"" + author + "\" --no-merges")
##hist = os.popen("git log --shortstat --reverse --pretty=oneline --since=07/06/2011 --author=\"" + author + "\" --no-merges").read()
hist = os.popen("git log --shortstat --reverse --pretty=oneline --since=07/05/2011 --author=herbert19lee@gmail.com").read()
print hist

##hist = os.popen("git log --shortstat --reverse --pretty=oneline --since=07/06/2011 --author=herbert19lee@gmail.com").read()

hist = hist.split("\n")
totalins = 0

for line in hist:
    if line.startswith(' '):
        ins =  line.split(",")[1]
        totalins = totalins + int(ins.split(" ")[1])


print "Since 07/06/2011 you (" + author + ") wrote " + str(totalins) + " lines of code!"