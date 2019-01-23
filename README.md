# ## UnrealEditorPythonScripts ##
Some of my personal scripts i made to use for my own projects, but free of charge to be used for any project and any purpose as long as it is not violating the Unreal Engine EULA.

In order to be able to sue those helper scripts, you must be sure this plugins are enabled first:

1. Scripting/Python Editor Script Plugin
2. Scripting/Editor Scripting Utilities

You can watch scripts in action in the play-list below (click the image):

[![](http://www.mamoniem.com/wp-content/uploads/2019/01/2019-01-21-02_05_42-pythonScriptsYoutubeThumbnails.psd-@-66.7-RGB_8-_.png)](https://www.youtube.com/playlist?list=PLTfMG1EpxB2ewNOlE1vFNqIGqPzgkqVk6)

Don't forget to follow this repo, [YouTube](http://www.youtube.com/channel/UCBBcKlWecOLdywouiZPGkgg) or [Twitter](https://twitter.com/_mamoniem) account in order to keep updated with the latest scripts.

## Aimation ##

- **[CleanNotifiesFromAnimations.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Animation/CleanNotifiesFromAnimations.py)** Run on a selected single or multiple animation file(s) in order to clean up the selected file(s) from any animation notifies. 

## Assets ##

- **[ReportUnusedAssets.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Assets/ReportUnusedAssets.py)** Running this script will look through all the project folders, and add to the log the assets that were found not in a use, or in another word, the assets that have no dependency with any other project files.
- **[DeleteUnusedAssets.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Assets/DeleteUnusedAssets.py)** Running this script will look through all the project folders, and delete the assets that were found not in a use, or in another word, the assets that have no dependency with any other project files. Note that, running this script won't show a confirmation message or accepting dialogue box, it will force delete the assets right a way, so make sure to evaluate the change before submitting to your repo.

## Materials ##
- **[CreateInstancesOfSelectedMaterial.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Materials/CreateInstancesOfSelectedMaterial.py)** Run on a selected single or multiple Material file(s) in order to generate material instances of it/them. The number of the final generated instances count can be set within the script before running, by changing the value of the variable *totalRequiredInstances*