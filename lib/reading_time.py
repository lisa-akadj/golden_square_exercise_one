
# 200 words per minute i.e. 60 seconds.
# how many seconds per word? 60/200 = 0.3seconds
# the code ignores punctuation marks anyway?

def reading_time(text):
    if len(text.split()) < 200:
        text_length = len(text.split())
        time_length = 0.3 * text_length
        return str(round(time_length, 1)) + " sec"
    
    elif len(text.split()) >= 200:
        text_length = len(text.split())
        time_length = 0.3 * text_length
        seconds_int = round(time_length % 60, 0)
        minutes = int((time_length - seconds_int)) // 60
        seconds_one_dec = round(time_length % 60, 1)
        return str(minutes) + " min " + str(seconds_one_dec) + " sec"
    

