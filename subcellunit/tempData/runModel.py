from pprint import pprint
from scipy.integrate import odeint
import CaMKIIs
import SBtabTools

sbTab_dict = SBtabTools.openSBtab_asBook('SBtab_CaMKII_Measurements.xls')
#print "sheets = ", SBtabTable_list

inputParams = {}
sbTab = sbTab_dict["InputParameters"].createSBtabDict()
for key,val in sbTab["!Name"].items():
    inputParams[val] = float(sbTab["!DefaultValue"][key])
sbTab = sbTab_dict["Parameters"].createSBtabDict()
for key,val in sbTab["!Name"].items():
    inputParams[val] = float(sbTab["!DefaultValue"][key])
#pprint(inputParams)
#print len(inputParams)
locals().update(inputParams)

params = [kf__CaM__Ca,kf__CaM_Ca1__Ca,kf__CaM_Ca2__Ca,kf__CaM_Ca3__Ca,kf__CaM__PP2B,kf__CaM_Ca1__PP2B,kf__CaM_Ca2__PP2B,kf__CaM_Ca3__PP2B,kf__CaM_Ca4__PP2B,kf__PP2B_CaM__Ca,kf__PP2B_CaM_Ca1__Ca,kf__PP2B_CaM_Ca2__Ca,kf__PP2B_CaM_Ca3__Ca,KD__CaM_Ca3__Ca,KD__CaM_Ca2__Ca,KD__CaM_Ca1__Ca,KD__CaM__Ca,KD__CaM_Ca4__PP2B,KD__PP2B_CaM_Ca3__Ca,KD__PP2B_CaM_Ca2__Ca,KD__PP2B_CaM_Ca1__Ca,KD__PP2B_CaM__Ca,kf__CaM__CaMKII,kf__CaMKII_CaM_Ca3__Ca,kf__CaMKII_CaM_Ca2__Ca,kf__CaMKII_CaM_Ca1__Ca,kf__CaMKII_CaM__Ca,kf__CaM_Ca1__CaMKII,kf__CaM_Ca2__CaMKII,kf__CaM_Ca3__CaMKII,kf__CaM_Ca4__CaMKII,KD__CaM_Ca4__CaMKII,KD__CaMKII_CaM_Ca3__Ca,KD__CaMKII_CaM_Ca2__Ca,KD__CaMKII_CaM_Ca1__Ca,KD__CaMKII_CaM__Ca,kf__pCaMKII_Ca3__Ca,kf__CaM__pCaMKIIaut,kf__CaM_Ca1__pCaMKIIaut,kf__CaM_Ca2__pCaMKIIaut,kf__CaM_Ca3__pCaMKIIaut,kf__pCaMKII_Ca2__Ca,kf__pCaMKII_Ca1__Ca,kf__CaM_Ca4__pCaMKIIaut,kf__pCaMKII_Ca0__Ca,KD__pCaMKII_Ca3__Ca,KD__pCaMKII_Ca2__Ca,KD__pCaMKII_Ca1__Ca,KD__pCaMKII_Ca0__Ca,KD__CaM_Ca4__pCaMKIIaut,kp__pairedCaMKIIc__CaMKIIc,kf__PP1__pCaMKIIaut,kr__PP1__pCaMKIIaut,kcat__PP1__pCaMKIIaut,Ca_set,PP1_0,CaMKII_0,CaM_0,PP2B_0]   # Assume the parameters have been set elsewhere
t = [i/10.0 for i in range(0,101)]
ic = [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
sol = odeint(CaMKIIs.vectorfield,ic,t,args=(params,),Dfun=CaMKIIs.jacobian)

"""
tablibObj = SBtabTable_obj.createDataset()
sbtabs = SBtabTools.oneOrMany(tablibObj)
print sbtabs

# print tablibObj.headers
# print tablibObj[1]
print SBtabTable_obj


#>> # Creates SBtab Python object from tablib object
#>> SBtT = SBtab.SBtabTable(tablibObj, 'SBtab_CaMKII_Measurements.xls')

# Creates a tablib object of the SBtab Python object
tablibObj = SBtabTable_obj.createDataset()

# Checks for multiple tables in a tablib object and cuts them into separate tablib objects
sbtabs = SBtabTools.oneOrMany(tablibObj)


print tablibObj

with open('SBtab_CaMKII_Measurements.csv','r') as sbtab_file:
    file_content = sbtab_file.read()



params = [kf__CaM__Ca,kf__CaM_Ca1__Ca,kf__CaM_Ca2__Ca,kf__CaM_Ca3__Ca,kf__CaM__PP2B,kf__CaM_Ca1__PP2B,kf__CaM_Ca2__PP2B,kf__CaM_Ca3__PP2B,kf__CaM_Ca4__PP2B,kf__PP2B_CaM__Ca,kf__PP2B_CaM_Ca1__Ca,kf__PP2B_CaM_Ca2__Ca,kf__PP2B_CaM_Ca3__Ca,KD__CaM_Ca3__Ca,KD__CaM_Ca2__Ca,KD__CaM_Ca1__Ca,KD__CaM__Ca,KD__CaM_Ca4__PP2B,KD__PP2B_CaM_Ca3__Ca,KD__PP2B_CaM_Ca2__Ca,KD__PP2B_CaM_Ca1__Ca,KD__PP2B_CaM__Ca,kf__CaM__CaMKII,kf__CaMKII_CaM_Ca3__Ca,kf__CaMKII_CaM_Ca2__Ca,kf__CaMKII_CaM_Ca1__Ca,kf__CaMKII_CaM__Ca,kf__CaM_Ca1__CaMKII,kf__CaM_Ca2__CaMKII,kf__CaM_Ca3__CaMKII,kf__CaM_Ca4__CaMKII,KD__CaM_Ca4__CaMKII,KD__CaMKII_CaM_Ca3__Ca,KD__CaMKII_CaM_Ca2__Ca,KD__CaMKII_CaM_Ca1__Ca,KD__CaMKII_CaM__Ca,kf__pCaMKII_Ca3__Ca,kf__CaM__pCaMKIIaut,kf__CaM_Ca1__pCaMKIIaut,kf__CaM_Ca2__pCaMKIIaut,kf__CaM_Ca3__pCaMKIIaut,kf__pCaMKII_Ca2__Ca,kf__pCaMKII_Ca1__Ca,kf__CaM_Ca4__pCaMKIIaut,kf__pCaMKII_Ca0__Ca,KD__pCaMKII_Ca3__Ca,KD__pCaMKII_Ca2__Ca,KD__pCaMKII_Ca1__Ca,KD__pCaMKII_Ca0__Ca,KD__CaM_Ca4__pCaMKIIaut,kp__pairedCaMKIIc__CaMKIIc,kf__PP1__pCaMKIIaut,kr__PP1__pCaMKIIaut,kcat__PP1__pCaMKIIaut,Ca_set,PP1_0,CaMKII_0,CaM_0,PP2B_0]   # Assume the parameters have been set elsewhere
t = [i/10.0 for i in range(0,101)]
ic = [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
sol = odeint(CaMKIIs.vectorfield,ic,t,args=(params,),Dfun=CaMKIIs.jacobian)
"""
