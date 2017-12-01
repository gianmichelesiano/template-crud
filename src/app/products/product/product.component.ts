import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms'

import { ProductService } from '../shared/product.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  constructor(private productService: ProductService) { }

  ngOnInit() {
    this.resetForm();
  }


  onSubmit(form: NgForm) {
    
    if (form.value.$key == null){ 
     
      this.productService.insertProduct(form.value);
    }
    else {
      this.productService.updateProduct(form.value);
    }
    this.resetForm(form);
  }

  resetForm(form?: NgForm) {
    if (form != null)
      form.reset();
    this.productService.selectedProduct = {
$key: null,
name: "",
position: "",
office: "",
salary: 0,

    }
  }

  onDelete(form: NgForm) {
    if (confirm('Are you sure to delete this record ?') == true) {
      this.productService.deleteProduct(form.value.$key);
      this.resetForm(form);
    }
  }
}
