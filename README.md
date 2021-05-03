# ImageRepository

### SEARCH FUNCTION
#### My assumptions/definitions/scope
* I'm interpreting this task as a search function for a marketplace app for artists and photographers, but it can easily be adapted for other types of online stores that people might want to search through for images.
* A user can search from characteristics of images. The characteristics I've included are: file type (string, e.g. 'png'), the average rating by people who've bought it (integer, range 1-->5), price (float), and whether an item is in stock (boolean, 1 or 0).
  * A user can search for multiple file types (space separated text). In the frontend, a user might select file types from a number of checkboxes and the flags could be fed into this program.
  * When a user selects a rating, the results include that all images with that rating and higher. When a user selects a price, the results include that all images with that price and lower. In the front end, a user might use a slider to select these attributes and their input could be fed into this program.
  * When a user only wants to view images of what sellers currently have "in stock", then only those images will appear in the results. Otherwise, all images that match the other search parameters will appear. In the frontend, a user might select whether they care that an item is in stock via a single checkbox and the flag could be fed into this program.
* A user can also search from text related to the image. Text attributes of images I've include are: name, description, tags that are required and fixed (e.g. tags that correspond to menu options on the site to help people browse) and tags that are optional and freeform (e.g. tags that the sellers have added to their image to help potential buyers find them). 
  * A user can search like they would on any search engine (alphanumeric characters and symbols, space-separated words) 
* A user can search from an image they find on the site to find similar image. Each image in my search database has a unique img_id that is a foreign key to the actual images database that would then hold the actual image file. The search database itself only needs to contain attributes that may be relevant to the search, not the actual image file.
  * When a user searches by image (via img_id), they get results that match that image's file type, price (and lower), rating (and higher), in stock boolean, and text information (scored by mongoDB). In the front end, the user might right click on an image and select a 'search' option or they might type the img_id into a search field.
* The results of any type of search are the img_ids that can be used to key into the images database where the actual image files to be rendered are stored.

### MY TOOLS
* Python3 v3.9.0
* Embedded NoSQL (mongoDB v4.4.3) - flexible for future development as it doesn't require a schema (easily scalable for more or less or different attributes), cheaper to set up

### FILES
* *search.py* - the program
* *README.md* - YOU ARE HERE :)
* *searchdb_contents.csv* — a sample of data
* *test_cases/* - see Test Cases section #3 for usage instructions

### HOW TO USE
1. Clone the repo: `git clone https://github.com/JeanneColeongco/ImageRepositorySearch.git`
2. Open 2 terminal windows.
3. In the first terminal window, type `mkdir mongoDBlog` followed by `mongod --port 27017 --dbpath mongoDBlog &`
4. In the second terminal window, type `python3 search.py`
5. If you haven't made any changes to searchdb_contents.csv but want to repeat step 4, you can comment out `load_searchdb()` in the `main()` function
6. Type your answers to the prompts to find the images you desire
7. Repeat the previous step as many times as you like!

### TEST CASES
* The expected results are the img_ids that can be used to key into the images database where the actual image files to be rendered are stored.
* Searching by any invalid values individually or together does not crash the program.
1. *All blank:* Keep hitting enter until you're taken back to the first prompt. You should see all the image ids in the database.  
2. *Search by img_id:* If you're using the original searchdb_contents.csv type `2840` ("Finding Dory") and you will also find 22891 ("Finding Nemo")
3. *More search options:* Select a `test_X.txt` from the `test_cases/` folder where X is a number between 1 and 15. In response to the first prompt, Copy and paste the contents into the terminal window (you may have to hit enter afterwards). The expected result will be contained within `test_X_result.txt` in the `test_cases/` folder.
