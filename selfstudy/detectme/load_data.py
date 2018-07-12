from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo,
                      RelationshipFrom,db)
import yaml
import csv
from models import *
config.DATABASE_URL = 'bolt://neo4j:DetectMe@localhost:11002'

def load_productcategories():
    names = ['Coffee_tables','Chairs','Lamps','Sofas']
    for i in range(0,len(names)):
        ProductsCategory(name = names[i]).save()

def load_product():
    # with open("..\data\chairs_names.txt", 'r') as stream:
        Chairs = yaml.load(open("../data/chairs_names.txt"))
        Coffee_tables = yaml.load(open("../data/coffee_tables_names.txt"))
        Lamps  = yaml.load(open("../data/lamps_names.txt"))
        Sofas = yaml.load(open("../data/sofas_names.txt"))
        list = [Chairs,Coffee_tables,Lamps,Sofas]
        names = ['Chairs','Coffee_tables','Lamps','Sofas']
        for i in range(0,len(names)):
            product_cat = ProductsCategory.nodes.get(name = names[i])
            for j in range(1,len(list[i])+1):
                prod = Product(name = list[i][j-1],label_id = j).save()
                product_cat.product.connect(prod)


#load_productcategories()
def add_properties(file):
	count = 0
	with open(file) as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			name = line["Name"]
			try:
				prod = Product.nodes.get(name = name)
				prod.price = line["Price"]
				prod.save()
				count+=1
			except Product.DoesNotExist:
				print(" ")
		print(count)

def add_brand_relation(file):
	with open(file) as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			name = line["Name"]
			try:
				prod = Product.nodes.get(name = name)
				try:
					brand = Brand.nodes.get(b_name = line["Brand"])
				except Brand.DoesNotExist:
					brand = Brand(b_name = line["Brand"]).save()
				prod.brand_rel.connect(brand)
			except:
				print(" ")
	
def add_primarymaterial_relation(file):
	with open(file) as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			name = line["Name"]
			try:
				prod = Product.nodes.get(name = name)
				try:
					prime_mat = Primary_Material.nodes.get(pm_name = line["Primary_material"])
				except Primary_Material.DoesNotExist:
					prime_mat= Primary_Material(pm_name = line["Primary_Material"]).save()
				prod.prime_rel.connect(prime_mat)
			except:
				print(" ")
	

load_productcategories()
load_product()
add_properties("sofas.csv")
add_brand_relation("sofas.csv")
add_properties("chairs.csv")
add_brand_relation("chairs.csv")
add_properties("coffee_tables.csv")
add_brand_relation("coffee_tables.csv")
add_properties("lamps.csv")
add_brand_relation("lamps.csv")
