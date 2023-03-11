import json
import os
import datetime
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for
import web_navigator

### Flask Initialization ###
app = Flask(__name__)

### Routing ###
################ START PAGES!#################################

@app.route("/Recipe_Collector",methods = ["GET"])
def home_path():
    return render_template('searchpage.html')

##############################################################

@app.route("/collection", methods= ['GET', 'POST'])
def collection():
    if request.method == 'POST':
        recipe_obj = {}
        recipe_list = []
        req_dat = request.form.getlist('chkbx')
        for each in req_dat:
            recipe_obj.update(json.loads(each))
        # print("req_dat P", recipe_obj, flush=True)
        return_package = web_navigator.web_collect(recipe_obj)
    return render_template('resultsPage.html', return_package=return_package)

##############################################################

@app.route('/pass_data', methods= ['GET', 'POST'])
def pass_data():
    #POST request
    if request.method == 'POST':
        req_dat = request.get_json()
        print("POSTED DATA: ", req_dat, flush=True)
        if req_dat['location'] == "webNavSearch":
            return_package = web_navigator.search_recipe(req_dat)
        else:
            return_package = "Error occured"
        return jsonify(return_package)
    #GET request
    else:
        message = {'greeting': 'Error from /Pass_data in main.py'}
        return jsonify(message)
    
################ END PAGES!#################################



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
       print('################### Restarting @ {} ###################'.format(datetime.datetime.utcnow()))    
    app.run(host='0.0.0.0', port=9000)