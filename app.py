from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])  # Changed from '/contact' to '/'
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('All fields are required.', 'error')
        else:
            # Process the data (e.g., send email or store in DB)
            flash('Thank you for your message!', 'success')
            return redirect('/')
    return render_template('index.html')  # Make sure your HTML is named index.html and is in templates/

if __name__ == '__main__':
    app.run(debug=True)
