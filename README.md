# Music In JPG
## 0x01 Introduction
Basically it is just my... imagination?<br>
I think that JPG and zip have their own magic number, then if I can place musics in a archive and append into the JPG file?<br>
After some tries and search on internet, I succedd, however I found that there are already some ways to do it on internet.<br>
However don't know why sometimes those methods cannot be used, so I still decided to post it.<br>
## 0x02 Usage (Creating / Modifying picture)
There will be a file called "music_track.py" (well, there's no GUI this time)<br>
When you run this script, it will ask you for a picture (can be the picture proceed or a JPEG picture)<br>
And it will jump into a fake "interaction shell"<br>
You can input some command into it<br>
Input help will result in<br>
```
add - Add songs to SoundTrack
rem - Remove songs from SoundTrack
save - Save changes and exit
exit - Discard changes and exit
```
## 0x03 Usage (Music Player)
A small script for playing the music inside picture called "play.py"
## 0x04 Notes
The script for extract the files inside have not been implemented, but will be uploaded later<br>
You can also do it yourself! (As known as, DIY)<br>
The zip archive is append just after the JPEG file, and<br>
it is also correct to said that the archive is stored after the first FF D9 (b'\xff\xd9')<br>
so no matter use ZipFile in python or write it in a file and extract it is also OK.<br>
## Postscript
There are a example picture which include two japanese music I like is inside the repo.
You can test with it.
