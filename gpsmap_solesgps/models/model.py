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


        ahora = datetime.datetime.utcnow()
        ayer = ahora - datetime.timedelta(days=25)
    
        vehicle_args                            =[]        
        return_positions                        ={}
        vehicle_data                            =self.search(vehicle_args, offset=0, limit=None, order=None)

        for vehicle in vehicle_data:
            print("# VEHICLE =============",vehicle["name"])
            if((vehicle["recargado"]=="" OR vehicle["recargado"]==NULL)):        
                ahora = datetime.datetime.utcnow()
                ayer = ahora - datetime.timedelta(days=25)
                #ayer2 = vehicle["recargado"] - datetime.timedelta(days=25)                

                #vehicle.devicetime
                print("# RECARGADO = ", vehicle["recargado"], " ayer=",ayer)
                #print("######## RECARGADO = ", vehicle["recargado"], " ayer=",ayer , " ayer2=",ayer2)        

