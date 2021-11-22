"""

A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. Social distancing guidelines require that every diner be seated such that K seats their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.

There are currently M diners seated at the table, the ith of whom is in seat Si. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.

"""


import math


def getMaxAdditionalDinersCount(num_seats, num_seats_gap, currently_seated, occupied_seats):
    # sort the seats
    occupied_seats.sort()
    extra_diner = 0

    # Handle cases to accommodate extra diner between 2 person
    i = 0
    while i < currently_seated-1:
        start = occupied_seats[i] + (num_seats_gap+1)
        end = occupied_seats[i+1] - (num_seats_gap + 1)
        extra_diner = extra_diner + get_extra_diner(start, end, num_seats_gap)
        i += 1

    extra_diner_start_case = get_extra_diner(
        1, occupied_seats[0]-(num_seats_gap+1), num_seats_gap)
    extra_diner_end_case = get_extra_diner(
        occupied_seats[-1] + num_seats_gap+1, num_seats, num_seats_gap)

    return extra_diner_start_case + extra_diner + extra_diner_end_case


def get_extra_diner(start, end, num_seats_gap):
    '''
    Diner can occupy start and end
    '''
    if end < start:
        return 0
    seats = end - start + 1

    out = int(seats / (num_seats_gap + 1))
    if seats % (num_seats_gap + 1) != 0:
        out = out + 1
    return out


if __name__ == "__main__":
    # num_seats = 15
    # num_seats_gap = 2
    # currently_seated = 3
    # occupied_seats = [11, 6, 14]

    num_seats = 10
    num_seats_gap = 1
    currently_seated = 2
    occupied_seats = [2, 6]
    print(getMaxAdditionalDinersCount(
        num_seats, num_seats_gap, currently_seated, occupied_seats))
