from shiftPuller import shiftPuller
from parseShift import parseShift
from shiftAdder import addShift

shiftObj = shiftPuller("a1339279", "Lim12nic$")
times = shiftObj.pullShifts()

for time in times:
	print(time)
	
choice = input("Would you like to add shifts to Google Calender? (Y/N): ")

if choice == 'y':
	for time in times:
		temp = parseShift(time)
		addShift(temp[0], temp[1])
	print("ALL SHIFTS ADDED")


input("\nPRESS ANY KEY TO CONTINUE... ")
