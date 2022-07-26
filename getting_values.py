#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:41:31 2022

@author: adeenakhan
"""

# Go through each of the columns, take in it

import pandas as pd 
import numpy as np 
import math

#format of this will be a rat: x coordinate data index
dictionary_of_index = {}
#this holds total distance and velocity
rats_distance={}

video_name=input("What is the file name of the csv file you want to input? Ex: Video17.csv ")
#need to open csv file and look at only the columns that mention the ears 
all_data=pd.read_csv(video_name)

title_names= list(all_data.iloc[1])


#this is an easy way of getting the coordinate values for multiple rats
#all this is doing is saying that in this column you can find rat #_ ears
#does it for every rat
count=0
#for amount in the top of tables
for i in range(0,len(title_names)):
    if "rightear" in title_names[i] and i-1 not in dictionary_of_index.values() and i-2 not in dictionary_of_index.values():
        count+=1
        current_name="rat "+ str(count)
        dictionary_of_index[current_name]= i
        rats_distance[current_name]=None





#60 frames in a second (if nan for  30 frames or more then we do distance formula )

#how many seconds for velocity?
#so bin it 
#20 seconds 
#60.06 fps tech but using 60 frames

#20 seconds is therefore --> 1200 frames


pixels_to_inches=float(input("How many pixels are in an inch (according to ImageJ)? Ex: 22.75 "))
frame=int(input("What second do you want to start the analysis at? Ex: 25 "))

#add 3 because the first index of the csv spreadhsheets
#say the rat number, the body part, and then either x/y/likelihood
#multiply by 60 because 60 frames per second
frame=frame*60+3



#finds specific column for right ear of each rat
#gets x and y column
for r in dictionary_of_index:
    
    total_distance=0
    value=dictionary_of_index[r]

    x_column= all_data.iloc[:,value]
    y_column =all_data.iloc[:,value+1]

    


    #checks how many na/no data has passed
    nan_counter=0
    last_recorded=(0,0)
    frames_passed=0
    
    #first distance value for velocity, will be updated in code almost immediately
    
    reference_point=0
    
    
    reference=(math.inf,math.inf)
    
    #taken at 20 second intervals
    velocity_values=[]
    #starts when all rats have entered
    for data in range(frame,len(all_data)):
        
        current_x_value=float(x_column[data])
        current_y_value=float(y_column[data])
        
        #last x and y value
        old_x_value=float(x_column[data-1])
        old_y_value=float(y_column[data-1])
         
        #checks to see if 30 frames have been skipped in a row
        if nan_counter>=30 and not (pd.isna(current_x_value)) and not (pd.isna(current_y_value)):
            nan_counter=0
            distance= (math.sqrt((current_x_value-last_recorded[0])**2+(current_y_value-last_recorded[1])**2))/pixels_to_inches
            total_distance+=distance
        elif pd.isna(current_x_value) or pd.isna(current_y_value) or pd.isna(old_x_value) or pd.isna(old_y_value):
            nan_counter+=1
            continue
        elif abs(old_x_value-current_x_value)>10 or abs(old_y_value-current_y_value)>10:
            continue
        else:
            #keeps track of the last value that is not nan
            last_recorded=(current_x_value,current_y_value)
            
            if reference==(math.inf,math.inf):
                reference=last_recorded
                
            #resets nan counter because we have not skipped
            nan_counter=0
            #distance formula w/ conversion from pixels to inches!
            distance= (math.sqrt((current_x_value-old_x_value)**2+(current_y_value-old_y_value)**2))/pixels_to_inches
            total_distance+=distance
        
        #if 20 seconds have passed. THIS IS ASSUMING A 60 FRAME VIDEO
        frames_passed+=1
        if frames_passed>=1200:
            frames_passed=0
            
            #NOTE: THESE TWO COMMENTED OUT LINES ARE IF YOU WANT SPEED CALC, NOT VELOCITY
            #speed=(total_distance-reference_point)/20 #this is pixels/second (speed calc)
            #reference_point=total_distance

            velocity=(math.sqrt((last_recorded[0]-reference[0])**2+(last_recorded[1]-reference[1])**2)/pixels_to_inches)/20
            reference=(last_recorded[0],last_recorded[1])
            velocity_values.append(velocity)
            
    rats_distance[r]=[f"Total Distance: {total_distance} inches",f"Velocity: {velocity_values}"]

print("")
print(rats_distance)


interactions={}

#now need to see how long and which rats are in contact with each other
#possible combinations: rat1+rat2, rat1+3, rat2+rat3 for ex
#do I want to see when they're interaction potentially?

#first two for loops allow every possible combo of rats to occur

#first rat being interacted with
for i in range(1,len(dictionary_of_index)+1):
    value=dictionary_of_index["rat "+str(i)]
    first_column_x= all_data.iloc[:,value]
    first_column_y =all_data.iloc[:,value+1]
    distance=0
   
    #second rat being interacted with
    for l in range(i+1,count+1):
        friend_score=0
        last_next=False
        value2=dictionary_of_index["rat "+str(l)]
        second_column_x= all_data.iloc[:,value2]
        second_column_y =all_data.iloc[:,value2+1]
        
        #looking at every frame after first rat goes in
        for data in range(frame,len(all_data)):
            first_rat_x=float(first_column_x[data])
            first_rat_y=float(first_column_y[data])
            
            second_rat_x= float(second_column_x[data])
            second_rat_y =float(second_column_y[data])
            
            #if we have both x and y coordinates for both rats
            if (not pd.isna(first_rat_x)) and (not pd.isna(first_rat_y)) and (not pd.isna(second_rat_x)) and (not pd.isna(second_rat_y)):
                distance= (math.sqrt(((first_rat_x-second_rat_x)/pixels_to_inches)**2+((first_rat_y-second_rat_y)/pixels_to_inches)**2))
              #if distance less than 5 inches
                if distance<=5:
                    friend_score+=1
                    last_next=True
                #otherwise they're not next to each other
                else:
                    last_next=False
            elif last_next:
                #assuming still next to each other, just out of frame
                friend_score+=1
                
        interactions["rat "+str(i)+" and rat "+str(l)+ " Interactions (Total seconds)"]= friend_score/60
print("-------------")
print(interactions)

            
                  


#CONVERSION: 22.75 pixels/inch (according to ImageJ)




    

