# this program will perform task 2 in the project,
# giving us exactly what notification to send to a particular student
# by giving us the index of the notification present in notifications.txt split by line
import task3            # email to subscriber
import task1            # get fresh data from the website
def notify():
    import json
    with open("./data/notifications.txt", "r") as f:
        data = f.read()
        content = data.lower().replace(".", "").replace("/", " ").replace("(", "").replace(")", "").replace(",", "")
        notifications = content.split("\n")
        data = data.split("\n")
        
        with open("./data/students.json", 'r') as f:       # this file will be through subscription
            students = json.load(f)

#        students = {"Ahmed":{"level": "ba","notified about": ["nil","online result of ba ","download practical w",],"email": "ahmedsiddique95@gmail.com"}}
        for name, student in students.items():
            for notification in notifications:
                words = notification.split()
                for word in words:
                    if student.get("level") == word: # it is related to same degree
                        # checking whether same notification has been previously sent or not
                        new = notification[:30] not in student.get("notified about")
                        if new:
                            # new notification, add to the list and send email
                            student.get("notified about").append(notification[:30])
                            # emailing the student
                            message = (data[notifications.index(notification)])
                            task3.send_notification(student.get("email"), message)
                        continue        # no need to iterate for other words
        with open("./data/students.json", "w") as f:
            json.dump(students, f, indent=4)
#notify()
def deploy():
    task1.get_notifications()           # get notification from the website
    f_old = open("./data/notifications.txt",'r')
    f_new =open("./data/notifications_new.txt",'r')
    exect = False
    n_old = f_old.read()
    n_new = f_new.read()
    f_old.close()
    f_new.close()
    if n_old != n_new:
        exect = True
        f_old = open("./data/notifications.txt",'w+')
        f_old.write(n_new)
    f_old.close()
    if exect:
        notify()

# calling all troops
deploy()

