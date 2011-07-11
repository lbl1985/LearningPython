import sys
sys.path.insert(0, 'C:\\CProjects\\LearningPython\\LinesCounting')

import LinesCounting_folder
import numpy

folderNameS = ["C:\CProjects\Kinect_OpenNI\RGBDemo-0.5.0-Source\RGBDemo-0.5.0-Source\mysuperdemo", 
               "C:\CProjects\LearningBoost", "C:\CProjects\LearningPython"]

folderNameS = ["C:\CProjects\LearningBoost", "C:\CProjects\Kinect_OpenNI\RGBDemo-0.5.0-Source\RGBDemo-0.5.0-Source\mysuperdemo", 
               "C:\CProjects\LearningPython"]
linesTotalProject = 0
linesPerProject = [];
for folder in folderNameS:
    linesOneProject = LinesCounting_folder.folderLines(folder)
    linesPerProject.append(str(linesOneProject))
    linesTotalProject = linesTotalProject + linesOneProject


print "total lines is: " + str(linesTotalProject)
