#jackson bauer
#online status

statuses= {
    'alice':'online',
    'bob':'offline',
        'jo':'offline',
        'joe':'online',
        'joseph':'online',
        'patrick':'offline',   #status key
        'blacktrick':'offline',
    'eve' : 'online'}

def online_status(statuses):
#     x = 'online'
#     o = 0
#     for x in statuses:
#         print('There are ' + str(o+1) + ' users online')
    return sum(status == 'online' for status in statuses.values()) #returns the 'x' value of users, uses a for loop
print('there are ' + str(online_status(statuses))    + ' people online')
