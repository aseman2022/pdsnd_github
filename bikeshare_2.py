import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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

    city = ' '
    while(city.lower() not in CITY_DATA):
        city = input('\nHello! Let\'s explore some US bikeshare data! \n'
                     'Then see the data for Chicago, New York city, or Washington?\n')
        city = city.lower()
        if city not in CITY_DATA:
            print('Input is invalid and select a valid city from Chicago, New York city, or Washington.')
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)

    month = ' '
                        
    while(month.lower() not in months):
        month = input('\nEnter name of month (jan, feb, mar, apr, may, jun) to see the data:')
        month = month.lower()
        if month not in months:
            print('Input is invalid and type in a month between Jan and Jun')
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

  day = ' '
    while(day.lower() not in days):
        day = input('\n Enter the day of week (monday, tuesday, so on....) to see the data: ')
        day = day.lower()
        if day not in days:
            print('\n Input is invalid and type a correct day of the week')
        else: 
            break

            
            
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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
     print('The most common month:', months[df['month'].mode()[0] - 1].title())


    # TO DO: display the most common day of week

    print('The most common day of week:', df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour

    print('The most common start hour:', df['hour'].mode()[0])

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('The most commonly used start station: ', df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station
    
    print('The most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    num_trips = df.groupby(['Start Station', 'End Station']).size()
    
    print('The most frequent combination of start station and end station trip:\n', num_trips[num_trips == num_trips.max()])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print("Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time

    print("\nMean travel time:", df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('Counts of user types:\n', df['User Type'].value_counts())
    
    # TO DO: Display counts of gender

    print('\nCounts of gender:\n', df['Gender'].value_counts())
    
    # TO DO: Display earliest, most recent, and most common year of birth

    print('\nThe Earliest year of birth: ', int(df['Birth Year'].min()))
    print('\n Most common year of birth: ', int(df['Birth Year'].mode()[0]))
    print('\n The latest year of birth: ', int(df['Birth Year'].max()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
