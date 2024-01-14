import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-vehicle-list',
  templateUrl: './vehicle-list.component.html',
  styleUrls: ['./vehicle-list.component.css']
})
export class VehicleListComponent implements OnInit  {
  vehicles: any[] = []

  constructor(private api: ApiService){}

  ngOnInit() {
    this.api.getAllVehicles().subscribe((data: any[]) => {
      this.vehicles = data
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

}
