from ma import ma
from models.store import StoreModel
from models.item import ItemModel
from schemas.item import ItemSchema


class StoreSchema(ma.Schema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = StoreModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
