# world_data.py
# AUTHOR NAME: Chandrahas Reddy Pola
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 5 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library, including numpy and pandas.
# Remember to include docstrings and comments.

#importing pandas, numpy and chain(from itertools)
import pandas as pd
import numpy as np
from itertools import chain
print('ENSF 592 World Data')
#reading the excel file and assigned to world_data variable
world_data = pd.read_excel(r"Assign5Data.xlsx", sheet_name='world_data')
#adding new column with name delta population and it gives difference between year 2020 and 2000 population
world_data["Delta Population"]=(world_data["2020 Pop"]-world_data["2000 Pop"])
#adding new column with name density and it gives the results of the 2020 year density 
world_data["Density"]=(world_data["2020 Pop"]/world_data["Sq Km"])
#assigned a UN Sub-Region column to variable named sub_regions
sub_regions = world_data["UN Sub-Region"]
#converting sub_regions dataframe to list
sub_regions_list=list(sub_regions)
#assigned a UN Region column to variable named UN_Region
UN_Region = world_data['UN Region']
#converting UN_Region dataframe to list
UN_Sub_Region = world_data['UN Sub-Region']
# columns made as catogerised with columns UN Region, UN Sub-Region, Country
world_data_categorised=world_data.set_index(['UN Region','UN Sub-Region','Country'])
#assigned IndexSlice to idx variable
idx=pd.IndexSlice
'''
Created main functiom.
It checks whether region is valid or not, if it's not valid prompt the user to type the valid UN Sub-Region name
In try we check whether the UN-Region is valid else it throws error and ask the user to give valid UN Sub-Region
It doesn't take no argumnets 
no return values
'''
def main():
    def valid_region():
        while(True):
            x = input("Please enter a sub-region: ")
            '''
            Created a find_null function.
            find_null function results if there're any Nan values in square km values, if yes it prints the UN Region, UN Sub-Region and country with Nan Sq values
            It doesn't take any arguements
            No return value
            '''
            def find_null():
                y= world_data.where(world_data['UN Sub-Region']==x).dropna(how='all')
                if(y['Sq Km'].isnull().values.any()):
                    print("Sq Km are missing for: ")
                    print(y.where(y['Sq Km'].isnull()).dropna(how ='all').loc[:,['UN Region','UN Sub-Region','Country','Sq Km']])
                    
                

            try:
                if x in sub_regions_list:
                    find_null()
                    # It gives the UN Region name by using UN Sub-Region
                    region = world_data.where(world_data['UN Sub-Region']==x).dropna(how='all').reset_index()['UN Region'][0]
                    #prints the change in population and lastest density data
                    print("Calculating change in population and latest density...\n",world_data_categorised.loc[idx[[region],[x],:],:'Density'])
                    #assigned the UN Sub-Region values to variable y
                    y=world_data.where(world_data["UN Sub-Region"]==x)
                    #prints the number of threatned species in each country
                    print("Number of threatened species in each country of the sub-region:\n",world_data_categorised.loc[idx[[region],[x],:],'Plants (T)':'Mammals (T)'])
                    z=pd.DataFrame(y['Sq Km']/y.loc[:,['Plants (T)','Fish (T)','Birds (T)','Mammals (T)']].sum(axis=1))
                    world_data_categorised[' ']=list(chain.from_iterable(z.values.tolist()))#It converts dataframe to list and created a new column ' '
                    print("The calculated sq km area per number of threatned species in each country is: \n",world_data_categorised.loc[idx[[region],[x],:],' '])
                    break
                else:
                    raise ValueError("You must enter a valid UN-Sub region name. ")
            except ValueError:
                print("You must enter a valid UN-Sub region name. ")
    valid_region()


                    


                   

   
if __name__ == '__main__':
    main()

