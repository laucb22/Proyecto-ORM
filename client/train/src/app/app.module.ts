import { NgModule, LOCALE_ID } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ApiService } from './api.service';
import { CardDetailComponent } from './card-detail/card-detail.component';
import { NavbarComponent } from './navbar/navbar.component';
import { InsertVehicleComponent } from './insert-vehicle/insert-vehicle.component';
import { FooterComponent } from './footer/footer.component';
import { VehicleListComponent } from './vehicle-list/vehicle-list.component';
import { FormsModule }   from '@angular/forms';
import { EditVehicleComponent } from './edit-vehicle/edit-vehicle.component';
import { registerLocaleData } from '@angular/common';
import localeEs from '@angular/common/locales/es';
registerLocaleData(localeEs);


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CardDetailComponent,
    NavbarComponent,
    InsertVehicleComponent,
    FooterComponent,
    VehicleListComponent,
    EditVehicleComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ApiService, { provide: LOCALE_ID, useValue: 'es-ES'}],
  bootstrap: [AppComponent]
})
export class AppModule { }
