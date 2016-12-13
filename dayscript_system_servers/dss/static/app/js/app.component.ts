import { Component,Pipe, PipeTransform} from '@angular/core';
import {CORE_DIRECTIVES, NgClass, FORM_DIRECTIVES, Control, ControlGroup, FormBuilder, Validators} from '@angular/common';
import {HttpInfoService} from "./getResults";

declare var jQuery:any;


@Pipe({name: 'keys'})// Library Pipe permit ngFor keys the object
export class KeysPipe implements PipeTransform {
  transform(value, args:string[]) : any {
    let keys = [];
    for (let key in value) {
      keys.push({key: key, value: value[key]});
    }
    return keys; 
  }
}

@Component({
  selector: 'my-app',
  templateUrl: 'static/app/templates/server_info.html',
  directives: [CORE_DIRECTIVES, FORM_DIRECTIVES],
  pipes: [KeysPipe],
  providers: [HttpInfoService]
})
export class AppComponent {
  getMyCarsFromServer:string;
  getInfoServer:string;
  getInfoCommand:string;


  constructor(private _httpInfoService:HttpInfoService){ // extends to HttpCarService class
    this.getDataFromServer()
    this.getDataInfoServer()
    this.reloadFoundationElements()
  }
  reloadFoundationElements(){ // update Foundation elements
    jQuery(document).foundation()
  }
  getDataFromServer(){
        this._httpInfoService.getCarsRestful() // extends to method for HttpCarService clas
            .subscribe(
                data => this.getMyCarsFromServer = data, // put the data returned from the server in our variable
                error => console.log("Error HTTP GET Service"), // in case of failure show this message
                () => console.log(this.getMyCarsFromServer)//run this code in all cases
            );
    }
    getDataInfoServer(){
          this._httpInfoService.getServersInfo()
              .subscribe(
                  data => this.getInfoServer = data, // put the data returned from the server in our variable
                  error => console.log("Error HTTP GET Service"), // in case of failure show this message
                  () => console.log(this.getInfoServer)//run this code in all cases
              );
      }

    excecute_command(id,service){
      if( service == "mysql" || service == "files" || service == "history" ){
        var command = 'show_databases'
        var url = '/service/'+service+'/id/'+id+'/command/'+command
      }
      if( service == "mysql_backup"){
        var command = 'mysql_backup '
        var url = '/service/'+service+'/id/'+id+'/command/'+command
      }
      this._httpInfoService.getCommadResult(url)
          .subscribe(
              data => this.getInfoCommand = data, // put the data returned from the server in our variable
              error => console.log("Error HTTP GET Service"), // in case of failure show this message
              () => console.log(this.getInfoCommand)//run this code in all cases
          );
    }
}
