from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def home():
    return redirect(url_for('contact'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Simple validation
        if not name or not email or not message:
            flash('Please fill out all required fields.', 'error')
            return redirect(url_for('contact'))

        # Simulate form processing (e.g., print or save)
        print(f"Message received from {name} <{email}>: {subject} - {message}")
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')
    
if __name__ == '__main__':
    app.run(debug=True)
