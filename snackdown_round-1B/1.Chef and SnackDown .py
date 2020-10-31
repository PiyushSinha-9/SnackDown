#Chef is interested in the history of SnackDown contests. He needs a program to verify if SnackDown was hosted in a given year.
#
#SnackDown was hosted by CodeChef in the following years: 2010, 2015, 2016, 2017 and 2019.

years = [2010, 2015, 2016, 2017, 2019]
for _ in range(int(input())):
    n = int(input())
    if n in years:
        print("HOSTED")
    else:
        print("NOT HOSTED")
