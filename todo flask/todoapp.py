# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect, url_for
# import the SQLAlchemy class from the flask_sqlalchemy module
from flask_sqlalchemy import SQLAlchemy
# import the datetime class from the datetime module
from datetime import datetime

app = Flask(__name__)   # create an instance of the Flask class
# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)        # create an instance of the SQLAlchemy class
db.create_all()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # primary key
    content = db.Column(db.String(200), nullable=False)     # content
    date_created = db.Column(   # date created
        db.DateTime, default=datetime.utcnow)      # date created

    def __repr__(self):                 # return a string representation of the object
        return '<Task %r>' % self.id        # return the id of the task


@app.route('/', methods=['POST', 'GET'])        # route to the home page
def index():        # function to handle the home page
    if request.method == 'POST':        # if the request method is POST
        # get the content from the form
        task_content = request.form['content']
        new_task = Todo(content=task_content)       # create a new task

        try:        # try to add the task to the database
            db.session.add(new_task)    # add the new task to the database
            db.session.commit()     # commit the changes to the database
            return redirect('/')        # redirect to the home page
        except:     # if there is an error
            return 'There was an issue adding your task'        # return an error message

    else:       # if the request method is GET
        # get all the tasks from the database
        tasks = Todo.query.order_by(Todo.date_created).all()
        # render the index.html template and pass the tasks to it
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')    # route to the delete page
def delete(id):    # function to handle the delete page
    task_to_delete = Todo.query.get_or_404(id)      # get the task to delete

    try:        # try to delete the task from the database
        # delete the task from the database
        db.session.delete(task_to_delete)
        db.session.commit()     # commit the changes to the database
        return redirect('/')        # redirect to the home page
    except:     # if there is an error
        return 'There was a problem deleting that task'     # return an error message


# route to the update page
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):     # function to handle the update page
    task = Todo.query.get_or_404(id)    # get the task to update

    if request.method == 'POST':        # if the request method is POST
        # get the content from the form
        task.content = request.form['content']

        try:        # try to update the task in the database
            db.session.commit()         # commit the changes to the database
            return redirect('/')        # redirect to the home page
        except:     # if there is an error
            return 'There was an issue updating your task'      # return an error message

    else:    # if the request method is GET
        # render the update.html template and pass the task to it
        return render_template('update.html', task=task)


if __name__ == "__main__":      # if this is the main module

    app.run(debug=True)     # run the app in debug mode
