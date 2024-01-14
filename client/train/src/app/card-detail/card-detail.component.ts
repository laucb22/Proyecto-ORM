import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-card-detail',
  templateUrl: './card-detail.component.html',
  styleUrls: ['./card-detail.component.css']
})
export class CardDetailComponent implements OnInit{
  plateNumber: any;
  vehicle: any;

  constructor(private route: ActivatedRoute, private apiService: ApiService) {}

  ngOnInit() {
    this.plateNumber = this.route.snapshot.paramMap.get('plateNumber');
    console.log(this.plateNumber);
    this.apiService.getVehicleById(this.plateNumber).subscribe(
      data => {
        this.vehicle = data[0];
        console.log(this.vehicle);
      },
      error => {
        console.error('Error al obtener los detalles del vehículo', error);
      }
    );
  }
}
