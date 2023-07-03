
time=input("enter time HH:MM:SS\n " )
time=time.split(':')
second=int(time[2])
min=int(time[1])
hour=int(time[0])
if 0<= second <60 and 0<= min <60 and 0<= hour <24:
    sum=hour*3600+min*60+second
    print(sum,'seconds')

else:
    print("Enter the correct time :")