import time
import pandas as pd
import numpy as np


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        None.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''

    city = input("""\nHello! Let\'s explore some US bikeshare data!\n
                         __o
                        _\ <,
                      (_)/ (_) \n """
                    '\nWould you like to see data for Chicago, New York, or Washington?\n').title()
    if city == 'Chicago' or city == 'C':
        return 'chicago.csv'
    elif city == 'New York' or city == 'N':
        return 'new_york_city.csv'
    elif city == 'Washington' or city == 'W':
        return 'washington.csv'
    else:
        print("\nI'm sorry, I'm not sure which city you're referring to. Let's try again.")
        return get_city()

    print('-'*40)


def check_info(city,filter,month,day):
    '''Asks the user if the filtering information is correct.
    Args:
        (str) A string with the name of a city
        (str) A string with the type of filter applied
        (int) An int with the month in the filter
        (int) An int with the day in the filter
    Returns:
        (bool) Boolean showing with True if decision was correct and False if decision was wrong.
    '''

    check = input('\nThis is the filtering information I have:\n'
                    '   The city you are interested in is: {}\n'
                    '   The time filtering you want is: {}\n'
                    '     Day(s): {}\n'
                    '     Month(s): {}\n'
                    'Is this information correct? (Yes/No)\n'.format(city[:-4].replace('_', ' ').title(),filter.title(), convert_day(day).title(), convert_month(month).title())
                    ).lower()
    if check == 'yes' or check == 'y':
        return True
    elif check == 'no' or check == 'n':
        print('\nLet\'s try again\n')
        return False
    else:
        print('\nThis is not a valid answer. Please answer only yes or no\n')


def get_time():
    '''Asks the user if they want to filter by day, month, both or none and returns a string with filter.
    Args:
        None.
    Returns:
        (list) List containing one string and two integers: the filter, the day (if any) and the month(if any).
    '''

    time = input('\nWould you like to filter the data by month, day, both or not at all? Type "none" or "n" for no time filter\n').lower()
    if time == 'day' or time == 'd':
        return ['day', get_day(), 99]
    elif time == 'month' or time == 'm':
        return ['month', 99, get_month()]
    elif time == 'both' or time == 'b':
        return ['both', get_day(), get_month()]
    elif time == 'none' or time == 'n':
        return ['none', 99, 99]
    else:
        print("\nI'm sorry, I'm not sure I understand what you want to filter by. Let's try again.")
        return get_time()

    print('-'*40)


def get_month():
    '''Asks the user for a month and returns the month.
    Args:
        None.
    Returns:
        (int) An integer representing the number of the month
    '''

    month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
    if month == 'January':
        return 1
    elif month == 'February':
        return 2
    elif month == 'March':
        return 3
    elif month == 'April':
        return 4
    elif month == 'May':
        return 5
    elif month == 'June':
        return 6
    else:
        print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")
        return get_month()

    print('-'*40)


def convert_month(month):
    '''Converts month number to month name.
    Args:
        (int) Integer with the number of the month.
    Returns:
        (str) String with the name of the month
    '''

    if month == 99:
        return 'all'
    elif month == 1:
        return 'january'
    elif month == 2:
        return 'february'
    elif month == 3:
        return 'march'
    elif month == 4:
        return 'april'
    elif month == 5:
        return 'may'
    elif month == 6:
        return 'june'
    else:
        print('\n Invalid month argument. Try again.\n')


def get_day():
    '''Asks the user for a day of the week and returns the specified day.
    Args:
        none.
    Returns:
        (int) An integer representing the day of the week, where Monday is 0 and Sunday is 6
    '''

    day_of_week = input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
    if day_of_week == 'Monday':
        return 0
    elif day_of_week == 'Tuesday':
        return 1
    elif day_of_week == 'Wednesday':
        return 2
    elif day_of_week == 'Thursday':
        return 3
    elif day_of_week == 'Friday':
        return 4
    elif day_of_week == 'Saturday':
        return 5
    elif day_of_week == 'Sunday':
        return 6
    else:
        print("\nI'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")
        return get_day()

    print('-'*40)


def convert_day(day):
    '''Converts month number to month name
    Args:
        (int) Integer with the number of the month.
    Returns:
        (str) String with the name of the month
    '''

    if day == 99:
        return 'all'
    elif day == 0:
        return 'monday'
    elif day == 1:
        return 'tuesday'
    elif day == 2:
        return 'wednesday'
    elif day == 3:
        return 'thursday'
    elif day == 4:
        return 'friday'
    elif day == 5:
        return 'saturday'
    elif day == 6:
        return 'sunday'
    else:
        print('\n Invalid month argument. Try again.\n')


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

    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (dataframe) A dataframe with the filtered information.
    Returns:
        (str) A string with the name of the most common month.
        (str) A string with the name of the most common day of the week.
        (int) An integer with the most common hour.
    """
    print('-'*40)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].value_counts().idxmax()
    print("Most common month: {}".format(convert_month(common_month).title()))

    common_day = df['day_of_week'].value_counts().idxmax()
    print("Most common day of the week: {}".format(common_day))

    common_start_hour = df['hour'].value_counts().idxmax()
    print("Most common hour: {}".format(common_start_hour))

    print("\nThis took %s seconds." % ("%.4f" % (time.time() - start_time)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        (dataframe) A dataframe with the filtered information.
    Returns:
        (str) A string with the name of the most commonly used start station.
        (str) A string with the name of the most commonly used end station.
        (str) A string with the most common combination of start and end station trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most common start station: {}".format(common_start_station))

    common_end_station = df['End Station'].value_counts().idxmax()
    print("Most common end station: {}".format(common_end_station))

    # NEED TO REVIEW THIS
    trips = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    trips_ordered = trips.sort_values(ascending=False)
    print('Most common trip: from {} to {}.'.format(trips_ordered.index[0][0],trips_ordered.index[0][1]))

    print('\nThis took %s seconds.' % ("%.4f" % (time.time() - start_time)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (dataframe) A dataframe with the filtered information.
    Returns:
        (int) An integer with the total travel time.
        (int) An integer with the avegrage travel time.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds'.format(total_travel_time))

    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time: {} seconds'.format("%.2f" % average_travel_time))

    print('\nThis took %s seconds.' % ("%.4f" % (time.time() - start_time)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

    Args:
        (dataframe) A dataframe with the filtered information.
    Returns:
        (int) An integer with the total count of user types.
        (int) An integer with the total count of user genders.
        (int) An integer with the earliest year of birth.
        (int) An integer with the most recent year of birth.
        (int) An integer with the most common year of birth.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_count = df['User Type'].value_counts()
    print('Breakdown of counts by user types:\n', user_type_count.to_string())

    try:
        user_gender_count = df['Gender'].value_counts()
        print('\nBreakdown of counts by gender:\n', user_gender_count.to_string())
    except:
        print('Uh oh! No information on the user\'s gender available!')

    try:
        earliest_yob = df['Birth Year'].min()
        print('\nEarliest year of birth: {}'.format("%.0f" % earliest_yob))
        recent_yob = df['Birth Year'].max()
        print('Most recent year of birth: {}'.format("%.0f" % recent_yob))
        common_yob = df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth: {}'.format("%.0f" % common_yob))
    except:
        print('Uh oh! No information on the user\'s birth year available!')

    print("This took %s seconds." % ("%.4f" % (time.time() - start_time)))
    print('-'*40)

def raw_data(df):
    """Displays raw statistics on bikeshare users.

    Args:
        (dataframe) A dataframe with the filtered information.
    Returns:
        (list) A list of user information as displayed in the dataframe.
    """
    raw = input('\nWould you like to check out some raw data? Please type yes or no.\n').lower()
    if raw == 'yes' or raw == 'y':
        return True
    elif raw == 'no' or raw == 'n':
        print('\nOk, no problem!')
        return False
    else:
        print('\nThis is not a valid answer. Please answer only yes or no.\n')
        return raw_data()


def main():
    while True:
        city = get_city()
        filter, day, month = get_time()
        check = check_info(city,filter,month,day)

        while check is False:
            city = get_city()
            filter, day, month = get_time()
            check = check_info(city,filter,month,day)

        df = load_data(city, convert_month(month), convert_day(day))
        df.head(5)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more = raw_data(df)
        row = 0

        while more is True:
            print(df[row: row + 5])
            row = row + 5
            more = raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
