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
mastersWithTwoSided = 0
instancesWithTwoSided = 0

if (allAssetsCount > 0):
    with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as slowTask:
        slowTask.make_dialog(True)
        for asset in allAssets:
            assetData = editorAssetLib.find_asset_data(asset)
            selectedAssetPath = assetData.asset_name
            if(assetData.asset_class == "Material"):
                if(assetData.get_asset().get_editor_property("two_sided") == True):
                    unreal.log_warning("Master material [%s] is TWO-SIDED" % assetData.asset_name)
                    mastersWithTwoSided += 1
                else:
                    unreal.log("Master material [%s] OK" % assetData.asset_name)
            elif (assetData.asset_class == "MaterialInstance" or assetData.asset_class == "MaterialInstanceConstant"):
                baseOverrides = assetData.get_asset().get_editor_property("base_property_overrides")
                if (baseOverrides.get_editor_property("override_two_sided") == True):
                    unreal.log_warning("Material Instance [%s] is TWO-SIDED" % assetData.asset_name)
                    instancesWithTwoSided += 1
                else:
                    unreal.log("Material Instance [%s] OK" % assetData.asset_name)

                if slowTask.should_cancel():
                    break
                slowTask.enter_progress_frame(1, asset)

    unreal.log_warning("Found [%d] Master Materials && [%d] Material Instance that hast the Two-Sided flag" % (mastersWithTwoSided, instancesWithTwoSided))