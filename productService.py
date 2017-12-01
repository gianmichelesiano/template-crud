modello = 'Product'
modelli = modello+'s'
modelloList = modello.lower()+'List'


classModello = {
    '$key' : 'string',
    'name' : 'string',
    'position' : 'string',
    'office' : 'string',
    'salary' : 'number',
}

listaClass = [
    '$key',
    'name',
    'position',
    'office',
    'salary'
]

listaVar = ""
for uno in listaClass:

    listaVar = listaVar + uno+": "+modello.lower()+"."+uno+",\n"





service = """
import { Injectable } from '@angular/core';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';



import { Employee } from './employee.model';

@Injectable()
export class EmployeeService {
  employeeList: AngularFireList<any>;
  selectedEmployee: Employee = new Employee();
  constructor(private firebase: AngularFireDatabase) { }

  getData() {
    this.employeeList = this.firebase.list('employees');
    return this.employeeList;
  }

  insertEmployee(employee: Employee) {
    this.employeeList.push({
    """+listaVar+"""
    });
  }

  updateEmployee(employee : Employee){
     this.employeeList.update(employee.$key,{
     """+listaVar+"""
     })
  }

  deleteEmployee(key : string){
    this.employeeList.remove(key);
  }

}
"""

service_out = service.replace('employee', modello.lower()).replace('Employee', modello).replace('employees', modelli.lower()).replace('Employees', modelli).replace('employeeList', modelloList)
print service_out



