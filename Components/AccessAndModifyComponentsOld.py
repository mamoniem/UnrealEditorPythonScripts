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

#notice that this version affects only components that are (not) inherited. This is possibly due to unreal bug!
#inherited components usually have a blue icon, where none-inherited have gray icon

import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedActors = MyEditorUtility().get_selection_set()

for actor in selectedActors:
    unreal.log(actor.get_name())
    unreal.log("****************************************************")

    SMCompts = actor.get_components_by_class(unreal.StaticMeshComponent)
    for SMCompt in SMCompts:
        SMComptT = SMCompt.get_editor_property("relative_location")
        print(SMComptT)
        SMCompt.set_editor_property("relative_location", unreal.Vector(0.0, 0.0, 0.0))
        print(SMComptT)
