from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo,
                      RelationshipFrom,db)
import yaml
import csv
from models import *
config.DATABASE_URL = 'bolt://neo4j:DetectMe@localhost:11002'
def brand_traversal():
	