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

@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

editorAssetLib = GetEditorAssetLibrary()

processAssetPath = ""

allAssets = editorAssetLib.list_assets(workingPath, True, False)
allAssetsCount = len(allAssets)


with unreal.ScopedSlowTask(allAssetsCount, processAssetPath) as slowTask:
    slowTask.make_dialog(True)
    for processAsset in allAssets:
        _processAssetData = editorAssetLib.find_asset_data(processAsset)
        _processAsset = _processAssetData.get_asset()
        _processAssetName = _processAssetData.get_asset().get_name()
        processAssetPath = _processAssetData.get_asset().get_path_name()

        assetsMatching = []

        for asset in allAssets:
            _assetData = editorAssetLib.find_asset_data(asset)
            _assetName = _assetData.get_asset().get_name()

            if (_assetName == _processAssetName):
                if (asset != processAssetPath):
                    _assetLoaded = editorAssetLib.load_asset(asset)
                    assetsMatching.append(_assetData.get_asset())

        if (len(assetsMatching) != 0):
            editorAssetLib.consolidate_assets(_processAsset, assetsMatching)
            print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print (">>> The unifing process completed for %d assets" % len(assetsMatching))
            print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print (">>> There were no duplicates found for the selected asset")
            print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if slowTask.should_cancel():
            break
        slowTask.enter_progress_frame(1, asset)