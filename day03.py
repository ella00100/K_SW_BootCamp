song = """When an eel grabs your arm, 
And it cause great harm,
That's -a moray"""

#방법 1
print(song.replace(' m',' M'))

song = """When an eel grabs your arm, 
And it cause great harm,
That's -a moray"""

#방법 2
idx = song.rfind('m')
print(song[0:idx]+song[idx].upper()+song[idx+1:])