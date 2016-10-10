import {Injectable} from '@angular/core';// Library angular2 core for inject dependences in app.componet file
import {Http, Response} from '@angular/http';
import {Headers, RequestOptions} from '@angular/http';
import 'rxjs/add/operator/map';// Library angular2 contrib run the .map() method in Json
import {Observable}     from 'rxjs/Observable';




@Injectable()// indicate to angular2 the class HttpCarService is injectable dependence
export class HttpInfoService {
    private _carsUrl:string = "http://192.168.188.128:8000/command/ls/";
    private _serversInfo:string = "http://192.168.188.128:8000/index_json/";

    constructor(private _http: Http){ }

    getCarsRestful(){// method return variable
        this._http.get(this._carsUrl).map(res => res.json());
        return this._http.get(this._carsUrl).map(res => res.json());
    }
    getServersInfo(){
        this._http.get(this._serversInfo).map(res => res.json());
        return this._http.get(this._serversInfo).map(res => res.json());
    }
    getCommadResult(url){
        this._http.get(url).map(res => res.json());
        return this._http.get(url).map(res => res.json());
    }
}
