from hotpie import HOTP
from binascii import a2b_hex
from os import access, F_OK

def get_hotp():
    try:
        seed_file = open("ImportAlpine.dat", "r")
    except Exception as e:
        return "Error"
    counter = 0
    for line in seed_file.readlines():
        if line.split(':')[0] == "sccTokenData":
            line = line.split(';')[0]
            key = a2b_hex(line.split('=')[1])
            break
    seed_file.close()
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

