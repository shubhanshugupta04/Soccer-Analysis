import numpy as np
import pandas as pd 
import re
import matplotlib.pyplot as plt
import seaborn as sns
import math

# converting Height to cm
def change_to_cm(ht):
    
    """
    Converting height from inches to cm
    
    Parameter:
    ht : Height of the players in inches
    
    Return:
    returns height in cm
    
    """
    height = ht.split(r"'")
    feet = float(height[0])
    inches = float(height[1].replace("\"",""))
    total_ht = 12*feet + inches
    return round(total_ht * 2.54, 1)

# Filling contract end date
def contract_end_date(start_date,end_date):
    """
    Filling player contract end date where it is missing. Using startdate to fill the enddate as these are players who don't have a contract     with any club
    
    Parameter:
    startDate : Start date of contract
    endDate: End date of contract
    
    Return:
    returns the enddate
    
    """  
    if end_date == None:
        return start_date
    else:
        return end_date
    
# Checking if player is on loan    
def check_loan(end_date):
    """
    Check the enddate of a loan for a player
    
    Parameter:
    endDate: End date of contract on loan
    
    Return:
    returns the enddate
    
    """
    if 'On Loan' in end_date:
        return end_date[7:12].strip()
    else:
        return end_date
    
    
# Calculating remaining contract years
def contract_remaining(end_date,current_date):
    """
    Number of years remaining in player's contract
    
    Parameter:
    endDate: End date of contract on loan
    
    Return:
    returns the enddate
    
    """
    remain = int(end_date) - int(current_date)
    if int(end_date) == 0 or remain <= 0 :
        return 0
    else:
        return remain
    
# Cleaning Value,Wage, Release Clause Columns
def player_value(val):
    if 'K' in val:
        int_val = re.sub(r'\D',r'',val)
        return int(int_val) * 1000
    elif 'M' in val:
        int_val = re.sub(r'\D',r'',val)
        return int(int_val) * 1000000
    else:
        int_val = re.sub(r'\D',r'',val)
        return int(int_val)
    
    
# plotting boxplots for some features to gain insight about relationship with different player categories
def generateBoxplots(df,dataset,cols=3, width=20, height=12, hspace=0.8, wspace=0.5):
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure(figsize=(width,height))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=wspace, hspace=hspace)
    rows = math.ceil(len(dataset) / cols)
    for i,feature in enumerate(dataset):
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.set_title(feature)
        g = sns.boxplot(x=df["Category"], y=df[feature])
        plt.xticks(rotation=25)

    
    
 


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    