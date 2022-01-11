#										_
#									   (_)
#  _ __ ___   __ _ _ __ ___   ___  _ __  _  ___ _ __ ___
# | '_ ` _ \ / _` | '_ ` _ \ / _ \| '_ \| |/ _ \ '_ ` _ \
# | | | | | | (_| | | | | | | (_) | | | | |  __/ | | | | |
# |_| |_| |_|\__,_|_| |_| |_|\___/|_| |_|_|\___|_| |_| |_|
#					www.mamoniem.com
#					  www.ue4u.xyz
#Copyright 2022 Muhammad A.Moniem (@_mamoniem). All Rights Reserved.
#

import unreal

workingPath = "/Game/"
archivePath = "/Game/_ARCHIVE/"

@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

editorAssetLib = GetEditorAssetLibrary()

allAssets = editorAssetLib.list_assets(workingPath, True, False)

processingAssetPath = ""
allAssetsCount = len(allAssets)
if ( allAssetsCount > 0):
    with unreal.ScopedSlowTask(allAssetsCount, processingAssetPath) as slowTask:
        slowTask.make_dialog(True)
        for asset in allAssets:
            processingAssetPath = asset

            deps = editorAssetLib.find_package_referencers_for_asset(asset, False)
            if (len(deps) <= 0):
                print (">>> Archiving >>> %s" % asset)

                _assetData = editorAssetLib.find_asset_data(asset)
                _assetName = _assetData.get_asset().get_name()
                _assetPathName = _assetData.get_asset().get_path_name()

                _targetPathName = "%s%s%s%s" % (archivePath, _assetName, ".", _assetName)

                editorAssetLib.rename_asset(_assetPathName, _targetPathName)
                print(">>> the asset original Name [%s] and new  is [%s]" % (_assetPathName, _targetPathName))

            if slowTask.should_cancel():
                break
            slowTask.enter_progress_frame(1, processingAssetPath)