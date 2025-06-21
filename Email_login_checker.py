# DEFINE CORRECT EMAIL AND PASSWORD

correct_email  = "krishna@example.com"
correct_password  = "krishna154"

# INPUT TAKE FROM USER

email = input ("entre your email:")
password = input ("entre your password:")

# FUNCTION TO CHECK LOGIN

def login_check (email , password):
    if email == correct_email and password == correct_password:
        
        print ("✅ login successful , welcome",email )
    else :
        
        print ("❌ invalid or password, try again")

# CALLED THE FUNCTION
login_check (email, password )
