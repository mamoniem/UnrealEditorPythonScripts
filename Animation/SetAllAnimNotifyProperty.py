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
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

@unreal.uclass()
class GetAnimationLibrary(unreal.AnimationLibrary):
    pass

editorUtility = GetEditorUtility()
animLib = GetAnimationLibrary()

selectedAssets = editorUtility.get_selected_assets()

for selectedAsset in selectedAssets:
    allEventsForSelectedAsset = animLib.get_animation_notify_events(selectedAsset)
    if len(allEventsForSelectedAsset) != 0:
        print("For the animation [%s] found [%d] notifies" % (selectedAsset.get_name(), len(allEventsForSelectedAsset)))
		
        selectedAsset.modify(True)
		
        for notifyEvent in allEventsForSelectedAsset:
		
            notifyEvent.set_editor_property("trigger_on_dedicated_server", False)
            notifyEvent.set_editor_property("trigger_on_follower", True)
            notifyEvent.set_editor_property("notify_trigger_chance", 0.5)

            #Can also change the memebr variables right away, they are exposed as memebers to python API
            #notifyEvent.trigger_on_dedicated_server = False
            #notifyEvent.trigger_on_follower = True
            #notifyEvent.notify_trigger_chance = 0.5

            #Can get some more detials about the notify, like it's name & color
            notifyItself = notifyEvent.notify
            Notifycolor =  notifyItself.notify_color
            NotifyName =  notifyItself.get_notify_name()
            print("The notify [%s] has the color is {%d, %d, %d, %d}" % (NotifyName, Notifycolor.r, Notifycolor.g, Notifycolor.b, Notifycolor.a))

            #Can also change the notify colors. Keep in mind we can't use the notifyItself.notify_color as it is read-only, but we can use the set_editor_property("notify_color", VALUE)
            clr = unreal.Color(0, 0, 255, 255)
            notifyItself.set_editor_property("notify_color", clr)
    else:
        print("No notifies found within the animation [%s]" % (selectedAsset.get_name()))