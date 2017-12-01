import { Injectable } from '@angular/core';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';



import { Product } from './product.model';

@Injectable()
export class ProductService {
  productList: AngularFireList<any>;
  selectedProduct: Product = new Product();
  constructor(private firebase: AngularFireDatabase) {
     this.productList = firebase.list('products');
  }

  getData() {
    this.productList = this.firebase.list('products');
    return this.productList;
  }

  insertProduct(product: Product) {
    this.productList.push({
    name: product.name,
    position: product.position,
    office: product.office,
    salary: product.salary,

    });
  }

  updateProduct(product : Product){
    this.productList.update(product.$key,{
    name: product.name,
    position: product.position,
    office: product.office,
    salary: product.salary,

     })
  }

  deleteProduct(key : string){
    this.productList.remove(key);
  }

}