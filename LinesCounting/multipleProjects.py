import sys
if sys.platform.startswith('win32'):
    sys.path.insert(0, 'C:\\CProjects\\LearningPython\\LinesCounting')
elif sys.platform.startswith('darwin'):
    sys.path.insert(0, '/Users/herbert19lee/Develop/DevelopPython/LearningPython')
                    

import LinesCounting_folder
import numpy

folderNameS = ["C:\CProjects\Kinect_OpenNI\RGBDemo-0.5.0-Source\RGBDemo-0.5.0-Source\mysuperdemo", 
               "C:\CProjects\LearningBoost", "C:\CProjects\LearningPython",
               "C:\Users\lbl1985\Documents\MATLAB\work\celltrack"]

if sys.platform.startswith('win32'):
    folderNameS = ["C:\CProjects\Kinect_OpenNI\RGBDemo-0.5.0-Source\RGBDemo-0.5.0-Source\mysuperdemo", 
               "C:\CProjects\LearningBoost", "C:\CProjects\LearningPython",
                   "C:\Users\lbl1985\Documents\MATLAB\work\HFeature"]
elif sys.platform.startswith('darwin'):
    folderNameS = ["/Users/herbert19lee/Develop/LearningPython",
                   "/Users/herbert19lee/Documents/MATLAB/work/celltrack",
                   "/Users/herbert19lee/Documents/MATLAB/work/HFeature",
                   "/Users/herbert19lee/Documents/eclipse/MyRobots", 
                   "/Users/herbert19lee/Develop/LearningJava"
                   ]

linesTotalProject = 0
linesOneProjectArray = [];
for folder in folderNameS:
    linesOneProject = LinesCounting_folder.folderLines(folder)
    #linesOneProjectArray.append(str(linesOneProject))
    print("Project: \n" + folder + "\n" + str(linesOneProject)) + " LINES"
    linesTotalProject = linesTotalProject + linesOneProject


print "total lines is: " + str(linesTotalProject)
