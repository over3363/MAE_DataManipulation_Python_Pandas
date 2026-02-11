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
#print("Columns as a List")
#print(list(wine_df.columns))
# print list winedata frame columns 
# list is another built in python function take the wine data frame column object and convert it into the python data frame or python data type list 
# run this now: you see I got columns printed out as this list object
# you call tell because of the open and closed brackets , all the elements of the list have quotes around them and they're seperated by a column 
# that is a list in python

# Troubleshooting: sometimes if your in the virtual enviorments sometimes you might have accidently installed the packages in the base or a different enviorment, so you might have to reinstall those

#sometimes its also good to explore so basic data statistics based on the columns like the mean, the minimum and the max and the standard deviation of the values in there
#another function on the pandas library we can use called describe which is really useful to do that

#Describe the data 
#print("Describe the data")
#print(wine_df.describe())
# run program: for each of the columns within the data it has printed out the count
# count: the number of elements we have in each column 
# mean
# standard deviation std
# min
# percential values 
# max 
# can see the minimum quality is 3 , we know that we dont have any wines in our dataframe that have a score under 3 
# maximum is 9 so even though theoretically we have a range of 0-10 on this particular dataframe we only have wines that are between 3 and 9
# the standard deviation is about .8 to about 1 from the mean which is 5 
# so most of our wines are going to be somewhere between like 4 and 6 or 5.5 and 5 


#indexing the data 
#one of the most useful things we can do in general with pandas is index it to get different subsets of data 
#a lot of times when were looking at data what we are doing is filtering different views of the data to use for a specific task
#there are a lot of ways to do this in pandas 
#going over only a subset of ways to do this 

# goal: try to get just one whole column of the dataframe  
# command: quality_series ....
# want just the quality aspect call it quality_series
#because when you use this method it is going to return it as a series 
# series is a slightly different datatype that a dataframe but very similar
# say quality_series is equal to winedataframe and then we are going to use an open and close bracket
# open and close bracket is pretty common used when indexing something in python 
# then type quality 
# what this does is it is taking just the quality column of the wine dataframe and its going to return it as a variable named quality_series.
# print quality series : not going to print out the whole thing but our first five elements had a quality of six and our last five had six,five,six,seven,six
# we have filtered it down to just the quality variable of the whole series 

#Indexing 
#Return a series with the 'quality' column of of the dataset
#quality_series = wine_df['quality'] 
#print("Quality series")
#print(quality_series)

# can also pass it a list of multiple column names so if you want quality and you want sulfides you can get those two together
# that would return not a series but a smaller dataframe 
# only has the column names you passed in 

# sometimes we get a series or an index or something and we want it as a list of values 
# sometimes your reading in data and you only care about a certain column and you needed a list or different format
# the way to do that with python is to use values to list 

#Get a list of values from a column
#quality_list = wine_df['quality'].values.tolist()
#print("Quality List")
#print(quality_list)

#quality_list is a variable we are creating thats going to be equal to the winedataframe which were indexing with this quality 
#and then we are going to say I want the values of that and we are going to convert them to a list 
# they should return the values just as a list set up as an object
# run program: see how its a python list
# python cares a lot less about spamming your screen which is sometimes good and sometimes bad
# you can see we have this entire almost 5000 values of just the quality as a list in the order they are presented in the data

# .loc the location property of the location indexer for the dataframe 
# this allows you to select different rows and columns 
# there are two ways to do this sort of selection using pandas 
# one is loc and one is iloc
# i standing for index 
# the main difference between the two of them is if your using loc your going to select a column by its name and then the row by its index 
# if your using iloc youre selecting both by their index 
# you can also pass conditions into loc
# if your passing both row and column indexes at the same time, you pass them in the order row column 
# follow python slicing rules 
# python slicing allows you take different ranges 
# loc favors columns more 
# iloc favors rows more 
# if you pass two indexers into loc its going to be row column 
# if you pass only the label its just going to index on column (which sometimes you want)
# for iloc if you only pass it one number its going to assume thats the row
# but they're always in the order row column for both 
# annoying component of pandas is they follow python slicing rules 
# loc if your slicing includes the start and end value in a slice 
# iloc doesnt include the end value in a slice 

# get everything in the quality column using python slicing rules and loc to do it
# print wine dataframe (our dataframe object) dot loc and then use an open and close bracket 
# first thing we are going to pass in is the rows 
# want all the rows for one column 
# so if we want everything we are going to pass in a colon : for a row
# if you just see a colon that means include everything 
# for normal slicing you would put numbers on either side of the colon 
# if you dont do that it says include everything 
# then a comma , thats for rows 
# and then we are going to say quality for column because thats the only column we want 


#loc 
#Get everything in quality 
#print("Entire quality column")
#print(wine_df.loc[:,"quality"])

# run program: entire quality column, got all the rows , its only printing the first and last five but only the quality value in those rows 
# successfully filtered down to one column using loc




#Get the first value in quality
#print("First quality value")
#print(wine_df.loc[0,"quality"])

# next try to slice on the rows but still stay in the quality column 
# should give us the first 6 values in there
# what we are going to do is we are going to print , we are going to use wine dataframe loc 
# and we are going to say give me index rows between 0 and 5. 
# again this is the index number and its zero index so this should give us six rows 
# and then we are going to say we only want the quality column 
#print("First and up to 5th-indexed quality values")
#print(wine_df.loc[0:5,"quality"])

# other thing with slicing is if we don't pass it a number on the left it will get everthing up to and before that 

#print("Everything up to 5th indexed row quality value")
#print winedataframe loc. going to give it a colon and say 5 ; where 5 is the outer boundary for the row , give me everything before that 
# and i still just want the quality value 
#print("Everything before and up to the 5th-indexed quality values")
#print(wine_df.loc[:5,"quality"])
#same result as print(wine_df.loc[0:5, "quality"]) but we didnt have to specify the 0

#get the quality value for the last couple
#give it starting argument as 4890 and then we wont put anything after it 
#we have 4898 total values but its zero index so the last index will be 4897 (the index is 1 less)
#print("Everything after the 4890th-indexed quality value")
#print(wine_df.loc[4890:,"quality"])

# we can get both indexed now and we can pass it more than one column 
# print the wine data frame dot loc. then we are going to say give me row 0 through 5 
# and then on the column side i am now going to create a sublist (using []) so I can pass in more than one column 
# so give me quality and sulphates 
#print("First through 5th-indexed quality and sulphates values")
#print(wine_df.loc[0:5,["quality", "sulphates"]])
# can see it returns a smaller dataframe
# has 0 1 2 3 4 5 rows and it gives me both the quality and the sulphate values for those 6 rows 

#there are some cases where you specifically know what the index is of the rows you want to use or the columns 
#but most of the time you know the column and you dont necessarly know the rows
#your kind of filtering based on a condition
# talk about iloc first but then really what you will probably be doing the most of is filtering the data/dataframe based on whether the values meet a certain condition 

# iloc will exclude the last value we give it two
# very similar to loc but now we cant pass in column names 

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

