# #SESSION 1: PRINTING CALCULATIONS

# #print(8 + 30 + 2018)

# #E2 Q1 - how many seconds = 2562 seconds
# print((42 * 60) + 42)

# #E2 Q2 - how many miles is 10 km = 6.25 miles
# print(10 / 1.6)

# #E2 Q3a - average pace in miles per second = 409.92 mps
# print(2562 / 6.25)
# #E2 Q3b - average pace in miles per minute = 6.832 mpm
# print(409.92 / 60)
# #E2 Q3c - average pace in miles per hour = 8.782201405152225 mph
# print(60 / 6.832)

#SESSION 2 EXERCISES
#1. The volume of a sphere with radius r is (4/3)πr^3. 
#What is the volume of a sphere with radius 5?
import math
print(math.pi)

r = 5
print(r)

v = (4/3) * math.pi * (r ** 3)
print(v)

print('The volume of a sphere with radius 5 has a volume of {:.2f}'.format(v))

#2. Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
dp = (24.95-(24.95 * .4)) #discount price
print(dp)
sh = (3) #shipping price for first copy
print(sh)
ash = (.75) #shipping for additional copies
print(ash)

wholesalecost = ((dp * 60) + sh + (59 * ash))
print(wholesalecost)

print('The wholesale cost for 60 copies is {:.2f} dollars'.format(wholesalecost))

#3. HELP: If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
start_time_hr = 6 + 52 / 60.0 #hour 6 + min 52 / 60min
print(start_time_hr)

easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0

running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
print(running_time_hr)

breakfast_hr = start_time_hr + running_time_hr
print(breakfast_hr)
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
print(breakfast_min)

print('You would get home for breakfast at {:.0f}:{:.0f}AM'.format(breakfast_hr, breakfast_min))

#4. If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.
gradeA = 82
gradeB = 89

gradeincrease = (((89-82) / 82) *100)
print(gradeincrease)

print('The grade percent increase is {:.1f}%'.format(gradeincrease))