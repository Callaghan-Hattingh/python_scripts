def add_time(start, duration, day = 'N'):

    day = day.upper()
    dw = int()
    if day == 'N':
        pass
    elif day == 'MONDAY':
        dw = 0
    elif day == 'TUESDAY':
        dw = 1
    elif day == 'WEDNESDAY':
        dw = 2
    elif day == 'THURSDAY':
        dw = 3
    elif day == 'FRIDAY':
        dw = 4
    elif day == 'SATURDAY':
        dw = 5
    elif day == 'SUNDAY':
        dw = 6

    i = start.upper().split()
    x1 = i[0].split(':')
    h1 = int(x1[0])
    m1 = int(x1[1])

    x2 = duration.split(':')
    h2 = int(x2[0])
    m2 = int(x2[1])

    if i[1] == 'PM':
        h1 = h1 + 12
    
    h3 = h1 + h2
    m3 = m1 + m2
    l3 = "AM"
    d3 = 0 

    while m3 > 59:
        m3 = m3 - 60
        h3 = h3 + 1
    
    while h3 > 23:
        h3 = h3 - 24
        d3 = d3 + 1

    if h3 > 12:
        h3 = h3 - 12
        l3 = "PM"

    if h3 == 12 and m3 > 0:
        l3 = "PM"

    if h3 == 0:
        h3 = 12

    if day != 'N':
        dw = dw + d3
        dw = dw%7
        if dw == 0:
            day = 'Monday'
        elif dw == 1:
            day = 'Tuesday'
        elif dw == 2:
            day = 'Wednesday'
        elif dw == 3:
            day = 'Thursday'
        elif dw == 4:
            day = 'Friday'
        elif dw == 5:
            day = 'Saturday'
        elif dw == 6:
            day = 'Sunday'

    d3t = str()
    if d3 == 1:
        d3t = "(next day)"
    elif d3 > 1:
        d3t = f"({d3} days later)"

    m3t = str()
    if m3 < 10:
        m3t = f"0{m3}"
    else:
        m3t = m3

    if d3 == 0 and day == 'N':
        new_time = f"{h3}:{m3t} {l3}"
    elif d3 > 0 and day == 'N':
        new_time = f"{h3}:{m3t} {l3} {d3t}"
    elif d3 == 0:
        new_time = f"{h3}:{m3t} {l3}, {day}"
    elif d3 > 0:
        new_time = f"{h3}:{m3t} {l3}, {day} {d3t}"

    return new_time