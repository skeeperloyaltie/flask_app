# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re, click
# from flask import current_app, g
# from flask.cli import with_appcontext
# from flask import session
# import sqlite3 as sql




# # def get_db():
# #     if 'db' not in g:
# #         g.db = sqlite3.connect(
# #             current_app.config['DATABASE'],
# #             detect_types=sqlite3.PARSE_DECLTYPES
# #         )
# #         g.db.row_factory = sqlite3.Row
# #     return g.db

# # def close_db(e=None):
# #     db = g.pop('db', None)
# #     if db is not None:
# #         db.close()
        

# # def init_db():
# #     db = get_db()
# #     with current_app.open_resource('schema.sql') as f:
# #         db.executescript(f.read().decode('utf8'))

# # @click.command('init-db')
# # @with_appcontext
# # def init_db_command():
# #     """Clear the existing data and create new tables."""
# #     init_db()
# #     click.echo('Initialized the database.')

# # def init_app(app):
# #     app.teardown_appcontext(close_db)
# #     app.cli.add_command(init_db_command)
    
# # def create_app():
# #     app = Flask(__name__)
# #     app.config['SECRET_KEY'] = 'secret'
# #     app.config['DATABASE'] = 'database.db'
# #     init_app(app)
# #     return app
# # app = create_app()
# con = sql.connect("database.db", check_same_thread=False)
# con.row_factory = sql.Row
# cur = con.cursor()

# app = Flask(__name__)

# mysql = MySQL(app)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             session['username'] = account['username']
#             flash('You were successfully logged in')
#             return redirect(url_for('home'))
#         else:
#             flash('Incorrect username or password')
#             return redirect(url_for('/home'))
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('username', None)
#     flash('You were successfully logged out')
#     return redirect(url_for('login'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST':
#         try:
#             ln = request.form['username']
            
#             with sql.connect("database.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (ln, request.form['password']))
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#             con.commit()
#             msg  = "error in insert operation"
#         finally:
#             return render_template("login.html", msg=msg)
#             con.close()
            
            

        
