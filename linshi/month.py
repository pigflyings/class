sMonthName = input("Please input month name: ")
y=input("Please input year name: ")
y=int(y)
if y % 4 == 0 and y%100!=0:
    print("this year is 闰年")
elif y % 400 == 0:
    print("this year is 闰年")
else:
    print("非润年")
sMonthName = sMonthName.strip().title()
if sMonthName in ['January','March','May','July',
                  'August','October','December']:
    print("There are 31 days in the designated month.")
elif sMonthName in ['1','3','5','7','8','10','12']:
    print("There are 31 days in the designated month.")
elif sMonthName in ['April', 'June','September', 'November']:
    print("There are 30 days in the designated month.")
elif sMonthName in ['4','6','9','11']:
    print("There are 30 days in the designated month.")
elif sMonthName == "February" or sMonthName.startswith("Feb"):
    print("There are 28 or 29 days in the designated month.")
elif sMonthName == "2" :
    print("There are 28 or 29 days in the designated month.")
else:
    print("Unrecognized month name.")