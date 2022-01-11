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

allAssets = editorAssetLib.list_assets(workingPath, True, False)
allAssetsCount = len(allAssets)

selectedAssetPath = workingPath

with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as slowTask:
    slowTask.make_dialog(True)
    for asset in allAssets:
        _assetData = editorAssetLib.find_asset_data(asset)
        _assetName = _assetData.get_asset().get_name()
        _assetPathName = _assetData.get_asset().get_path_name()
        _assetClassName = _assetData.get_asset().get_class().get_name()

        _targetPathName = "/Game/%s%s%s%s%s" % (_assetClassName, "/", _assetName, ".", _assetName)


        editorAssetLib.rename_asset(_assetPathName, _targetPathName)

        if slowTask.should_cancel():
            break
        slowTask.enter_progress_frame(1, asset)