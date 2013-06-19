# coding=utf-8
"""Print/Get nose stopwatch times"""
import sys


FILENAME = '.nose-stopwatch-times'


def get_times(threshold=0.0):
    with open(FILENAME, 'r') as time_file:
        info = time_file.readlines()[1:]

    for pos in xrange(0, len(info) - 1, 3):
        name_info = info[pos][3:-2].strip('()')
        time_info = float(info[pos+2][1:])
        if time_info >= threshold:
            yield (name_info, time_info)


def print_times(threshold=0.0):
    for name, time in get_times(threshold):
        print '%s: %.6f' % (name, time)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        threshold = 0.0
    elif len(sys.argv) == 2:
        threshold = float(sys.argv[1])
    else:
       print 'Usage: %s [threshold_time_as_float]'
       sys.exit(1)

    print_times(threshold)
