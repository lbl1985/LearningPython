#!/usr/bin/python
import commands
import os
import datetime


def folderLines(folder):


#os.chdir("/git/project/dir")
#folder = "C:\CProjects\Kinect_OpenNI\RGBDemo-0.5.0-Source\RGBDemo-0.5.0-Source\mysuperdemo"
#folder = "C:\CProjects\LearningBoost"
#folder = "C:\CProjects\LearningPython"
    os.chdir(folder)

    author = "herbert19lee@gmail.com"

##hist = os.popen("git log --shortstat --reverse --pretty=medium --since=07/06/2011 --author=\"" + author + "\" --no-merges").read()
    d = datetime.date.today()
    date = d.isoformat()
    time = "08:00am"
##    time = "yesterday"
    time = "01:00am"
##    time = "yesterday"
##    time = "today"
    commandline = "git log --shortstat --reverse --pretty=oneline --since \"" + time + "\" --author=herbert19lee@gmail.com --no-merges"

##print commandline
    hist = os.popen(commandline).read()
    print hist

    hist = hist.split("\n")
    totalins = 0

    for line in hist:
        if line.startswith(' '):
            ins =  line.split(",")[1]
            # Because, every commit should be less than 100 lines, if one commit
            # more than 100 lines, it's probably for copy based or import a new
            # library into the project
            if int(ins.split(" ")[1]) < 150:
                totalins = totalins + int(ins.split(" ")[1])


    print "Since " + date + "-" +  time + " you (" + author + ") wrote " + str(totalins) + " lines of code!"
    return (totalins)
