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
/* INFORMACIóN */
/*import { nombres de las clases a importar separadas por comas } from 'nombre del archivo';*/
var core_1 = require("@angular/core"); // importar nucleo de anguar
var common_1 = require("@angular/common"); // importa librerias adicionales
var testing_1 = require("./testing");
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
    return KeysPipe;
}());
KeysPipe = __decorate([
    core_1.Pipe({ name: 'keys' }) // permite convertir un objeto en un arreglo
    ,
    __metadata("design:paramtypes", [])
], KeysPipe);
exports.KeysPipe = KeysPipe;
var AppComponent = (function () {
    function AppComponent(_HttpInfoService) {
        this._HttpInfoService = _HttpInfoService;
        this.NameServer = "Servidor de prueba";
        this.ProcessData();
    }
    AppComponent.prototype.ProcessData = function () {
        var _this = this;
        this._HttpInfoService.getJsonTest().subscribe(function (data) { return _this.json = data; }, function (error) { return console.log('Error obteniendo el json'); }, function () { return console.log(_this.json); });
    };
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        templateUrl: '/static/app/templates/block-server-intro.html',
        directives: [common_1.CORE_DIRECTIVES, common_1.FORM_DIRECTIVES],
        pipes: [KeysPipe],
        providers: [testing_1.HttpInfoService]
    }),
    __metadata("design:paramtypes", [testing_1.HttpInfoService])
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map