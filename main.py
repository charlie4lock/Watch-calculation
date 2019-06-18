hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here

#calculate how many hours to add to the hour coloumn to the near integer
left_over_hours = (dura//60)
#calculate how many minutes are left over after subracting hours
left_over_minutes = (dura%60)
#add the leftover minutes together to see if it makes more than an hour
Minutes = ((left_over_minutes+mins)%60)
#If the addition of the minutes are greater than 60
incase_hour_over_60 = ((left_over_minutes+mins)//60)
#if the hours go over 24
Hours = int((hour+left_over_hours+incase_hour_over_60)%24)


#Final result all added together
print (Hours,":",Minutes)