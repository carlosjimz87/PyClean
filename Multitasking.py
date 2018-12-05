#!/usr/bin/env python
#
# Created by carlosjimz on 24/11/2018 11:15
#
##############################################################

import multiprocessing
import collections
from pprint import pprint
import time
import os

Scientist = collections.namedtuple("Scientist", [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1851, nobel=False),
)


def transform(x):
    pprint(f"Process {os.getpid()} working record {x.name}")
    time.sleep(1)
    result = {'name': x.name, 'age': 2017-x.born}
    return result


if __name__ == '__main__':
    pprint(scientists)
    pprint("*********************************************************")

    start = time.time()

    with multiprocessing.Pool(len(scientists)) as pool:
        result = pool.map(transform, scientists)

    end = time.time()
    pprint(result)
    pprint(f'Time to complete: {end-start:.2f} seconds')
