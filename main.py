"""Problem:
Clark is conducting an online Quiz competition daily where daily participation for contestants is optional.
Clark want to send specific notifications to following group of participants
- Participants who participated everyday
- Participants who participated only once
- Participants who participated on the first day and never participated again.
Help Clark to write functions in python to get the above information. Sample function definitions are already created.
Participants data will be sent as list of lists. Each row will represent the participants attended on that day.
Sample input:
participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]
send the solution to cutshort+fresher@adnabu.com with the subject line "Solution to Puzzle"
Bonus points for optimising the solution w.r.t. time and space.
"""
participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
    ['Brad', 'Walter', 'Sam', 'Krish', 'Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer', 'Desmond', 'Harry', 'Nicole', 'Sam']
]


# Added function for keeping the track of each participant on each day in a dictionary
def get_participiant_record(participants_list):
    record = {}
    for i in participants_list:
        for j in i:
            if j not in record:
                record[j] = 1
            else:
                record[j] += 1
    return record


def daily_participants(participants_list):
    """Returns the list of all participants who participated everyday
    for the sample input, the right answer is
    ['Desmond', 'Krish', 'Sam']
    expected return object is a list of strings
    """
    record = get_participiant_record(participants_list)
    data = []
    for i in record:
        if record.get(i) == 6:
            data.append(i)
    return data


def one_time_participants(participants_list):
    """Returns the list of all participants who participated only once
    for the sample input, the right answer is
    ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
    expected return object is a list of strings
    """
    record = get_participiant_record(participants_list)
    data = []
    for i in record:
        if record.get(i) == 1:
            data.append(i)
    return data


def first_day_only_participants(participants_list):
    """Returns the list of all participants who participated on the first day and never participated again.
    for the sample input, the right answer is
    ['John', 'Joan']
    expected return object is a list of strings
    """
    first_day_record = participants_list[0]
    record = {}

    for i in first_day_record:
        record[i] = 0
        for j in range(1, len(participants_list)):
            if i in participants_list[j]:
                record[i] += 1
    data = []
    for i in record:
        if record.get(i) < 1:
            data.append(i)
    return data


print(daily_participants(participants_list))
print(one_time_participants(participants_list))
print(first_day_only_participants(participants_list))