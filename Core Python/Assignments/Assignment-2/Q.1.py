# 1. Convert the time entered in hh,min and sec into seconds.

hh = int(input('Enter the hours : '))
min = int(input('Enter the minute : '))
sec = int(input('Enter the sec : '))
total_sec = ( hh * 3600)+ (min *60)+ (sec *1)

print(f'the time in seconds : {total_sec} seconds')