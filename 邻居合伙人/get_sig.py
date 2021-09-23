import time
import hashlib

def get_sign(password,phone):
    now = int(time.time())
    password = str(password).upper()
    phone = str(phone).upper()
    str1 = '{}COUNTRIES_CODE=+86&P=ANDROID&PASSWORD={}&PHONE={}&TIME={}&V=73'.format(now,password,phone,now)
    str2 = 'COUNTRIES_CODE=+86&P=ANDROID&PASSWORD={}&PHONE={}&TIME={}&V=731632299809'.format(password,phone,now)

    sig1 = hashlib.md5(str1.encode('utf8')).hexdigest()
    sig2 = hashlib.md5(str2.encode('utf8')).hexdigest()

    str3 = sig1 + sig2
    return hashlib.md5(str3.encode('utf8')).hexdigest()

print(get_sign('1234567890g','18915461235'))
