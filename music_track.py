import zipfile, io
print("Image file/SoundTrack: ")
s = input()
try:
    of = zipfile.ZipFile(io.BytesIO(open(s, 'rb').read().split(b'\xff\xd9', 1)[1]), 'r')
    newfile = False
except zipfile.BadZipFile:
    newfile = True
existfile = []
if not newfile:
    for x in of.namelist():
        existfile.append(x)
removefile = []
exi = True
fzip = io.BytesIO()
while exi:
    if len(existfile)-len(removefile) == 0:
        print("Empty SoundTrack")
    else:
        x = 0
        for y in existfile:
            if y not in removefile:
                x += 1
                print(x, ":", y.split("\\")[-1].split("/")[-1])
    cmd = input(">>> ")
    if cmd=="help":
        print("add - Add songs to SoundTrack")
        print("rem - Remove songs from SoundTrack")
        print("save - Save changes and exit")
        print("exit - Discard changes and exit")
    else:
        if cmd == "add":
            d = input("Song Paths: ")
            try:
                if d[-4:].lower() not in ['.mp3', '.wav', '.ogg']:
                    print("Format not supported")
                else:
                    try:
                        open(d, 'rb')
                        if d in existfile:
                            if d in removefile:
                                removefile.remove(d)
                            else:
                                print("File Already Exists")
                        else:
                            newl = []
                            for x in existfile:
                                if x not in removefile:
                                    newl.append(x)
                            if d.split("\\")[-1].split("/")[-1] not in newl:
                                existfile.append(d)
                            else:
                                print("File Already Exists")
                    except:
                        print("File not found")
            except Exception as e:
                raise e
                print("Input incorrect")
        if cmd == "rem":
            try:
                d = int(input("Song Index: "))-1
                if d<0 or d>=len(existfile)-len(removefile):
                    print("Out of boundary")
                else:
                    newl = []
                    for x in existfile:
                        if x not in removefile:
                            newl.append(x)
                    removefile.append(newl[d])
            except Exception as e:
                raise e
                print("Not an Integer")
        if cmd == "exit":
            exi = False
        if cmd == "save":
            fkzip = zipfile.ZipFile(fzip, "w")
            for x in existfile:
                if x not in removefile:
                    try:
                        open(x)
                        fkzip.writestr(x.split('\\')[-1].split("/")[-1], open(x, 'rb').read())
                    except:
                        if x in of.namelist():
                            fkzip.writestr(x, of.read(x))
                        else:
                            print("File %s not found, skip"%x)
            try:
                of.close()
            except:
                pass
            fkzip.close()
            fzip.seek(0, 0)
            st = fzip.read()
            d = input("Output Filename: ")
            yy = open(d, 'wb')
            yy.write(open(s, 'rb').read())
            yy.write(st)
            yy.close()
            exi = False
