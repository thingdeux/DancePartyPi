# Dance Party
    A daemon that will listen for the words 'Dance Party' and start playing techno music complete with LED "rave" lights for my daughter.
    This will run on a micro controller platform (arduino or r. pi) and be wrapped as a toy with which my daughter can interact.
    

## Additional Installation Instructions:

#### Python requirements are in requirements.txt

    * Install OpenAL
    * apt-get install openal
    * Install AVBin (http://avbin.github.io/AVbin/Download.html)
    * Optional - (May need to perform additional steps to install PyAudio
    * Optional - brew install portaudio (MacOSX)
    * Optional - apt-get install portaudio ??( Unsure as yet)
    * Optional - sudo apt-get install swig -or- brew install swig  (For PocketSphinx)
    
### Notes:
PocketSphinx recognition isn't on par with Google API ... would prefer to have an offline
Solution for dealing with recognizing the one phrase but the detection isn't up to par.

