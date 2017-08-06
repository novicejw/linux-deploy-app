# Wine Catalog

This application provides a list of wines (referred to as 'items') within a number of wine categories, as well as provide a user registration and authentication system. Users need to log in to add or edit categories and items in the catalog, and are only able to edit the categories and items that they created.

To launch the application, please follow the following steps in this order:

**Database Set-up**
1. In your terminal, navigate to the directory where `project.py` resides.
2. Run `python database_setup.py`. This will set up the structure of the database for this application.
3. Then, run `lotsofitems.py`. This will populate the database with some initial categories and items.

**Launching the Application**
1. Update the Google OAuth credentials with your own:
    - Update `client_secrets.json` with your own Google client ID, client secret and project ID.
    - Update `data-clientid` on line 33 of the `login.html` file in the `templates` folder to your Google client ID
2. In your terminal, run `python project.py`.
3. Go to http://localhost:8000/ and you should see the landing page of the application. Log in using your Google credentials and start editing!

