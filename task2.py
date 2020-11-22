# this program will perform task 2 in the project,
# giving us exactly what notification to send to a particular student
# by giving us the index of the notification present in notifications.txt split by line
def notify():
    with open("notifications.txt", "r") as f:
        data = f.read()
        content = data.lower().replace(".", "").replace("/", " ").replace("(", "").replace(")", "").replace(",", "")
        notifications = content.split("\n")
        data = data.split("\n")
        students = [
            {"name": "student1", "level": "mphil", "notification no.": []},
            {"name": "student2", "level": "msc", "notification no.": []},
            {"name": "student3", "level": "ba", "notification no.": []},
            {"name": "student4", "level": "law", "notification no.": []},
            {"name": "student5", "level": "bcom", "notification no.": []},
        ]
        #keywords = ["admission", "registeration", "admissions", "date", "sheet", "result", "roll", "no", "download", "schedule",
        #"regular", "self", "private", "part-i", "part-ii",  "associate", "degree"]
        for student in students:
            for notification in notifications:
                words = notification.split()
                for word in words:
                    if student.get("level") == word:
                        student.get("notification no.").append(notifications.index(notification))
            '''
            #Turn on this code block if code is to be checked or verified
            print("==========================================================")
            print("notifications related to ", student.get("name"), ":")
            for i in student.get("notification no."):
                print(data[i])
            '''
        return students
notify = notify()
