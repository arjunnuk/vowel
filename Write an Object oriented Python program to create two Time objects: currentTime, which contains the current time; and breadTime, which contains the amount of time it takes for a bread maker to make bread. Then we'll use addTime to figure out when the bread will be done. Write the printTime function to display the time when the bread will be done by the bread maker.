class time:
    def printtime(self,time):
        print("the time req to make the bread",str(time.hours),":",str(time.min),":",str(time.sec))
def addtime(t1,t2):
    sum=time()
    sum.hours=t1.hours+t2.hours
    sum.min=t1.min+t2.min
    sum.sec=t1.sec+t2.sec
    if sum.sec>=60:
        sum.sec=sum.sec-60
        sum.min=sum.min+1
    if sum.min>=60:
        sum.min=sum.min-60
        sum.hours=sum.hours+1
    return sum
currenttime=time()
currenttime.hours=10
currenttime.min=40
currenttime.sec=15
breadtime=time()
breadtime.hours=2
breadtime.min=30
breadtime.sec=0
donetime=addtime(currenttime,breadtime)
donetime.printtime(donetime)
