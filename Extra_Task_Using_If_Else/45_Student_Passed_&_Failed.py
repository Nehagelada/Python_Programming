#45. Count how many students passed/failed in a list.
list=[72,42,77,33,50,40,24,45,80,30]
length=len(list)
print(f"Total Student:- {length}")
passed_count=0
failed_count=0
for count in list:
    if count >= 40:
        passed_count+=1
    else:
        failed_count+=1
print("--------------------------")
print(f"Passed Students:- {passed_count}")
print(f"Failed Student:- {failed_count}")
 