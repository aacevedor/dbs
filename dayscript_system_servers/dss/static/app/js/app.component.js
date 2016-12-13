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
var core_1 = require('@angular/core');
var common_1 = require('@angular/common');
var getResults_1 = require("./getResults");
var KeysPipe = (function () {
    function KeysPipe() {
    }
    KeysPipe.prototype.transform = function (value, args) {
        var keys = [];
        for (var key in value) {
            keys.push({ key: key, value: value[key] });
        }
        return keys;
    };
    KeysPipe = __decorate([
        core_1.Pipe({ name: 'keys' }), 
        __metadata('design:paramtypes', [])
    ], KeysPipe);
    return KeysPipe;
}());
exports.KeysPipe = KeysPipe;
var AppComponent = (function () {
    function AppComponent(_httpInfoService) {
        this._httpInfoService = _httpInfoService;
        this.getDataFromServer();
        this.getDataInfoServer();
        this.reloadFoundationElements();
    }
    AppComponent.prototype.reloadFoundationElements = function () {
        jQuery(document).foundation();
    };
    AppComponent.prototype.getDataFromServer = function () {
        var _this = this;
        this._httpInfoService.getCarsRestful() // extends to method for HttpCarService clas
            .subscribe(function (data) { return _this.getMyCarsFromServer = data; }, // put the data returned from the server in our variable
        function (// put the data returned from the server in our variable
            error) { return console.log("Error HTTP GET Service"); }, // in case of failure show this message
        function () { return console.log(_this.getMyCarsFromServer); } //run this code in all cases
         //run this code in all cases
        );
    };
    AppComponent.prototype.getDataInfoServer = function () {
        var _this = this;
        this._httpInfoService.getServersInfo()
            .subscribe(function (data) { return _this.getInfoServer = data; }, // put the data returned from the server in our variable
        function (// put the data returned from the server in our variable
            error) { return console.log("Error HTTP GET Service"); }, // in case of failure show this message
        function () { return console.log(_this.getInfoServer); } //run this code in all cases
         //run this code in all cases
        );
    };
    AppComponent.prototype.excecute_command = function (id, service) {
        var _this = this;
        if (service == "mysql" || service == "files" || service == "history") {
            var command = 'show_databases';
            var url = '/service/' + service + '/id/' + id + '/command/' + command;
        }
        if (service == "mysql_backup") {
            var command = 'mysql_backup ';
            var url = '/service/' + service + '/id/' + id + '/command/' + command;
        }
        this._httpInfoService.getCommadResult(url)
            .subscribe(function (data) { return _this.getInfoCommand = data; }, // put the data returned from the server in our variable
        function (// put the data returned from the server in our variable
            error) { return console.log("Error HTTP GET Service"); }, // in case of failure show this message
        function () { return console.log(_this.getInfoCommand); } //run this code in all cases
         //run this code in all cases
        );
    };
    AppComponent = __decorate([
        core_1.Component({
            selector: 'my-app',
            templateUrl: 'static/app/templates/server_info.html',
            directives: [common_1.CORE_DIRECTIVES, common_1.FORM_DIRECTIVES],
            pipes: [KeysPipe],
            providers: [getResults_1.HttpInfoService]
        }), 
        __metadata('design:paramtypes', [getResults_1.HttpInfoService])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map