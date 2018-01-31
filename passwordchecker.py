import re
from sys import exit


# Checking the input using regex
def validNum(passw):
    return bool(re.search('\d', passw))

def validStr(passw):
    return bool(re.search('[a-z]', passw))

def validSTR(passw):
    return bool(re.search('[A-Z]', passw))

def main():
    passw = input('Password: ')
    if len(passw) > 7 and validNum(passw) == True and validSTR(passw) == True and validStr(passw) == True:
        print('Good password')
        exit()
    else:
        print('Bad password')
        main()

if __name__ == "__main__":
    main()