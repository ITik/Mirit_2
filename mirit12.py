def OpenFileAndCreateUsers (name_file):
    f = open(name_file, 'rt')
    f1 = list(f)
    user =set()
    for i in range(1, len(f1), 4):
        user_name = f1[i].split()
        if len(user_name) == 1:
            us = str(user_name[0])
        else:
            us = str(user_name[1])
        user.add(us)
    print(user)
    return user, f1

def Case_1(users, f1):
    case1 = open("case1.txt", "a")
    for i in range(0, len(f1)-3, 4):
        user_name = f1[i+1].split()
        if len(user_name) == 1:
            us = str(user_name[0])
        else:
            us = str(user_name[1])
        count_com = users.get(us)
        count_com = count_com + 1
        users.update({us: count_com})
    #print("-"*20, "Case 1","-"*20)
    print(" Кто это сделал? ---- Сколько раз?----В процентах.")
    keyses = list(users.keys())
    summa = 0
    for i in range(len(users)):
        summa = summa + users.get(keyses[i])
    for i in range(len(users)):
        print(keyses[i], "----", users.get(keyses[i]), "----", users.get(keyses[i])*100/summa)
        case1.write(str(keyses[i])+ "----" + str( users.get(keyses[i]))+ "----" + str(users.get(keyses[i])*100/summa) + "\n")

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
            years.add(year[0])
    dict_time = dict.fromkeys(years, " ")
    user_t = set()
    for i in range(0, len(f1)-3, 4):
        user_name_t = f1[i+1].split()

        us = f1[i+1]
        time = f1[i+2].split()

        if len(user_name_t) == 1:
            us_t = str(user_name_t[0])
        else:
            us_t = str(user_name_t[1])
        user_t.add(us_t)
        if len(time) < 3:
            data_commit = dict_time.get("Non_data")
            data_commit = data_commit + us
            dict_time.update({"Non_data": data_commit})
        else:
            data_com = time[2]
            year = data_com.split("-")
            data_commit = dict_time.get(year[0])
            data_commit = data_commit +" "+ us
            dict_time.update({year[0]: data_commit})
    list_data = list(dict_time.keys())
    for i in range(len(list_data)):
        print("-"*10, list_data[i], "-"*10+"\n")
        case2.write("-"*10+str(list_data[i])+"-"*10)
        list_users = dict_time.get(list_data[i])
        print(" Кто это сделал? ---- Сколько раз?----В процентах.")
        summa = len(list_users)
        user_t= list(user_t)
        for i in range(len(user_t)):
            count_user = list_users.count(user_t[i])
            print(user_t[i], "----", count_user, "----", count_user * 100 / summa)
            case2.write(str(user_t[i])+ "----"+str( count_user)+ "----"+str(count_user * 100 / summa)+ "\n")


name_file = 'test_data_commits.log'

user, f1 = OpenFileAndCreateUsers(name_file)
users = dict.fromkeys(user, 0)
print(users)
print("Выполнить пункт 1, 2 ")
print("-"*20, "Case 1", "-"*20)
Case_1(users, f1)
print("-"*20, "Case 2", "-"*20)
Case_2(f1)
