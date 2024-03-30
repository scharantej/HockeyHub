## Design for Flask Application

### HTML Files

- **index.html**: The main web page that users will see. It will contain the HTML table to display the hockey player data, as well as the search bar and dropdown filters.
- **base.html**: A base template that other HTML files can inherit from. It will contain common elements such as the header and footer.

### Routes

- **index**: Renders the index.html page.
- **fetch_data**: Fetches the hockey player data from the database and returns it in JSON format.
- **add_player**: Adds a new hockey player to the database.
- **update_player**: Updates an existing hockey player in the database.
- **delete_player**: Deletes a hockey player from the database.
- **search_players**: Searches for hockey players in the database based on their name.
- **filter_players**: Filters the hockey players in the database based on the selected metrics.