import flask
from flask import request, jsonify
from helperer import Converter

app = flask.Flask(__name__)
app.config["DEBUG"] = True

path = 'database.json'
obj = Converter(path)

@app.route('/api/v1/resources/students', methods = ['GET'])
def get_all_students():
    
    students = obj.deserialization()
    return jsonify(students)


@app.route('/api/v1/resources/student', methods = ['GET'])
def get_student_by_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error!!! Please give id."

    results = []

    students = obj.deserialization()
    for student in students:
        if student['id'] == id:
            results.append(student)
    return jsonify(results)


@app.route('/api/v1/resources/students/addStudent', methods = ['POST'])
def add_student():

    response = request.get_json()
    if response is None:
        return "Error!!! You have not transmitted the required data․"
    else:
        exists = False
        students = obj.deserialization()
        for student in students:
            if (response['name'] == student['name']) and (response['surname'] == student['surname']) and (response['age'] == student['age']) and (response['university'] == student['universiti']):
                exists = True
                break

        if exists:
            return "Error!!!: Current student already exists․"
        else:
            student = {
                'id': students[-1]['id'] + 1,
                'name' : response['name'],
                'surname' : response['surname'],
                'age' : response['age'],
                'university' : response['university'],
            }
            students.append(student)
            students = obj.serialization(students)
            return "Student successfully added to the database"


@app.route('/api/v1/resources/students/remove/<int:_id>', methods = ['DELETE'])
def remove(_id):

    students = obj.deserialization()
    student_to_remove = [student for student in students if student['id'] == _id]
    if len(student_to_remove) == 0:
        return "No student with this id"
    else:
        students.remove(student_to_remove[0])  
        students = obj.serialization(students) 
        return "Deleted: {}\n".format(student_to_remove)
    

@app.route('/api/v1/resources/students/edit', methods = ['PUT'])
def edit_student():

    response = request.get_json()
    if response is None:
        return "Error!!!: You have not transmitted the required data․"
    else:
        exist = False
        students = obj.deserialization()
        for student in students:
            if student['id'] == response['id']:
                exist = True
                break
        if exist:
            student['name'] = response['new_name']
            student['surname'] = response['new_surname']
            student['age'] = response['new_age']
            student['university'] = response['new_university']
            students = obj.serialization(students)
            return "Updated: {}\n".format(student)
        else:
            return "No student with this id"



if __name__ == '__main__':
    app.run()