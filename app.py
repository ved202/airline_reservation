from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store reservations as dictionaries
reservations = []

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html', reservations=reservations) # Render the main page template and pass the reservations list to it

@app.route('/submit', methods=['POST'])# Route for form submission (POST method)
def submit():
    name = request.form['name']# Retrieve form data from the request
    contact = request.form['contact']
    seat = request.form['seat']

    reservation = {'name': name, 'contact': contact, 'seat': seat}# Create a dictionary representing a reservation
    reservations.append(reservation) # Add the reservation to the list

    return redirect(url_for('index'))# Redirect to the main page after submission


if __name__ == '__main__':# Run the Flask application
    app.run(debug=True)
