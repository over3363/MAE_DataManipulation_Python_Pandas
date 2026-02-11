#Help from the pandas documentation:
#https://pandas.pydata.org/docs/user_guide/

#The matplotlib documentation:
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

#And from here:
#https://stackoverflow.com/questions/39409866/correlation-heatmap

#pip install pandas for native installation 
#conda install pandas for non-native installation
#same with matplotlib and seaborn

# Goal: Investigating the data set using python and pandas 
# have CSV file in the folder that I am working in, if you have it in a different folder just make sure you change the path when we import it 

# First Step: Import the Libraries 
# A Library in Python is a collection of functions and variables and things you might be able to use that you didn't have to code yourself- somebody else made them for you
# To import something in python as a library you type import and then you type the name of the library
# Another thing you can do in python is alias libraries - you can rename them so they are a little easier to use 
# The reason we alias libraries is because whenever we call a function or a class or a variable for pandas we type the library name first and then a period and then the name of the function of the class or the object
# if you dont want to type out pandas the whole time you can alias it 
# import pandas as pd
# in data science notebooks and stuff like that its pretty normal for PD to stand for the pandas library
# pd makes pandas a little shorter depending on how readable or reusable you want your code to be fore you, feel free to import it not aliased


# matplotlib is the overall graphing library 
# pyplot is a submodule of that library 
# matplotlib is a fairly large library
# if you want your code to maybe be imported a little bit faster you can say I only want this specific module of it 
# dont want to type matplotlib.pyplot everytime so I am going to import it is a plt for plot

# if you use seaborn a little more often sns makes sense 

# using Python programming language 
# MAE file was called explore.py
# create a file and name it anything: is the code file 
# run it using the python program : python3 <nameoffile.py>
# make sure youre in the folder when your running it 
# command not powershell in VSCode

#Import the pandas dataset 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# ran didn't do anything nothing errored out so it imported the libraries 
# if youre getting a module not found error make sure you virtual enviorment is activated 
# so if you have a virtual enviorment and you named it something specific - if your using vs code you should see the virtual enviorment in () before you path
# if you dont you might have used the wrong python/ python3 command becuase sometimes you have different installations of those
# lots to troubleshoot 

# Step 2: Load in CSV file
# use the panadas library to do that because there isnt a great structured way to load an excel file in python without using a library like this 
# function call we are going to be using is called read_csv()
# we are going to load in a file and save it in a particular variable 
# in pandas the structured object you normally work with with excel like data or any kind of tabular data they call it a dataframe 
# for short you will often see dataframe abreviated as DF 

# create a variable called wine_df
# equal to the pd (which is the pandas library) . read_csv (is the function call) 
# pass read_csv two arguments one is the name of the csv file we are going to be using (winequality-white.csv) 
# putting the name in "" because its a string. names are usually strings. 
# the other argument is the keyword argument 
# pythons a little different than other languages in that you can have arguments that you just pass in in order like you would see in a c/cpp function but you can also have keyword arguments
# keyword arguments are ususally optional. 
# when they define the function they usually have a default for keyword arguments
# For the read csv file their default separator because its a comma seperated value file is a comma 
# in this case : this particular code file came in with a semicolon separator 
# so we need to say override the default and use the separator as a semicolon 
# entire line is a statement

#Read the dataset into the "wine_df" variable
#wine_df = pd.read_csv("winequality-white.csv", sep=";")
wine_df = pd.read_csv(r'C:\Users\Tori\Documents\MAELecture\DataExplorationAIModelOverview\winequality-white.csv', sep=";")
# PROBLEM: When Pandas throws a FileNotFoundError despite the CSV being in the same folder, it’s usually due to a mismatch between the current working directory and the file’s actual location.
# FIX: Or use the absolute path directly: data = pd.read_csv(r'C:\path\to\your\folder\data.csv')

# As we are going through and doing data manipulation good to spot check how we are doing
# 1 test: once we have this read into this wine dataframe variable we can do is we can print out the head
# the head gives us a little bit  of an overview of the data we just read in 
# use the built in python function called print which will print it out to the console 
# print this wine dataframe head 
# head is a function of the object wine data frame and its going to print out a little summary of information 

#Get an overview of the data 
#print(wine_df.head())

# a couple of pitfalls when working with this IDE (VScode) in particular is make sure you saved your file before you run it 
# or its going to run the last thing that saved and you might get weird behavior 
# In VScode you can use ctrl s 
# Run program: If I did it right got a little print out of the head. 
# What it does: is it prints the first five rows of data. It prints six or so columns. 
# It has the elipsies (...) in the middle because it has more columns than it can realistically fit in my output 
# so it printed the first three and the last three columns 
# index 0 wine has a fixed acidity of 7 a citric acid of .36 and a quality of 6 

# As we are going through kind of the code file we are running this whole file everytime 
# so its going to continue to print this head 
# if we dont want it to print everytime we could comment it out 
# if you use the number key or the hashtag or the pound symbol # thats the comment in python 
# if this # is in front of a line its not going to execute this line the interpreter will completely skip it 
# in vscode it puts it in this green color so you know it wont be executed 

# Step 3: Print the Columns 
# Another thing we can do is print the columns. A lot of times it nice to know all the columns you have available 
# A couple different ways we can do this. 
# The first way is just using the native columns property of this data set. we can print that out
# Add comments so you know what your doing in the code 

#Print the columns - method 1
#print("Columns Index")
#print(wine_df.columns)
# so this is a property of the wine dataframe not a function of it (kinda interesting) so im not putting the parenthesis (). its not executing anything 
# this is a stored property of this object in the underlying pandas library
# save and run program: should see I have this columns index which is an object property of the dataframe and CDC index
# the index is composed of a list of the columns here.
# we can see it even prints out the datatype here which is an object. 
# the columns object is a property of the dataframe object
# can see all the other columns we have
# this is nice for spot checking but the datatype that is more native to pandas is a list 
# sometimes its more useful to work with columns as the python datatype was

# second way we can do that: print the columns as a list
#Print the columns - method 2
print("Columns as a List")
print(list(wine_df.columns))

#Describe the data 
#print("Describe the data")
#print(wine_df.describe())


#Indexing 
#Return a series with the 'quality' column of of the dataset
#quality_series = wine_df['quality'] 
#print("Quality series")
#print(quality_series)


#Get a list of values from a column
#quality_list = wine_df['quality'].values.tolist()
#print("Quality List")
#print(quality_list)


#loc 
#Get everything in quality 
#print("Entire quality column")
#print(wine_df.loc[:,"quality"])

#Get the first value in quality
#print("First quality value")
#print(wine_df.loc[0,"quality"])

#print("First and up to 5th-indexed quality values")
#print(wine_df.loc[0:5,"quality"])

#print("Everything before and up to the 5th-indexed quality values")
#print(wine_df.loc[:5,"quality"])

#print("Everything after the 4890th-indexed quality value")
#print(wine_df.loc[4890:,"quality"])

#print("First through 5th-indexed quality and sulphates values")
#print(wine_df.loc[0:5,["quality", "sulphates"]])

#Use iloc 
#print("Row indexes 1-2 and column indexes 1-4")
#print(wine_df.iloc[1:3, 1:5])

#print("4th row index, first item")
#print(wine_df.iloc[4, 0])

#print("All columns, row index 4")
#print(wine_df.iloc[4, :])



#Selecting a row based on a condition 
#print("All rows where quality is above 5")
#print(wine_df.loc[wine_df["quality"] > 5])
#How many rows is this?
#print("How many rows is this?")
#print(len(wine_df.loc[wine_df["quality"] > 5].index))

#print("All rows where quality is above 5 and sulphates are above 0.45")
#sub_df = wine_df.loc[(wine_df["quality"] > 5) & (wine_df["sulphates"] < 0.45)]
#print(sub_df.head())
#print("How many rows is this?")
#print(len(sub_df.index))


#Find and Handle NaNs 
#We don't have an NaN values
#print(wine_df.isna())
#print(wine_df.isna().value_counts())


#Insert an NaN value
#print(wine_df.loc[0, 'quality'])
#new_df = wine_df
#new_df.loc[0, 'quality'] = None
#print(new_df.loc[0, 'quality'])

#Drop the na value 
#print("Number of rows before dropping NaN")
#print(len(new_df.index))
#cleaned_df = new_df.dropna()
#Reset the index - in place this time 
#cleaned_df.reset_index(inplace=True)
#print("Number of rows after dropping NaN")
#print(len(cleaned_df.index))
#print(cleaned_df.loc[0, "quality"])



#Visualize 
#Correlation
#print(wine_df.corr())
#plot = sns.heatmap(wine_df.corr()) 
#plt.show()
#plt.clf()

#Scatter
#plt.scatter(wine_df["quality"], wine_df["alcohol"])
#plt.show()
#plt.clf()

