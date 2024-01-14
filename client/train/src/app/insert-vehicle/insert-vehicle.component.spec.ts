import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsertVehicleComponent } from './insert-vehicle.component';

describe('InsertVehicleComponent', () => {
  let component: InsertVehicleComponent;
  let fixture: ComponentFixture<InsertVehicleComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InsertVehicleComponent]
    });
    fixture = TestBed.createComponent(InsertVehicleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
