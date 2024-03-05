import factory
from Errors.invaliddataerror import invalid_data_error

conn = factory.getCursor()


def add_student(student_details):
    cursor = conn.cursor()
    collage = getCollage(student_details['collage_name'])
    if(collage == None): raise invalid_data_error
    department = getDepartment(student_details['department_name'],collage[0])
    if(department==None): raise invalid_data_error
    query = 'insert into student_table (name,dob,department_id,email_id) values (%s,%s,%s,%s)'
    cursor.execute(query,[student_details['student_name'],student_details['date_of_birth'],department[0],student_details['email_id']])
    cursor.execute('select id from student_table where email_id=%s',[student_details['email_id']])
    student_data  = cursor.fetchone()[0]
    for course_name in student_details['course_list']:
        course = find_course(course_name)
        if(course == None): raise invalid_data_error
        cursor.execute('insert into student_course_table (course_id,student_id) values(%s,%s)',[course[1],student_data])
    conn.commit()

    

def getDepartment(name,collage_id):
    query = f'select id,department_name from department_table where department_name=\'{name}\' AND collage_id = \'{collage_id}\''
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if(cursor.rowcount==0): return None
    return cursor.fetchone()

def getCollage(name):
    query  = f'select id,collage_name from collage_table where collage_name=\'{name}\''
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if(cursor.rowcount==0): return None
    return cursor.fetchone()

def create_collage(collage_name):
    cursor = conn.cursor()
    query = f'insert into collage_table (collage_name) values (\'{collage_name}\')'
    try:
        cursor.execute(query)
    except Exception as e:
        raise invalid_data_error
    finally:
        conn.commit()


def create_department(depart_name,collage_name):
    cursor = conn.cursor()
    collage = getCollage(collage_name)
    print(collage)
    if(collage == None):
        raise invalid_data_error
    query = f'insert into department_table (department_name,collage_id) values (\'{depart_name}\',\'{collage[0]}\')'
    try:
        cursor.execute(query)
    except Exception as e:
        raise invalid_data_error
    finally:
        conn.commit()


def create_course(course_name):
    cursor = conn.cursor()
    query = f'insert into course_table (course_name) values (\'{course_name}\')'
    try:
        cursor.execute(query)
    except Exception as e:
        raise invalid_data_error
    finally:
        conn.commit()
    

def find_course(course_name):
    cursor = conn.cursor()
    query = f'select course_name,id from course_table where course_name =\'{course_name}\''
    cursor.execute(query=query)
    if(cursor.rowcount==0): return None
    return cursor.fetchone()
