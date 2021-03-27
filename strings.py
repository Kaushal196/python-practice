message = "Hello World"
print(len(message))    #find length of string
print(message[0])       #index starts at zero
print(message[0:5])     #prints string in range message[startIndex(inclusive): secondIndex]
# string slicing video https://www.youtube.com/watch?v=ajrtAuDg3yw

#[:5] from 0th index upto 5th
#[6:] from 6th to last

print(message.lower())   #.upper() or .lower()
print(message.count('l'))  #count(arg) it will count arg
print(message.find('l'))   # will return first occurance index otherwise -1

new_message = message.replace('l', 'n', 1) # replace(old, new, count) if count first count will be replaced only 
print(new_message)

#concate string
message = "Hello" + ", " + "World"
print(message)

first_name = 'Kaushal'
last_name = 'Pandey'
message = '{} {} Welcome'.format(first_name, last_name)
print(message)

message = f'{first_name} {last_name} Welcome'
print(message)

message = f'{first_name} {last_name.upper()} Welcome'
print(message)

######## to check help

print(dir(message))
print(help(str))
print(help(str.lower))