import datetime

SecToConvert = int(input("Enter seconds: "))

ConvertedSec = str(datetime.timedelta(seconds = SecToConvert))

print(ConvertedSec)