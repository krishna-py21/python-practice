from datetime import datetime 
def exact_age_calculator (name , dob):
    today = datetime.today ()
    delta = today-dob
    total_days = delta.days
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30
    weeks = total_days // 7
    hours = total_days * 24
    
    result = f'''👋 hello {name}!
🗓️ you were born on {dob.strftime("%d %B %Y")}
📈 your exact age is :
➡️ {years} years , {months } months , {days} days

You have lived:
🔹 {total_days} Days
🔹 {weeks} Weeks
🔹 {hours} Hours'''
    return result 
# input 

name = input ("entre your name")
dob_input = input(". entre your date of birth, (DD-MM-YYYY)")


try :
    dob = datetime.strptime(dob_input,"%d-%m-%Y")
    result = exact_age_calculator (name , dob )
    print (result )
    
except ValueError :
    print ("❌ invalid date of birth , please entrd DOB in DD-MM-YYYY format" )




