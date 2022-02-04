
from flask import Flask, jsonify, request, Blueprint, flash, g , redirect, render_template, url_for
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from bingads import *

bp = Blueprint("ads", __name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

ENVIRONMENT = 'sandbox'
authorization_data = AuthorizationData(
    account_id=None, 
    customer_id=None, 
    developer_token=None, 
    authentication=None)

@bp.route("/")
def index():
    campaign_service = ServiceClient(
    service='CampaignManagementService', 
    version = 13,
    authorization_data=authorization_data, 
    environment = ENVIRONMENT,
)
    print(campaign_service.GetCampaignsByIds)
    return jsonify(incomes)

