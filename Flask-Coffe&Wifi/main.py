from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import csv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('Location URL', validators=[DataRequired()])
    open_time = StringField('Opening time', validators=[DataRequired()])
    close_time = StringField('Closening time', validators=[DataRequired()])

    coffee = SelectField('Coffee rating', choices=[('✘'), ('☕️'),('☕️☕️'),('☕️☕️☕️'),('☕️☕️☕️☕️'),('☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi =  SelectField('Wifi rating', choices=[('✘'),('💪'),('💪💪'),('💪💪'),('💪💪💪💪'),('💪💪💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power outlet rating', choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', encoding='utf-8', mode='a') as file:
            file.write(f'\n{form.cafe.data},{form.location_url.data},{form.open_time.data},{form.close_time.data},{form.coffee.data},{form.wifi.data},{form.power.data}')
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
	app.run(debug = True)
	
