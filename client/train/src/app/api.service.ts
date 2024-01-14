import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient ) { }

  getVehicles(): Observable<any[]>{
    return this.http.get<any[]>("http://localhost:5000/")
  }

  getVehicleById(plateNumber: any): Observable<any[]>{
    return this.http.get<any[]>(`http://localhost:5000/getVehicleById/${plateNumber}`)
  }

  getAllVehicles(): Observable<any[]>{
    return this.http.get<any[]>("http://localhost:5000/getAllVehicles")
  }

  deleteVehicle(plateNumber: string): Observable<any> {
    return this.http.delete("http://localhost:5000/deleteVehicle", { body: { number: plateNumber } })
  }

  getBrands(): Observable<any[]>{
    return this.http.get<any[]>("http://localhost:5000/getBrands");
  }
}
