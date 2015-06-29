from flask.ext.mysqldb import MySQL
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'coder123'
app.config['MYSQL_DB'] = 'nelisa'
#	app.config['MYSQL_CHARSET'] = 'utf-8'

@app.route('/')
def show_entries():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM product''')
	entries = [dict(prod_id=row[0], prod_name=row[1], cat_id=row[2]) for row in cur.fetchall()]
    	return render_template('show_entries.html', entries=entries)

if __name__ == '__main__':

	app.run(debug=True)
