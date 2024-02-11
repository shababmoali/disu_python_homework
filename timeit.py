"""
Pick an I/O operation
E.g. reading the contents of a file
Figure out how to do that operation in non-async and async
For non-async, that's regular old open('myfile').read() or whatever
For async, PYTHON DOESN'T EVEN HAVE A BUILT-IN WAY TO READ A FILE WITH ASYNC. THAT'S HOW DUMB IT IS TRYING TO DO THINGS WITH ASYNC.
Anyway you can google "read a file python async" or whatever, looks like there's an aiofile library
Write two tiny Python programs, one which does the thing non-async style, the other which does the thing async style
Figure out how to run the two programs a bunch of times, and keep track of the time
You could do this in Python itself, with a for loop, and t0 = time(); ...do stuff...; t1 = time(); print(t1 - t0) or whatever
"""

import time
import logging

import asyncio
import aiofiles

from collections import defaultdict
from typing import DefaultDict

log = logging.getLogger(__name__)

"""
Anyway, I would therefore suggest the following steps for this homework (most are very quick):
[EASY] Get your code to report average time, not total time
[EASY] Increase the number in your loop from 1000 to 100000 and see if the numbers stabilize at all
[EASY] Try using different timers (perf_counter, process_time, thread_time, etc) and see if they change the results!
BONUS: try using different file sizes with different timers! The size of the file should cause "wall time" (e.g. time.time, time.perf_counter) to increase, but shouldn't affect "user time" (e.g. process_time, thread_time).
[MEDIUM] Add an outer loop! So like, for _ in range(5). And each time through the inner loop, calculate its average time, append that to a list of results, and then after the outer loop is done, print(f"Lowest average time was: {min(results)}")
[BIT HARDER] Figure out how to read from multiple files concurrently! The non-async code can use threads, async code can use asyncio.gather!
"""

NUM_EVENTS = 5
SAMPLING_EVENTS = range(NUM_EVENTS)
IO_ITERATIONS_SERIES = [0, 10, 100, 1000, 10000]


def pretty_print_result(header, runtime_table):
    """print aggregated contents of runtime mappings"""
    io_iterations_times_sums = defaultdict(int)
    for event in SAMPLING_EVENTS:
        for io_iter in IO_ITERATIONS_SERIES:
            io_iterations_times_sums[io_iter] = io_iterations_times_sums[io_iter] + runtime_table[event][io_iter]

    io_iterations_times_averages = defaultdict(int)
    for io_iter in IO_ITERATIONS_SERIES:
        io_iterations_times_averages[io_iter] = io_iterations_times_sums[io_iter] / NUM_EVENTS

    log.debug("summary:", dict(runtime_table))
    log.debug(io_iterations_times_sums)

    print(header)
    print(f"{'Iterations':<12}: Average Time (_milli_seconds)")
    for io_iter in IO_ITERATIONS_SERIES:
        print(f"{io_iter:<12}: {io_iterations_times_averages[io_iter]*10**-6:.2f}")


async def read_async() -> DefaultDict[int, DefaultDict[int, int]]:
    result = defaultdict(defaultdict)
    for event in SAMPLING_EVENTS:
        for iters in IO_ITERATIONS_SERIES:
            start_time = time.perf_counter_ns()
            for _ in range(iters):
                async with aiofiles.open('t8_shakespeare.txt') as f:
                    await f.read()
            end_time = time.perf_counter_ns()
            result[event][iters] = end_time - start_time
    pretty_print_result(
        "ASync --",
        result
    )

    return result


def read_sync() -> DefaultDict[int, DefaultDict[int, int]]:
    result = defaultdict(defaultdict)
    for event in SAMPLING_EVENTS:
        for iters in IO_ITERATIONS_SERIES:
            start_time = time.perf_counter_ns()
            for _ in range(iters):
                with open('t8_shakespeare.txt') as f:
                    f.read()
            end_time = time.perf_counter_ns()
            result[event][iters] = end_time - start_time
    pretty_print_result(
        "Sync -- ",
        result
    )

    return result


# Run the async main function
asyncio.run(
    read_async()
)

# Run sync
read_sync()
