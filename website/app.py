from flask import Flask, render_template, request
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
        venue = maps.queryVenue(dest)
        print(covidsafe.checkCovidSafe(venue))
    return render_template('individual.html')

@app.route('/group/')
def group():
    return render_template('group.html')

if __name__ == '__main__':
	app.run(debug=True)