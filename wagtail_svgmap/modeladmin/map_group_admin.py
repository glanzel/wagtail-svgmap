from wagtail.contrib.modeladmin.options import ModelAdminGroup
from .image_maps import ImageMapModelAdmin
from .regions import RegionModelAdmin

class MapGroup(ModelAdminGroup):
    menu_label = 'Map'
    menu_icon = 'site'
    items = (ImageMapModelAdmin, RegionModelAdmin)