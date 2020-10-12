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
    #recargado                                   = fields.Datetime('Recargado')
    def run_scheduler_recarga(self):
        taecel_obj                             =self.env['taecel']
        
        ahora = datetime.datetime.utcnow()
        ayer = ahora - datetime.timedelta(days=25)
    
        vehicle_args                            =[]        
        return_positions                        ={}
        vehicle_data                            =self.search(vehicle_args, offset=0, limit=None, order=None)

        for vehicle in vehicle_data:
            recargar=0
            print("# VEHICLE =============",vehicle["name"])
            if(vehicle["recargado"] not in {"",False}):        
                ahora = datetime.datetime.utcnow()
                ayer = ahora - datetime.timedelta(days=25)
                
                #print("# RECARGADO = ", vehicle["recargado"], " ayer=",ayer)
                if str(vehicle["recargado"]) < str(ayer):
                    recargar=1
            else:
                recargar=1
                                
            if(recargar==1):
                print("# POSIBLE RECARGA NUEVA")
                taecel_data                     ={}
                taecel_data["name"]             ="TEL030"
                taecel_data["referencia"]       =vehicle["phone"]

                taecel_obj.create(speed)                                               
