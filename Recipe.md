# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem
```
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
```
## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
```python
def reading_time(text):
    """ 
    Parameter: a certain length of text or string. 
    String can include punctuation marks. 
    
    Return value: the length of time required to "read" the string
    in minutes, or in minutes and seconds, or in seconds...?

    Side effects: none? (unsure)
    """

    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text with less than 200 words
It returns a the number of seconds it will take to read e.g. 10 sec. with one decimal place
"""
def test_less_than_two_hundred_words():
    result = reading_time("this sentence is less than two hundred words")  => "60 seoconds to read 200 words. (60/200)*8 = 2.4 seconds"

"""
Given a text longer than 200 words (the example has 254 words)
Return the length of time it takes to read in minutes and seconds. e.g. 1 min a few seconds (calculate no. of seconds later)
"""
def test_more_than_two_hundred_words() 
result = reading_time("I need to write a random phrase that has more than two hundred words the phrase will not contain any punctuation marks as it is for the purpose of code writing and I can not be bothered to go through the hassle of writing a code that will ignore the punctuation marks and take the words only also does one digit count as one word question mark what if it is a very long number something like one million six hundred and seventy five thousand eight hundred and twenty one question mark if that was written with digits it would be technically one word but to read it out loud it would be thirteen words full stop that is thirteen words if I counted it correctly something that I seem completely unable to do is write a sophisticated witty article or a story in English full stop when I read a newspaper article or a magazine article I find myself bemused open bracket bemused is a new word I learnt recently close bracket I am only good at everyday English full stop I do not know how to write an article let alone understand one exclamation mark I have just counted the number of words in this phrase using python and I wrote the code for that from memory hehe insert sunglasses emoji the words have been counted and there were one hundred and ninety seven words full stop I have added a few words so this is definitely more than two hundred now") => "1 min XX.X sec

"""
Given an empty string
Returns zero minutes zero seconds
"""
reading_time("") => 0 min 0.0 sec

"""


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


Ensure all test function names are unique, otherwise pytest will ignore them!
