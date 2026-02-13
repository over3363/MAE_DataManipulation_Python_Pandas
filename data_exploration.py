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
# we can only pass in indexes to both the rows and the columns 
# and when we are slicing they are going to exclude the end value 

# print row indexes 1 and 2 and column indexes 1 through 4
# if we want these rows and columns wee are going to have to add a number to our index
# slice 1:3 for the rows, slice 1:5 for the columns 
#Use iloc 
#print("Row indexes 1-2 and column indexes 1-4")
#print(wine_df.iloc[1:3, 1:5])

# we dont have to pass it slices either.
# we could just pass it values 
# we dont have to worry about excluding anything because we are not slicing 
# we are only passing it one number 
# give it the 4th index row which is actually the 5th row , first column 
# it will give us back that exact value 
#print("4th row index, first item")
#print(wine_df.iloc[4, 0])

#when to use iloc vs loc 
#use loc when indexing based on column name 
#there will be situations in whihc you will want to use on or the other 
# sometimes the column name gets messed up and then you will want to use iloc because its easier to index it than get the name 
# sometimes your iterating then you would use iloc
# for pandas they tried to design it so your not iterating a whole lot but sometimes you are  

# like with slicing you can pass in just a colon as code for everything 
# row index 4 will actually be row 5 and all columns  
# we can double check the ouptut with our dataframe 
# its the entire row essentially
#print("All columns, row index 4")
#print(wine_df.iloc[4, :])

#tend to do this using loc becasue the names are more readable
#a little weird becasue of instead passing in specific column names or something like that that meet the condition you actually pass the dataframe back to the dataframe 
# locgically way to do this would be to say quality greater than 5 
# but actually what you do is you say grab the wine dataframe and the quality column of it and then grab the values where that is above 5
# passing in the dataframe twice, just be aware that is the convention to use that 
# has to do with how they are storing the object - pandas always makes copies and whatnot
# thinks there are some function calls you can use where you dont have to pass the whole data frame 
# you could just say the column for very specific conditions 
#Selecting a row based on a condition 
#print("All rows where quality is above 5")
#print(wine_df.loc[wine_df["quality"] > 5])
#run program: only going to print out the ones the meet this condition 
#can see here all of them are above 5
#if we want to double check we can swap 5 for something else 6 - if it gets reprinted we shouldnt see anything with a 6
#print(wine_df.loc[wine_df["quality"] > 6])
# now everything in our dataframe has a quality above 6

# what do you notice about the rows? 
# answer: its printing five rows and the last five rows of this new dataframe we have made
# its printing the index so its keeping the original index 
# thats not always an issue when your slicing a data frame 
# but sometimes you want to make a new dataframe based on some condition you have 
# like your going to exclude certain data  
# then you just want to start fresh with the dataframe made only of your clean data 
# keep in mind if you do that your going to have to reset the index to only include those rows

# can also check how many rows that leaves us 
# We might want to know how many in the overall dataset actually have a score of around 5?
# the index is how they are identifying indivudal rows in your dataframe 
# so if you take the length of your overall index itll give you a count of how many rows are in this subset

#how many rows have a quality score above 5
# going to print the length (len) of the same sort of filter we used before (wine_df.loc[wine_df["quality"] > 5])
# say dot index 
# so wine_df.loc[wine_df["quality"] > 5] returned a different dataframe object 
# that new dataframe object has a property called index which gives you the index of all the rows 
# they are now not going to be zero index because its a new slice 
# dont care about the individual row index , all i want to know is how many total rows there are 
# getting that with this length function we are using
#How many rows is this?
#print("How many rows is this?")
#print(len(wine_df.loc[wine_df["quality"] > 5].index))
# program run: this will give me out a number and that will be the number that meets the condition 
# we can see there are nearly 3258 of the 5000 wines that have the quality of about 5
# if we change the 5 to 6 , we should probably see less (1060 wines meet criteria)
# you could also make a better histogram or something like that 
# there are better visualizations than tabbing through them indivisually on each number
# goal describe how you filter things

#other thing you can do is to use logic operators to get filters of your data as well
# you can use logical and &
# you can use logical or |
# can combine the conditions into different expressions 
# when you have subconditions what your going to be using (if your using and or) your going to have to those in parenthese ()
# or pandas really doesnt like it 


#we have been printing out these slices of dataframes that are kind of long 
#its going to be more useful (especially as we are going) is to take that slice of the dataframe and store it in a subvariable
#subvariable that is a little easier to access than typing out the expression everytime
#create a new dataframe and call it sub_df
# sub_df is equal to the wine dataframe then i say locate (loc) where 
# and then i am going to have an and condition so I am going to have a set of parenthese () the logical operator and & and another set of parentheses ()
# since we are using an and operator it has to meet both of these conditions to be returned into the new dataframe
# winedataframe quality is greater than 5 and suphates are greater than 0.45
# now we can print and get head on this dataframe
# which is now a lot easier than having to access the whole long condition becuase we stored it in a sub variable.
# can also check how many rows is this
# we can print out the length of the subdataframes index 

#print("All rows where quality is above 5 and sulphates are above 0.45")
#sub_df = wine_df.loc[(wine_df["quality"] > 5) & (wine_df["sulphates"] > 0.45)]
#print(sub_df.head())
#print("How many rows is this?")
#print(len(sub_df.index))

# that was the and operator so they have to amke both
# if we use the or operator instead : are we going to have more or less? MORE
# sub_df = wine_df.loc[(wine_df["quality"] > 5) | (wine_df["sulphates"] > 0.45)]
# so now we can see we have to have the wines either be above 5 in quality or be above .45 in sulphates
# we see around 4200 at that condition , almost all of them did

#filtering this data and storing it in these new variables 
# a lot of times were only going to be interested in , a lot of times were using data we ourselves didnt collect 
# so there is stuff in the dataset we dont want to use or doesnt meet a condition that the experiment were trying to run 
# so filtering the data is very useful in order to meet those criteria 
# selecting rows based on a condition is very common 
# another thing that is very common in processing is taking out missing data or trying to find data that was completely filled in 

# handling missing data and how to drop data 
# null data 
# pandas is the majority of this library for this code file
# in pandas if a column or row is missing part of the data its going to go in a a Nan value
# Nan stands for not a number
# depending on the language your working with sosmetimes this comes in as null or none or something else

# First thing want to do : is find and see if we have any missing values in the dataframe 
# we are going to use this is NA property of the dataframe 
# that will return a dataframe were the values are replaced by true or false to indicate whether or not the value is not a number or not 
# if it is true it will indicate that there is not a number of value in there , false otherwise 
# there are other ways to look at this : but this is one way 
# print wine_df the object we created for the pandas library this dataframe type object named wine_df
# and then going to call isna property on it 
#Find and Handle NaNs 
#We don't have an NaN values
#print(wine_df.isna())
#print(wine_df.isna().value_counts())
# run this, you can see we have this giant new dataframe and all the values are replaced with true or false. 
#true would indicate that the particular position has a Nan value 
# so far see all of them are false but its not printing the whole dataframe 
# so lets actually get a value count by the column 
# take function of isna() and another kind of strange thing you can do in Python is you can chain on subfunctions to the end
# this isna property of wine_df (wine dataframe) when you call the function on this, wine_df.isna() becomes a new dataframe 
# and so this new dataframe has some functions you can call on it 
# so we can chain it just by adding another period  there
# take this dataframe and call this value count funciton on it 
# printing part of it is irritating because the terminal is not very large but you could kind of step through each column and print 
# basically you can see for the all the columns we have here , all of them have false values equal to 4898
# not a single on of them has a true value 
# so we can say confidently there is no missing data in this dataframe 

# could use that as a filter to another dataframe (returns a dataframe of true false values)
# could say these have the same indexes give me the original values where the filter dataframes is only false or only true
# there are other ways to do it , other than filtering on a dataframe label
# you can use that object however you want (should be smart enough to understand...)
# demonstrate 
#boolean_df= wine_df.isna()
#print(boolean_df.head())
# wine_df.isna() created a new dataframe that we have now saved in this variable called boolean_df
# this boolean_df no longer contains the values all it contains is whether or not a value at that position 
# and the original one was true or false
# basically creates a mask or filter dataframe 
# you could use that to remove a Nan dataframes but we are going to use a different function 

#realistically your not going to get super nice curated data like this 
# insert a nan value into this dataframe and try to take care of it after that
# first thing we are going to do is checck a random value and put a non number value in it 
# print wine dataframe location very first row index 0 [0] , and I want to grab the quality value  
# print out for now to verify that there is a number there, and yes it printed 6 so thats the value in there 
# next thing to do is create a copy so im not messing with my original dataframe 
# by default most of the time pandas makes a completely new copy of the dataframe to assign to the variable 
# a lot of times the pitfalls you run into with python is if you worked with other programing languages sometimes you copy something by reference and sometimes you copy things by value 
# if you copy it by reference you end up creating two references to one singular object
# and if you update one you tend to update the other 
# and if you thought they were seperate objects that will get you in trouble  
# with pandas by default it is going to make a new copy so you dont have to specify make a new copy or copy it by value its already doing that
# handy for not accidently changing something you didnt mean to change
# not so handy for memory or time management so it will take longer 
# new dataframe new_df is equal to wine_df wine dataframe this is going to create a copy 
# we dont have to specify copy or anything 
# now we are going to say this new dataframe locate position of row 0 quality score and assign that to none 
# pandas can understand Nan values , python really doesnt it uses none instead.
# when we run program and print it out we should see a nan value there 
# originally location 0 quality column was 6 , we created a copy of the new dataframe and then we assign that specific position to none , and so pandas now says thats a non number value there thats a null reference

#Insert an NaN value
#print(wine_df.loc[0, 'quality'])
#new_df = wine_df
#new_df.loc[0, 'quality'] = None
#print(new_df.loc[0, 'quality'])

# how you want to deal with not number values nan will definetly vary by what you are doing
# sometimes you will want to fill them 
# sometimes you want to just drop them completely 

# in the case of dropping it, it will remove the entire row if any of its columns have a nan in it
# sometimes you dont want to that , especially when we get to the time series data part 
# sometimes you actually fill that , you take okay it was this number right before the missing number , it was this number right after so we are going to average it, or we are going to fill it with the last known value (if its like a set point or something)
# since these are all instances of kind of the same or completely independent wine just dropping any incomplete data makes sense for this use case
# First thing want to do: put some checks for ourselves : number of rows before dropping nan using print length of this new dataframes index
#index is the rows that are in the dataframe , the index number of the rows 
# do length of that index on dataframe will tell us the total number of rows in the dataframe 
# then we are going to create the cleaned dataframe , cleaned dataframe is equal to its new dataframe and then we are going to call this drop na function on it 
# that will completely get rid of those
#Drop the na value 
#print("Number of rows before dropping NaN")
#print(len(new_df.index))
#cleaned_df = new_df.dropna()
# reset index
#to reset index first way
#cleaned_df = cleaned_df.reset_index()
#cleaned_df.reset_index(inplace=True)
#before resetting index example
#print(cleaned_df.head())
#print("number of rows after dropping NaN")
#print(len(cleaned_df.index))
# before resetting index example
#print(cleaned_df.loc[0, "quality"])

# before dropping it we had 4898 and after we dropped it we had 4897 
# will say this is where I want to get into this index behavior 
# if we print, right after we drop this NaN value , cleaned dataframe head:
# print(cleaned_df.head()) 
# remember the head prints out the first 5 rows 
# in this case its printing out row 1, 2,3, 4, 5: what are we missing: zero row which is great we dropped that but that got rid of that index completely
# if I use: #print(cleaned_df.loc[0, "quality"]) after dropping nan should get an error because that index no longer exists
# because after dropping this row it didnt reset the index 
# sometimes thats useful if your taking subsets of the dataframes and you want indexes to be the same as the original becuase your doing some weird filtering thing or you want to page through specific indexes. thats good behavior 
# however if you want zero to always refer to the first row or if your iterating through based on index number in a loop this can be really annoying because zero is supposed to be the frist index no matter what, now we got rid of it
# good thing is its pretty easy to reset the index 
# so after we drop not a number value 
# we are going to go ahead reset the index 

# two ways to reset the index 
# we can take this cleaned data frame variable and say it is equal to the cleaned dataframe variable dot reset index 
# again almost everying in pandas creates a copy so this creates a new dataframe
# cleaned_df = cleaned_df.reset_index()
# if you just call reset index value its not going to make changes, fundamental changes to this clean dataframe 
# its returning a value 
# you have to reassign it back to the value (common problem forgetting)
# run program: no error the zero index was a valid option 
# if you dont want to reassign it to back to the variable theres one more thing you can do 
# you can say clean_df.reset_index() and then pass it this argumnet called inpace 
#clean_df.reset_index(inplace = True) by defualt its false cause it makes a copy 
# but if you dont want to reassign it back to the variable its totally a matter of your preference 
# havent looked into the runtime implications of either method but they should do exactly the same thing 
# run program: now you can see we have one less row but our index 0 is valid 
# reset index renumbers the indexes back to the order they are now in 0-4 in this case
# got the zero index back again because it basically shifted them all 1 
# if we had multiple out there it would have renumbered them completely just the number of rows 
# so we will have 0 through 4896 as our total index (because we now have 4897 rows)

#common mistake to make: if your having wierd behavior on indexes one thing I would check to make sure you either reset it in place or reassigned it back to the variable you were using 

#Reset the index - in place this time 
#cleaned_df.reset_index(inplace=True)
#print("Number of rows after dropping NaN")
#print(len(cleaned_df.index))
#print(cleaned_df.loc[0, "quality"])

# make sure matplotlib and seaborn is imported 
# standard convention is to put it at the top so all your packages are there and you dont have weird import errors as your running the script 
# python in a lot of cases will let you import it somewhere else in the script though 

# correlation heatmap
# pretty useful to see what variables might be correlated to others
# going to use seaborn and the corr() correlation function on the data frame to create one 
# print out the correlation wine_df.corr()
# this will create a correlaiton matrix with how strongly each variable is correlated to the others
# run the program: will get rid of the middle stuff (...) so that is kind of annoying, if you were to actually printing this out to look at the raw data make sure you have your print settings set differently
#can see fixed acidity and fixed acidity are perfectly correlated to each other thats good - same value should be 
# what we really want to know probably is whats correlatd with quality 
# fixed acidity has a very small negative correlation with quality 
# if we go to alchol we see we have a not super srong but probably relevant correlation with quality 
# putting the correlation might be nicer to see it as a plot 
# plot is equal to seaborn library using the alias we imported it with , and we are going to go heatmap and then 
# we are going to pass it this wine dataframe correlation matrix 
# better coding practice would probably be to say assign this correlation matrix to a variable called coorelation or something and then pass that in 
# then if we go plt , so we are going to use the gui functions in matplotlib and we are going to say plt.show() and then under plt.clf (clear)
# show will show the model we created clf will clear the figure for the next one so its not overlapping on itself 
#Visualize 
#Correlation
#print(wine_df.corr())
#plot = sns.heatmap(wine_df.corr()) 
#plt.show()
#plt.savefig("correlation_plot.png") 
# I legit dont know where this saved at lol 
# after searching it was saved at this path : /Tori
#plt.clf()

#there is a lot you can do with graphing functions 
#how to add a plot title and whatnot (check documentation)
# this is the heatmap 
# the much lighter colors have a very strong positive correlaiton 
# see on the diagonal of this matrix here evidence 

# if your not getting your graph to pop up it has to do with your enviorment (sometimes specific virtual enviorments)
# gal with error bigger canvas ag or user warning . bigger canvas ag is not interactive and thus cannot be shown
# work around 
# this works with marys graphical interface to pop it up: instead of show we can save it as a png using command plt.savefig("correlation_plot.png")
# plt.savefig("name.png")
# that should create this file in my enviorment 
# depending on your enviorment it might have saved it really small 
# again there are settings you can mess with to actually get out a resolution (worked for mary's)
# matplotlib can be a little gui specific 
# virtual enviorment probably has a way to interact but it something that would need to be a setting that you would have to looked up
# at least most of them do
# anaconda I know in partiuclar and matplotlib are not always friends 

# on the diagonal we can see we have perfect correlation 
# various colors give various levels of positive or ngative correlation 
# we can see that alchol and density are somewhat negatively correlated 
# quality is what we really want to knwo here so 
# we can see quality and quality are perfectly correlated with each other  as they should be 
# and then we can see alchol as maybe the most positive correlation of any other variable with quality 
# we can see density has a slight negative 
# overall there is not a whole lot of strong correlation of any of these individual values or the quality 
# becauee its a wine dataset its probably not super scientific 
# you can also press s if you have the interactive gui to save the figure that way 
# or you can click the little save icon 
# clear figure because matplotlib kinda layers the figures on top of each other 
# so if you dont use that you might have two plots trying to interact with each other or on top of each other 
# you might get some weird results (it depends)
# correlation plot can be really useful to investigate things that might have some relations 
# then you can kind of dig deeper and create these plots that let you see it more granularly 

# scatter plot creation 
# now we are using matplotlib primarially 
# use plt to call that library and we are going to say scatter and we are going to give it the wine dataframe 
# quality score and the wine dataframe alchol score 
# again you might have to use save fig 

#Scatter
dependent_var = "quality"
independent_var = "alcohol"
plt.scatter(wine_df[independent_var], wine_df[dependent_var])
#plt.scatter(wine_df["alcohol"], wine_df["quality"])
#plt.scatter(wine_df["quality"], wine_df["alcohol"])
#plt.title("Correlation Between Quality and Alcohol")
plt.title(f"Correlation Between {independent_var} and {dependent_var}")
plt.xlabel(independent_var)
plt.ylabel(dependent_var)
plt.show()
plt.clf()

# run program: can see its kind of a correlation between quality and alchol but its not the best looking one in the world 
# clear doesnt matter where you call it so long as its sometimes before you display the next graphs if you have a pervious one 
# add a title plt title pass it a string 
# maybe i would rather have this between alchol and quality because quality is my actual dependent variable 
# so I can alway switch those around 
# plt.scatter(wine_df["alcohol"], wine_df["quality"])
# should get a new plot that has alchol on the x axis and quality for the y axis 

# coding practice wise: often you are going to be running through a lot of these 
# so id maybe recommend saving these as varaiables 
# dependent_var...
# nice thing you can do in python are called f strings 
# take the string as my plot title and put an f in front of it . I can now put brackets inside the string with variable names 
# and it will replace that with the variable value 

# run this can see we got this plot got a correlation between alchol and quality 
# wnat to label axises to xlabel, ylabel
# now if you wanted to investigate something else you could just replace alchol with say density
# independent_var = "density"
# should update the whole rest of the plot if I run it again 
#if you were doing a scatter plot and it had perfect correlation it would look it would be the x = y graph 
# scatter plot takes every instance in your dataset and for the x axis it plots the corresponding y 
# so this is all the wines in the dataset represented each as a dot 
# and then if you look at general trends you can sort of maybe assume so correlations 
# but the corelation plot gives you the actual numerical value
# look at quality and quality they have perfect correlation should see an x equal y graph 

# wine dataset
# use this datset because its fairely easy to mess with and understand and probably wont fry your potato of a computer 
# its really not the best dataset to start with on any kind of statistical or mathmatical basis because its pretty subjective 
# theres not a lot of great strong correlations in it 

# keyboard command to comment an entire area: linux computer 
# if you highly the whole area and I go ctrl+k+c it will comment the whole thing as a block
# ctrl+k+u it will uncomment 
# there is a way in VScode to look at all the keyboard shortcuts 
# your editor might have different ones if your not using VScode 
# someones says ctrl ? is the same so idk

# basics of looking at data in python 
