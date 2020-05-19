import random, hou

#init
ramp_node = hou.selectedNodes()[0]
ptspos = []
ptsvalue = []
ramp_name = "rampparm"
numpts = 10
type = hou.rampBasis.Constant
rand_min = .1
rand_max = .5

#evenly split range and add rand values
for i in range(numpts+1):
    currentpos = i*1.0 / numpts
    ptspos.append(currentpos)
    currentvalue = random.uniform(rand_min,rand_max)
    ptsvalue.append(currentvalue)

#convert list to tuples for hou.Ramp
ptspos = tuple(ptspos)
ptsvalue = tuple(ptsvalue)

#apply random values
newramp = hou.Ramp((type,type),ptspos,ptsvalue)
ramp_node.setParms({ramp_name: newramp})