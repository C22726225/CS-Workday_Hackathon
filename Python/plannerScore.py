# schedule
class Day:
    def __init__(self, events = []):
        self.events = events

    def addEvent(self, name, startTime, endTime, category):
        self.events.append(Event(name, startTime,endTime,category))

    def __str__(self):
        pass

class Event:
    def __init__(self, name, startTime, endTime, category):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.category = category

class Time:
    def __init__(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins

    def getMins(self):
        return self.hrs*60 + self.mins
    
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Week:
    def __init__(self, day, month, year):
        self.days = {"mon": Day(), "tue": Day(),
                     "wed": Day(), "thu": Day(),
                     "fri": Day(), "sat": Day(),
                     "sun": Day()   }
        
        self.date = Date(day, month, year)

    def createEvent(self,day, name, startTime, endTime, category):
        self.days[day].addEvent(name,startTime,endTime,category)
        pass
    
#main 
# reccomended fitness
recFit = 150
# reccomended meditation
recMind = 120
# reccomended work by company
recWork = 35*60


mySchedule = Week(25,3,2024)
data = [
        ["mon", "Morning Workout", Time(8,0), Time(9,0), "fitness"],
        ["mon", "Guided Meditation", Time(9,0), Time(10,0), "mindfulness"],
        ["mon", "Meeting", Time(10,0), Time(11,0), "work"],
        ["mon", "Deep Focus Work", Time(12,0), Time(13,0), "work"],
        ["mon", "finish Work", Time(14,0), Time(17,0), "work"]
    ]

weeklyHrs = {"work" : 0,"mindfulness" : 0,"fitness" : 0,}

for i in range(len(data)):
    day = data[i][0]
    name = data[i][1]
    startTime = data[i][2]
    endTime = data[i][3]
    category = data[i][4]
    mySchedule.createEvent(day,name,startTime,endTime,category)
    
    weeklyHrs[category] += endTime.getMins() - startTime.getMins()

print(weeklyHrs)

mindScore = round((weeklyHrs["mindfulness"] / recMind)  * 100, 0)
if mindScore >= 100:
    mindScore = 100

fitScore = round((weeklyHrs["fitness"] / recFit)  * 100, 0)
if fitScore >= 100:
    fitScore = 100

workScore = round((weeklyHrs["work"] / recWork)  * 100, 0)
if workScore >= 100 and workScore <= 150:
    workScore = 100
elif workScore > 150:
    workScore = 50


print(f"mindfulness: {mindScore}%")
print(f"fitness: {fitScore}%")
print(f"work: {workScore}%")

finalScore = round((mindScore + fitScore + workScore) / 3,0)
print(f"Overall {finalScore}%")

