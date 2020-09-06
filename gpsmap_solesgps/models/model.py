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
        #vehicle_args                            =[('devicetime', '>=', (context_today()-datetime.timedelta(days=10)).strftime('%Y-%m-%d'))]
        vehicle_args                            =[]                
        return_positions                        ={}
        vehicle_data                            =self.search(vehicle_args, offset=0, limit=None, order=None)

        for vehicle in vehicle_data:
            #vehicle.devicetime
            print("######## Devicetime #########", vehicle["recargado"])    


            fields.Datetime.from_string(item.delivery) + relativedelta(days=5)    
