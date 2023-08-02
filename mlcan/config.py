from enum import Enum


COMMENT_ORIGIN_ALLOWED = ['container','activity']

class COMMENT_TYPE(Enum):
    REPAIR = 'repair'
    QUOTE = 'quote'
    INSPECTION = 'inspection'
    CONTAINER = 'container'
    INVOICE = 'invoice'

class CONTAINER_IMAGE_TYPE(Enum):
    DOOR_PHOTO = 'door_photo'
    LEFT_SIDE_PHOTO = 'left_side_photo'
    RIGHT_SIDE_PHOTO = 'right_side_photo'
    FRONT_SIDE_PHOTO = 'front_side_photo'
    INTERIOR_PHOTO = 'interior_photo'
    UNDERSIDE_PHOTO = 'underside_photo'
    ROOF_PHOTO = 'roof_photo'
    CSC_PLATE_PHOTO = 'csc_plate_photo'


DEFAULT_PAGE_SIZE = 10

CONTAINER_FILTER_FIELDS = ['customer','yard']

MERC_UPDATE = 'merc_update'
NON_MERC_UPDATE = 'non_merc_update'
MERC_TYPE = 'merc'
NON_MERC_TYPE = 'non_merc'
VERSION_PARAM = 'version'

MERC_REPAIR_LIST_OBJ = ['repair_serializer_type','max_material_cost','unit_material_cost','hour_per_cost','max_price','units','repair_mode','mode_number','repair_code','combined','description','id_source']
MERC_REPAIR_LIST = ['repair_component_type_id','repair_id','version','container_repair_area_id','container_damaged_area_id','repair_type_id']

NON_MERC_REPAIR_LIST_OBJ = ['repair_serializer_type','hours','material_cost','container_section','damaged_area','repair_type','description','comp_id','rep_id','dam_id','component_id','event_id','location','lgth_qty_area','lgth_qty_area2','id_source']
NON_MERC_REPAIR_LIST = ['repair_component_type_id','repair_id','version','container_repair_area_id','container_damaged_area_id','repair_type_id','is_deleted']
