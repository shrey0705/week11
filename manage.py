from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        
        emp_name = request.form['emp_name']
        emp_gender = request.form['emp_gender']
        emp_phone = request.form['emp_phone']
        emp_bday = request.form['emp_bday']

        
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO employees (EmpName, EmpGender, EmpPhone, EmpBday)
            VALUES (?, ?, ?, ?)
        ''', (emp_name, emp_gender, emp_phone, emp_bday))
        conn.commit()
        conn.close()

        return 'Employee registered successfully.'
    
    return render_template('registration.html')


@app.route('/information')
def information():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employees')
    employees = c.fetchall()
    conn.close()

    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
