import React , {useContext} from 'react'
import all_product from '../Components/Assets/all_product'
import {Product2} from '../Components/Product2/Product2';
import './CSS/Product.css'
const Product = () => {
  
  return (
    <div className='shop'>
      <div className='shopTitle'>
        <h1>All Cars</h1>
      </div>
      <div className='products'>
        {" "}
        {all_product.map((product)=> (
          <Product2 data={product}/>
        ))}
      </div>
      
    </div>
  )
}

export default Product
