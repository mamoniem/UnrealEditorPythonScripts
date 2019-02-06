#UnrealEditorPythonScripts#
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
- **[UnifyAssetDuplicates.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Assets/UnifyAssetDuplicates.py)** Run on a selected single asset in order to look through the project for similar assets with the same name, and will remove all of them, and replace all their references with the selected one. This is a very common case if for example have added several packs or assets to the project and you will end up with several files (textures, materials or such) that have the same exact name and parameters *(add Paragon characters for example to a single project could result that)*, but a unique version coming from each imported pack; and there it come the usage of that script in unifying them.
- **[UnifyAllAssetsDuplicates.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Assets/UnifyAllAssetsDuplicates.py)** It working the same as the previous script (UnifyAssetDuplicated) except this time, you don't have to select any asset. The script will run through the entire project seeking any asset duplicated (same type & same name) and will unify them into one version only.
- **[OrganizeAssetsPerType.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Assets/OrganizeAssetsPerType.py)** When you start new project, you don't have to worry about organizing the assets per family in folders. Just go ahead and focus on building the prototype or content, and then execute that script at any moment will make sure to move all the assets from the same type (*UClass*) to their own folder.
- **[PrefixAllAssets.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Assets/PrefixAllAssets.py)** Running this script will apply prefix to majority of the files. While those prefixes I used are more subjective to my own pipeline, but you can modify them simply by opening the script and set the prefix of your choice per file type at the top of the script. You can also add more cases if not exist!

## Materials ##
- **[CreateInstancesOfSelectedMaterial.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Materials/CreateInstancesOfSelectedMaterial.py)** Run on a selected single or multiple Material file(s) in order to generate material instances of it/them. The number of the final generated instances count can be set within the script before running, by changing the value of the variable *totalRequiredInstances*
- **[AssignMaterialToAllSimilarNamedMeshes.py](https://github.com/mamoniem/UnrealEditorPythonScripts/blob/master/Materials/AssignMaterialToAllSimilarNamedMeshes.py)** Select a static mesh and then a material *(Yup, has to be in that order)* and run the script in order to run through the project looking for similar static meshes, and then assign the selected material to all of found clones of that mesh. The script can be extended easily to add more materials in case of the mesh is not using a single material slot.