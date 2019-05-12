# Task 0

Summary:

* Big O:  O(1)
* Instructions (N): 13
* Time estimate: ~13ns

## Given

* Process 1 record from `texts` list
* Process 1 record from `calls` list

Worst cast: 1 record to process for each message.

## The Problem

1. Identify the first texts record.
2. Identify the last calls record.
3. Populate each given message with the items from the record.

## Design Explanation

The code is held in the `main()` function.  There is no need for a separate algorithm function(s) due to the simplicity
of the task.

Each message requires a single record.  As the `texts` and `calls` are lists, the code can use the following indices to
get the respective record:

* `texts[0]` gets the first record
* `calls[-1]` gets the last record

I chose to use the native `*` to unpack the items from each record.  Why? I find the implementation more readable with
less code to maintain.

Consider the following implementation:

```
first_text = texts[0]
print("First record of texts, {} texts {} at time {}".format(first_text[0], first_text[1], first_text[2]))

last_call = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call[0], last_call[1], last_call[2], last_call[3]))
```

To avoid multiple lookups for each item in the record, this implementation stores the record into a variable.  Then each item
is explicitly identified in the `.format()`.

This implementation is equivalent to my implementation, though it is more verbose.


## Time Complexity Summary

The Big O time complexity for Task 0 is O(1).

Worst case: 1 record to process for each message.

### Analysis

Let's break it down by print statement.

```
print("First record of texts, {} texts {} at time {}".format(*texts[0]))
```

O(1) | `texts[0]` is a get, which is O(1)
O(3) | get 3 items from the record, O(1) x 3 = O(3)
O(1) | .format
O(1) | print
======
O(6)

```
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*calls[-1]))
```

O(1) | `calls[-1]` is a get, which is O(1)
O(4) | get 4 items from the record, O(1) x 4 = O(4)
O(1) | .format
O(1) | print
======
O(7)

T1 = texts print
T2 = calls print

T1 = O(1) + 3 x O(1) + O(1) + O(1)
   = c1 + 3c2 + c3 + c4
   = 1 <- drop the constants

T2 = O(1) + 4 x O(1) + O(1) + O(1)
   = c1 + 4c2 + c3 + c4
   = 1 <- drop the constants

N = T1 + T2
  = O(1)

#### Time Analysis

N = O(6) + O(7)
  = O(13)

