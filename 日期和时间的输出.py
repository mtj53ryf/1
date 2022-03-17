from datetime import datetime
now=datetime.now()
print(now)
print(now.strftime("%x"))
print(now.strftime("%X"))
print(now.strftime("%Y-%m-%d %H:%M:%S"))