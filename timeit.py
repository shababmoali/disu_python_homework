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

import asyncio
import aiofiles

async def read_async():
    start_time = time.time()
    asnc = ""
    for _ in range(1000):
        async with aiofiles.open('t8_shakespeare.txt') as f:
            asnc += await f.read()
    end_time = time.time()
    print(f"ASync Execution time: {end_time - start_time} seconds")


def read_sync():
    start_time = time.time()
    snc = ""
    for _ in range(1000):
        with open('t8_shakespeare.txt') as f:
            snc += f.read()
    end_time = time.time()
    print(f"Sync Execution time: {end_time - start_time} seconds")


async def main():
    await read_async()
    read_sync()

# Run the async main function
asyncio.run(main())
print('end script')