import pandas as pd

scores = {"Zone": ["North","North","South","South","East","East","West","West"],
         "School": ["Rushmore","Rushmore","Bayside","Rydell","Shermer","Shermer","Ridgemont","Hogwarts"],
         "Name": ["Jonny","Mary","Joe","Jakob","Jimmy","Erik","Lam","Yip"],
         "Math": [78,39,76,56,67,89,100,55],
         "Science": [70,45,68,90,45,66,89,32]}

df = pd.DataFrame(scores,columns =
                 ["Zone","School","Name",
                 "Science","Math"])

print (df)

df = pd.DataFrame (
    {
        "Gender":["Male","Male","Female","Female","Female"],
        "Team": [1,2,3,3,1]
    })

print (df)

import numpy as np
schools = np.array (["Cambridge","Oxford","Oxford","Cambridge","Oxford"])
df["School"] = schools
print (df)
