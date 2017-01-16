import {Injectable} from '@angular/core';// Library angular2 core for inject dependences in app.componet file
import {Http, Response} from '@angular/http';
import {Headers, RequestOptions} from '@angular/http';
import 'rxjs/add/operator/map';// Library angular2 contrib run the .map() method in Json
import {Observable}     from 'rxjs/Observable';


@Injectable()// indica a angular que la clase se puede injectar en otra clase
export class HttpInfoService {
    private JsonTest:string = "http://blaa.demodayscript.com/api/node.json";

    constructor(private _http: Http){ }

    getJsonTest(){
        this._http.get(this.JsonTest).map(res => res.json());
        return this._http.get(this.JsonTest).map(res => res.json());
    }

}
