import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ApiService } from './api.service';
<<<<<<< HEAD
import { CardDetailComponent } from './card-detail/card-detail.component';
=======
import { NavbarComponent } from './navbar/navbar.component';
import { InsertVehicleComponent } from './insert-vehicle/insert-vehicle.component';
import { FooterComponent } from './footer/footer.component';

>>>>>>> d4a08a00aaca442f5c461316cd3e6f1c848a4d09

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
<<<<<<< HEAD
    CardDetailComponent
=======
    NavbarComponent,
    InsertVehicleComponent,
    FooterComponent
>>>>>>> d4a08a00aaca442f5c461316cd3e6f1c848a4d09
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
