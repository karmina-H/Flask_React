from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template

from Dao import EmpDao

app = Flask(__name__, static_url_path="", static_folder='static')


@app.route('/')
@app.route('/emp02')
def emp():
    empList = EmpDao().getEmps()
    return render_template("emp02.html", empList=empList)


@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    empno = data['empno']
    name = data['name']
    department = data['department']
    phone = data['phone']
    cnt = EmpDao().insEmp(empno, name, department, phone)
    result = "success" if cnt == 1 else "fail"
    return jsonify(result=result)


@app.route('/mod.ajax', methods=['POST'])
def mod_ajax():
    data = request.get_json()
    empno = data['empno']
    name = data['name']
    department = data['department']
    phone = data['phone']
    cnt = EmpDao().updEmp(empno, name, department, phone)
    result = "success" if cnt == 1 else "fail"
    return jsonify(result=result)


@app.route('/del.ajax', methods=['POST'])
def del_ajax():
    data = request.get_json()
    empno = data['empno']
    cnt = EmpDao().delEmp(empno)
    result = "success" if cnt == 1 else "fail"
    return jsonify(result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)