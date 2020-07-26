# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

class geofence(models.Model):
    _inherit = "gpsmap.geofence"
    

class vehicle(models.Model):
    _inherit = "fleet.vehicle"
    recargado                                   = fields.Datetime('Recargado')
    def run_scheduler_recarga(self):
        
        
        data_position                           = self.js_positions()        
        for position in data_position:
        
        
        print("#################")    
        print(data_position)

