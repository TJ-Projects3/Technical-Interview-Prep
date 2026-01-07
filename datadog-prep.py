# You are given two arrays slots1 and slots2 that represent the available time slots for two people, 
# and an integer duration representing the length of a meeting they need to schedule.
# Each time slot is represented as an array [start, end], where start and end are inclusive boundaries 
# (meaning the person is available from time start to time end, including both endpoints). Your task is to find the earliest 
# time slot where both people are available for at least duration minutes. If such a common time slot exists, 
# return an array [meetingStart, meetingEnd] where the meeting would start at meetingStart and end at 
# meetingStart + duration. If no such time slot exists, return an empty array [].

# Key constraints:

# Within each person's schedule, time slots don't overlap (they are non-intersecting)
# For any two slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1

# For example:
# If person 1 has slots [[9, 10], [ , ]]
# And person 2 has slots [[1, 2], [6, 8]]
# With duration = 5
# The earliest common available time would be [45, 53] (both are free from 45 to 50, which gives us at least 8 minutes)

# We will sort the list to make it easier to find the EARLIEST available time and have meeting times more aligned.
# We will use two pointer to point at each person time slots. We will check time slots using end - start on each time
# First we check if

def meeting_scheduler(slots1, slots2, duration):
    slots1.sort()
    slots2.sort()

    n1 = len(slots1)
    n2 = len(slots2)

    i = j = 0

    while i < len(slots1) and j < len(slots2):
        s1, e1 = slots1[i]
        s2, e2 = slots2[j]

        if min(e2, e1) - max(s1, s2) >= duration:
            return [max(s1, s2), max(s1, s2) + duration]
        
        if e1 >= e2:
            j += 1
        else:
            i += 1
    return []

slots1 = [[10, 50], [60, 120]]
slots2 = [[0, 15], [45, 70]]
print(meeting_scheduler(slots1, slots2, 8))