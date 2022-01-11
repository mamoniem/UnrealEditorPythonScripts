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

#notice that this version works with both type of blueprint/actor components inherited & none-inherited.
#inherited components usually have a blue icon, where none-inherited have gray icon

import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedActors = MyEditorUtility().get_selection_set()

for actor in selectedActors:
    unreal.log(actor.get_name())
    unreal.log("*************************************************")

    SMCompts = actor.root_component.get_children_components(True)
    comptsCount = len(SMCompts)
    print("Found [%d] components attached to the root"%(comptsCount))
    for SMCompt in SMCompts:
        print ("Checking compontnt [%s] which is [%s] if StaticMeshComponent"%(SMCompt.get_name(), SMCompt.get_class().get_name()))
        if (SMCompt.get_class().get_name() == "StaticMeshComponent"):
            print(">>TRUE")
            SMComptT = SMCompt.relative_location
            print(SMComptT)
            SMCompt.set_relative_location(unreal.Vector(0.0, 0.0, 0.0), False, True)
            print(SMComptT)
        else:
            print(">>FALSE")
