import time
import getpass
username=getpass.getuser()
timex=time.localtime()
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print "Hello "+username.title()+", today is "+week[timex[6]]+" and "+str(timex[7])+" th day of the year, the date is "+str(timex[2])+","+str(timex[1])+","+str(timex[0])+" and the time is "+str(timex[3])+":"+str(timex[4])+":"+str(timex[5])
#for tup in ("Hello ",username.title(),", today is the ",str(timex[7])," th day of the year, the date is ",str(timex[2]),",",str(timex[1]),",",str(timex[0])," and the time is ",str(timex[3]),",",str(timex[4]),",",str(timex[5])):
#     sentence=''.join(tup)
#print type(("\nHello ",username.title(),", today is the ",str(timex[7])," th day of the year, the date is ",(timex[1],timex[2],timex[0])," and the time is ", (timex[3],timex[4],timex[5])))
#print sentence
#print username
#print timex
