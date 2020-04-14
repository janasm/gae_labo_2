#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2

import datetime

class GenerarFactura(webapp2.RequestHandler):
    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)

        datos = {}

        datos["cifEm"] = self.request.get("cifEm")
        datos["nombreEm"] = self.request.get("nombreEm")
        datos["direccionEm"] = self.request.get("direccionEm")
        datos["problacionEm"] = self.request.get("problacionEm")
        datos["cpEm"] = self.request.get("cpEm")
        datos["paisEm"] = self.request.get("paisEm")
        datos["contactoEm"] = self.request.get("contactoEm")
        datos["emailEm"] = self.request.get("emailEm")
        datos["tlfnEm"] = self.request.get("tlfnEm")

        datos["cifCli"] = self.request.get("cifCli")
        datos["nombreCli"] = self.request.get("nombreCli")
        datos["direccionCli"] = self.request.get("direccionCli")
        datos["problacionCli"] = self.request.get("problacionCli")
        datos["cpCli"] = self.request.get("cpCli")
        datos["paisCli"] = self.request.get("paisCli")
        datos["contactoCli"] = self.request.get("contactoCli")
        datos["emailCli"] = self.request.get("emailCli")
        datos["tlfnCli"] = self.request.get("tlfnCli")

        datos["concepto"] = self.request.get("concepto")
        datos["precioUd"] = self.request.get("precioUd")
        datos["uds"] = self.request.get("uds")
        datos["importeTotal"] = self.request.get("importeTotal")
        datos["iva"] = self.request.get("iva")

        datos["fechaFactura"] = str(datetime.datetime.now())


        self.response.write(jinja.render_template("menuFacturas.html", **datos))

app = webapp2.WSGIApplication([
    ('/generarFactura', GenerarFactura)
], debug=True)
