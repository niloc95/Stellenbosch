#prints a welcome message
print("\nWelcome to PY_Triathlon, note all calculation are in minutes\n")
#User to enter time for each event
swimming = float(input("Please enter time for the swimming event in minutes: "))
running = float(input("Please enter time for the running event in minutes: "))
cycling = float(input("Please enter time for the cycling event in minutes: "))
qualifying_time = 100

# Calc the total time
total_time = (swimming + running + cycling)
print(total_time)

#if statement to determine the users award
if total_time <= qualifying_time:
    print("You are within the qualifying time","%0.2f minutes you are awarded with your Provincial Colours" %total_time, "\nWell Done")
elif total_time <= (qualifying_time + 5):
    print("You are within 5 minutes of the qualifying time","%0.2f minutes you are awarded with your Provincial half Colours" %total_time, "\nWell Done")
elif total_time <= (qualifying_time + 10):
    print("You are within 10 minutes of the qualifying time","%0.2f minutes you are awarded with your Provincial Scroll" %total_time, "\nWell Done")
else: 
    print("Sorry you are not within our qualifying time","%0.2f minutes " %total_time, "\nNo Award")