
from datetime import datetime, timedelta

#start variable
def schedule_meeting(worker1_calender, working_hours_1, worker2_calendar, working_hours_2, meeting_duration):
    events = worker1_calendar + worker2_calendar
    events.sort(key=lambda event: datetime.strptime(event[0], '%H:%M'))

# the common start and end time 

    earliest_start_time = max(working_hours_1[0], working_hours_2[0])
    latest_end_time = min(working_hours_1[1],working_hours_2[1])
    start_time = datetime.strptime(earliest_start_time, '%H:%M')
    end_time = datetime.strptime(latest_end_time, '%H:%M')

# for loop to find available blocks

    available_blocks = []
    prev_end_time = start_time
    for event in events:
        event_start_time = datetime.strptime(event[0], '%H:%M')
        event_end_time = datetime.strptime(event[1], '%H:%M')
        if prev_end_time + timedelta(minutes=meeting_duration) <= event_start_time:
            available_blocks.append([prev_end_time.strftime('%H:%M'), event_start_time.strftime('%H:%M')])
        prev_end_time = max(prev_end_time, event_end_time)
    if prev_end_time + timedelta(minutes=meeting_duration) <= end_time:
        available_blocks.append([prev_end_time.strftime('%H:%M'), end_time.strftime('%H:%M')])
        
    return available_blocks


worker1_calendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
working_hours_1 = ['9:00', '20:00']
worker2_calendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
working_hours_2 = ['10:00', '18:30']
meeting_duration = 30
timings_available= schedule_meeting(worker1_calendar, working_hours_1, worker2_calendar, working_hours_2, meeting_duration)
print('the available time slots  are',timings_available)
#Output: [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


# Time complexity: O(nlogn) because the events are sorted (n = total no. of events provided)
# Space complexity: O(n) because all the events as input are stored(n = total no. of events provided)