def convertVar(val):
    if val == '$key':
        return 'null'
    elif val == 'number':
        return '0'
    else:
        return '""'


modello = 'Product'
modelli = modello+'s'
modelloList = modello.lower()+'List'


classModello = {
    '$key' : '$key',
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

    #listaVar = listaVar + uno+": "+modello.lower()+"."+uno+",\n"
    listaVar = listaVar + uno +': '+convertVar(classModello[uno])+',\n'
    print listaVar
    print "*************************"





componentTS = """
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms'

import { EmployeeService } from '../shared/employee.service';

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  constructor(private employeeService: EmployeeService) { }

  ngOnInit() {
    this.resetForm();
  }


  onSubmit(form: NgForm) {
    if (form.value.$key == null)
      this.employeeService.insertEmployee(form.value);
    else
      this.employeeService.updateEmployee(form.value);
    this.resetForm(form);
  }

  resetForm(form?: NgForm) {
    if (form != null)
      form.reset();
    this.employeeService.selectedEmployee = {
"""+listaVar+"""
    }
  }

  onDelete(form: NgForm) {
    if (confirm('Are you sure to delete this record ?') == true) {
      this.employeeService.deleteEmployee(form.value.$key);
      this.resetForm(form);
    }
  }
}

"""

componentTS = componentTS.replace('employee', modello.lower()).replace('Employee', modello).replace('employees', modelli.lower()).replace('Employees', modelli).replace('employeeList', modelloList)
print componentTS



