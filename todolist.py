# Write your code here
# print("Today:")
# print("1) Do yoga")
# print("2) Make breakfast")
# print("3) Learn basics of SQL")
# print("4) Learn what is ORM")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base     # Clase modelo DeclarativeMeta
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')  # Crear base de datos (todo.db)

Base = declarative_base()


class Table(Base):      # Nombre de la clase modelo
    __tablename__ = 'task'        # Especifica el nombre del a tabla en la base de datos
    id = Column('id', Integer, primary_key=True)  # id es columna, primary_key=True dice que esta columna es la clave principal
    task = Column('task', String)  # Columna de tipo string con valor predeterminado
    deadline = Column('deadline', Date, default=datetime.today())     # Columna que almacena la fecha

    def __repr__(self):     # Metodo que devuelve una cadena del objeto de la clase
        return self.task    #

Base.metadata.create_all(engine)    # Crea la tabla descrita en la base de datos
from sqlalchemy.orm import sessionmaker # Crea una sesion para admin la base y tabla

Session = sessionmaker(bind=engine) # Crea el objeto para admin
session = Session()

# session.query(Table).delete()

# print(first_row.task)   # Will print value of the string_field
# print(first_row.id)             # Will print the id of the row.
# print(first_row.deadline)                # Will print the string that was returned by __repr__ method


def today_tasks():
    # rows = session.query(Table).all()  # Pasamos la clase modelo(Tabla) al metodo query para seleccionar todas las filas
    # El metodo all() devuelve todas las filas como una lista
    # first_col = rows[0:1]  # In case rows list is not empty
    # print(first_col)
    today = datetime.today()
    day = str(today.day)
    print("Today", day, today.strftime('%b') + ':')
    rows = session.query(Table).filter(Table.deadline == today.date()).all()    # Aplica filtro para fecha de hoy
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows)):
            print(str(rows[i].id) + '.', rows[i].task)
    print()
    session.commit()
    session.close()


def add_task():
    print("Enter task")
    new_task = input()
    print("Enter deadline")
    dead_line = input()
    new_row = Table(task=new_task, deadline=datetime.strptime(dead_line, '%Y-%m-%d'))
                    # deadline=datetime.strptime('01-24-2020', '%m-%d-%Y').date())  # Crea fila(objeto) en nuestra tabla
    session.add(new_row)  # Agrega el nuevo objeto a la tabla
    session.commit()
    session.close()
    print("The task has been added!")
    print()


def week_day(n_day):
    # today = datetime.today()
    w_day = n_day.weekday()
    if w_day == 0:
        return 'Monday'
        # print('Monday', day, today.strftime('%b') + ':')
    elif w_day == 1:
        return 'Tuesday'
        # print('Tuesday', day, today.strftime('%b') + ':')
    elif w_day == 2:
        return 'Wednesday'
        # print('Wednesday', day, today.strftime('%b') + ':')
    elif w_day == 3:
        return 'Thursday'
        # print('Thursday', day, today.strftime('%b') + ':')
    elif w_day == 4:
        return 'Friday'
        # print('Friday', day, today.strftime('%b') + ':')
    elif w_day == 5:
        return 'Saturday'
        # print('Saturday', day, today.strftime('%b') + ':')
    elif w_day == 6:
        return 'Sunday'
        # print('Sunday', day, today.strftime('%b') + ':')


def week_tasks():
    today = datetime.today()
    day = str(today.day)
    s_day = week_day(today)
    print(s_day, day, today.strftime('%b') + ':')
    rows = session.query(Table).filter(Table.deadline == today.date()).all()
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows)):
            print(str(rows[i].id) + '.', rows[i].task)
    print()
    today_1 = today + timedelta(days=1)
    day_1 = str(today_1.day)
    s_day_1 = week_day(today_1)
    print(s_day_1, day_1, today.strftime('%b') + ':')
    rows_1 = session.query(Table).filter(Table.deadline == today_1.date()).all()
    if len(rows_1) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows_1)):
            print(str(rows_1[i].id) + '.', rows_1[i].task)
    print()
    today_2 = today + timedelta(days=2)
    day_2 = str(today_2.day)
    s_day_2 = week_day(today_2)
    print(s_day_2, day_2, today.strftime('%b') + ':')
    rows_2 = session.query(Table).filter(Table.deadline == today_2.date()).all()
    if len(rows_2) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows_2)):
            print(str(rows_2[i].id) + '.', rows_2[i].task)
    print()
    today_3 = today + timedelta(days=3)
    day_3 = str(today_3.day)
    s_day_3 = week_day(today_3)
    print(s_day_3, day_3, today.strftime('%b') + ':')
    rows_3 = session.query(Table).filter(Table.deadline == today_3.date()).all()
    if len(rows_3) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows_3)):
            print(str(rows_3[i].id) + '.', rows_3[i].task)
    print()
    today_4 = today + timedelta(days=4)
    day_4 = str(today_4.day)
    s_day_4 = week_day(today_4)
    print(s_day_4, day_4, today.strftime('%b') + ':')
    rows_4 = session.query(Table).filter(Table.deadline == today_4.date()).all()
    if len(rows_4) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows_4)):
            print(str(rows_4[i].id) + '.', rows_4[i].task)
    print()
    today_5 = today + timedelta(days=5)
    day_5 = str(today_5.day)
    s_day_5 = week_day(today_5)
    print(s_day_5, day_5, today.strftime('%b') + ':')
    rows_5 = session.query(Table).filter(Table.deadline == today_5.date()).all()
    if len(rows_5) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows_5)):
            print(str(rows_5[i].id) + '.', rows_5[i].task)
    print()
    today_6 = today + timedelta(days=6)
    day_6 = str(today_6.day)
    s_day_6 = week_day(today_6)
    print(s_day_6, day_6, today.strftime('%b') + ':')
    rows_6 = session.query(Table).filter(Table.deadline == today_6.date()).all()
    if len(rows_6) == 0:
        print("Nothing to do!")
    else:
        for i in range(len(rows_6)):
            print(str(rows_6[i].id) + '.', rows_6[i].task)
    print()
    session.commit()
    session.close()


def all_tasks():
    rows = session.query(Table).order_by(Table.deadline).all()
    for i in range(len(rows)):
        print(str(rows[i].id) + '.', rows[i].task + '.', rows[i].deadline.day, rows[i].deadline.strftime('%b'))
    print()
    session.commit()
    session.close()


def missed_task():
    today = datetime.today()
    rows = session.query(Table).filter(Table.deadline < today.date()).order_by(Table.deadline).all()    # Aplica filtro para antes de hoy
    if len(rows) == 0:
        print("Nothing is missed!")
    else:
        for i in range(len(rows)):
            print(str(rows[i].id) + '.', rows[i].task + '.', rows[i].deadline.day, rows[i].deadline.strftime('%b'))
    print()
    session.commit()
    session.close()


def delete_task():
    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) == 0:
        print("Nothing to delete!")
    else:
        print("Choose the number of the task you want to delete:")
        for i in range(len(rows)):
            print(str(rows[i].id) + '.', rows[i].task + '.', rows[i].deadline.day, rows[i].deadline.strftime('%b'))
        num = int(input())
        specific_row = rows[num-1]  # in case rows is not empty
        session.delete(specific_row)
        session.commit()
        print("The task has been deleted!")
    print()
    session.close()


while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    action = str(input())
    if action == '1':
        today_tasks()
    elif action == '2':
        week_tasks()
    elif action == '3':
        all_tasks()
    elif action == '4':
        missed_task()
    elif action == '5':
        add_task()
    elif action == '6':
        delete_task()
    elif action == '0':
        print("Bye!")
        break
