from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_mission.find_one()
    print(mars_data)
    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function and save the results to a variable
    #mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!
    #mars_mission.insert_one({},)
    listings = mongo.db.mars_mission
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)
    # Redirect back to home page


if __name__ == "__main__":
    app.run(debug=True)
