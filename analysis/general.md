# Project Assumptions

Assumptions for all tasks:

* Processor: 1b instructions per second = 1ns/instruction

# Design Concepts

* When a centralized container is needed to hold the work, I'll use a global variable to conserve memory
  and processing.
* Algorithm will be a separate function, when appropriate.
* Calls to algorithm(s) done from a `main()` function.
* Each task will include a test suite comprised of assertions. To run, uncommenting at the bottom of the task.
* Final task will run `main()` only.

# Time Complexity Resources

The following documents were used for the time complexity analyzes:

* Python - [TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
* [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
