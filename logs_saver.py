from datetime import datetime

def create_array(message):
    log_date = datetime.now()
    log_array = ['id:',message.chat.id,'name:',message.chat.first_name, message.chat.last_name, 'time:',log_date, 'text:',message.text,]
    return(log_array)

def save_log(array,file_dir):
    logs = ''
    log_file = open(file_dir, 'a')
    for i in range(len(array)):
        logs = logs + str(array[i])+' '
    log_file.write(logs+'\n')
    log_file.close()

def create_log(message):
    log = create_array(message)
    save_log(log,'Logs.txt')