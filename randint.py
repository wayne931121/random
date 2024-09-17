import time

def random(start,end,dpv=1):
    cal = end-start+1
    result = start+round(time.time()*cal*dpv)%cal
    return result

print(random(0,10))
