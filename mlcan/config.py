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



QUOTE_ACTIVITY = 'quote'
REPAIR_ACTIVITY = 'repair'
INSPECTION_ACTIVITY = 'inspection'

READY_FOR_BILLING = 'ready for billing'
BILLED = 'billed'
REPAIR_DONE = 'repair done'

INSPECTION_STATE_IDLE = 'idle'
INSPECTION_STATE_DRAFT = 'inspection draft'
INSPECTION_STATE_DONE = 'inspection done'
INSPECTION_STATE_READY_FOR_BILLING = READY_FOR_BILLING
INSPECTION_STATE_BILLED = BILLED
INSPECTION_STATE_ORDER = [INSPECTION_STATE_IDLE,INSPECTION_STATE_DRAFT,INSPECTION_STATE_DONE,INSPECTION_STATE_READY_FOR_BILLING, INSPECTION_STATE_BILLED]

QUOTE_STATE_IDLE = 'idle'
QUOTE_STATE_DRAFT = 'quote draft'
QUOTE_STATE_PENDING = 'quote pending'
QUOTE_STATE_ISSUED = 'quote issued'
QUOTE_STATE_APPROVED = 'quote approved'
QUOTE_STATE_REPAIR_DONE = REPAIR_DONE
QUOTE_STATE_READY_FOR_BILLING = READY_FOR_BILLING
QUOTE_STATE_BILLED = BILLED
QUOTE_STATE_ORDER = [QUOTE_STATE_IDLE,QUOTE_STATE_DRAFT, QUOTE_STATE_PENDING, QUOTE_STATE_ISSUED, QUOTE_STATE_APPROVED, QUOTE_STATE_REPAIR_DONE, QUOTE_STATE_READY_FOR_BILLING, QUOTE_STATE_BILLED]


REPAIR_STATE_IDLE = 'idle'
REPAIR_STATE_DRAFT = 'repair draft'
REPAIR_STATE_PENDING = 'repair pending'
REPAIR_STATE_DONE = REPAIR_DONE
REPAIR_STATE_READY_FOR_BILLING = READY_FOR_BILLING
REPAIR_STATE_BILLED = BILLED
REPAIR_STATE_ORDER = [REPAIR_STATE_IDLE,REPAIR_STATE_DRAFT, REPAIR_STATE_BILLED, REPAIR_STATE_DONE, REPAIR_STATE_READY_FOR_BILLING, REPAIR_STATE_DONE]



ALL_ACTIVE_LIST = set()
ALL_ACTIVE_LIST.update(INSPECTION_STATE_ORDER.copy())
ALL_ACTIVE_LIST.update(REPAIR_STATE_ORDER.copy())
ALL_ACTIVE_LIST.update(QUOTE_STATE_ORDER.copy())
ALL_ACTIVE_LIST.remove(READY_FOR_BILLING)
ALL_ACTIVE_LIST.remove(BILLED)


ADD_REPAIR_QUOTE = ['repair','quote']
ADD_REPAIR_QUOTE_ATTACHMENTS = ['damaged_area','repair_area']