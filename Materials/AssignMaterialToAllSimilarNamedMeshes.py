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
selectedAssetMesh = selectedAssets[0]
selectedAssetMaterial = selectedAssets[1]

selectedAssetName = selectedAssetMesh.get_name()
selectedAssetPath = selectedAssetMesh.get_path_name()
selectedAssetClass = selectedAssetMesh.get_class()

allAssets = editorAssetLib.list_assets(workingPath, True, False)
allAssetsCount = len(allAssets)

assetsMatching = []
assetsMatching.append(selectedAssetMesh)

with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as slowTask:
    slowTask.make_dialog(True)
    for asset in allAssets:
        _assetData = editorAssetLib.find_asset_data(asset)
        _assetName = _assetData.get_asset().get_name()
        _assetClass = _assetData.get_asset().get_class()

        if (_assetName == selectedAssetName):
            if (asset != selectedAssetPath):
                print (">>> There is a duplicate found for the asset %s located at %s" % (_assetName, asset))
                _assetLoaded = editorAssetLib.load_asset(asset)
                if(_assetClass == selectedAssetClass):
                    assetsMatching.append(_assetData.get_asset())
        if slowTask.should_cancel():
            break
        slowTask.enter_progress_frame(1, asset)


if (len(assetsMatching) != 0):
    for x in range(len(assetsMatching)):
        editorAssetLib.load_asset(assetsMatching[x].get_path_name())
        assetsMatching[x].set_material(0, selectedAssetMaterial)