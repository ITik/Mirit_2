def OpenFile(name_file):
    f = open(name_file, 'rt')
    f1 = list(f)
    return f1

def CreateUsers(f1, h, num): #f1 - список по которому идем h- с каким шагом num- номер строки
    user =set()  #создаем множество, идет из набора строк - список из имен users
    for i in range(0, len(f1)-h+1, h):
        user_name = f1[i+num].split()
        if len(user_name) == 1:
            us = str(user_name[0])
        else:
            us = str(user_name[1])
        user.add(us)
    user = list(user)
    return user    # считается, что строка про имя юзера полностью записанно в виде commiter: NAMEUSER    # возвращает множество имен, но только как список

def Case_1(f1, case_name):
    case1 = open(case_name, "a")
    users = CreateUsers(f1, 4, 1)
    point1(f1, users, case1, 4)

def point1(f1, users, case, h):
    print(" Кто это сделал? ---- Сколько раз?----В процентах.")
    summa = len(f1)/h
    f2 =list()
    for i in range(len(f1)):
        a = f1[i].split()
        for j in range(len(a)):
            f2.append(a[j])
    for i in range(len(users)):
        print(users[i], "----", f2.count(users[i]), "----", f2.count(users[i])*100/summa)
        case.write(str(users[i]) + "----" + str(f2.count(users[i])) + "----" + str(f2.count(users[i])*100/summa) + "\n")

def Case_2(f1):
    case2 = open("case2.txt", "a")
    years = set()
    dict_time = {}
    for i in range(0, len(f1)-3, 4):
        time = f1[i+2].split()
        if len(time) < 3:
            years.add("Non_data")
        else:
            data_com = time[2]
            year = data_com.split("-")
            years.add(year[0]) # есть множество из того, какие года
    years = list(years)
    dict_time = dict.fromkeys(years, " ")
    for i in range(0, len(f1)-3, 4):
        time = f1[i+2].split() #строка где дата
        if len(time) < 3:
            data_commit = dict_time.get("Non_data")
            data_commit = data_commit + " " + f1[i+1]
            dict_time.update({"Non_data": data_commit})
        else:
            data_com = time[2]
            year = data_com.split("-")
            data_commit = dict_time.get(year[0])
            data_commit = data_commit + " " + f1[i+1]
            dict_time.update({year[0]: data_commit})
    list_data = list(dict_time.keys())
    for i in range(len(list_data)):
        print("\n","-"*10, list_data[i], "-"*10)
        case2.write("\n"+"-"*10+str(list_data[i])+"-"*10+"\n")
        list_users = dict_time.get(list_data[i])
        list_users = list_users.split("\n")
        #list_users = list_users.split()
        list_users.remove("")
        user = CreateUsers(list_users, 1, 0)
        point1(list_users, user, case2, 1)

def Case_3 (f1):
    case3 = open("case3.txt", "a")
    count_m = 3
    time = f1[2].split()  # строка где дата
    m = time[2].split("-")
    mm_last = int(m[1])
    a = list()
    print(m[0], "-", m[1])
    case3.write("\n" + "-" * 10 + str(m[0] + "-" + m[1]) + "-" * 10 + "\n")
    for i in range(0, len(f1)-3, 4):
         if (count_m != 0):
            time = f1[i+2].split() #строка где дата
            m = time[2].split("-")
            mm = int(m[1])
            if (len(time) < 3): print("Commit без даты ", f1[i-1])
            elif (mm != mm_last):
                count_m = count_m - 1
                user = CreateUsers(a, 1, 0)
                point1(a, user, case3, 1)
                if (count_m != 0):
                    print(m[0], "-", m[1])
                    case3.write("\n" + "-" * 10 + str(m[0] + "-" + m[1]) + "-" * 10 + "\n")
                a.clear()
                a.append(f1[i + 1])
                mm_last = mm
                m = time[2].split("-")
                mm = int(m[1])
            else:
                a.append(f1[i + 1])
         else:
            break

name_file = 'test_data_commits.log'
case = open("case1.txt", "w").close()
case = open("case2.txt", "w").close()
case = open("case3.txt", "w").close()
case1_name = "case1.txt"
f1 = OpenFile(name_file)
print("-"*20, "Case 1", "-"*20)
Case_1(f1, case1_name)
print("-"*20, "Case 2", "-"*20)
Case_2(f1)
print("-"*20, "Case 3", "-"*20)
Case_3(f1)
