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
# This file was built while supporting user of the python course

import unreal

#your lines to spawn the actor, i did use them as is, nothing changed
actor_class = unreal.CineCameraActor
actor_location = unreal.Vector(0.0,0.0,0.0)
actor_rotation = unreal.Rotator(0.0,0.0,0.0)
_spawnedActor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, actor_rotation)

#make the focus settings class, and set some values that we need
_focusSettings = unreal.CameraFocusSettings()
_focusSettings.manual_focus_distance = 1320.0
_focusSettings.focus_method = unreal.CameraFocusMethod.MANUAL
_focusSettings.focus_offset = 19.0
_focusSettings.smooth_focus_changes = False

#Apply the focus settings to the camera we made
_cineCameraComponent = _spawnedActor.get_cine_camera_component()
_cineCameraComponent.set_editor_property("focus_settings",_focusSettings)