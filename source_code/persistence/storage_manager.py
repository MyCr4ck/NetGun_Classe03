import sys
sys.path.insert(0,"../../../NetGun_Classe03")
import os, pickle
from source_code.business_logic.testing_misconfigurations.services_misconfigurations import Services_misconfigurations
from source_code.business_logic.tips.tip import Tip
from source_code.business_logic.tutorial.tutorial_collection import Tutorial_collection

class Storage_manager:
    MISCONFIGURATIONS_XML_PATH = "../../persistence/storage/misconfiguration.xml"
    MISCONFIGURATIONS_PKL_PATH = "../../persistence/storage/misconfigurations.pkl"

    TIPS_XML_PATH = "../../persistence/storage/tip.xml"
    TIPS_PKL_PATH = "../../persistence/storage/tip.pkl"

    TUTORIALS_XML_PATH = "../../persistence/storage/tutorial.xml"
    TUTORIALS_PKL_PATH = "../../persistence/storage/tutorial.pkl"

    @classmethod
    def load_resource(cls, xml_path, pkl_path, create_object_from_file):
        if os.path.exists(pkl_path):
            return Storage_manager.deserialize_object_from_file(pkl_path)
        else:
            obj = create_object_from_file(xml_path)
            Storage_manager.serialize_object_into_file(obj,pkl_path)
            return obj
    @classmethod
    def deserialize_object_from_file(cls,file):
        obj = None
        with open(file, 'rb') as f:
            # Deserialize the object
            obj = pickle.load(f)
        return obj

    @classmethod
    def serialize_object_into_file(cls,obj,file):
        with open(file, 'wb') as f:
            # Serialize the object
            pickle.dump(obj,f)

    @classmethod
    def load_misconfigurations(cls):
        return Storage_manager.load_resource(Storage_manager.MISCONFIGURATIONS_XML_PATH, Storage_manager.MISCONFIGURATIONS_PKL_PATH, Services_misconfigurations.inizialize_object_from_file_xml)

    @classmethod
    def load_tips(cls):
        return Storage_manager.load_resource(Storage_manager.TIPS_XML_PATH, Storage_manager.TIPS_PKL_PATH, Tip.parse_tips_from_file)

    @classmethod
    def load_tutorials(cls):
        return Storage_manager.load_resource(Storage_manager.TUTORIALS_XML_PATH, Storage_manager.TUTORIALS_PKL_PATH, Tutorial_collection.inizialize_object_from_file_xml)

if __name__ == "__main__":
    for i in Storage_manager.load_tutorials().tutorials_dict:
        Storage_manager.load_tutorials().tutorials_dict[i].print_toString()