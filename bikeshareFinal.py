import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
      city=input("Please enter your required city either chicago ,new york city, washington : ")
      city=city.lower()
      if (city in CITY_DATA ):
         break
    filters=['month','day','both','none']        
    while True :
        fil=input("Would you like to filter the data by 'month' , 'day' , 'both' or 'none' ?")
        fil=fil.lower()
        if fil in filters:
            break
            
 # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if fil=='month':
        while True:    
          month=input("Please enter your required month or enter all for no filter: ")
          month=month.lower()
          if (month in months )or month=='all':
             break
        day='all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
    if fil=='day':
        while True:
          day=input("Please enter your required day or enter all for no filter: ")
          day=day.lower()
          if (day in days )or day=='all':
             break
        month='all'
    
    if fil=='both':
        while True:    
          month=input("Please enter your required month or enter all for no filter: ")
          month=month.lower()
          if (month in months )or month=='all':
             break
        while True:
          day=input("Please enter your required day or enter all for no filter: ")
          day=day.lower()
          if (day in days )or day=='all':
             break
                
    if fil=='none':
        month ='all'
        day='all'
            
        
      
    
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    if day!='all':
        df=df[df['day_of_week']==day.title()]
        
    if month!='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df=df[df['month']==month]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("Most common start month is :",months[common_month-1].title())

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print("Most common start day is: ",common_day)

    # TO DO: display the most common start hour
    
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print("Most common start hour is: ",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("most commonly used start station is: ",common_start_station)

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    
    print("most commonly used end station is: ",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination']=df['Start Station']+" to "+df['End Station']
    common_station=df['Station Combination'].mode()[0]
    print("most commonly combination of start station and end station trip is: ",common_station)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time is :",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average travel time is :",df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types counts :",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    
    try:
        print("User types counts :",df['Gender'].value_counts())
    except :
        print("Gender information not available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest year of birth is :",df['Birth Year'].min())
        print("Most recent year of birth is :",df['Birth Year'].max())
        print("Most common year of birth is :",df['Birth Year'].mode())
    except:
        print("Birth Year information not available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    start=0
    while True :
       view= input("Would you like to view 5 rows of the raw data? Enter yes or no.\n ")
       view=view.lower()
       if view !='yes' and view !='no':
         continue
       elif view=='yes':
         print(df[start:start+5])
         start+=5
       elif view=='no':
         break
    
       
           
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
