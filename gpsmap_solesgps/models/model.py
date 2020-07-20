# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

class geofence(models.Model):
    _inherit = "gpsmap.geofence"
    

