import pyreadr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import string
import datetime 

import seaborn  as sns

class descriptivestat1: 
    def __init__(self, inputdf): 
        self.df = inputdf 
        # to take out the unique codes
        self.kod = inputdf['code'].unique().tolist() 
        # to collect all unique components 
        self.components = inputdf['component'].unique().tolist()  
        # to create an empty diction for data collection
        # to store the users divided by the component usage
        self.collectdict1 = {} 
        # to store the results by users 
        self.collectdict2 = {} 
        
    def dictionary_packing(self): 
        # to fetch the object data frame 
        newdf = self.df[['code', 'component', 'stamps']] 
        
        # to divide the code into eight groups 
        L =  newdf.shape[0] 
        newdict = {} 
        for i in range(L): 
            [tempcode, tempcomp, temptime] = newdf.iloc[i, :] 
            if tempcode in newdict: 
                tempdict =  newdict[tempcode] 
                if tempcomp in tempdict:
                    templist = tempdict[tempcomp]
                    templist= templist + temptime
                    tempdict[tempcomp] = templist
                else: 
                    tempdict[tempcomp] = temptime
                newdict[tempcode] = tempdict
            else: 
                # to store the results in a dictionary 
                tempdict = { } 
                tempdict[tempcomp] = temptime
                newdict[tempcode] = tempdict
                
        return newdict  
        
        
        
        
        class descriptivestat_time:   
    def __init__(self, inputdf): 
        self.df = inputdf 
        # to look at the loged time stamps
        self.timestamps = inputdf['stamps'].tolist() 
        
    def timestamp_sort(self): 
        # in this function, the time stamps are sorted into seven week days
        tempstams = self.timestamps 
            
        new_time_list = []  
        
        for tid in tempstams:
            string1 = list(tid.split(", "))
            string.punctuation2='!"#$%&\'()*+,./;<=>?@[\\]^_`{|}~'
            timestring = [item.translate(str.maketrans('', '', string.punctuation2))  for item in string1] 
            new_time_list += timestring 
            
        self.timestorage= new_time_list
        
    def weekday_survey(self): 
        # to call the function, constructed previously
        self.timestamp_sort( )
        weekday_dict = { }
        
        # to store the data into a dictionary 
        timedatan = self.timestorage 
        weekdays = [ ]
        timelogs = [ ] 
        monthlist = [ ]
        
        for elem in timedatan: 
            temp = pd.Timestamp(elem) 
            
            # to check which days the users like to use the app
            weekdays.append(temp.day_name()  )
            monthlist.append(temp.month )
            
            # to check what time of the day the users like to use the app 
            timelogs.append(temp.time().hour  )
            
        for days in weekdays: 
            
            if days not in weekday_dict:
                weekday_dict[days] = 1
            else: 
                weekday_dict[days] +=1
            
            
        return weekdays,  timelogs, weekday_dict, monthlist
    def plot_dist1(self): 
        weekdays,  timelogs, weekday_dict = self.weekday_survey( ) 
        
        weekday_dict = {}
        
        weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

        values = []

        for day in weekday_list: 
            values.append(weekday_dict[day]) 
        weekday_data ={'Weekdays': weekday_list, 'Counts': values} 
        plt.figure(figsize=(15, 10))
        sns.barplot(x="Weekdays", y="Counts", data=weekday_data, palette="Blues_d" )
        plt.grid(True)
        
