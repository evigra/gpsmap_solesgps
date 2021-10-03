# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import http, api, fields, models, _
from odoo.http import request
from odoo.addons.portal.controllers.web import Home



class WebsiteSort(Home):
   @http.route()
   def index(self, **kw):
       super(WebsiteSort, self).index()
       return request.render('website.homepage', {})


class geofence(models.Model):
    _inherit = "gpsmap.geofence"
    

class vehicle(models.Model):
    _inherit = "fleet.vehicle"


