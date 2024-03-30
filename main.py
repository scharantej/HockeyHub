
# Import the necessary modules.
from flask import Flask, render_template, request, jsonify
import mysql.connector

# Create a Flask application.
app = Flask(__name__)

# Connect to the database.
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hockey_players"
)

# Define the routes.
@app.route("/")
def index():
    # Render the index.html page.
    return render_template("index.html")

@app.route("/fetch_data")
def fetch_data():
    # Fetch the hockey player data from the database.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hockey_players")
    data = cursor.fetchall()
    cursor.close()

    # Return the data in JSON format.
    return jsonify(data)

@app.route("/add_player", methods=["POST"])
def add_player():
    # Get the player data from the request.
    data = request.get_json()

    # Add the player to the database.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hockey_players (name, team, position, goals, assists, points) VALUES (%s, %s, %s, %s, %s, %s)", (data["name"], data["team"], data["position"], data["goals"], data["assists"], data["points"]))
    conn.commit()
    cursor.close()

    # Return a success message.
    return jsonify({"success": True})

@app.route("/update_player", methods=["POST"])
def update_player():
    # Get the player data from the request.
    data = request.get_json()

    # Update the player in the database.
    cursor = conn.cursor()
    cursor.execute("UPDATE hockey_players SET name=%s, team=%s, position=%s, goals=%s, assists=%s, points=%s WHERE id=%s", (data["name"], data["team"], data["position"], data["goals"], data["assists"], data["points"], data["id"]))
    conn.commit()
    cursor.close()

    # Return a success message.
    return jsonify({"success": True})

@app.route("/delete_player", methods=["POST"])
def delete_player():
    # Get the player ID from the request.
    data = request.get_json()

    # Delete the player from the database.
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hockey_players WHERE id=%s", (data["id"],))
    conn.commit()
    cursor.close()

    # Return a success message.
    return jsonify({"success": True})

@app.route("/search_players", methods=["POST"])
def search_players():
    # Get the search term from the request.
    data = request.get_json()

    # Search for the players in the database.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hockey_players WHERE name LIKE %s", ("%" + data["search_term"] + "%",))
    data = cursor.fetchall()
    cursor.close()

    # Return the data in JSON format.
    return jsonify(data)

@app.route("/filter_players", methods=["POST"])
def filter_players():
    # Get the filter data from the request.
    data = request.get_json()

    # Filter the players in the database.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hockey_players WHERE position=%s", (data["position"],))
    data = cursor.fetchall()
    cursor.close()

    # Return the data in JSON format.
    return jsonify(data)

# Run the application.
if __name__ == "__main__":
    app.run(debug=True)
