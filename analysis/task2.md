# Task 2

Summary:

* Big O: O(n)
* Lines (N): 116,869
* Time estimate: ~116,869ns = ~117µs = ~0.117ms = ~.000117s

## Given

* `calls` list has 2 sets of phone numbers and durations
* Records in `calls` are all from September 2016

Worst case: all phone numbers are unique.


## The Problem

Which telephone number spent the longest time on the phone during the period?
Don't forget that time spent answering a call is also time spent on the phone.

1. Analyze `calls` list, which has call duration.
2. We can ignore the `texts` list as we don't time on the phone for each text, i.e. time to type out the message or
   time to read the text when received. We could make assumptions.  But in this problem, I'm choosing to use the
   information given.

Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016.".


## Design Considerations

1. Analyze `calls` list, which has call duration.
2. Ignore the `texts` list. Why?
    - don't know the time on the phone for each text, e.g.
        - time to type out the message
        - time to read the text when received
    - I choose to use the given information and not make assumptions or guestimations.
3. It's possible to have more than one telephone number with the same longest time spent on the phone.
    - For example, this could happen when:
        - all the call records are from distinct phone numbers
        - more than record has the same call duration


## Design Explanation

The algorithm is in the function called `get_longest_time_on_phone`.  In the design of this algorithm, I had to consider
the following tasks:

1. Summing the call durations for each phone number
2. How to handle identifying the longest call durations

I included the ability to return the `call_durations` dictionary.  Why? A use case might require it for further
processing.  It also gave me a way to look inside for testing.

Given that this algorithm is specifically for the `calls` list, I'm using the global variable instead of passing it
into the function as a parameter.

### Summing Call Durations per Phone Number

The implementation for summing the call durations for each phone number is handled by:

1. Looping through the call records.
2. Looping through the 2 phone numbers in each call record.
3. Summing or adding the phone number and its duration to the dictionary


I chose this implementation for summing the duration:

```
call_durations[phone_number] = call_durations.get(phone_number, 0) + duration
```

It gets a specific value from the dictionary by the given key.  If that key doesn't exist, it returns a default of 0.
Since I'm getting a specific key from the dictionary, it's faster O(1) than checking key in dict and it's less
instructions to execute as compared to:

```
if phone_number in call_durations:
    call_durations[phone_number] += duration
else:
    call_durations[phone_number] = duration
```


### What about identifying the longest call durations?

There are many ways to implement this solution including:

1. Building a separate function that sorts the dictionary by the durations.
2. Building a separate function to search the dictionary.
3. Check the duration within the same record loops.

I chose to check the durations within the record loops as it is faster.  Why?

1. It avoids having to iterate again through the entire dictionary. Another O(n).
2. Comparison happens within the current loop and with the current record. No sort or search is needed. O(1).

## Time Complexity Summary

The Big O time complexity for Task 0 is O(n).

Worst case: all phone numbers are unique.

### Analysis

##@# `main()`

Description:    This function is the main controller for the task.  It invokes `get_longest_time_on_phone`, passing
                the `calls` list to it.  What is returned is the telephone number(s) and total time for the
                longest duration on the phone.  As it's possible to have more than one telephone number, it joins
                the set of telephone numbers and separates each with a `', '`. Then it populates the values into the
                message and prints it out.

Big O:          The Big O time complexity is O(n).


```python
def main():
    phone_numbers, total_time = get_longest_time_on_phone(calls)                                    #O(n)
    phone_number = ', '.join(phone_numbers)                                                         #O(n)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, total_time)) #O(2) format args + O(1) print
```

T1  = O(n) + O(n) + O(2) + O(1)
    = 2 x O(n) + c1 + c2
    = n <- drop the constants

N   = O(n)

### `get_longest_time_on_phone()`

Description:    This function is the algorithm.  It iterates through each telephone number in each record, i.e. there
                are 2 telephone numbers in each record.  It then adds this call's duration to the telephone number's
                total duration (i.e. tracked in the `call_durations` dictionary).  Then it compares the total time
                to the previous longest duration time.  If greater, it stores the telephone number and total time.
                If the same, it adds the telephone number to the collection of telephone numbers for this longest
                duration time.

Big O:          The Big O time complexity is O(n).

```python
def get_longest_time_on_phone(records):
    global call_durations

    phone_numbers = set()                                                                           #O(1)
    longest_duration = 0                                                                            #O(1)

    for record in records:                                                                          #O(n)
        for i in range(2):                                                                              #O(2)
            phone_number = record[i]                                                                        #O(1)
            duration = int(record[-1])                                                                      #O(2) => O(1) get + O(1) type cast to int

            # Add the duration to this phone number.
            call_durations[phone_number] = call_durations.get(phone_number, 0) + duration                   #O(2) => O(1) get + O(1) addition

            # Check if the total duration is the largest.
            if call_durations[phone_number] > longest_duration:                                             #O(2) => O(1) get + O(1) for comparison
                longest_duration = call_durations[phone_number]                                                 #O(1) get
                phone_numbers = {phone_number}                                                                  #O(1)
            elif call_durations[phone_number] == longest_duration:                                          #O(2) => O(1) get + O(1) for comparison
                phone_numbers.add(phone_number)                                                                 #O(1)

    return phone_numbers, longest_duration                                                          #O(1)
```

T1  = O(1) + O(1) + O(1) + n x ( 2 x ( O(1) + O(2) + O(2) + O(2) + O(1) + O(1) ) )
    = c1 + c2 + c3 + n x (2 x (c4 + c5 + c6 + c7 + c8 + c9))
    = c10 + n x 2c11
    = O(n) <- drop the constants

N   = O(n)


#### Number of Instructions Executed - Worst Case

##### `get_longest_time_on_phone()`

T1 = 1 + 1 + n x ( 1 + 2 x ( 1 + 1 + 2 + 2 + 2 + 1 + 1 ) )
  = 2 + n x 21
  = 2 + 21n

N = 21 x 5,312 + 2 
  = 111,552 + 2
  = 111,554

|   calls | N            | code
---------:|--------------|----------------------
|       1 | O(1)         | `phone_numbers = {}`
|       1 | O(1)         | `longest_duration = 0`
|   5,312 | O(n)         | `for record in calls:`
|  10,624 | O(2) x O(n)  |      `for i in range(2):`
|  10,624 | O(1) x O(2n) |           `phone_number = record[i]`
|  21,248 | O(2) x O(2n) |           `duration = int(record[-1])`
|  21,248 | O(2) x O(2n) |           `call_durations[phone_number] = call_durations.get(phone_number, 0) + duration`
|  21,248 | O(2) x O(2n) |           `if call_durations[phone_number] > longest_duration:`
|  10,624 | O(1) x O(2n) |               `longest_duration = call_durations[phone_number]`
|  10,624 | O(1) x O(2n) |               `phone_numbers = {phone_number}`
---------:|--------------|----------------------
| 111,554 | total        |  

##### `main()`

T1 = 1 + 1 + n x ( 1 + 2 x ( 1 + 1 + 2 + 2 + 2 + 1 + 1 ) )
  = 2 + n x 21
  = 2 + 21n

N = 21 x 5,312 + 2 
  = 111,552 + 2
  = 111,554

|   calls | N            | code
---------:|--------------|----------------------
| 111,554 | O(n)         | `phone_numbers, total_time = get_longest_time_on_phone(calls)`
|   5,312 | O(1)         | `phone_number = ', '.join(phone_numbers)`
|       3 | O(3)         | `print().format()`
---------:|--------------|----------------------
| 116,869 | total        |  

This task runs 100,691 instructions in the worst case for a execution time estimate of ~116,869ns or ~117µs.
