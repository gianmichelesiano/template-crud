import { Component, OnInit } from '@angular/core';

import { ProductService } from '../shared/product.service';
import { Product } from '../shared/product.model';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  productlist: Product[];
  constructor(private productService: ProductService) { }

  ngOnInit() {
    var x = this.productService.getData();
    x.snapshotChanges().subscribe(item => {
      this.productlist = [];
      item.forEach(element => {
        var y = element.payload.toJSON();
        y["$key"] = element.key;
        this.productlist.push(y as Product);
      });
    });

  }

  onItemClick(emp : Product){
    this.productService.selectedProduct = Object.assign({},emp);
  }


}
