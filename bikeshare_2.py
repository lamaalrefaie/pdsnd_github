
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:18:03 2022

@author: lamaa
#Lama majed alrefaie 

"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthdata = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

daydata = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityName = ''
    while cityName.lower() not in CITY_DATA:
        cityName = input("\n choose one of these three cities (new york city , washington or chicago) that you want to analyze\n")
        if cityName.lower() in CITY_DATA:
            #if user get the name correct 
            city = CITY_DATA[cityName.lower()]
        else:
            #if user get the name wrong => will do a loop to get the correct answer 
            print("its not correct ,Please enter either new york city , washington or chicago\n")
            
            

    # TO DO: get user input for month (all, january, february, ... , june)
    monthName = ''
    while monthName.lower() not in monthdata:
        monthName = input("\n Enter the name of the month that you want to analyze (choose 'all' or from january to june \n")
        if monthName.lower() in monthdata:
            #if user get the name correct 
            month = monthName.lower()
        else:
            #if user get the name wrong => will do a loop to get the correct answer
            print("its not correct ,Please enter either 'all' or choose one of the months from january to june \n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayName = ''
    while dayName.lower() not in daydata:
        dayName = input("\n Enter the name of the day that you want to analyze (choose 'all' or from monday to sunday \n")
        if dayName.lower() in daydata:
            #if user get the name correct 
            day = dayName.lower()
        else:
           #if user get the name wrong => will do a loop to get the correct answer
            print("its not correct ,Please enter either 'all' or choose one of the Days from monday to sunday \n")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

   # load data 
    df = pd.read_csv(city)

    # convert the Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # create new columns
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        #we will use the index months get the identical int
        month = monthdata.index(month)
        
        #create the new dataframe
        df = df.loc[df['month'] == month]  
        
    if day != 'all':
        # analyze and create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    commonMonth = df['month'].mode()[0]

    print('the most common Month:\t', commonMonth)

    # display the most common day of week
    commonDay = df['day_of_week'].mode()[0]

    print('the most common Day Of Week:\t', commonDay)

    # display the most common start hour
    commonStartHour = df['hour'].mode()[0]

    print('the most Common Start Hour:\t', commonStartHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popularStartStation = df['Start Station'].mode()[0]

    print('the most Start Station:\t', popularStartStation)

    # display most commonly used end station
    popularEndStation = df['End Station'].mode()[0]

    print('the most end Station:\t', popularEndStation)



    # display most frequent combination of start station and end station trip
    groupField=df.groupby(['Start Station','End Station'])
    
    frequentCombination = groupField.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\t', frequentCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTravelTime = df['Trip Duration'].sum()

    print('the total travel time:\t', totalTravelTime)

    # display mean travel time
    meanTravelTime = df['Trip Duration'].mean()

    print('the mean travel time:\t', meanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    
    print('User Type')
    print(df['User Type'].value_counts())
    
    if  city == 'new_york_city.csv' or city == 'chicago.csv':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year:')
        mostCommonYear = df['Birth Year'].mode()[0]
        print('the most common year:\t',mostCommonYear)
        mostRecentYear = df['Birth Year'].max()
        print('the most recent year:\t',mostRecentYear)
        earliestYear = df['Birth Year'].min()
        print('the earliest year:\t',earliestYear)
    else:
        print("washington does not have gender or birth data")
           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displayRawData(df):

    print(df.head())
    next = 0
    while True:
        DisplYRawData = input('\n Do you want to see next 5 row of data row?\n \tEnter yes or no\t ')
        if DisplYRawData.lower() == 'yes':
            print(df.iloc[next:next+5])
            next = next + 5
        elif DisplYRawData.lower() == 'no':
            break
        else:
            print('sorry you either enter wrong answer or there is no more data to view  ')
 
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
   
        while True:
            DisplyRawData = input('\n Do you want to see firt 5 row of data row?\n \tEnter yes or no\t ')
            if DisplyRawData.lower() != 'yes' :
                break
            displayRawData(df)
            break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
   print('thank you and have a good day !')

if __name__ == "__main__":
	main()