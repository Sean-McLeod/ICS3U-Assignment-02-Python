#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program can calculate the area of a trapezoid with
#    dimensions entered by users


def main():
    # This function calculates the area of a trapezoid

    # input
    lower_base = int(input("Enter the lowerbase of the trapezoid (cm):"))
    upper_base = int(input("Enter the upperbase of the trapezoid (cm):"))
    height = int(input("Enter the height of the trapezoid (cm):"))

    # process
    area = ((lower_base + upper_base)/2) * height

    # output
    print("")
    print("The area of the trapezoid is {}cm²".format(area))


if __name__ == "__main__":
    main()
