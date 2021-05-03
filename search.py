import pymongo
from pymongo import TEXT
import csv

myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
# mongod --port 27017 --dbpath mongoDBlog &
# can change port number if you want, just be sure to do it both in here and the terminal!

# has a foreign key to the actual imagesdb that contains image files
searchdb = myclient["searchdb"]

# in practice, searchdb would likely populate gradually along with the main imagesdb, each time a seller uploads a new image
# this function is for the sake of this implementation
def load_searchdb():
	global searchdb

	# if search_images collection exists, delete and make a new one
	search_collections = searchdb.list_collection_names()
	if 'search_images' in search_collections:
		search_images = searchdb['search_images']
		search_images.drop()

	search_images = searchdb['search_images']

	# read from file, insert into collection
	with open("searchdb_contents.csv", "r") as file:
		reader = csv.reader(file, delimiter='\t')
		header = next(reader)
		for row in reader: 
			search_document = { header[0]: int(row[0]), # img_id
								header[2]: row[2], # file type
								"text_info": row[1]+' '+ # name
											 row[3]+' '+ # description
											 row[4].replace(",", " ")+' '+ # site_tags
											 row[5].replace(",", " "), # seller_tags
								header[6]: int(row[6]), # buyer_rating
								header[7]: float(row[7]), # price
								header[8]: int(row[8]) # in_stock
								}
			searchdb.search_images.insert_one(search_document)
			# print(search_document) # for checking

	# index the text information (name, description, site_tags, seller_tags)
	searchdb.search_images.create_index([("text_info", TEXT)])


# retrieve db attributes based on img_id and search
def search_by_image(img_id):
	global searchdb
	query = searchdb.search_images.find_one({ 'img_id': int(img_id) })
	if query:
		keywords = query['text_info']
		file_type = []
		rating = query['buyer_rating']
		price = query['price']
		in_stock = query['in_stock']
		search(in_stock, price, rating, file_type, keywords)
	else:
		print("\nImage does not exist.")


# given user input, search
def search(in_stock, price, rating, file_type, keywords):
	global searchdb
	all_results = set()

	# search from text/characteristics
	keyword_query = searchdb.search_images.find({ "$text": {"$search": keywords} }, 
												{ 'score': { "$meta": "textScore" } }).sort([('score', {'$meta': 'textScore'})])

	# search from (more) characteristics
	file_type_query = searchdb.search_images.find({ "file_type": { "$in": file_type}},
												  { 'img_id': True, '_id': False })
	
	
	rating_query = searchdb.search_images.find({ "buyer_rating": { "$gte": int(rating)}},
												  { 'img_id': True, '_id': False })

	# price query handled this way because number input is not guaranteed
	# if no number, don't need to query for it and images of all prices are considered
	price_img_ids = []
	if price != "":
		price_query = searchdb.search_images.find({ "price": { "$lte": float(price)}},
												  { 'img_id': True, '_id': False })
		for p in price_query:
			price_img_ids.append(p['img_id'])
			all_results.add(p['img_id'])

	# in stock query because text input must convert to number
	# and "n" case, don't need to query for it and all images considered
	stock_img_ids = []
	if in_stock == "y":
		stock_query = searchdb.search_images.find({ "in_stock": 1},
												  { 'img_id': True, '_id': False })
		for s in stock_query:
			stock_img_ids.append(s['img_id'])
			all_results.add(s['img_id'])

	# we only need img_ids to retrieve image files from imagesdb
	file_type_img_ids = []
	keyword_img_ids = []
	rating_img_ids = []
	
	# for narrow down
	for r in rating_query:
		rating_img_ids.append(r['img_id'])
		all_results.add(r['img_id'])
	for f in file_type_query:
		file_type_img_ids.append(f['img_id'])
		all_results.add(f['img_id'])
	for k in keyword_query:
		keyword_img_ids.append(k['img_id'])
		all_results.add(k['img_id'])
	
	# narrow down
	narrowed = []
	# print(rating_img_ids, file_type_img_ids, price_img_ids, stock_img_ids, keyword_img_ids) # for checking
	for i in all_results:
		if len(keyword_img_ids) == 0 or i in keyword_img_ids:
			if len(file_type_img_ids) == 0 or i in file_type_img_ids:
				if len(price_img_ids) == 0 or i in price_img_ids:
					if len(stock_img_ids) == 0 or i in stock_img_ids:
						if len(rating_img_ids) == 0 or i in rating_img_ids:
							narrowed.append(i)

	# results output
	print("\nYou have " + str(len(narrowed)) + " result(s).")
	for img_id in narrowed:
		print(img_id)

	take_input() # loop


# user input
def take_input():
	# search by img_id, quit, or more search by characteristics/text instead
	to_do = input("Provide img_id if you wish to search by image.\nType 'q' if you wish to quit\nOtherwise, hit Enter for more search options: ")
	
	if to_do == "q":
		exit()
	elif to_do == "":
		file_type = input("Prefered image file type(s), space-separated: ").split()
		# if none is provided, all types will be shown

		price = input("Maximum price: ")
		# if none is provided, all prices will be shown
		try:
			price = float(price)
		except ValueError:
			price = ""

		# similar to price range filter (except will output results gte instead of lte)
		rating = input("Prefered rating: (1 --> 5) ")
		# if none is provided, all ratings will be shown
		try:
			rating = int(rating)
			if (rating < 1 and rating > 5):
				rating = 1
		except:
			rating = 1
		
		# assumes users search like on any search engine, with spaces between words
		keywords = input("Please input your search terms: ")
		# if none is provided all images will be shown

		in_stock = input("Must the item you're looking for be in stock? (y/n) ")

		search(in_stock, price, rating, file_type, keywords)
	
	# assume users can only search by an image that's in the database to find similar images
	# when searching by an image, all that is needed is the image id, the rest can be retrieved from there
	try:
		search_by_image(int(to_do))
		take_input()
	except:
		take_input()


def main():
	global searchdb
	load_searchdb() # can comment out if you already ran it at least once and haven't changed input csv since
	take_input() # it begins!


if __name__ == "__main__":
    main()