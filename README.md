# ImageRepository

## SEARCH FUNCTION
### My assumptions/definitions/scope
* I'm interpreting this task as a search function for a marketplace app for artists and photographers, but it can easily be adapted for other types of online stores that people might want to search through for images.
* A user can search from characteristics of images. The characteristics I've included are: file type (string e.g. 'png'), the average rating by people who've bought it (integer), price (float), and whether an item is in stock (boolean).
  * A user can search for multiple file types (space separated). In the frontend, a user might select from a number of checkboxes and the flags could be fed into this program.
  * When a user selects a rating, the results include that all images with that rating and higher. When a user selects a price, the results include that all images with that price and lower. In the front end, a user might use a slider to select these attributes and their input could be fed into this program.
  * When a user only wants to view images of what sellers currently have "in stock" (e.g. for prints and paintings), then only those images will appear in the results. Otherwise, all images that match the other search parameters will appear. In the frontend, a user might select whether they care that an item is in stock via a single checkbox and the flags could be fed into this program.
* A user can also search from text related to the image. Text attributes of images I've include are: name, description, tags that are required and fixed (e.g. tags that correspond to menu options on the site to help people browse) and tags that are optional and freeform (e.g. tags that the sellers have added to their image to help potential buyers find them). 
  * A user can search like they would on any search engine (space-separated alphanumeric characters and symbols) 
* A user can search from an image they find on the site to find similar image. Each image in my database has a unique img_id that is a foreign key to the actual images database that would then hold the actual image file.
  * When a user selects an image to search by or if they know the img_id, they get results that match that image's file type, price (and lower), rating (and higher), and text information (scored by mongoDB). In the front end, the user might right click on an image and select a 'search' option or they might type the img_id into a search field.
  * The results are the img_ids that can be used to key into the images database where the actual image files to be rendered are stored.

## MY TOOLS
* Python3 v3.9.0
* Embedded NoSQL (mongoDB v4.4.3) - flexible for future as it doesn't require a schema (easily scalable for more or less or different attributes), cheaper to set up

## FILES
* search.py - the program
* README.md - YOU ARE HERE :)
* searchdb_contents.csv — a small sample of data
* mongoDBlog/ - the database
* test_cases/ - for multiple inputs

# HOW TO USE
1. Clone the repo: `git clone https://github.com/JeanneColeongco/ImageRepositorySearch.git`
2. Open 2 terminal windows.
3. In the first terminal window, type `mongod --port 27017 --dbpath mongoDBlog &`
4. In the second terminal window, type `python3 search.py`
5. The database and text search index is already loaded, but if you modify searchdb_contents.csv to achieve different search results, uncomment `load_searchdb()` in the main function and then repeat the previous step
6. Type your answers to the prompts to find the images you desire
7. Repeat the previous step as many times as you like!

# TEST CASES
* The expected results are the img_ids that can be used to key into the images database where the actual image files to be rendered are stored.
1. *All blank:* Keep hitting enter until you're taken back to the first prompt. You should see all the image ids in the database.  
2. *Search by img_id:* If you're using the original searchdb_contents.csv type `2840` ("Finding Dory") and you will also find 22891 ("Finding Nemo")
3. *Search by file type only:* Hit enter to skip past the search by image option. If you're using the original searchdb_contents.csv type `png` and `jpeg` Hit enter until you're taken back to the first prompt. You should get 72266 ("Wind-swept Horse") and 40895 ("Cute Puppy").
4. *Search by price only:* Hit enter 2 times to skip past the search by image option and the file type option. If you're using the original searchdb_contents.csv type `2.50`. Hit enter until you're taken back to the first prompt. You should get 72266	("Wind-Swept Horse"), 22891 ("Finding Nemo") and 2840 ("Finding Dory").
5. *Search by rating only:* Hit enter 3 times to skip to the rating selection. If you're using the original searchdb_contents.csv type `4`. Hit enter until you're taken back to the first prompt. You should get 72266 ("Wind-swept Horse") and 40895 ("Cute Puppy").
6. *Search by text only:* Hit enter 4 times skip to the text search. If you're using the original searchdb_contents.csv type `wild`. Hit enter to get 72266 ("Wind-swept Horse").
7. *Search by multiple categories:* Select a `test_X.txt` from the `test_cases/` folder where X is a number between 1 and 9. In response to the first prompt, Copy and paste the contents into the terminal window. The expected result will be contained within `test_result_X.txt` in the `test_cases/` folder.
