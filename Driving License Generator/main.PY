def sname(sn):
    a = len(sn)
    if a == 0:
        b = "99999"
    elif a == 1:
        b = sn+"9"*4
    elif a == 2:
        b = sn+"9"*3
    elif a == 3:
        b = sn+"9"*2
    elif a == 4:
        b = sn+"9"
    elif a >= 5:
        b = str(sn)[0:5]
    return b


def mon(mm, gn):
    mm = str((mm.split("-"))[1])[0:3]
    if gn == "M":
        if mm == "Jan":
            return "01"
        elif mm == "Feb":
            return "02"
        elif mm == "Mar":
            return "03"
        elif mm == "Apr":
            return "04"
        elif mm == "May":
            return "05"
        elif mm == "Jun":
            return "06"
        elif mm == "Jul":
            return "07"
        elif mm == "Aug":
            return "08"
        elif mm == "Sep":
            return "09"
        elif mm == "Oct":
            return "10"
        elif mm == "Nov":
            return "11"
        elif mm == "Dec":
            return "12"
    else:
        if mm == "Jan":
            return "51"
        elif mm == "Feb":
            return "52"
        elif mm == "Mar":
            return "53"
        elif mm == "Apr":
            return "54"
        elif mm == "May":
            return "55"
        elif mm == "Jun":
            return "56"
        elif mm == "Jul":
            return "57"
        elif mm == "Aug":
            return "58"
        elif mm == "Sep":
            return "59"
        elif mm == "Oct":
            return "60"
        elif mm == "Nov":
            return "61"
        elif mm == "Dec":
            return "62"


def dec(d):
    c = (d.split("-"))[-1]
    return c[2]


def yea(r):
    c = (r.split("-"))[2]
    return c[-1]


def day(aa):
    aa = str((aa.split("-"))[0])
    return aa


def ini(iff, imm):
    if len(imm) == 0:
        return iff[0]+"9"
    else:
        return iff[0]+imm[0]


def driver(data):
    return str(sname(data[2])).upper() + str(dec(data[3]))+str(mon(data[3], data[4])) + day(data[3]) + str(yea(data[3])) + ini(data[0], data[1]) + "9AA"


print(["First Name", "Middle Name(if any)", "Last Name", "DD-Month-YYYY", "Gender(M/F)"])
apple = input(" ")
print(driver(apple))