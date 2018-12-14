import shutil
import sys

# ~/RosettaCodeData/Lang/Python
# ~/rc-python
# outputdir can't exist or copytree fails

if len(sys.argv) < 3:
    print("Please call this program as follows:")
    print("    copyfromlink.py dirwsymlink outputdir")
    exit()
    
dirwsymlink = sys.argv[1]

outputdir = sys.argv[2] 

shutil.copytree(dirwsymlink, outputdir)
