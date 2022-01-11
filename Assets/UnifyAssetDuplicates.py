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
class EditorUtil(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

editorUtil = EditorUtil()
editorAssetLib = GetEditorAssetLibrary()

selectedAssets = editorUtil.get_selected_assets()
selectedAsset = selectedAssets[0]

selectedAssetName = selectedAsset.get_name()
selectedAssetPath = selectedAsset.get_path_name()

allAssets = editorAssetLib.list_assets(workingPath, True, False)
allAssetsCount = len(allAssets)

assetsMatching = []

with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as slowTask:
    slowTask.make_dialog(True)
    for asset in allAssets:
        _assetData = editorAssetLib.find_asset_data(asset)
        _assetName = _assetData.get_asset().get_name()

        if (_assetName == selectedAssetName):
            if (asset != selectedAssetPath):
                print (">>> There is a duplicate found for the asset %s located at %s" % (_assetName, asset))
                _assetLoaded = editorAssetLib.load_asset(asset)
                assetsMatching.append(_assetData.get_asset())
        if slowTask.should_cancel():
            break
        slowTask.enter_progress_frame(1, asset)


if (len(assetsMatching) != 0):
    editorAssetLib.consolidate_assets(selectedAsset, assetsMatching)
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print (">>> The unifing process completed for %d assets" % len(assetsMatching))
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
else:
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print (">>> There were no duplicates found for the selected asset")
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")