import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import *
from string import ascii_lowercase

mycolumns = ["class","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13"]
df = pd.DataFrame(columns=mycolumns)

# index for dataframe
p=0
for c in ascii_lowercase:
    for k in range (20):
        row_data=[]
        path="/Users/zy/Desktop/Course/CSCE624_Sketch/HW1/Data/letters-txt/"+c+"/"+c+"_"+str(k+1)+".txt"
        sample = pd.read_csv(path,sep=',|;', engine='python',names=['x','y','time'], header=None,index_col=False)
        x0=sample['x']
        y0=sample['y']
        t0=sample['time']
        
        # total number of original points
        n_old=len(sample)
        
        # clean data, delete point without movement and movement without time change
        delete=[]
        try:
            for i in range(n_old):
                if (x0[i]==x0[i+1]) and (y0[i]==y0[i+1]):
                    delete.append(i+1)
                if (t0[i] == t0[i+1]) and ((x0[i]!=x0[i+1]) or (y0[i]!=y0[i+1])):
                    delete.append(i+1)
        except KeyError:
            pass
        
        sample_new=sample.drop(sample.index[[delete]])
        sample_new=sample_new.reset_index(drop=True)
        # total number of points after cleaning
        n=len(sample_new)
        
        # new points information
        x=sample_new['x']
        y=sample_new['y']
        t=sample_new['time']
        
        
        # max,min of x,y,t
        x_max=max(x)
        x_min=min(x)
        y_max=max(y)
        y_min=min(y)
        t_max=max(t)
        t_min=min(t)
        
        # get the difference array of x and y
        try:
            d_x=[]
            d_y=[]
            d_t=[]
            for i in range(n-1):
                d_x.append(x[i+1]-x[i])
                d_y.append(y[i+1]-y[i])
                d_t.append(t[i+1]-t[i])
        except KeyError:
            pass
        
        # feature 1: The cosine of the starting angle pof the stroke.
        f1= (x[3]-x[0])/sqrt((y[3]-y[0])**2+(x[3]-x[0])**2)
        
        # feature 2: The sine of the starting angle pof the stroke.
        f2= (y[3]-y[0])/sqrt((y[3]-y[0])**2+(x[3]-x[0])**2)
        
        # feature 3: the length of the diagqonal of the bounding box of the stroke
        f3=sqrt((y_max-y_min)**2+(x_max-x_min)**2)
        
        # feature 4: the angle of the diagonal
        f4=atan((y_max-y_min)/(x_max-x_min))
        
        # feature 5: Start and endpoint distance
        f5=sqrt((x[n-1]-x[0])**2+(y[n-1]-y[0])**2)
        
        # feature 6: Angle from the start to endpoint (cos)
        f6=(x[n-1]-x[0])/f5
        
        # feature 7: Angle from the start to endpoint (sin)
        f7=(y[n-1]-y[0])/f5
        
        # feature 8: Stroke Length
        f8=0
        for i in range(n-2):
            length= sqrt(d_x[i]**2+d_y[i]**2)
            f8 = length + f8
        
        # feature 9: the total rotational change in a stroke
        f9=0
        for i in range(n-2):  
                theta= atan((d_x[i+1]*d_y[i]-d_x[i]*d_y[i+1])/(d_x[i+1]*d_x[i]+d_y[i]*d_y[i+1]))
                f9 = theta + f9
        
        # feature 10: the total absolute rotational change
        f10=0
        for i in range(n-2):
                theta= atan((d_x[i+1]*d_y[i]-d_x[i]*d_y[i+1])/(d_x[i+1]*d_x[i]+d_y[i]*d_y[i+1]))
                f10 = abs(theta) + f10  
        
        # feature 11: the smoothness of the stroke
        f11=0
        for i in range(n-2):
                theta= atan((d_x[i+1]*d_y[i]-d_x[i]*d_y[i+1])/(d_x[i+1]*d_x[i]+d_y[i]*d_y[i+1]))
                f11 = theta**2 + f11  
        
        # feature 12: the squared value of the maximum speed reached
        f12=0
        for i in range(n-1):
            speed=(d_x[i]**2+d_y[i]**2)/d_t[i]**2
            if speed > f12:
                f12= speed
        
        # feature 13: the total time to draw a stroke from start to finish
        f13=t[n-1]-t[0]
        
        # generate a row information
        print c,p
        row_data.extend([c,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13])
        
        # generate csv file
        df.loc[p]=row_data
        p+=1

df.to_csv("/Users/zy/Desktop/Course/CSCE624_Sketch/HW1/Data/letters-txt/letters.csv",index=False)