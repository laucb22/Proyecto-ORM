import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-insert-vehicle',
  templateUrl: './insert-vehicle.component.html',
  styleUrls: ['./insert-vehicle.component.css']
})
export class InsertVehicleComponent implements OnInit {
  brands: any[] = []
  formData: any = {};

  constructor(private api: ApiService){}

  onSubmit(value: any){
    console.log(value)
  }

  ngOnInit(): void {
    this.api.getBrands().subscribe((data: any[]) =>{
      this.brands = data
    })
  }
}
