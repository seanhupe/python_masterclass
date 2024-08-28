# 1
def dollarizer(word):
    return word.replace('s', "$")


# Example usage
word = "success"
result = dollarizer(word)
print(result)  # Output: $ucce$$


# 2-----------------------------------------------------------------
def eurizer(word2):
    return word2.replace('e', "€")


# Example Usage
word2 = "elevator"
result2 = eurizer(word2)
print(result2)  # Output: €l€vator


#-----------------------------------------------------------------
def replacer(word3, char1, char2):
    return word3.replace(char1, char2)


word3 = "elevators"

result = replacer(word, 'e', "€")
print(result)

result = replacer(word, "s", "$")
print(result)


#-----------------------------------------------------------------
def replacer(word3, char1, char2):
    return word3.replace(char1, char2)


def wonky_text(word3):
    word3 = replacer(word3, 's', '$')
    word3 = replacer(word3, 'e', '€')
    word3 = replacer(word3, 'l', '£')
    return word3


word3 = 'elevators'
result = wonky_text(word3)
print(result)


#-----------------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}C is equal to {fahrenheit_temp}F")


#-----------------------------------------------------------------
def age_in_days(age_in_years):
    days = age_in_years * 365
    return days


age_in_years = 25
age_days_result = age_in_days(age_in_years)
print(f"{age_in_years} years is equal to {age_days_result} days")


#-----------------------------------------------------------------
def simple_interest(principal, rate, time):
    interest_calc = (principal * rate * time)
    return interest_calc

principal = 1000
rate = .05
time_in_years = 3

interest = simple_interest(principal, rate, time_in_years)
print(f"The simple interest is {interest}")

#-----------------------------------------------------------------

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
