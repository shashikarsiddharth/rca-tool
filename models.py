from app import db

class RCA(db.Model):
    ''' Class used for creating table in database. ''' 

    __tablename__ = 'rca'

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(), nullable=False)
    incident_report_for = db.Column(db.String(), nullable=False)
    incident_datetime = db.Column(db.DateTime(), nullable=False)
    incident_reported_by = db.Column(db.String(), nullable=False)
    report_datetime = db.Column(db.DateTime(), nullable=False)
    fixed_on = db.Column(db.DateTime(), nullable=False)
    outage_duration = db.Column(db.DateTime(),nullable=False)
    outage_severity = db.Column(db.String(),nullable=False)
    sre_on_call = db.Column(db.String(),nullable=False)
    summary = db.Column(db.Text(),nullable=False)
    root_cause_analysis = db.Column(db.Text(),nullable=False)
    error_message = db.Column(db.Text)
    bugs = db.Column(db.Text())
    recovery = db.Column(db.Text(),nullable=False)
    workaround = db.Column(db.Text())
    closing_remarks = db.Column(db.Text)
    action_items = db.Column(db.Text)
    comment = db.Column(db.Text)
    
    def __init__(self, title, incident_report_for, incident_datetime, incident_reported_by, report_datetime, fixed_on, outage_duration, outage_severity, sre_on_call, summary, root_cause_analysis, error_message, bugs, recovery, workaround, closing_remarks, action_items, comment):
        ''' Function for initializing class variables. '''
        self.title = title
        self.incident_report_for = incident_report_for
        self.incident_datetime = incident_datetime
        self.incident_reported_by = incident_reported_by
        self.report_datetime = report_datetime
        self.fixed_on = fixed_on
        self.outage_duration = outage_duration
        self.outage_severity = outage_severity
        self.sre_on_call = sre_on_call
        self.summary = summary
        self.root_cause_analysis = root_cause_analysis
        self.error_message = error_message
        self.bugs = bugs
        self.recovery = recovery
        self.workaround = workaround
        self.closing_remarks = closing_remarks
        self.action_items = action_items
        self.comment = comment

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'incident_report_for': self.incident_report_for,
            'incident_datetime': self.incident_datetime,
            'incident_reported_by': self.incident_reported_by,
            'report_datetime': self.report_datetime,
            'fixed_on': self.fixed_on,
            'outage_duration': self.outage_duration,
            'outage_severity': self.outage_severity,
            'sre_on_call': self.sre_on_call,
            'summary': self.summary,
            'root_cause_analysis': self.root_cause_analysis,
            'error_message': self.error_message,
            'bugs': self.bugs,
            'recovery': self.recovery,
            'workaround': self.workaround,
            'closing_remarks': self.closing_remarks,
            'action_items': self.action_items,
            'comment': self.comment
        }
  


