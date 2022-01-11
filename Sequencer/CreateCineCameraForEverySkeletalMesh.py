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
class MyEditorLvelLib(unreal.EditorLevelLibrary):
    pass

allLevelActors = MyEditorLvelLib().get_all_level_actors()

for actor in allLevelActors:
    if (actor.get_class() == unreal.SkeletalMeshActor.static_class()):

        unreal.log("Adding camera to actor: [%s]" % (actor.get_name()))

        actor_class = unreal.CineCameraActor
        actor_location = actor.get_actor_location() + (actor.get_actor_right_vector() * 200) #move it slightly to the front of the character
        actor_location.z += 150 #move on up vec (z) to fit the Mannequin head hight
        actor_rotation = actor.get_actor_rotation()
        _spawnedActor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, actor_rotation)

        _focusSettings = unreal.CameraFocusSettings()
        _focusSettings.manual_focus_distance = 1320.0
        _focusSettings.focus_method = unreal.CameraFocusMethod.MANUAL
        _focusSettings.focus_offset = 19.0
        _focusSettings.smooth_focus_changes = False

        _lookAtSettings = unreal.CameraLookatTrackingSettings()
        _lookAtSettings.actor_to_track = actor
        _lookAtSettings.allow_roll = True
        _lookAtSettings.enable_look_at_tracking = True
        _lookAtSettings.relative_offset  = unreal.Vector(0.0,0.0,150.0)

        _cineCameraComponent = _spawnedActor.get_cine_camera_component()
        _cineCameraComponent.set_editor_property("focus_settings", _focusSettings)

        _spawnedActor.lookat_tracking_settings = _lookAtSettings

        unreal.log("****************************************************")