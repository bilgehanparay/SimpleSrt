import pysrt


# Function to load srt file
def load(fname):
    # Error check
    return pysrt.open(fname)


# Compute time diff between two time objects
def compute_diff(t1, t2):
    tms1 = t1.hours*t1.HOURS_RATIO+t1.minutes*t1.MINUTES_RATIO+t1.seconds*t1.SECONDS_RATIO + t1.milliseconds
    tms2 = t2.hours*t2.HOURS_RATIO+t2.minutes*t2.MINUTES_RATIO+t2.seconds*t2.SECONDS_RATIO + t2.milliseconds
    return abs(tms1 - tms2)/t1.SECONDS_RATIO


filename = 'deneme.srt'
subs = load(filename)
for i in range(0, len(subs)):
    if i==0:
        print(subs[i].text)
        tprev = subs[i].end
    else:
        tcurr = subs[i].start
        tdiff = compute_diff(tprev, tcurr)
        print("[[addpause %.3f]]" % tdiff)
        print(subs[i].text)
        tprev = subs[i].end
