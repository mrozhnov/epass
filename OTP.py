from hotpie import HOTP, TOTP
from binascii import a2b_hex
from os import access, F_OK
from datetime import datetime
from hashlib import sha256

def totimestamp(dt, epoch=datetime(1970, 1, 1)):
    td = dt - epoch
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6


def get_otp():
    try:
        seed_file = open("ImportAlpine.dat", "r")
    except Exception as e:
        return "Error"
    for line in seed_file.readlines():
        if line.split(':')[0] == "sccTokenData":
            key_line = line.split(';')[0]
            key = a2b_hex(key_line.split('=')[1])
            sync_line = line.split(';')[1]
            sync = sync_line.split('=')[1]
            break
    seed_file.close()

    if sync == 'E':
        counter = 0
        if not access("Counter.dat", F_OK):
            try:
                counter_file = open("Counter.dat", "w")
                counter_file.write("0")
                counter_file.close()
            except Exception as e:
                return "Error"
        try:
            counter_file = open("Counter.dat", "r+")
            counter = int(counter_file.readline())
            counter_file.seek(0)
            counter_file.write(str(counter + 1))
        except Exception as e:
            return "Error"
        return HOTP(key, counter)
    elif sync == 'T':
        start_time = 946684800
        current_time = totimestamp(datetime.utcnow())
        key = a2b_hex('1080da3c61a1bb7a7cca278e2a9ef73431d8c926a4d36a0d25b69f6d88e6f997')
        return TOTP(key, digits=6, window=30, clock=current_time - start_time, digestmod=sha256)
    else:

        return 'Error'
