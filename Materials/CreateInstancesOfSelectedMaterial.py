#By Muhammad A.Moniem (@_mamoniem) www.mamoniem.com
#feel free to edit and/or use for any purpose :)
#It requires the Unreal python scripting plugin to be enabled first!

import unreal

#Set the instances count needed
totalRequiredInstances = 10

#General variables, will be auto set
newAssetName = ""
sourceAssetPath = ""
createdAssetsPath = ""

@unreal.uclass()
class EditorUtil(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class MaterialEditingLib(unreal.MaterialEditingLibrary):
    pass

editorUtil = EditorUtil()
materialEditingLib = MaterialEditingLib()

selectedAssets = editorUtil.get_selected_assets()

factory = unreal.MaterialInstanceConstantFactoryNew()

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

for selectedAsset in selectedAssets:
    newAssetName = selectedAsset.get_name() + "_%s_%d"
    sourceAssetPath = selectedAsset.get_path_name()

    createdAssetsPath = sourceAssetPath.replace(selectedAsset.get_name(), "-")
    createdAssetsPath = createdAssetsPath.replace("-.-", "")


    for x in range(totalRequiredInstances):

        newAsset = asset_tools.create_asset(newAssetName %("inst", x+1), createdAssetsPath, None, factory)

        materialEditingLib.set_material_instance_parent(newAsset, selectedAsset)