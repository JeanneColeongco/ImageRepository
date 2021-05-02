# ImageRepository

SEARCH FUNCTION - my assumptions/definitions/scope
* A user can search from characteristics of images. The characteristics I've included are: file type (string e.g. 'png'), the average rating by people who've bought it (integer), and price (float).
  * A user can search for multiple file types (space separated). In the frontend, a user might select from a number of checkboxes and the flags could be fed into this program.
  * When a user selects a rating, the results include that all images with that rating and higher. When a user selects a price, the results include that all images with that price and lower. In the front end, a user might use a slider to select these attributes and their input could be fed into this program.
* A user can also search from text related to the image. Text attributes of images I've include are: name, description, tags that are required and fixed (e.g. tags that correspond to menu options on the site to help people browse) and tags that are optional and freeform (e.g. tags that the sellers have added to their image to help potential buyers find them). 
  * A user can search like they would on any search engine (space-separated alphanumeric characters and symbols) 
* A user can search from an image they find on the site to find similar image. Each image in my database has an associated img_id that is a foreign key to the actual images database that would then hold the actual image file.
  * When a user selects an image to search by or if they know the img_id, they get results that match that image's file type, price (and lower), rating (and higher), and text information (scored by mongoDB). In the front end, the user might right click on an image and select a 'search' option or they might type the img_id into a search field.

MY TOOLS
* Python3 v3.9.0
* Embedded NoSQL (mongoDB v4.4.3)
* macOS

FILES
* search.py
* README.md
* searchdb_contents.csv
* mongoDBlog/
* test_input_char.txt
* test_input_text.txt
* test_input_img.txt

# HOW TO USE
1. Clone the repo: `git clone https://github.com/JeanneColeongco/ImageRepositorySearch.git`
2. Open 2 terminal windows.
3. In the first terminal window, type `mongod --port 27017 --dbpath mongoDBlog &`
4. In the second terminal window, type `python3 search.py`
5. The database and text search index is already loaded, but if you modify searchdb_contents.csv to achieve different search results, uncomment `load_searchdb()` in the main function and then repeat the previous step
6. Type your answers to the prompts to find the images you desire
