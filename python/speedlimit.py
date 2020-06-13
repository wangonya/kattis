#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://open.kattis.com/problems/speedlimit
import sys

distances = []


def speedlimit(compiled_records):
    time_already_spent = 0
    distance = 0
    for record in compiled_records:
        speed, time = record.split()
        time = int(time) - time_already_spent
        distance += int(speed) * time
        time_already_spent += time
    distances.append(distance)


if __name__ == '__main__':
    for _ in range(0, 10):
        number_of_records = int(sys.stdin.readline())
        if number_of_records == -1:
            for distance in distances:
                print(f'{distance} miles')
            break
        compiled_records = []
        for record in range(0, number_of_records):
            record = sys.stdin.readline().strip('\n')
            compiled_records.append(record)

        speedlimit(compiled_records)
