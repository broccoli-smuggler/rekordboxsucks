# rekordboxsucks

Reckordbox / Pioneer are pretty poos at some things. 

1. Music is in a format that older pioneer devices won't read (.flac .m4a) and you'd like to convert the audio files without breaking your whole library.
2. Moving your library to a different location

## Convert my library
The assumption here is that you already have a largish library that is already sorted into playlists ect. with a variety of .flac files. This will save you the hassle of re-importing and re-sorting after you convert the audio files.

Someday I'll get round to converting within the script, but for now use this excellent converter which is free, carries over metadata and works fast.

* Download [xAct](http://xact.scottcbrown.org/) and install.
* Drag all of your .flac, .wav and .m4a files into the `decode` tab of the xAct program.
* Click Decode button

Your library is now in the correct format - aiff (or wav) yay!

* Go into rekordbox and click File->Export collection in xml format - this will be the input file used for the script
* `python3 main.py {location of rekordbox.xml file eg. /Users/login/Desktop/rekordbox.xml}` this will produce a 'new.xml' file.
* In Preferences->Advanced->Imported library locate the `new.xml` and select it.
* In View->Layout click on rekordbox xml checkbox
* You should see all your playlists in the rekordboxml tab on the left of the player
* Drag the playlists from the xml tab to the playlists tab

At point you should have a load of new tracks importing and analysing. Yay! 

You may want to go onto File->Display missing files and delete all the files that no longer exist. 
