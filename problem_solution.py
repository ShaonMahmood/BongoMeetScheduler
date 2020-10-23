from utils import stringToMinute, minuteToString, minutesInDay
from utils import measure_time


@measure_time
def suggested_meeting_time(employees_list : list,
                           office_start_time : str = "08:00",
                           office_end_time : str = "17:00",
                           duration : int = 60
                           ) -> list:

    """
    :param employees_list: the list of occupied timeslots for different persons
    :param office_start_time: office start time (24 hour format)
    :param office_end_time: office end time (24 hour format)
    :param duration: meeting duration in minutes
    :return: returns a list of tuples mentioning the available meeting time slots between office start and end time
    """

    if not isinstance(employees_list, list):
        raise TypeError('Please provide a list argument for employee_list')
    if not isinstance(office_start_time, str):
        raise TypeError('Please provide a string argument for office_start_time')
    if not isinstance(office_end_time, str):
        raise TypeError('Please provide a string argument for office_end_time')
    if not isinstance(duration, int):
        raise TypeError('Please provide a integer argument for meeting duration')

    meetings = [
        list(map(stringToMinute, meeting)) for p in employees_list
        for meeting in p
    ]
    freeTime = [True] * minutesInDay

    for meet in meetings:
        for i in range(int(meet[0]), int(meet[1])):
            freeTime[i] = False

    start_minute = stringToMinute(office_start_time)
    end_minute = stringToMinute(office_end_time)

    result = list()
    openInterval = False
    beg, end = 0, 0

    for i, slot in enumerate(freeTime):
        if not openInterval and slot and i >= start_minute:
            openInterval = True
            beg = i
        elif openInterval and not slot:
            openInterval = False
            end = i
            if end - beg >= duration:
                beg = minuteToString(beg)
                end = minuteToString(end)
                result.append((beg, end))

        elif i >= end_minute:
            openInterval = False
            end = i
            if end - beg >= duration:
                beg = minuteToString(beg)
                end = minuteToString(end)
                result.append((beg, end))
            break

    if not result:
        return []

    return result


if __name__ == '__main__':
    p1 = [
        ('08:00', '12:30'),
        ('14:00', '15:00'),
    ]

    p2 = [
        ('09:00', '12:00'),
        ('14:00', '15:30'),
    ]
    result = suggested_meeting_time(employees_list=[p1,p2], duration=60)
    if not result:
        print("No available time slots for meeting")
    else:
        print(result)