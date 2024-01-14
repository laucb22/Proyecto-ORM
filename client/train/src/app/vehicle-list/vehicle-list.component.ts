import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-vehicle-list',
  templateUrl: './vehicle-list.component.html',
  styleUrls: ['./vehicle-list.component.css']
})
export class VehicleListComponent implements OnInit  {
  vehicles: any[] = []
  brands: any[] = []
  types: any[] = [];
  statuses: any[] = []
  constructor(private api: ApiService){}

  ngOnInit() {
    this.api.getAllVehicles().subscribe((data: any[]) => {
      this.vehicles = data
    })
    this.api.getBrands().subscribe((data: any[]) =>{
      this.brands = data
    })
    this.api.getTypes().subscribe((data: any[]) =>{
      this.types = data;
    })
    this.api.getStatuses().subscribe((data: any[]) =>{
      this.statuses = data
    })
  }
  
  onDelete(plateNumber: string){
    this.api.deleteVehicle(plateNumber).subscribe(
      response => {
        console.log('Vehicle deleted successfully', response);
      },
      error => {
        console.error('Error deleting vehicle', error);
      }
    );
  }

  onSubmit(value: any){
    console.log(value)
  }
  clearFilters(){
    console.log("CLEARING")
    this.api.getAllVehicles().subscribe((data: any[]) => {
      this.vehicles = data
    })
  }

}
