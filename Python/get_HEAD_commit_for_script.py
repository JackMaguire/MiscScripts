import os
import subprocess
#git --git-dir ~/HBondMachineLearning/.git rev-parse HEAD

pwd = os.path.realpath(__file__)
HBondMachineLearning_index = pwd.find( "HBondMachineLearning" )
path = pwd[:HBondMachineLearning_index]

#print( path )
full_name = "~/HBondMachineLearning/.git".replace( "~", path )

sha1 = subprocess.check_output(["git", "--git-dir", full_name, "rev-parse", "HEAD"]).strip()
print ( sha1 )

