"""

Created on Mon Oct 30 15:14:06 2023

Marco Miani
Computational Support Specialist
Climate and Atmosphere Research Center (CARE-C)
The Cyprus Institute
20 Konstantinou Kavafi Street, 2121, Nicosia, Cyprus
Tel: +357 22 397 561 | Email: m.miani@cyi.ac.cy
Web: cyi.ac.cy | emme-care.cyi.ac.cy
"""



modules2import = ['wrf', 'matplotlib', 'cartopy', 'netCDF4', 'pandas']


print("\n")
print("There are {} necessary modules we are going to need for this training. Let me check if you have them".format(len(modules2import)))
print(2*"\n")
for module in modules2import: 
    try: 
        eval("exec('import {}')".format(module))
        print('[OK] \t {} is availble! All right!' .format(module))
    except: 
        print("[NO] \t >>Error when loading module {}\n\t\t\t Use conda or pip to install it -- you will need it".format(module))




import platform 
import os
print(1*"\n")
print(30*"-")
plt = platform.system()
print('You username is: ', os.getlogin())
if plt == "Windows":
    print("Your system is Windows (by the way I dont like your OS...)")
    # do x y z
elif plt == "Linux":
    print("Your system is Linux")
    # do x y z
elif plt == "Darwin":
    print("Your system is MacOS")
    # do x y z
else:
    print('What OS are you running on???')
    
print("")
os.system('df -h /')  

