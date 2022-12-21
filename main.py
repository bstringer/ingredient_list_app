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


@app.route('/pass_data', methods= ['GET', 'POST'])
def pass_data():
    #POST request
    if request.method == 'POST':
        req_dat = request.get_json()
        print("POSTED DATA: ", req_dat, flush=True)
        menu_list = web_navigator.search_recipe(req_dat)
        return jsonify(menu_list)
    #GET request
    else:
        message = {'greeting': 'Error from /Pass_data in main.py'}
        return jsonify(message)
    
################ START PAGES!#################################



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
       print('################### Restarting @ {} ###################'.format(datetime.datetime.utcnow()))    
    app.run(host='0.0.0.0', port=9000)