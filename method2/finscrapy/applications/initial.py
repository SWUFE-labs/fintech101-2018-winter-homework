from flask import Blueprint, request, render_template, jsonify
from models.finscrapy import FR, ECB

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/index', methods=['GET'])
def initial():
    return render_template('index.html')

@index.route('/data', methods=['POST'])
def data_ajax():
    returnObj = []
    try:
        status = request.form.get('status_query')
        print(status)
        if status == '1':
            for data in FR.objects.order_by('-date'):
                dataObj = {}
                dataObj['date'] = data.date
                dataObj['title'] = data.title
                dataObj['content'] = data.content
                dataObj['href'] = data.href
                returnObj.append(dataObj)
        elif status == '2':
            for data in ECB.objects.order_by('-date'):
                dataObj = {}
                dataObj['date'] = data.date
                dataObj['title'] = data.title
                dataObj['content'] = data.content
                dataObj['href'] = data.href
                returnObj.append(dataObj)
    except Exception as e:
        print('data_ajax error:', e)
    finally:
        data_for_ajax = {'data': returnObj}
        return jsonify(data_for_ajax)