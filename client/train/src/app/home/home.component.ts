import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  vehicles: any[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getVehicles().subscribe((data: any[]) => {
      this.vehicles = data;
    })

  }
}
