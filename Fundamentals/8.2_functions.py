# 1. Create a function called 'dollarizer' that takes a word and replaces every s with a $
def dollarizer(word):
    return word.replace('s', "$")


# Example usage
word = "success"
result = dollarizer(word)
print(result)  # Output: $ucce$$

# 2.-----------------------------------------------------------------
"""Create a function called 'eurizer' that takes a word and replaces every 3 with a euro sign"""


def eurizer(word2):
    return word2.replace('e', "€")


# Example Usage
word2 = "elevator"
result2 = eurizer(word2)
print(result2)  # Output: €l€vator

# 3.-----------------------------------------------------------------
"""Combine dollarizer and eurizer functions into one, more general function called 'replacer' that takes a word
and 2 characters as input and replaces every occurrence of character 1 with character 2"""


def replacer(word3, char1, char2):
    return word3.replace(char1, char2)


word3 = "essential"

result = replacer(word3, 'e', "€")
print(result)  # €ss€ntial

result = replacer(word3, "s", "$")
print(result)  # e$$ential

# 4.-----------------------------------------------------------------
"""Create a function 'wonky_text' that replaces every s with the $ sign, every e with the euro sign, and 
every l with £ """


def replacer(word3, char1, char2):
    return word3.replace(char1, char2)


def wonky_text(word3):
    word3 = replacer(word3, 's', '$')
    word3 = replacer(word3, 'e', '€')
    word3 = replacer(word3, 'l', '£')
    return word3


word3 = 'elevators'
result = wonky_text(word3)
print(result)  # €£€vator$

word3 = 'sales'
result = wonky_text(word3)
print(result)  # $a£€$

# 5. -----------------------------------------------------------------
"""Create a function named 'celsius_to_farenheit that takes a temperature in Celsius and
returns its equivalent in Fahrenheit.  Use the forumula: F=C * 9/5 + 32"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}C is equal to {fahrenheit_temp}F")  # 25C is equal to 77.0F

#6.-----------------------------------------------------------------
"""Create a function named 'age_in_days that takes an age in years (assume whole years only) and
returns the age in days. Assume each year has 365 days"""


def age_in_days(age_in_years):
    days = age_in_years * 365
    return days


age_in_years = 49
age_in_days_result = age_in_days(age_in_years)
print(f"{age_in_years} years is equal to {age_in_days_result} days")

#7.-----------------------------------------------------------------
"""Create a function named 'simple_interest' that calculates simple interest. It should take three arguments:'
principal amount, rate of interest, and time in years. Use the formula: (SI = P*R*T). Return the calculated SI"""


def simple_interest(principal, rate, time):
    interest_calc = (principal * rate * time)
    return interest_calc


principal = 1000
rate = .05
time_in_years = 3

interest = simple_interest(principal, rate, time_in_years)
print(f"The simple interest is {interest}")

#8.-----------------------------------------------------------------
"""Write a function named 'plan_finances' that takes a principal amount, rate of interest, time in years, and
a desired final amount after simple interest. The function should return whether the final amount after simple
interest is achieved from the principal within the given time and rate"""


def simple_interest(principal, rate, time):
    si = (principal * rate * time)
    return si


def plan_finances(prinicpal, rate, time, desired):
    interest = simple_interest(principal, rate, time)
    final_amount = principal + interest
    return final_amount >= desired


principal_amount = 1
rate_of_interest = .05
time_in_years = 1
desired = 1150

result = plan_finances(principal_amount, rate, time_in_years, desired)
if result:
    print("Desired final amount is achievable")
else:
    print("Desired final amount is NOT achievable")
