import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { InsertVehicleComponent } from './insert-vehicle/insert-vehicle.component';


const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'insert', component: InsertVehicleComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
