from lib.reading_time import reading_time

def test_less_than_two_hundred_words():
    result = reading_time("This sentence is less than two hundred words.")
    assert result == "2.4 sec"

def test_more_than_two_hundred_words():
    result = reading_time("I need to write a random phrase that has more than two hundred words the phrase will not contain any punctuation marks as it is for the purpose of code writing and I can not be bothered to go through the hassle of writing a code that will ignore the punctuation marks and take the words only also does one digit count as one word question mark what if it is a very long number something like one million six hundred and seventy five thousand eight hundred and twenty one question mark if that was written with digits it would be technically one word but to read it out loud it would be thirteen words full stop that is thirteen words if I counted it correctly something that I seem completely unable to do is write a sophisticated witty article or a story in English full stop when I read a newspaper article or a magazine article I find myself bemused open bracket bemused is a new word I learnt recently close bracket I am only good at everyday English full stop I do not know how to write an article let alone understand one exclamation mark I have just counted the number of words in this phrase using python and I wrote the code for that from memory hehe insert sunglasses emoji the words have been counted and there were one hundred and ninety seven words full stop I have added a few words so this is definitely more than two hundred now")
    assert result == "1 min 16.2 sec"

def test_empty_string():
    result = reading_time("")
    assert result == "0.0 sec"
