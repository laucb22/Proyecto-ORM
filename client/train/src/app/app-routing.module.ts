import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { InsertVehicleComponent } from './insert-vehicle/insert-vehicle.component';
import { CardDetailComponent } from './card-detail/card-detail.component';
import { VehicleListComponent } from './vehicle-list/vehicle-list.component';
import { EditVehicleComponent } from './edit-vehicle/edit-vehicle.component';


const routes: Routes = [
  
  { path: '', component: HomeComponent },
  {path: 'home', component: HomeComponent},
  {path: 'insert', component: InsertVehicleComponent},
  { path: 'vehicle-detail/:plateNumber', component: CardDetailComponent },
  { path: 'vehicle-edit/:plateNumber', component: EditVehicleComponent },
  {path: 'list', component: VehicleListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
