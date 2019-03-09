import math
#interests=[492308]
#interests=[1607692]
interests=[9211,9211,8617,9211,8880,9163,8867,9119,9066,8773,9066,8773,26444,26444,26444,26444,26444,26444,26444,26444,26444,26444,26444,26444,26444,11800,5894,2000,6302,6527,6527,6527,6302,6677,6677,6677,6752]
totalpaidInt=0
count=0
for interest in interests:
    #totalpaidInt=totalpaidInt+interest
    count+=1
    if(37-count>0):
        #print(36-count)
        #multiplier=math.pow(1.015, 37-count)
        multiplier=math.pow(1.005833, 37-count)
        #print(multiplier)
        accumulatedInt=multiplier*interest-interest
        #print('total interest for '+str(37-count)+" month:::")
        print(str(round(accumulatedInt,3)))
        #+" for amount:: "+str(interest))
        totalpaidInt=totalpaidInt+accumulatedInt

print(totalpaidInt)
