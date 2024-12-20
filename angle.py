import pandas as pd
import numpy as np
import math
import os

df = pd.read_csv('/AdV2024_report/Book1.csv')

a = 10
b = 11

l = []
lc = np.array(l)

bbox = 360 * ((1169 + (192/2)) / 5376)
print(bbox)

while(b < 70):
    df_center = df[a:b]

    p = df.iat[a,1]
    q = df.iat[b,1]
    
    p = float(p)
    q = float(q)

    #print(p)
    ang = math.degrees(math.atan2(float(p), float(q)))

    if ang < 0 :
        nang = ang + 270
    elif ang > 0 :
        nang = ang - 90
    else:
        nang = 0
    

    lc = np.append(lc, nang)

    print(nang) 
    #print(df_center)
    #print(df_center.loc["Column2"])
    a += 11
    b += 11

print(lc)

srt = np.abs(lc - bbox).argsort()[0].tolist() + 1

print("obstacle_number: ", srt)
