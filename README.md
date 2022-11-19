# Welcome to ISMIR 2022 virtual platform creation code!!
1. Clone this repo 
2. Clone complete metadata from: https://github.com/ismir2022program/miniconf-data
3. Post the above steps you should have the two repos `ismir2022program.github.io` and `miniconf-data` under the same folder
4. Go to `ismir2022program.github.io` folder and run `>> python miniconf_prep.py` this will prepare the data as required by miniconf. Read through this code for the details of preprocessing
5. To build the miniconf site run `>> export FLASK_DEBUG=True; export FLASK_DEVELOPMENT=True; python main.py --path sitedata/`
6. To update the site on production push the changes to the `dev` branch