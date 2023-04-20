import pyttsx3
import platform
"""
PowerShell code to make the extra installed Narrator voices available to pyttsx3

$sourcePath = 'HKLM:\software\Microsoft\Speech_OneCore\Voices\Tokens' #Where the OneCore voices live
$destinationPath = 'HKLM:\SOFTWARE\Microsoft\Speech\Voices\Tokens' #For 64-bit apps
$destinationPath2 = 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\SPEECH\Voices\Tokens' #For 32-bit apps
cd $destinationPath
$listVoices = Get-ChildItem $sourcePath
foreach($voice in $listVoices)
{
$source = $voice.PSPath #Get the path of this voices key
copy -Path $source -Destination $destinationPath -Recurse
copy -Path $source -Destination $destinationPath2 -Recurse
}
"""
def VertelMij(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if platform.system() == 'Windows':
        engine.setProperty('voice', voices[0].id) #for the default US Male voice
    else:
        engine.setProperty('voice', 'dutch') #for the default US Male voice
    #engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_nlNL_Frank')
    engine.setProperty('rate', 150)
    #print(text)
    engine.say(text)
    engine.runAndWait()

#VertelMij("Twee kilo bananen en een blik soep")  