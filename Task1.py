"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def get_distinct_phone_numbers(records):
    """
    Get the distinct phone numbers from the given list.

    There are 2 sublists of phone numbers in the given list, i.e.
    calling from (index 0) and number being called (index 1).
    """
    global distinct_phone_numbers

    for record in records:
        for i in range(2):
            distinct_phone_numbers.add(record[i])


def main():
    """
    Prints the number of unique telephone numbers in texts and calls combined.

    Both lists have sublists of outgoing (index 0) and incoming (index 1) phone numbers.
    """
    get_distinct_phone_numbers(texts)
    get_distinct_phone_numbers(calls)

    print("There are {} different telephone numbers in the records.".format(len(distinct_phone_numbers)))

def run_tests():
    """
    Runs the test suite.  Prints "All tests passed!" when all of the tests pass; else, assertion error is displayed.
    """

    phone_numbers = [
        ['97424 22395', '90365 06212', '01-09-2016 06:03:22'],
        ['97424 22395', '92415 91418', '01-09-2016 06:03:22'],
        ['94489 72078', '97424 22395', '01-09-2016 06:05:35'],
    ]
    expected_numbers = {
        '97424 22395', '90365 06212', '92415 91418', '94489 72078'
    }
    expected_count = 4

    # Run the test.
    get_distinct_phone_numbers(phone_numbers)
    assert(distinct_phone_numbers == expected_numbers)
    assert(len(distinct_phone_numbers) == expected_count)

    # Run it again to ensure the phone numbers are excluded.
    get_distinct_phone_numbers(phone_numbers)
    assert(distinct_phone_numbers == expected_numbers)
    assert(len(distinct_phone_numbers) == expected_count)

    # Test with another list.
    phone_numbers = [
        ['78130 00821', '92415 91418', '01-09-2016 06:01:12,186'],
        ['90365 06212', '(022)28952819', '01-09-2016 06:01:59,2093'],
        ['97424 22395', '94489 72078', '01-09-2016 06:03:51,1975'],
    ]
    expected_numbers = {
        '97424 22395', '90365 06212', '92415 91418', '94489 72078',
        '78130 00821', '(022)28952819',
    }
    expected_count = 6

    # Run with another list of phone numbers.
    get_distinct_phone_numbers(phone_numbers)
    assert(distinct_phone_numbers == expected_numbers)
    assert(len(distinct_phone_numbers) == expected_count)

    # Run it again to ensure the phone numbers are excluded.
    get_distinct_phone_numbers(phone_numbers)
    assert(distinct_phone_numbers == expected_numbers)
    assert(len(distinct_phone_numbers) == expected_count)

    print('All tests passed!')


# A list of distinct (unique) phone numbers.  Global to simply handling the separate texts and calls lists.
distinct_phone_numbers = set()

#run_tests()
main()
