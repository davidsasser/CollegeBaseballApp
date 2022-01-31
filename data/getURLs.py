file = open('./schedule.txt', 'r')
out = open('./clean_schedule.txt', 'a')
lines = file.readlines()

for i in lines:
    if('/team/' in i):
        out.write('https://d1baseball.com' + i.split('"')[1] + '\n')