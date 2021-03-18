def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("bhaaag")

a = increment('swdefrgt')
print(a)