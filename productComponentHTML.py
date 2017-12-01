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



html_begin_form = """
<form #employeeForm="ngForm" (ngSubmit)="onSubmit(employeeForm)">
<input type="hidden" name="$key" #$key="ngModel" [(ngModel)]="employeeService.selectedEmployee.$key">

"""

html_end_form = """
  <div class="form-group">
    <button type="submit" class="btn btn-default" [disabled]="!employeeForm.valid">
     <i class="fa fa-floppy-o"></i> Submit</button> 
    <button type="button" class="btn btn-default" *ngIf="employeeService.selectedEmployee.$key!=null" (click)="onDelete(employeeForm)">
        <i class="fa fa-trash"></i> Delete</button>
    <button type="button" class="btn btn-default" (click)="resetForm(employeeForm)">
        <i class="fa fa-repeat"></i> Reset</button>
  </div>
</form>
"""

html_middle = """

"""
for uno in listaClass:
    if classModello[uno] == 'string':
        html_middle = html_middle+"""
          <div class="form-group">
            <label>"""+uno.capitalize()+"""</label>
            <input class="form-control" name='"""+uno+"""' #"""+uno+"""="ngModel" [(ngModel)]='employeeService.selectedEmployee."""+uno+"""' placeholder='"""+uno+"""'>
          </div>
        """
    elif classModello[uno] == 'number':
        html_middle = html_middle+"""
          <div class="form-group">
            <label>"""+uno.capitalize()+"""</label>
            <div class="input-group">
              <div class="input-group-addon">
                <i class="fa fa-dollar"></i>
              </div>
              <input class="form-control" name='"""+uno+"""' #"""+uno+"""="ngModel" [(ngModel)]='employeeService.selectedEmployee."""+uno+"""' placeholder='"""+uno+"""'>
            </div>
          </div>
        """        

html = html_begin_form+html_middle+html_end_form
html_out = html.replace('employee', modello.lower()).replace('Employee', modello).replace('employees', modelli.lower()).replace('Employees', modelli).replace('employeeList', modelloList)
print html_out



