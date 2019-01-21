import unreal

@unreal.uclass()
class GetEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class GetAnimationLibrary(unreal.AnimationLibrary):
    pass

editorUtility = GetEditorUtility()
animLib = GetAnimationLibrary()

selectedAssets = editorUtility.get_selected_assets()

for selectedAsset in selectedAssets:
    selectedAsset.modify(True)
    animLib.remove_all_animation_notify_tracks(selectedAsset)