# Import the dependencies.

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from datetime import datetime, timedelta
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

    # Get the most recent date in the data
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Calculate the date 12 months before the most recent date
    one_year_ago = (dt.datetime.strptime(recent_date, "%Y-%m-%d") - dt.timedelta(days = 365)).date()

    # Query for the last 12 months of precipitation data
    precipitation_data = (session.query(Measurement.date, Measurement.prcp)
                          .filter(Measurement.date >= one_year_ago)
                          .order_by(Measurement.date)
                          .all()
    )

    # Return the JSON representation of your dictionary.
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

    return jsonify(precipitation_dict)


@app.route("/api/v1.0/stations")
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/tobs")
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
    
@app.route("/api/v1.0/<start>")
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature
# for a specified start or start-end range.
# For a specified start, calculate TMIN , TAVG , and TMAX for all the dates greater than or equal to the start
# date.
# For a specified start date and end date, calculate TMIN , TAVG , and TMAX for the dates from the start date
# to the end date, inclusive.

@app.route("/api/v1.0/<start>/<end>")
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature
# for a specified start or start-end range.
# For a specified start, calculate TMIN , TAVG , and TMAX for all the dates greater than or equal to the start
# date.
# For a specified start date and end date, calculate TMIN , TAVG , and TMAX for the dates from the start date
# to the end date, inclusive.
