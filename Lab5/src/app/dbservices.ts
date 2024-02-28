import { Injectable } from '@angular/core';
import {Category} from "./category.model";

@Injectable({
  providedIn: 'root'
})
export class DBService {
  categories: Category[] = [
    {
      "id": 1,
      "name": "Electronics",
      "products": [
        {
          "id": 101,
          "name": "Smartphone",
          "likes" : 121
        },
        {
          "id": 102,
          "name": "Laptop",
          "likes" : 23
        },
        {
          "id": 103,
          "name": "Smartwatch",
          "likes" : 45
        },
        {
          "id": 104,
          "name": "Headphones",
          "likes" : 12
        },
        {
          "id": 105,
          "name": "Tablet",
          "likes" : 76
        }
      ]
    },
    {
      "id": 2,
      "name": "Clothing",
      "products": [
        {
          "id": 201,
          "name": "T-shirt",
          "likes" : 452
        },
        {
          "id": 202,
          "name": "Jeans",
          "likes" : 128
        },
        {
          "id": 203,
          "name": "Sneakers",
          "likes" : 2345
        },
        {
          "id": 204,
          "name": "Dress",
          "likes" : 35
        },
        {
          "id": 205,
          "name": "Jacket",
          "likes" : 87
        }
      ]
    }
  ]
  
  removeProduct(productId: number) {
    this.categories.forEach(category => {
      const index = category.products.findIndex(product => product.id === productId);
      if (index !== -1) {
        category.products.splice(index, 1);
      }
    });
  }


  likeProduct(productId: number){
    this.categories.forEach( category =>{
      category.products.forEach(product => {
        if(product.id === productId) product.likes++;
      })
    })
  }
}

