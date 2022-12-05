#!/usr/bin/env python3
'''
    -   This script was developed to convert any xlsx to csv file using pandas module.
    -   You can change the file name to your file name both (.xlsx) and (.csv).
    
'''
import pandas as pd 
import os

# get the current directory path
dir_name = os.path.dirname(os.path.abspath(__file__)) 
var_name = os.path.dirname(os.path.abspath(__file__)) +'\\'+'Student_data.xlsx'
read_file = pd.read_excel(var_name)
read_file.to_csv (os.path.dirname(os.path.abspath(__file__)) +'\\'+'Student_data.csv', index = None, header=True)

