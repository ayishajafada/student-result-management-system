#Create a system that stores student details:

students=[{"name":"ayisha","python":75,"SQL":86,"Java":78},
          {"name":"sharjad","python":76,"SQL":80,"Java":70},
          {"name":"jafada","python":90,"SQL":82,"Java":98},
          {"name":"akhil","python":96,"SQL":85,"Java":79},
          {"name":"priya","python":82,"SQL":88,"Java":91},
          {"name":"rahul","python":70,"SQL":75,"Java":68},
          {"name":"amaya","python":95,"SQL":90,"Java":85},
          {"name":"sneha","python":78,"SQL":84,"Java":80},
          {"name":"kiran","python":88,"SQL":92,"Java":87},
          {"name":"meera","python":85,"SQL":89,"Java":92},
          {"name":"arjun","python":77,"SQL":81,"Java":74},
          {"name":"devika","python":91,"SQL":87,"Java":90},
          {"name":"naveen","python":68,"SQL":72,"Java":65},
          {"name":"ananya","python":94,"SQL":93,"Java":88},
          {"name":"rohan","python":80,"SQL":78,"Java":83}]

total_marks=list(map(lambda x:(x["name"], x["python"] + x["SQL"] + x["Java"]), students))
print(total_marks)

average_mark=list(map(lambda x:(x[0],x[1]/3),total_marks))
print(average_mark)

results=[]
for name, avg in average_mark:
    if avg >= 90:
        grade = "A"
        status = "Pass"
    elif avg >= 80:
        grade = "B"
        status = "Pass"
    elif avg >= 70:
        grade = "C"
        status = "Pass"
    elif avg >= 60:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"
    
    results.append({"name": name, "average_mark": avg, "grade": grade, "status": status})

passed_students=list(filter(lambda x:x["average_mark"]>=60,results))
print(passed_students)

students_sorted=sorted(results,key=lambda x:x["average_mark"],reverse=True)

topper=sorted(results,key=lambda x:x["average_mark"],reverse=True)[0]
print("Topper:",topper)

from functools import reduce
class_average=reduce(lambda a,b:a+b,map(lambda x:x["average_mark"],results))/len(results)
print("Class average is:",class_average)