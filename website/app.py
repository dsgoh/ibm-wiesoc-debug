from flask import Flask, render_template, request, redirect, url_for
import maps
import covidsafe
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
        print(dest, datetimein)
        venueOut = maps.queryVenue(dest)
        venueCOVIDSafeStatus = covidsafe.checkCovidSafe(venueOut)
        #print(covidsafe.checkCovidSafe(venue))
        return redirect(url_for('individual_search', dest=dest, datetimein=datetimein, venueOut=venueOut, venueCOVIDSafeStatus=venueCOVIDSafeStatus))
    return render_template('individual.html')

@app.route('/individual/search/', methods=["GET", "POST"])
def individual_search():
    dest = request.args.get('dest', None)
    datetimein = request.args.get('datetimein', None)
    venueOut = request.args.get('venueOut', None)
    venueCOVIDSafeStatus = request.args.get('venueCOVIDSafeStatus', None)
    return render_template('individual_search.html', dest=dest, datetimein=datetimein, venueOut=venueOut, venueCOVIDSafeStatus=venueCOVIDSafeStatus)

@app.route('/group/')
def group():
    return render_template('group.html')

if __name__ == '__main__':
	app.run(debug=True)