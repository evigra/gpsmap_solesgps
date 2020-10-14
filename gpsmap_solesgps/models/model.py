# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
class taecel(models.Model):
    _inherit = "taecel"


class geofence(models.Model):
    _inherit = "gpsmap.geofence"
    

class vehicle(models.Model):
    _inherit = "fleet.vehicle"
    #recargado                                   = fields.Datetime('Recargado')
    def run_scheduler_recarga(self):
        taecel_obj                             =self.env['taecel']
        
        ahora = datetime.datetime.utcnow()
        ayer = ahora - datetime.timedelta(days=25)
        antes = ahora - datetime.timedelta(minutes=20)
    
        vehicle_args                            =[]        
        return_positions                        ={}
        vehicle_data                            =self.search(vehicle_args, offset=0, limit=None, order=None)

        for vehicle in vehicle_data:
            recargar=0
            
            print("# VEHICLE ========================",vehicle["name"])
            if(vehicle["recargado"] not in {"",False} and str(vehicle["recargado"]) < str(ayer)  and str(vehicle["devicetime_compu"]) < str(antes)):        
                recargar=1
            else:
                recargar=2
                                
            if(recargar>0 and vehicle["phone"] not in {"",False}):
                print("# POSIBLE RECARGA NUEVA=", recargar)
                taecel_data                     ={}
                taecel_data["name"]             ="TEL030"
                taecel_data["referencia"]       =vehicle["phone"]

                taecel_new                      =taecel_obj.create(taecel_data)
                
                
                
                if(taecel_new["transID"]!=""):                    
                #if(taecel_new["mensaje2"]=="Recarga Exitosa" and taecel_new["status"]=="Exitosa"):
                    vehicle["recargado"]=ahora
                    print("transID==", taecel_new["transID"])
                    self.write(vehicle)
                                
