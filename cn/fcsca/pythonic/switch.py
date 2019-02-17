day = 0
switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}
day_name = switcher[day]
day_n = switcher.get(day, 'Unkown')
