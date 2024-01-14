import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-insert-vehicle',
  templateUrl: './insert-vehicle.component.html',
  styleUrls: ['./insert-vehicle.component.css']
})
export class InsertVehicleComponent implements OnInit {
  brands: any[] = []
  types: any[] = [];
  statuses: any[] = []
  formData: any = {};

  constructor(private api: ApiService){}

  onSubmit(value: any){
    this.api.newVehicle(value).subscribe(
      (response) => {
        console.log('API Response:', response);
      },
      (error) => {
        console.error('API Error:', error);
      }
    );
  }

  ngOnInit(): void {
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
}
