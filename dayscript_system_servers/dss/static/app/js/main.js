"use strict";
/* Importar librerias adicionales */
var platform_browser_dynamic_1 = require('@angular/platform-browser-dynamic'); // importa boostrap de angular
var http_1 = require('@angular/http'); // importal soporte http
var app_component_1 = require('./app.component'); //
platform_browser_dynamic_1.bootstrap(app_component_1.AppComponent, [http_1.HTTP_PROVIDERS]);
//# sourceMappingURL=main.js.map