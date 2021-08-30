# school_data.py
# AUTHOR NAME: Chandrahas_Reddy_Pola
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
#importing pandas, numpy and statictics(to find mean and median for lists)
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import statistics  
school_data = pd.read_csv("/Users/apple/Desktop/Spring-2021/ensf592-assignments/assignment-4-school-data-chandu-55/Assignment4Data.csv")
'''
Created  main function to get the School data base enrollments
It shows the shape and dimensions of the array
Created a function called valid_school() to check the school name and school code
Prompts the user to give input as school code and school name
It shows the school name and school code and mean enrollments of grades
It shows the total enrollments as per year
If there is any enrollments more than 500, it takes the median value
It shows the General statistics as well
'''
def main():
    print("ENSF 592 School Enrollment Statistics")
    # Print Stage 1 requirements here
    #school_data dataframe is converted into array assigned to arr variable
    arr = np.array(school_data)
    #By using reshape function of numpy we reshaped the school_data array into three dimensional
    new_array = np.asarray(arr).reshape(16,10,10)
    print("Shape of the full data array",new_array.shape)
    #Prints the number of dimensions in the array
    print("Dimensions of the full data array",new_array.ndim)

    # Prompt for user input

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    #drop_duplicates drop the duplicates from School Code column in school_data data frame
    School_code = school_data["School Code"].drop_duplicates()
    #School Name column in school_data data frame is assigned to School_name variable
    School_name = school_data["School Name"]
    #drop_duplicates drop the duplicates from School name column in school_data data frame
    School_name = School_name.drop_duplicates()
    #Created a array of school names in the school_list variable
    school_list=np.array([School_name])
     #Created a array of school codes in the school_code variable
    school_code = np.array([School_code])
    #Created a dictionary to assign respective school names to school codes
    #Uses zip functions for assigning.
    d = {}
    for A, B in zip(school_list.flatten(), school_code.flatten()):#used flatten to convert 2d array to 1d array
        d[A] = B
    #Grouped School Name and Grade 10 columns and calculated the mean value in the school_data data frame and assigned it to grade_10_mean variable
    grade_10_mean=school_data.groupby('School Name',as_index=False, sort=False)["Grade 10"].mean()
    #Created array of grade_10_mean of Grade 10 columns and assigned it to grade_10_mean_values
    grade_10_mean_values = np.array(grade_10_mean["Grade 10"])
    #Created a dictionary to assign respective school names to grade 10 mean values
    #Uses zip functions for assigning.
    grade_10 ={}
    for A, B in zip(school_list.flatten(), grade_10_mean_values):#used flatten to convert 2d array to 1d array
        grade_10[A] = B 
    #Grouped School Name and Grade 11 columns and calculated the mean value in the school_data data frame and assigned it to grade_11_mean variable
    grade_11_mean = school_data.groupby('School Name',as_index=False,sort=False)["Grade 11"].mean()
    #Created array of grade_11_mean of Grade 10 columns and assigned it to grade_11_mean_values
    grade_11_mean_values = np.array(grade_11_mean["Grade 11"]) 
    #Created a dictionary to assign respective school names to grade 11 mean values
    #Uses zip functions for assigning.
    grade_11 ={}
    for A, B in zip(school_list.flatten(), grade_11_mean_values):#used flatten to convert 2d array to 1d array
        grade_11[A] = B
    #Grouped School Name and Grade 12 columns and calculated the mean value in the school_data data frame and assigned it to grade_12_mean variable
    grade_12_mean = school_data.groupby('School Name',as_index=False,sort=False)["Grade 12"].mean()
    #Created array of grade_12_mean of Grade 12 columns and assigned it to grade_12_mean_values
    grade_12_mean_values = np.array(grade_12_mean["Grade 12"])
    #Created a dictionary to assign respective school names to grade 12 mean values
    #Uses zip functions for assigning.
    grade_12 ={}
    for A, B in zip(school_list.flatten(), grade_12_mean_values):#used flatten to convert 2d array to 1d array
        grade_12[A] = B
    #Grouped School Name and Grade 10 columns and calculated the max value in the school_data data frame and assigned it to grade_10_max variable
    grade_10_max=school_data.groupby('School Name',as_index=False, sort=False)["Grade 10"].max()
    #Created array of grade_10_max of Grade 10 columns and assigned it to grade_10_max_values
    grade_10_max_values = np.array(grade_10_max["Grade 10"])
    #Created a dictionary to assign respective school names to grade 10 max values
    #Uses zip functions for assigning.
    grade_10_max ={}
    for A, B in zip(school_list.flatten(), grade_10_max_values):#used flatten to convert 2d array to 1d array
        grade_10_max[A] = B
    #Grouped School Name and Grade 11 columns and calculated the max value in the school_data data frame and assigned it to grade_11_max variable
    grade_11_max=school_data.groupby('School Name',as_index=False, sort=False)["Grade 11"].max()
    #Created array of grade_11_max of Grade 11 columns and assigned it to grade_11_max_values
    grade_11_max_values = np.array(grade_11_max["Grade 11"])
    #Created a dictionary to assign respective school names to grade 11 max values
    #Uses zip functions for assigning.
    grade_11_max ={}
    for A, B in zip(school_list.flatten(), grade_11_max_values):#used flatten to convert 2d array to 1d array
        grade_11_max[A] = B
    #Grouped School Name and Grade 12 columns and calculated the max value in the school_data data frame and assigned it to grade_12_max variable
    grade_12_max=school_data.groupby('School Name',as_index=False, sort=False)["Grade 12"].max()
    #Created array of grade_12_max of Grade 12 columns and assigned it to grade_112_max_values
    grade_12_max_values = np.array(grade_12_max["Grade 12"])
    #Created a dictionary to assign respective school names to grade 12 max values
    #Uses zip functions for assigning.
    grade_12_max ={}
    for A, B in zip(school_list.flatten(), grade_12_max_values):#used flatten to convert 2d array to 1d array
        grade_12_max[A] = B
    #Grouped School Name and Grade 10 columns and calculated the min value in the school_data data frame and assigned it to grade_10_min variable
    grade_10_min=school_data.groupby('School Name',as_index=False, sort=False)["Grade 10"].min()
    #Created array of grade_10_min of Grade 10 columns and assigned it to grade_10_min_values
    grade_10_min_values = np.array(grade_10_min["Grade 10"])
    #Created a dictionary to assign respective school names to grade 10 min values
    #Uses zip functions for assigning.
    grade_10_min ={}
    for A, B in zip(school_list.flatten(), grade_10_min_values):#used flatten to convert 2d array to 1d array
        grade_10_min[A] = B
    #Grouped School Name and Grade 11 columns and calculated the min value in the school_data data frame and assigned it to grade_10_min variable
    grade_11_min=school_data.groupby('School Name',as_index=False, sort=False)["Grade 11"].min()
    #Created array of grade_11_min of Grade 11 columns and assigned it to grade_11_min_values
    grade_11_min_values = np.array(grade_11_min["Grade 11"])
    #Created a dictionary to assign respective school names to grade 11 min values
    #Uses zip functions for assigning.
    grade_11_min ={}
    for A, B in zip(school_list.flatten(), grade_11_min_values):#used flatten to convert 2d array to 1d array
        grade_11_min[A] = B
    #Grouped School Name and Grade 12 columns and calculated the min value in the school_data data frame and assigned it to grade_12_min variable
    grade_12_min=school_data.groupby('School Name',as_index=False, sort=False)["Grade 12"].min()
    #Created array of grade_12_min of Grade 12 columns and assigned it to grade_12_min_values
    grade_12_min_values = np.array(grade_12_min["Grade 12"])
    #Created a dictionary to assign respective school names to grade 12 min values
    #Uses zip functions for assigning.
    grade_12_min ={}
    for A, B in zip(school_list.flatten(), grade_12_min_values):#used flatten to convert 2d array to 1d array
        grade_12_min[A] = B
    #Grouped School Name and School Year and assigned to school_year variable
    school_year = school_data.groupby('School Name',as_index=False, sort=False)["School Year"]
    #Created function named valid_school
    #It check whether school name and school code exists or not. If doesn't exists it prompts to give input by user.
    #Above defined dictionaries are used here to get the values of the respectives key(school name)
    #It also shows the each year enrollments
    #If any enrollment is greater than 500 it gives the median value, else it shows No enrollments over 500
    def valid_school():
        while True:
            print("Enter the school name and school code as it looks in database")
            x = (input("Please enter your school name or school code: "))
            try:
                if (x in school_list) or (x in map(str,school_code.flatten())):
                    key_list = list(d.keys())
                    val_list = list(d.values())
                    if (len(x)==4):
                        x = key_list[val_list.index(int(x))]
               
                        
                    print("School Name is: ", x)
                    print("School Code is: ", d.get(x))
                    print("Mean enrollment for Grade 10 across all years",grade_10.get(x))
                    print("Mean enrollment for Grade 11 across all years",grade_11.get(x))
                    print("Mean enrollment for Grade 12 across all years",grade_12.get(x))
                    print("Highest enrollment for a single grade within the entire time period",max(grade_10_max.get(x),grade_11_max.get(x),grade_12_max.get(x)))
                    print("Lowest enrollment for a single grade within the entire time period",min(grade_10_min.get(x),grade_11_min.get(x),grade_12_min.get(x)))
                    mask1 = school_data['School Name']==x
                    for i in range(0,8):
                        mask2=school_data['School Year']==i+2013
                        df = school_data.loc[mask1].loc[mask2]
                        print("Total enrollment for each year from {0} is {1}".format(i+2013,int(df["Grade 10"]+df["Grade 11"]+df["Grade 12"])))
                    enrollments_values=school_data.loc[school_data['School Name']==x]
                    values_array=np.array(enrollments_values[["Grade 10","Grade 11","Grade 12"]])
                    values_array_list = list(values_array.flatten())
                    i=0
                    ls = list()
                    while(True):
                        if(values_array_list[i]>500):
                            ls.append(values_array_list[i])
                        i=i+1
                   
                        if (i>=len(values_array_list)):
                            break
            
        
                    if (len(ls)>0):
                        print("For all enrollments over 500, the median value was: ",statistics.median(ls))
                    else:
                        print("No enrollments over 500")
                    
                    break
                else:
                    raise ValueError("You must enter valid school name or school code")
            except ValueError:
                print("You must enter valid school name or school code")
    valid_school()
    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    #It gives only School Year 2013 results and drops null values, assigned it to school_year_2013 variable
    school_year_2013=school_data.loc[school_data["School Year"]==2013].mask(school_data.isna(),0)
    #Grouped 2013 results(mentioned above) and Grade 10, Grade 11, Grade 12 values and calculated their mean and assigned it to school_year_2013_enrollments variable 
    school_year_2013_enrollments= school_year_2013.groupby('School Year',as_index=False,sort=False)[["Grade 10","Grade 11","Grade 12"]].mean()
    #Prints the mean enrollments in 2013 values
    print("Mean enrollment in 2013 :",float((school_year_2013_enrollments["Grade 10"]+school_year_2013_enrollments["Grade 11"]+school_year_2013_enrollments["Grade 12"])/3))
    #It gives only School Year 2013 results and drops null values, assigned it to school_year_2020 variable
    school_year_2020=school_data.loc[school_data["School Year"]==2020]
    #Grouped 2020 results(mentioned above) and Grade 10, Grade 11, Grade 12 values and calculated their mean and assigned it to school_year_2020_enrollments variable 
    school_year_2020_enrollments= school_year_2020.groupby('School Year',as_index=False,sort=False)[["Grade 10","Grade 11","Grade 12"]].mean()
    #prints the mean enrollment in 2020 value
    print("Mean enrollments in 2020 :",float((school_year_2020_enrollments["Grade 10"]+school_year_2020_enrollments["Grade 11"]+school_year_2020_enrollments["Grade 12"])/3))
    #Grade 12 enrollments values of school year 2020 and drops the null values and assigned it to total_graduating_2020 variable
    total_graduating_2020=school_data.loc[school_data["School Year"]==2020]
    #Groups the school year and grade 12 and calculates the sum and assigned it to the total_graduating_2020_enrollments
    total_graduating_2020_enrollments=total_graduating_2020.groupby('School Year',as_index=False,sort=False)["Grade 12"].sum()
    #Created a list for total_graduating_2020_enrollments and assigned it to total_graduating_enrollments_count variable
    total_graduating_enrollments_count=list(total_graduating_2020_enrollments["Grade 12"])

    #It have only one values and at index zero and it's the result of total graduating class of 2020
    print("Total graduating class of 2020 :",total_graduating_enrollments_count[0])
    #Grade 10 column maximum value and assigned it to grade_10_max variable
    grade_10_max = school_data["Grade 10"].max()
    #Grade 11 column maximum value and assigned it to grade_11_max variable
    grade_11_max = school_data["Grade 11"].max()
    #Grade 12 column maximum value and assigned it to grade_12_max variable
    grade_12_max = school_data["Grade 12"].max()
    #Prints the maximum value and it uses max() function
    print("Highest enrollments for a single grade: ",max(grade_10_max,grade_11_max,grade_12_max))
    #Grade 10 column minimum value and assigned it to grade_10_min variable
    grade_10_min = school_data["Grade 10"].min()
    #Grade 11 column minimum value and assigned it to grade_11_min variable
    grade_11_min = school_data["Grade 11"].min()
    #Grade 12 column minimum value and assigned it to grade_12_min variable
    grade_12_min = school_data["Grade 12"].min()
    #Prints the minimum value and it uses min() function
    print("Lowest enrollments for a single grade: ",min(grade_10_min,grade_11_min,grade_12_min))


if __name__ == '__main__':
    main()

