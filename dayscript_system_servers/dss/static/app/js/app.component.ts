/* INFORMACIóN */
/*import { nombres de las clases a importar separadas por comas } from 'nombre del archivo';*/
import {Component,Pipe, PipeTransform} from '@angular/core'; // importar nucleo de anguar
import {CORE_DIRECTIVES, NgClass, FORM_DIRECTIVES, Control, ControlGroup, FormBuilder, Validators} from '@angular/common'; // importa librerias adicionales
import {HttpInfoService} from "./testing";


declare var jQuery:any;

@Pipe({name: 'keys'})// permite convertir un objeto en un arreglo
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
  templateUrl: '/static/app/templates/block-server-intro.html',
  directives: [CORE_DIRECTIVES, FORM_DIRECTIVES],
  pipes: [KeysPipe],
  providers: [HttpInfoService]
})
export class AppComponent {
  NameServer:string ="Servidor de prueba";
  json:Object;
  constructor(private _HttpInfoService: HttpInfoService){
   this.ProcessData();
  }

  ProcessData(){
    this._HttpInfoService.getJsonTest().subscribe(
      data => this.json = data,
      error => console.log('Error obteniendo el json'),
      () =>  console.log(this.json) 
    )

  }

}
