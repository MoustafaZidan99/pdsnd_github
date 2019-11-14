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
    print('Hi! would you like to explore some US bikeshare data?!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago","new york city","washington"]
    city = input("please write the name of the city to analyze : ")
    while city not in cities:
         city = input("please write a valid name (chicago, new york city, washington):")
    # TO DO: get user input for month (all, january, february, ... , june)
    month_filter = ["all","january","february","march","april","may","june","juily","august","september","october","november","december"]
    month = input("please name of the month to filter by, or all to apply no month filter : ").lower()
    while month not in month_filter:
         month = input("please enter a valid option : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_filter = ["all","saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
    day = input("please name of the day to filter by, or all to apply no day filter : ").lower()
    while day not in day_filter:
         day = input("please enter a valid option : ").lower()

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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_name"] = df["Start Time"].dt.weekday_name

    month_filter, day_filter = "no", "no"

    if month != "all":
        index_of_monthes = ["january","february","march","april","may","june","juily","august","september","october","november","december"]
        month = index_of_monthes.index(month) + 1
        df = df[df["month"] == month]
        month_filter = "yes"
    if day != "all":
        df = df[df["day_name"] == day.title()]
        day_filter = "yes"
    return df ,month_filter, day_filter


def time_stats(df,month_filter,day_filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month_filter == "no":
        month_mode = df["month"].mode()[0]
        print("the most common month is {}".format(month_mode))
    else:
        print("your are displaying a specific month:")

    # TO DO: display the most common day of week
    if day_filter == "no":
        day_mode = df["day_name"].mode()[0]
        print("the most common day of the week is {}".format(day_mode))
    else:
        print("your are displaying a specific day:")

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    hour_mode = df["hour"].mode()[0]
    print("the most common start hour is {}".format(hour_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("most commonly used start station is",common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("most commonly used start station is",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["common_combination"] = df["End Station"] + " - " + df["Start Station"]
    most_common = df["common_combination"].mode()[0]
    print("most commonly combination stations is",most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    print("the total travel time is:",total_time)

    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("the mean travel time is:",mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df["User Type"].value_counts()
    print("counts of user types :",count_user_type, sep = "\n")

    # TO DO: Display counts of gender
    count_user_gender = df["Gender"].value_counts()
    print("ccounts of gender :",count_user_gender, sep = "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    early_dob = df["Birth Year"].min()
    print("the earliest year of birth is :",early_dob)

    recent_dob = df["Birth Year"].max()
    print("the most recent year of birth is :",recent_dob)

    common_dob = df["Birth Year"].mode()[0]
    print("the most common year of birth is :",common_dob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df, month_filter, day_filter = load_data(city, month, day)

        time_stats(df,month_filter,day_filter)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
