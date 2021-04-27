import zipfile, io, time
from pygame import mixer
import random
print("Initializing...")
mixer.init()
d = input("Sound Track: ")
try:
    zf = zipfile.ZipFile(io.BytesIO(open(d, 'rb').read().split(b'\xff\xd9', 1)[1]))
except FileNotFoundError:
    print("File Not Found")
    exit()
except IndexError:
    print("Not a valid sound track")
    exit()
except zipfile.BadZipFile:
    print("Not a valid sound track")
    exit()
v = float(input("Volume: "))
if v>100 or v<0:
    print("Out of boundary, set to 100")
    v = 1
else:
    v = v / 100
print("The Sound Track contains of following songs: ")
for x in range(len(zf.namelist())):
    print(x+1, ":", zf.namelist()[x])
print("Select Mode: ")
print("1. Play follow to this direction")
print("2. Play backwards")
print("3. Randomize")
try:
    d = int(input("Mode: "))
    if d<1 or d>3:
        print("Out of boundary, default to follow direction")
        d = 1
except:
    print("Error, default to follow direction")
    d = 1
print("Terminate the script or keyboard interrupt to stop playing")
st = True
if d==1:
    while st:
        for x in range(len(zf.namelist())):
            try:
                print("Start to play %s"%(zf.namelist()[x]))
                obj = mixer.Sound(io.BytesIO(zf.read(zf.namelist()[x])))
                obj.set_volume(v)
                obj.play()
                time.sleep(obj.get_length())
                obj.stop()
            except KeyboardInterrupt:
                print("Stop Playing")
                obj.stop()
                st = False
                break
            except Exception as e:
                raise e
if d == 2:
    while st:
        for x in range(len(zf.namelist())-1, -1, -1):
            try:
                print("Start to play %s"%(zf.namelist()[x]))
                obj = mixer.Sound(io.BytesIO(zf.read(zf.namelist()[x])))
                obj.set_volume(v)
                obj.play()
                time.sleep(obj.get_length())
                obj.stop()
            except KeyboardInterrupt:
                print("Stop Playing")
                obj.stop()
                st = False
                break
            except Exception as e:
                raise e
if d == 3:
    while st:
        x = random.randint(0, len(zf.namelist())-1)
        try:
            print("Start to play %s"%(zf.namelist()[x]))
            obj = mixer.Sound(io.BytesIO(zf.read(zf.namelist()[x])))
            obj.set_volume(v)
            obj.play()
            ox = time.time()
            while ox + obj.get_length() > time.time():
                pass
            obj.stop()
        except KeyboardInterrupt:
            print("Stop Playing")
            obj.stop()
            st = False
            break
        except Exception as e:
            raise e
