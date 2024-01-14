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

  getTypes(): Observable<any[]>{
    return this.http.get<any[]>("http://localhost:5000/getTypes")
  }

  newVehicle(vehicleData: any): Observable<any[]>{
    return this.http.post<any[]>("http://localhost:5000/insertVehicle", vehicleData)
  }

  getStatuses(): Observable<any[]>{
    return this.http.get<any[]>("http://localhost:5000/getStatuses")
  }

  filterVehicles(): Observable<any[]>{
    return this.http.get<any[]>("http://localhost:5000/filter")
  }
}
