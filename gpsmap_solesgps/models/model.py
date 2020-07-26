# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

class geofence(models.Model):
    _inherit = "gpsmap.geofence"
    
class positions(models.Model):
    _inherit = "gpsmap.positions"
    def run_scheduler_recarga(self):
        vehicle_obj                             =self.env['fleet.vehicle']        
        
        
        data_position                           = self.js_positions()
        print("#################")    
        print(data_position)



class vehicle(models.Model):
    _inherit = "fleet.vehicle"
    recargado                                   = fields.Datetime('Recargado')

