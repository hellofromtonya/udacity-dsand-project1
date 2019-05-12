# Task 1

Summary:

* Big O:  O(n)
* Lines (N): 100,691
* Time estimate: ~100,691ns = ~100µs = ~0.100ms = ~.000100s

## Given

* len(texts) = 9072
* len(calls) = 5312
* Total records = 14,384
* Each list has 2 sublists of phone numbers, i.e. calling from + calling to
* Total phone numbers: 28,768

Worst case: all phone numbers are unique.

## Design Explanation

All of the distinct phone numbers are held in a global variable called `distinct_phone_numbers`.  I chose a set data
type for this container.  I'll explain why below.

The algorithm is in the function called `get_distinct_phone_numbers`.  In the design of this algorithm, I had to
consider the challenges associated with extracting all of the phone numbers from both lists (i.e. `texts` and `calls`).
What do I mean?  Here are the challenges:

1. Each list holds sublists for each record.
2. There are 2 phone numbers in each record of each list:
    - "Calling from" phone number is at index 0.
    - "Calling to" phone number is at index 1.

Given that there are 2 columns of phone numbers, I chose to iterate through each record and then add each phone
number (index 0 and 1) to the `distinct_phone_numbers` set, thereby allowing the `set` to handle excluding duplicates
and adding only distinct strings into the collection.

### Why I Chose a Set Data Type

As I noted above, I chose a set data structure as the container to hold the distinct phone numbers.  Why?

1. Its native purpose is to hold distinct items.
2. It's a hashtable that has mutable methods, such as `add` and `clear`.
3. As a hashtable, we get performance gains over a

In this task, I'm taking advantage of the hashtable performance in comparison to implementing `distinct_phone_numbers`
as a list data type.  Here is an implementation where `distinct_phone_numbers` is a global list:

```python
def get_distinct_phone_numbers(records):
O(2)        indices = range(2)                                  #O(2)
O(n)        for record in records:                              #O(n)
                for i in indices:                                   #O(2)
                    if record[i] not in distinct_phone_numbers:         #Worst case O(n^2) where O(1) get + O(len(m)), where m is the `distinct_phone_numbers` list
                        distinct_phone_numbers.append(record[i])        #O(2) = (1) get + O(1) append()
```

In the worst case, `distinct_phone_numbers` list grows by 2 for each `record` iteration.  That means Big O for a list
implementation would be between O(len(d)n) or the very worst case of O(n^2).

By using a set data type for the `distinct_phone_numbers`, the Big O for the algorithm is O(n).

### Why Store Range(2) in a Variable?

I chose to pull the `range(2)` out of the record loop to avoid creating the Range object over and over again on each
iteration.  I'm familiar enough with Python's internals to know if Python is smart enough to create it once and reuse
when inside of the same scope block.  But if no, then pulling it out of the loop ensures that only one object is created,
i.e. not dependent upon n.

## Time Complexity Summary

The Big O time complexity for Task 0 is O(n).

Worst case:

* All phone numbers are unique.
* In that worst case, there will be (len(calls) + len(texts) x 2) distinct telephone numbers.


### Analysis

#### `main()`

Description:    This function is the main controller for the task.  It invokes `get_distinct_phone_numbers()` for each
                of the lists, i.e. `calls` and `texts`, to build a container of distinct phone numbers.  Then it
                prints the message with the number of distinct phone numbers.

Big O:          The Big O time complexity is O(n).


```python
def main():
    get_distinct_phone_numbers(texts)                           #O(n)
    get_distinct_phone_numbers(calls)                           #O(n)

    print("There are {} different telephone numbers in the records.".format(len(distinct_phone_numbers)))  #O(1) len + O(1) format + O(1) print

```

T1  = O(n) + O(n) + O(1) + O(1) + O(1)
    = O(2n) + c1
    = 2n <- drop constant
    = n

N   = O(n)


#### `get_distinct_phone_numbers()`

Description:    Iterate through the 2 phone numbers of each record and add each into the distinct container.  As the
                the container is a set, it handles excluding duplicates.

Big O:          The Big O time complexity is O(n).

```python
def get_distinct_phone_numbers(records):
    global distinct_phone_numbers
    
    for record in records:                                      #O(n)
        for i in range(2):                                          #O(2)
            distinct_phone_numbers.add(record[i])                       #O(1) get + O(1) .add()
```

T1  = n x ( 2 x ( O(1) + O(1) ) )
    = n x (2c1 + 2c2)
    = n x 2c1 + n x 2c2
    = n + n <- drop the constants
    = 2n <- drop the constant
    = n

N   = O(n)

#### Number of Instructions Executed - Worst Case

##### `get_distinct_phone_numbers()`

T1  = c1 + n x 3
    = n x (1 + 2 x ( 1 + 1 + 1 )
    = n x 7

T1  = (7 x 9,072) + (7 x 5,312)
    = 63,504 + 37,184
    = 100,688

 texts   | calls  | N            | code
 -------:|-------:|--------------|---------
   9,072 |  5,312 | O(n)         | `for record in records:` 
  18,144 | 10,624 | O(2) x O(n)  |      `for i in range(2):`
  18,144 | 10,624 | O(1) x O(2n) |           `record[i]`    
  18,144 | 10,624 | O(1) x O(2n) |           `distinct_phone_numbers.add()` 
 -------:|-------:|------------------------
  63,504 | 37,184 | totals       | 

Total Instructions: 100,688

##### `main()`

T2  = O(n) + O(n) + O(1) + O(1) + O(1)
    = O(2n) + c1
    = 2n <- drop constant
    = n
    
T2  = (7 x 9,072) + (7 x 5,312)
    = 63,504 + 37,184
    = 100,688

  Instructions | N      | code 
 -------------:|--------|---------
        63,504 | O(n)   | `get_distinct_phone_numbers(texts)`
        37,184 | O(n)   | `get_distinct_phone_numbers(calls)`
             3 | O(3)   | `print().format()` 
 -------------:|--------|---------             
       100,691 |        |  

This task runs 100,691 instructions in the worst case for a execution time estimate of ~100,691ns or ~100µs.
