import re

def stat_maker(logs):
    stats = ''
    log_file = (open(logs, 'r')).read()
    username = re.findall(r'name:(.*?)time:',log_file)
    for i in range(len(username)):
        stats = stats + username[i]
    return(stats)

t = stat_maker('Logs.txt')
print(t)
