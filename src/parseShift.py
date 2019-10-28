def parseShift(x):

    fullDate = list(x)
    fullDate[10] = 'T'

    if len(x) == 22:
        fullDate.insert(11, '0')
        fullDate.insert(18, '0')
    elif len(x) == 23:
        if x[17] == '-':
            fullDate.insert(18, '0')
        else:
            fullDate.insert(11, '0')
            print(fullDate)

    x = "".join(fullDate)

    start = int(x[11:13])
    end = int(x[18:20])

    if x[16] == 'p' and start != 12:
        start += 12
        fullDate[11:13] = str(start)
    if x[23] == 'p' and end != 12:
        end += 12
        fullDate[18:20] = str(end)

    startDate = fullDate[0:16] + [':','0','0']
    endDate = fullDate[0:10] + ['T'] + fullDate[18:23] + [':','0','0']

    startDate = "".join(startDate) + "-07:00"
    endDate = "".join(endDate) + "-07:00"

    return([startDate, endDate])