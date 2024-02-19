#!/usr/bin/env python3
import secrets, random, sys
def main():
    maxdigits=999999999
    sys.set_int_max_str_digits(maxdigits=maxdigits)
    while True:
        upper_limit = input("Input security score:")
        print(f"Normal passwd:{str(secrets.randbits(random.randint(a=0, b=int(upper_limit)))) + hex(secrets.randbits(random.randint(a=0, b=int(upper_limit))))}")
        print(f"Great passwd:{secrets.randbits(int(upper_limit))}")
if __name__ == '__main__':
    main()