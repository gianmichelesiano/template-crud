

modello = 'Product'
modelli = modello+'s'
modelloList = modello.lower()+'List'



componentListTS = """
<ul class="list-group hover">
  <li class="list-group-item" *ngFor="let employee of employeelist" (click)="onItemClick(employee)">
    {{employee.name}} - {{employee.position}}
  </li>
</ul>
"""

componentListTS_out = componentListTS.replace('employee', modello.lower()).replace('Employee', modello).replace('employees', modelli.lower()).replace('Employees', modelli).replace('employeeList', modelloList)
print componentListTS_out



