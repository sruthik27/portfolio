import requests
import hashlib

def api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'{response.status_code} doesn\'t exist, check the api')
    return response

def get_leaks(hash,hashes_to_check):
    hash = hash.text.splitlines()
    hash = (x.split(':') for x in hash)
    for h,count in hash:
        if h == hashes_to_check:
            return count
    return 0

def saw_input(password):
    p = password.encode('utf-8')
    sawpass = hashlib.sha1(p).hexdigest().upper()
    first5,rest = sawpass[:5],sawpass[5:]
    res = api_data(first5)
    return get_leaks(res,rest)

def check(arg):
    count = saw_input(arg)
    if count:
        return f'{arg} was found {count} times... you should probably change your password!'
    else:
        return f'{arg} was NOT found. Carry on!'
# def check(args):
#   for ppassword in args:
#     count = saw_input(ppassword)
#     if count:
#       return f'{ppassword} was found {count} times... you should probably change your password!'
#     else:
#       return f'{ppassword} was NOT found. Carry on!'


if __name__ == "__main__":
    b = input('Enter the password to be checked if exists')
    print(check(b))