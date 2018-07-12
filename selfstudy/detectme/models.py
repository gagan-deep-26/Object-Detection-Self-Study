from django.db import models
from neomodel import (BooleanProperty,DateTimeProperty,config,JSONProperty,FloatProperty,StructuredNode, StructuredRel,StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, RelationshipFrom,EmailProperty,Relationship)
# Create your models here.

class Color(StructuredNode):
    name = StringProperty()
    created_at = DateTimeProperty()
    updated_at = DateTimeProperty()

class Style(StructuredNode):
    name = StringProperty()
    created_at = DateTimeProperty()
    updated_at = DateTimeProperty()

    products = RelationshipTo('Product','PRODUCT_STYLE')

class ProductsCategory(StructuredNode):
    name = StringProperty()
    created_at = DateTimeProperty()
    updated_at = DateTimeProperty()

    subcategory = Relationship('ProductsCategory','SUB_CATEGORY')
    product = RelationshipTo('Product','HAS_PRODUCT')


class Product(StructuredNode):
    created_at = DateTimeProperty()
    updated_at = DateTimeProperty()
    name = StringProperty()
    label_id = IntegerProperty()
    price = FloatProperty()
    color = StringProperty()
    style = StringProperty()

    similar = Relationship('Product','SIMILARITY_SCORE')
    category = RelationshipFrom('ProductsCategory','HAS_PRODUCT')
    styles = RelationshipFrom('Style','PRODUCT_STYLE')
    brand_rel = RelationshipTo('Brand','BRAND')
    prime_rel = RelationshipTo('Primary_Material','PRIMARY MATERIAL')

class Brand(StructuredNode):
    b_name = StringProperty()

class Primary_Material(StructuredNode):
    pm_name = StringProperty()

