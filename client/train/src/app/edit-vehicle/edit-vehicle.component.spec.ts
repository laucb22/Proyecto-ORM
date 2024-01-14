import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditVehicleComponent } from './edit-vehicle.component';

describe('EditVehicleComponent', () => {
  let component: EditVehicleComponent;
  let fixture: ComponentFixture<EditVehicleComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditVehicleComponent]
    });
    fixture = TestBed.createComponent(EditVehicleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
