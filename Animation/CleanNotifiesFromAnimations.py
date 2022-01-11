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