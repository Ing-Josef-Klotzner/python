#!/usr/bin/python3

def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if __name__ == '__main__':
    year = int(input("Bitte geben Sie ein Jahr ein.\n"
                    "Es wird berechnet, ob es ein Schaltjjahr ist: "))
    print (is_leap(year))
