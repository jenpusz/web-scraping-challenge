from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record
    mars_info = mongo.db.collection.find_one()

    # Return index.html and data
    print(mars_info)
    return render_template("index.html", mars=mars_info)


# Route to start the scrape function
@app.route("/scrape")
def scrape():

    # Run scrape function
    mars_data = scrape_mars.scrape()
    print(mars_data)
    # Update  Mongo db
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
