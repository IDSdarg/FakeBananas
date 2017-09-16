# This is the main python file that aggregates all our seperate soruces.

# import numpy as np
import pandas as pd
# import local packages
# import ml
import rep
print("Pipeline running...")

##################
## WEB SCRAPING ##
##################

# example call to python2 file:
# result = call_python_version("2.7", "module(folder_name)", "filename.py", "function_name", ["param1", "param2"])

######################
## MACHINE LEARNING ##
######################

# runs predictions and outputs a .csv file
# predictions is a list of 0-4 for agree/dis..etc.

# stances = ml.mlPred()
stances = [1,2,3,2,3,3,2,2,3,1,0,0,2,3]
bodyID = range(len(stances))
sourceNames = range(len(stances))
urls = range(len(stances))

ml_output = pd.DataFrame(
    {'BodyID': bodyID,
     'Stances': stances,
     'SourceName': sourceNames,
     'URL': urls
    })

print(ml_output)

print(ml_output.loc[0,'Stances'])
print(ml_output.loc[1,'Stances'])



########################
## REPUTATION SYSTEMS ##
########################

rep.loadReputations(defaultReputations);


print("Pipeline complete")

