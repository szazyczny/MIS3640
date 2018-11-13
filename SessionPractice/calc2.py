# Volume of a sphere with radius r is (4/3)pir^2
# what is the volume with radius of 5

import math

volume = (4/3)*(math.pi)*(5**2)
print(volume)
'The volume is: {:.2f}'.format(volume)

# Cover price of a book is $24.95 but bookstores get 40% discount
# Shipping costs $3 for the first copy and $.75 for each additional
# What is the total wholesale for 60 copies?

coverprice = 24.95
bookstore = 24.95 - (24.95*.4)
bookstore
shipfirst = 3
shipadd = .75

firstcopy = bookstore + shipfirst
firstcopy

addcopy = 59*(bookstore + shipadd)
addcopy

wholesale = firstcopy + addcopy
wholesale

'The total wholesale for 60 copies is: {:.2f}'.format(wholesale)

# Average grade rises from 82 to 89. What is the percentage of the increase? Format as xx.x%

old = 82
new = 89

increase = new - old
increase

percincrease = (increase / old) * 100
percincrease

'The percentage of the increase is {:.1f}%'.format(percincrease)

