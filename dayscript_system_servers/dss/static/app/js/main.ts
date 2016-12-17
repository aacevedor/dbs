
/* Importar librerias adicionales */
import { bootstrap }    from '@angular/platform-browser-dynamic'; // importa boostrap de angular
import { HTTP_PROVIDERS } from '@angular/http'; // importal soporte http
import { BaseClass } from './app.component'; //
/**/
bootstrap(BaseClass,[ HTTP_PROVIDERS ]);
