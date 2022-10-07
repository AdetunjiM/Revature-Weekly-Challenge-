from datetime import datetime

def has_friday_13(month,year):
    
    dt= datetime(year,month,13)
    day = dt.strftime('%A')
    if day == "Friday":
        response = True
    else:
        response = False
        
    return response

print(has_friday_13(3, 2020) )


print(has_friday_13(10, 2017) )


print(has_friday_13(1, 1985) )