from datetime import date

def calculate_age(yearOfBirth):
    try:
        year = date.today().year
        result = year - int(yearOfBirth)
        print (f'You are {result} years old!')
    except:
        print("The input is not a valid year, please use only numbers.")
        calculate_age(input("What year where you born? "))        
    
calculate_age(input("What year where you born? "))