# FastAnalysis
 FastAnalysis is a python module for analysing result from [FastTrack](http://www.fasttrack.sh) tracking software.
 
 ## Project info
 ![Linux tests](https://github.com/FastTrackOrg/FastAnalysis/workflows/Linux%20tests/badge.svg) ![Macos tests](https://github.com/FastTrackOrg/FastAnalysis/workflows/Macos%20tests/badge.svg) ![Windows tests](https://github.com/FastTrackOrg/FastAnalysis/workflows/Windows%20tests/badge.svg)
 
 ## Installation
 To install the module:
 ```
 git clone https://github.com/FastTrackOrg/FastAnalysis.git
 cd FastAnalysis
 pip install .
 ```
 
 ## Development
 The project is under active development and do not have public API documentation, a more or less complete API documentation can be generated using Sphinx.
 
 ## Documentation
 
 ### Retrieve data from a tracking.txt file
 A tracking.txt file can be loaded and several method are available to select objects and frames:
 ```
 import fastanalysis as fa
 
 tracking = fa.Load("tracking.txt")
 fa.isObjectsInFrame(0, 100) # Check if object with id 0 is in the 100th frame
 fa.isObjectsInFrame([0, 1], 100) # Check if object with id 0 and 1 is in the 100th frame
 a = tracking.getObjectsInFrames(0, 100) # Select data of the object with id 0 in the 100th frame
 b = tracking.getObjectsInFrames([0,1], [100,101]) # Select data of the object with id 0 and 1 in the 100th and 101th frames
 c = tracking.getObjects(0) # Select data of the object with id 0 for all the frames
 d = tracking.getObjects([0,1]) # Select data of the object with id 0 and 1 for all the frames
 e = tracking.getFrame(100) # Select data for all the objects in the 100th frame
 f = tracking.getFrame([100,101]) # Select data for all the objects in the 100th and 101th frames
 ```       
 
 ### Export data
 ```
 import fastanalysis as fa
 
 tracking = fa.Load("tracking.txt")
 keys = fa.keys() # List export features
 fa.export("output.xlsx", delimiter='\t', keys=["xHead", "yHead", "imageNumber", "id"], ids=None, indexes=None, format="excel") # Export a list of features for all the frames and all the objects in an excel file.
 fa.export("output.txt", delimiter='\t', keys=None, ids=None, indexes=None, format="excel") # Export all thefeatures for all the frames and all the objects in an csv file.
 ```
 Two format are supported: csv and excel.
 
 ### Plot metrics
 ```
 import fastanalysis as fa
 import matplotlib.pyplot as plt
 
 tracking = fa.Load("tracking.txt")
 plotObj = fa.Plot(tracking)
 plotObj.velocityDistribution(ids=[0, 1], key="Body", pooled=False, subplots=True) # Plot velocity distribution for objects 1 and 0 in 2 subplots
 plotObj.velocityDistribution(ids=[0, 1], key="Body", pooled=False, subplots=False) # Plot velocity distribution for objects 1 and 0 in 1 plot
 plotObj.velocityDistribution(ids=[0, 1], key="Body", pooled=True) # Plot velocity distribution for objects 1 and 0 pooled in 1 distribution
 ```
