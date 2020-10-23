
secs = int(input("seconds: "))
def function(secs):
    days = secs//(60*60*24)
    secs = secs % (60*60*24)
    hours = secs// (60*60)
    secs = secs % (60*60)
    mins = secs//60
    secs = secs % 60
    s = secs
    return days, hours, mins, secs
print("days:", "hours:", "mins:", "secs:", (function(secs)))