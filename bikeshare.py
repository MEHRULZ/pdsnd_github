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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(" Please Choose a city to explore Bikeshare Data: Chicago, New York City or Washington ")
    while city.lower() not in ['chicago','new york city','washington']:
            city = input(" Wish we could help you with {} ,we just have data for Chicago, New York City, Washington, so choose from these ".format(city))
    city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nFilter by Month: All, January, February, March, April, May, June: Please type the full month name.\n')
    while month.strip().lower() not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('\n Please choose from these months: January, February, March, April, May, June or type All for all months \n')
        month = month.strip().lower()
    month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Select a day of the week(Sunday, Monday, Tuesday, Wednesday,Thursday, Friday ,Saturday) or enter all for all days: ")
    while day.title() not in ['All','Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday','Saturday']:
        day = input("Select a day of the week(Sunday, Monday, Tuesday, Wednesday,Thursday, Friday ,Saturday) or enter all for all days: ")
    day=day.title()
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Input: The dataframe with all the bikeshare data
    Returns: nothing
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month= df['month'].mode()[0]
    popular_month_count = df['month'].value_counts().max()
    print('Most Popular Month: {}  with Count {}' .format(popular_month,popular_month_count))

    # TO DO: display the most common day of week
    popular_day_of_the_week= df['day_of_week'].mode()[0]
    popular_day_of_the_week_count =df['day_of_week'].value_counts().max()
    print('Most Popular Day of the Week: {} with Count: {} '.format(popular_day_of_the_week,popular_day_of_the_week_count))

    # TO DO: display the most common start hour
    popular_start_hr= df['start_hour'].mode()[0]
    popular_start_hr_count= df['start_hour'].value_counts().max()

    print('Most Popular Start Hour: {} with Count: {} '.format (popular_start_hr,popular_start_hr_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Input: The dataframe with all the bikeshare data
    Returns: nothing
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(' Most common start station: ', common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(' Most common End station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'].map(str) + ' '+ '&' + ' ' +df['End Station']
    common_station_combo = df['Start End Station'].mode()[0]
    print(' Most common End station: ', common_station_combo)

    # Delete the column as its not need further
    df = df.drop(['Start End Station'],axis =1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Input: The dataframe with all the bikeshare data
    Returns: nothing
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] =  pd.to_datetime(df['End Time'])
    df['Trip Duration' ] = df['End Time'] - df['Start Time']
    total_travel_time = np.sum(df['Trip Duration'])
    print('The total Travel Time is :' + str(total_travel_time).split()[0] +' days')

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('The mean travel time is {} '.format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users.
    Input: The dataframe with all the bikeshare data
    Returns: nothing
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The User Types are: ',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_dist = df['Gender'].value_counts()
        print('What is the Gender Distribution : ',gender_dist)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year =df['Birth Year'].min()
        recent_year =df ['Birth Year'].max()
        common_year =df['Birth Year'].mode()[0]
    print('The Eldest user was born in : ',earliest_year)
    print('The Youngest user was born in  ',recent_year)
    print('The Average Age is  ',2019 -common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays 5 rows of data used to compute the stats
    Input: The dataframe with all the bikeshare data
    Returns: nothing
    """

    view_data=input('Would you like to see a glimpse of data used to compute the Bike Share Stats? Please write Yes or No \n')
    view_data = view_data.title()
    index =0
    total_rows = df.shape[0]
    while True:

    # Display data if Input is Yes
        if view_data =='Yes':
            print(df[index: index + 5])
            index = index + 5
            if index > total_rows:
                index = total_rows
            view_data =input('Would you like to see 5 more data records? Please write Yes or No \n')
            view_data = view_data.title()

        elif view_data == 'No':
            return
        else:
            view_data =input('Would you like to see a glimpse of data used to compute the Bike Share Stats? Please write Yes or No \n')
            view_data = view_data.title()
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Call The functions to view Time, Station and Trip Duration Stats
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
