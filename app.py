import os
import json
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import abort, Api, Resource
from flask_cors import CORS 
import datetime
import requests

app = Flask(__name__)
CORS(app)

api = Api(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models
  
def abort_if_rca_doesnt_exist(rca_id):
    abort(404, message="RCA {} doesn't exist".format(rca_id))

# Function for converting datetime object into string for json.dumps
def converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

class RCAList(Resource):
    def get(self):
        try:
            rca_items = models.RCA.query.all()
            return json.dumps([e.serialize() for e in rca_items], default= converter)
    
        except Exception as e:
            return str(e)

    def post(self):
        try:
            outerBody = request.get_json(force=True)
            body = outerBody['valArray']
            # import ipdb; ipdb.set_trace()
            rca = models.RCA(title=body["title"], incident_report_for=body["incident_report_for"], incident_datetime=body["incident_datetime"], incident_reported_by=body["incident_reported_by"], report_datetime=body["report_datetime"], fixed_on=body["fixed_on"], outage_duration=body["outage_duration"], outage_severity=body["outage_severity"], sre_on_call=body["sre_on_call"], summary=body["summary"], root_cause_analysis=body["root_cause_analysis"], error_message=body["error_message"], bugs=body["bugs"], recovery=body["recovery"], workaround=body["workaround"], closing_remarks=["closing_remarks"], action_items=body["action_items"], comment=body["comment"])
            db.session.add(rca)
            db.session.commit()
            return json.dumps({"added":"True"}) 

        except Exception as e:
            return str(e)

class RCAs(Resource):
    def get(self, rca_id):
        try:
            rca_item = models.RCA.query.filter_by(id=rca_id).first()
            return json.dumps(rca_item.serialize(), default= converter)

        except Exception as e:
            return str(e)
    
    def delete(self, rca_id):
        try:
            rca_item = models.RCA.query.filter_by(id=rca_id).first()
            session = db.session.object_session(rca_item)
            session.delete(rca_item)
            session.commit()
            return json.dumps({"deleted":"True"})

        except Exception as e:
            return str(e)

    def put(self, rca_id):
        try:
            rca_item = models.RCA.query.filter_by(id=rca_id).first()
            body = request.get_json(force=True)
            session = db.session.object_session(rca_item)
            rca_item.title = body["title"]
            session.commit()
            return json.dumps({"updated":"True"})  
            
        except Exception as e:
            return str(e)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/postRCA.html")
def postRCA():
    info = requests.post("http://172.17.0.1:5000/rcas")
    return render_template("postRCA.html")

@app.route("/loadRCA.html")
def loadRCA():
    info = requests.get('http://172.17.0.1:5000/rcas')
    info = json.loads(info.content)
    return render_template('loadRCA.html', info=info)
    # return render_template("loadRCA.html", result = {"title": "Sys Abort", "incident_report_for": "qwerty is good", "incident_datetime": "2020-1-1", "incident_reported_by": "James", "report_datetime": "2020-1-1", "fixed_on": "2020-1-1", "outage_duration": "2020-1-1", "outage_severity": "High", "sre_on_call": "James", "summary": "System crashed due to human error.", "root_cause_analysis": "Human error compromised the system.", "error_message": "failed transactions", "bugs": "none", "recovery": "avoid such mistakes", "workaround": "used second server", "closing_remarks": "issued resolved", "action_items": "none", "comment": "none"})

@app.route("/healthCheck")
def healthCheck():
    return 200

api.add_resource(RCAList, '/rcas')
api.add_resource(RCAs, '/rca/<string:rca_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0")    

