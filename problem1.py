import pandas as pd

mathdata = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
math = pd.DataFrame(mathdata,columns = ['Student','Math'])

elecdata = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
elec = pd.DataFrame(elecdata,columns = ['Student','Electronics'])

geasdata = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
geas = pd.DataFrame(geasdata,columns = ['Student','GEAS'])

esatdata = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
esat = pd.DataFrame(esatdata,columns = ['Student','ESAT'])

mathelec = pd.merge(math,elec,on='Student')
mathelecgeas = pd.merge(mathelec,geas,on='Student')
ece = pd.merge(mathelecgeas,esat,on='Student')

ece_long = pd.melt(ece, id_vars=['Student'],var_name='Subject', value_name='Grades')

print(ece,'\n')
print(ece_long)
