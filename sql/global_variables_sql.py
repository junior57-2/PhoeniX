# global variables will be assigned here
# can be imported in any module to make life easier.
from heroku_config import Var
LOGGER = Var.PRIVATE_GROUP_ID
PACK_NAME = Var.PACK_NAME
ANIM_PACK_NAME = Var.ANIM_PACK_NAME
PACKS = Var.PACKS_CONTENT
DL = Var.TEMP_DOWNLOAD_DIRECTORY
# add modules to this list using MODULES_LIST.append(MODULE_NAME)
MODULE_LIST = []
# add error to this list using ERROR.append(ERROR_NAME)
ERROR = []
# add syntax to this dictionary using SYNTAX.update()
SYNTAX = {}
# add errors to this dictionary using ERRORS.update()
ERRORS = {}
BUILD = "USER-49x03"
