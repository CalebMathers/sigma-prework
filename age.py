from datetime import datetime

# get the starting date from the user
def get_user_date():
    user_date = (input("Please enter a date in the format of DD-MM-YYYY: "))
    # convert the input string to datetime with the given format
    user_date = datetime.strptime(user_date, "%d-%m-%Y")
    return user_date

# get the current datetime
def get_current_date():
    current_date = datetime.now()
    return current_date

# calculate and return the age
def calculate_age():
    user_date = get_user_date()
    current_date = get_current_date()
    # take user datetime away from current datetime
    difference = (current_date - user_date)
    # divide the difference in days by 365 to give years
    age = (difference.days // 365)
    print(age)
    return age

calculate_age()