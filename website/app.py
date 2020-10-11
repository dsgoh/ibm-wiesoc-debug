from flask import Flask, render_template, request, redirect, url_for
import maps
import covidsafe
import covidlocation
import time
import venue
from datetime import datetime
import route as rt
import json
import sys
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/individual/', methods=["GET", "POST"])
def individual():
    if request.method == "POST":
        form = request.form
        dest = form.get('DestinationInput')
        datetimein = form.get('DatetimeIndividualInput')
        #print(dest, datetimein)
        v = maps.queryVenue(dest)
        venueOut = v["name"] + ", " + v["formatted_address"]
        venueCOVIDSafeStatus = covidsafe.checkCovidSafe(v["formatted_address"])
        venueName = v["name"]
        route = maps.queryRoute("Sydney City", dest, departure_time="now")
        if route is None:
            route = "No value returned for route."
        venueForecast = venue.forecastVenue(venueOut, datetimein)

        #route = maps.queryRoute("Sydney City", dest, departure_time=int(time.mktime(time.strptime(datetimein, '%Y-%m-%dT%H:%M'))))
        return redirect(url_for('individual_search', dest=dest, datetimein=datetimein, venueOut=venueOut, venueCOVIDSafeStatus=venueCOVIDSafeStatus, route=route, venueForecast=venueForecast))
    return render_template('individual.html')

@app.route('/individual/search/', methods=["GET", "POST"])
def individual_search():
    dest = request.args.get('dest', None)
    datetimein = request.args.get('datetimein', None)
    venueOut = request.args.get('venueOut', None)
    venueCOVIDSafeStatus = request.args.get('venueCOVIDSafeStatus', None)
    route = request.args.get('route', None)
    venueForecast = request.args.get('venueForecast', None).replace("\'", '\"')
    print("VF: ", venueForecast)
    newJson = json.loads(venueForecast)

    # Route
    route = rt.queryROAM(rt.getClosestStation(dest))
    busyRouteStatus = 0
    if (route <= 70):
        busyRouteStatus = 0
    if (route <= 120):
        busyRouteStatus = 1
    if (route <= 180):
        busyRouteStatus = 2
    if (route > 180):
        busyRouteStatus = 3

    # Venu
    busyVenueStatus = 0
    busyVenueData = 0
    datetimeobject = datetime.strptime(datetimein, '%Y-%m-%dT%H:%M')
    if "analysis" not in newJson:
        busyVenueData = 0
    else:
        for something in newJson['analysis']:
            if something["day_info"]["day_int"] == datetimeobject.weekday():
                venueForecast = something
                #print(datetimeobject.hour, something['peak_hours'][0]['peak_start'], something['peak_hours'][0]['peak_end'])
                if datetimeobject.hour in something['quiet_hours']:
                    busyVenueStatus = 0
                if datetimeobject.hour in something['busy_hours']:
                    busyVenueStatus = 1
                try:
                    if (int(datetimeobject.hour) >= int(something['peak_hours'][0]['peak_start'])) and (int(datetimeobject.hour) <= int(something['peak_hours'][0]['peak_end'])):
                        busyVenueStatus = 2
                except:
                    pass
                if datetimeobject.hour == something['surge_hours']['most_people_come']:
                    busyVenueStatus = 3
                busyVenueData = something

    covidCountsInSuburbs = covidlocation.checkCovidLocation(maps.queryVenue(venueOut))

    risk = "LOW_RISK"
    if venueCOVIDSafeStatus == False or covidCountsInSuburbs > 0:
        risk = "HIGH_RISK"
    elif (busyRouteStatus + busyVenueStatus) > 3:
        risk = "HIGH_RISK"
    elif (busyRouteStatus + busyVenueStatus) < 4:
        risk = "MEDIUM_RISK"
    else:
        risk = LOW_RISK
    
    return render_template('individual_search.html', dest=dest, datetimein=datetimein, venueOut=venueOut, venueCOVIDSafeStatus=venueCOVIDSafeStatus, route=route, venueForecast=venueForecast, busyVenueStatus=busyVenueStatus, busyVenueData=busyVenueData, busyRouteStatus=busyRouteStatus, covidCountsInSuburbs=covidCountsInSuburbs, risk=risk)

@app.route('/group/')
def group():
    return render_template('group.html')

if __name__ == '__main__':
	app.run(debug=True)


