# on start: import libraries
import hashlib
import datetime
import sys

# on startup, read hash from file
with open("password.txt", "r") as f:
    hashedAdminPassword = f.read().strip()

def main():
    global hashedAdminPassword
    attempt_count = 0
    while True:
        method = input("fingerprint / password / resetpassword: ")
        if method == "fingerprint":
            fingerCheck = verify_fingerprint()
            if fingerCheck == True:
                attempt_count += 1
                # add code here later to make the door unlock
                log_attempt(method, "success", attempt_count)
                attempt_count = 0
                break
            else:
                attempt_count += 1
                log_attempt(method, "failed", attempt_count)
                if attempt_count >= 3:
                    attempt_count = 0
                    sys.exit("too many failed attempts, you have been locked out.")

        # if password option selected, call check_password()
        elif method == "password":
            passwordattempt = input("Input password: ")
            passCheck = check_password(passwordattempt)
            if passCheck == True:
                # open the door
                # write a log
                attempt_count += 1
                log_attempt(method, "success", attempt_count)
                attempt_count = 0
                break
            else:
                attempt_count += 1
                log_attempt(method, "failed", attempt_count)
                # hard mode: lock the password after x attempts, can only be unlocked by master/sudo (aka me) -- store attempt_count as a variable or csv, which resets upon successful unlocking of the door
                if attempt_count >= 3:
                    attempt_count = 0
                    sys.exit("too many failed attempts. you have been locked out.")
        # if mum or dad forgot the password and wants to reset it, press 'reset password'
        elif method == "resetpassword":
            # this prompts them to use fingerprint or password to verify (calling the above 2 functs again)
            authCheck = verify_fingerprint() or check_password(input("Verify identity: "))
            if authCheck == False:
                print("Identity verification failed!")
                attempt_count += 1
                log_attempt(method, "failed", attempt_count)
                if attempt_count >= 3:
                    attempt_count = 0
                    sys.exit("too many failed attempts. you have been locked out.")
                continue
            # after which, prompt user to input new password
            newpassword = input("Input new password: ")
            # call assess_password_strength()
            strengthCheck = assess_password_strength(newpassword)
            if strengthCheck == True:
                newHashedPassword = hashlib.sha256(newpassword.encode()).hexdigest()
                # if return value is True, accept the new password & set variable admin_password to this new password
                # on password reset, write new hash to file
                with open("password.txt", "w") as f:
                    f.write(newHashedPassword)
                hashedAdminPassword = newHashedPassword
                attempt_count += 1
                log_attempt(method, "success", attempt_count)
                print("password reset successful!")
                attempt_count = 0
                continue
            else:
                print("password too weak, try again")
                continue
        else:
            print("invalid option, please try again")
    # log everything lol, write it to a csv (append, use "a")
    # since rzpi 3 has wifi support, i can access it remotely from my device! hehehe

def log_attempt(method, outcome, attempt_count):
    with open("log.csv", "a") as g:
        g.write(f"{datetime.datetime.now()},{method},{outcome},attempt {attempt_count}\n")

def verify_fingerprint():
    # mock for testing - replace with actual sensor code later
    # get input of fingerprint from sensor
    simulation = input("Simulating fingerprint scan... Enter 'match' or 'nomatch': ")
    # compare input & approved fingerprints
    # if match, return True
    if simulation == "match":
        return True
    else:
        # if no match, return False
        return False

def check_password(passinput):
# HASH the input
    hashedInput = hashlib.sha256(passinput.encode()).hexdigest()
    if hashedInput == hashedAdminPassword:
        return True
    else:
        return False
# compare HASHED passinput with admin password
# if match, return True
# if mismatch, return False

def assess_password_strength(p):
    if p.isalnum():
        pass
    else:
        return False
# if only numbers, fail the check
# if only letters, fail the check
    if p.isalpha():
        return False
    else:
        pass
    if p.isnumeric():
        return False
    else:
        pass
# if only lowercase and numbers, fail the check
# if uppercase, lowercase and numbers, continue
    if p.lower() == p:
        return False
    elif p.upper() == p:
        return False
    else:
        pass
# if length < 5, fail the check
# if length > 16, fail the check
    if len(p) < 5 or len(p) > 20:
        return False
    else:
        pass
# if contain "abc" or "123" or "password" or "admin" (case insensitive), fail the check
    if ("abc" in p.lower()) or ("123" in p) or ("admin" in p.lower()) or ("password" in p.lower()):
        return False
    else:
        pass
# if hasnt failed the check yet so far, pass the check
    return True

if __name__ == "__main__":
    main()