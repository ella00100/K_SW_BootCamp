#prob 5.1

song = """When an eel grabs your arm, 
And it cause great harm,
That's -a moray"""

#방법 1
print(song.replace(' m',' M'))

#방법 2
idx = song.rfind('m')
print(song[0:idx]+song[idx].upper()+song[idx+1:])

#방법3
song_list = song.split()
song_list[13] = song_list[13].title()
song_string = ' '.join(song_list)
print(song_string)