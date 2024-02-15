from datetime import datetime, timedelta
from random import randint


def generate_csv(file_name):
    # Use a breakpoint in the code line below to debug your script.
    field_texts = "id,emotion_id,sub_emotion_id,created_at\n"
    handle = open("{}.csv".format(file_name), "w")
    handle.write(field_texts)
    handle.close()

    startDate = datetime(2018, 1, 1, 0, 0, 0)
    k = 1

    for i in range(30):
        weekday = startDate.weekday()
        forday = 1000
        if weekday in range(0, 4):
            forday = randint(1500, 2500)
        elif weekday in range(5, 6):
            forday = randint(500, 1000)
        else:
            pass
        for j in range(forday):
            finalhour = 12
            hourchance = randint(1, 100)

            if hourchance == 1:
                finalhour = randint(0, 5)
            elif hourchance in range(2, 11):
                finalhour = randint(6, 8)
            elif hourchance in range(12, 30):
                finalhour = randint(9, 10)
            elif hourchance in range(31, 70):
                finalhour = randint(11, 13)
            elif hourchance in range(71, 89):
                finalhour = randint(14, 16)
            elif hourchance in range(90, 99):
                finalhour = randint(17, 20)
            elif hourchance == 100:
                finalhour = randint(21, 23)
            else:
                pass

            minute = randint(0, 59)
            second = randint(0, 59)
            date = datetime(startDate.year, startDate.month, startDate.day, finalhour, minute, second)

            finalsix = 1
            sixchance = randint(1, 100)
            if sixchance in range(1, 35):
                finalsix = 1
            elif sixchance in range(36, 45):
                finalsix = 2
            elif sixchance in range(46, 60):
                finalsix = 3
            elif sixchance in range(61, 85):
                finalsix = 4
            elif sixchance in range(86, 95):
                finalsix = 5
            elif sixchance in range(96, 100):
                finalsix = 6
            else:
                pass

            finalfour = 1
            fourchance = randint(1, 100)
            if fourchance in range(1, 65):
                finalfour = 1
            elif fourchance in range(66, 85):
                finalfour = 2
            elif fourchance in range(86, 95):
                finalfour = 3
            elif fourchance in range(96, 100):
                finalfour = 4
            else:
                pass

            handle = open("{}.csv".format(file_name), "a")
            handle.write("{},{},{},{}\n".format(k, finalsix, finalfour, date))
            handle.close()
            k += 1
        startDate += timedelta(days=1)
        print(startDate, i)


if __name__ == '__main__':
    generate_csv("test")
