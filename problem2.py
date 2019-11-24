import pandas as pd

data = {'Box':['Box 1','Box 1','Box 1','Box 2','Box 2','Box 2'],
        'Dimension':['Length','Width','Height','Length','Width','Height'],
        'Value':[6,4,2,5,3,4]}
box = pd.DataFrame(data,columns=['Box','Dimension','Value'])

boxl = box.pivot(index='Box',columns='Dimension',values='Value')

volbox1 = boxl.iat[0,0]*boxl.iat[0,1]*boxl.iat[0,2]
volbox2 = boxl.iat[1,0]*boxl.iat[1,2]*boxl.iat[1,2]
