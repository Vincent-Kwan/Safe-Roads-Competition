from math import trunc

def truncate(number, digits = 3) -> float:
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper

# agec doesn't make total sense
def agec(x):
    if x in ('0 to 4', '5 to 9', '10 to 14'):
        return 'Children'
    if x in ('15 to 19', '20 to 24'):
        return 'Young Adult'
    if x in ('25 to 29', '30 to 34', '35 to 39', '40 to 44', '45 to 49', '50 to 54', '55 to 59'):
        return 'Adult'
    if x in ('60 to 64', '65 to 69', '70 to 74'):
        return 'Senior'
    if x != 'Other':
        return 'Super Senior'
    return x

def lc(x):
    if x in ('Dawn, artificial', 'Dusk, artificial', 'Dark, artificial', 'Daylight, artificial'):
        return 'Artificial'
    return x

def tc(x):
    if x in ('Traffic Controller', 'Police Control'):
        return 'Controller present'
    if x in ('Stop Sign', 'Yield Sign'):
        return 'Stop/Yield Sign'
    return x

def actc(x):
    if x in ('Speed Too Fast For Condition', 'Exceeding Speed Limit'):
        return 'Speeding'
    return x

def condc(x):
    if x in ('Ability Impaired, Alcohol', 'Ability Impaired, Alcohol Over .08', 'Had Been Drinking', 'Ability Impaired, Drugs'):
        return 'Ability Impaired (Drugs/Alcohol)'
    return x

def vehc(x):
    if x in ('Motorcycle', 'Off Road - 2 Wheels'):
        return 'Two Wheeler'
    if x in ('Automobile, Station Wagon', 'Taxi', 'Passenger Van', 'Police Vehicle'):
        return 'Small-size Vehicle'
    if x in ('Truck - Open', 'Delivery Van', 'Pick Up Truck', 'Truck - Tractor', 'Truck - Closed'):
        return 'Medium-size Vehicle'
    if x != 'Other':
        return 'Large-size Vehicle'
    return x

def daygroup(hour):
    if hour >= 6 and hour < 10:
        return "Morning"
    elif hour >= 10 and hour < 12:
        return "Day"
    elif hour >= 12 and hour < 14:
        return "Lunch"
    elif hour >= 14 and hour < 16:
        return "Afternoon"
    elif hour >= 16 and hour < 18:
        return "Evening"
    elif hour >= 18 and hour < 22:
        return "Late Evening"
    else:
        return "Night"
    
def seasons(month):
    if month in ('March', 'April', 'May'):
        return 'Spring'
    if month in ('June', 'July', 'August'):
        return 'Summer'
    if month in ('September', 'October', 'November'):
        return 'Fall'
    if month in ('December', 'January', 'February'):
        return 'Winter'