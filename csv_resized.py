import csv

with open("train_labels.csv") as ct:
	reader= csv.reader(ct,delimiter=",")
	with open("train_labels_resized.csv","w") as ctr:
		writer = csv.writer(ctr, delimiter=',')
		for index,row in enumerate(reader):
			if index==0:
				writer.writerow(row)
				continue
			row[1]=int(int(row[1])/4)
			row[2]=int(int(row[2])/4)
			row[4]=int(int(row[4])/4)
			row[5]=int(int(row[5])/4)
			row[6]=int(int(row[6])/4)
			row[7]=int(int(row[7])/4)
			print(row)
			writer.writerow(row)
	# title=next(reader)
	# print(title)
		# print(row)
