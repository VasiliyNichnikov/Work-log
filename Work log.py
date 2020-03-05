from WEB_Introduction_flask_sqlalchemy.data import db_session
from WEB_Introduction_flask_sqlalchemy.data.jobs import Jobs
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


listUser = []

@app.route("/")
def Program():
    print(listUser)
    return render_template("/work_log.html", title="Журнал работ", listUsers=listUser)


def main():
    db_session.global_init("../db/lesson_02.sqlite")
    session = db_session.create_session()
    #  db_session.global_init("db/lesson_02.sqlite")

    listJobs = session.query(Jobs).all()
    for i in listJobs:
        dictUser = {}
        dictUser["id"] = i.id
        dictUser["job"] = i.job
        dictUser["team_leader"] = i.team_leader
        dictUser["work_size"] = i.work_size
        dictUser["collaborators"] = i.collaborators
        dictUser["is_finished"] = i.is_finished
        listUser.append(dictUser)
    print(listUser)

    app.run()


if __name__ == '__main__':
    main()
