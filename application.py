from flask import Flask,request
from flask_cors import CORS
from Errors.invaliddataerror import invalid_data_error
from ResponseSender import ResponseSender
from config import Config as configuration
import Services.student as student_services
import traceback
app = Flask(__name__)
from factory import getCursor

@app.route('/getAllTables',methods={"GET"})
def hello():
    try:
        cursor= getCursor().cursor()
        cursor.execute("SHOW TABLES")
        if cursor.rowcount==0:
            print("The Table list is Empty")
        table = []
        for tables in cursor:
            table.append(tables[0])
        return table,200
    except Exception as e:
        traceback.print_stack(e)
        return "error",500
    

@app.post('/createCollage')
def create_collage():
    collage_name = request.get_json()['collage_name']
    student_services.create_collage(collage_name)
    return "Created",201


@app.post('/createDepartment')
def create_department():
    collage_name = request.get_json()['collage_name']
    department_name = request.get_json()['department_name']
    student_services.create_department(department_name,collage_name)
    return "Created",201

@app.post('/createCourse')
def create_course():
    course_name = request.get_json()['course_name']
    student_services.create_course(course_name)
    return "Created",201


@app.post('/createStudent')
def create_student():
    student_details = dict(request.get_json())
    student_services.add_student(student_details=student_details)
    return "Created",201


@app.errorhandler(invalid_data_error)
def error_handler(error):
    app.log_exception(error)
    return "Invalid Data",401


if __name__=="__main__":
    app.run(debug=True,port=configuration.port,host='0.0.0.0')

