import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-edit-vehicle',
  templateUrl: './edit-vehicle.component.html',
  styleUrls: ['./edit-vehicle.component.css']
})
export class EditVehicleComponent {
  plateNumber: any;
  vehicle: any;
  vehiclePlateNumber: string = '';
  vehicleColor: string = '';
  vehicleStatus: string = '';
  vehiclePrice: any = '';

  constructor(private route: ActivatedRoute, private apiService: ApiService) {}

  onSubmit(value: any){
    console.log(value);
    this.apiService.editVehicle(value).subscribe(
      (response) => {
        console.log('API Response:', response);
      },
      (error) => {
        console.error('API Error:', error);
      }
    );
  }

  ngOnInit() {
    this.plateNumber = this.route.snapshot.paramMap.get('plateNumber');
    console.log(this.plateNumber);
    this.apiService.getVehicleById(this.plateNumber).subscribe(
      data => {
        this.vehicle = data[0];
        this.vehiclePlateNumber = this.vehicle.plate_number;
        this.vehicleColor = this.vehicle.color;
        this.vehiclePrice = this.vehicle.price;
        this.vehicleStatus = this.vehicle.status.status
      },
      error => {
        console.error('Error al obtener los detalles del vehículo', error);
      }
    );
  }
}
