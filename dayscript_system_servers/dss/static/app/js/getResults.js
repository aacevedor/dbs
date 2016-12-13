"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core'); // Library angular2 core for inject dependences in app.componet file
var http_1 = require('@angular/http');
require('rxjs/add/operator/map'); // Library angular2 contrib run the .map() method in Json
var HttpInfoService = (function () {
    function HttpInfoService(_http) {
        this._http = _http;
        this._carsUrl = "/command/ls/";
        this._serversInfo = "/index_json/";
    }
    HttpInfoService.prototype.getCarsRestful = function () {
        this._http.get(this._carsUrl).map(function (res) { return res.json(); });
        return this._http.get(this._carsUrl).map(function (res) { return res.json(); });
    };
    HttpInfoService.prototype.getServersInfo = function () {
        this._http.get(this._serversInfo).map(function (res) { return res.json(); });
        return this._http.get(this._serversInfo).map(function (res) { return res.json(); });
    };
    HttpInfoService.prototype.getCommadResult = function (url) {
        this._http.get(url).map(function (res) { return res.json(); });
        return this._http.get(url).map(function (res) { return res.json(); });
    };
    HttpInfoService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [http_1.Http])
    ], HttpInfoService);
    return HttpInfoService;
}());
exports.HttpInfoService = HttpInfoService;
//# sourceMappingURL=getResults.js.map