# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a list of times they are available ('HH:MM' 24-hour). Create a function that will take in an original list plus any number of lists of teammate's available times (*remember \*args*) and return a list of times where everyone can meet.

p1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
p2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
p3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
p4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# Available Times: '12:00' and '14:30'

def gmt(*times):
    gmt1 = set(p1)
    gmt2 = set(p2)
    gmt3 = set(p3)
    gmt4 = set(p4)
    gmt5 = gmt1 & gmt2 & gmt3 & gmt4
    return gmt5 

print(gmt())
    
    
    