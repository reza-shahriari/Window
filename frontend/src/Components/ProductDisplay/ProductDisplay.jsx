import React, { useContext } from 'react'
import './ProductDisplay.css'

const ProductDisplay = (props) => {
    const product = props;
  return (
    <div className='productdisplay'>
        <div className="productdisplay-left">
            <div className="productdisplay-img-list">
                <img src={product.image} alt="" />
                <img src={product.image} alt="" />
                <img src={product.image} alt="" />
                <img src={product.image} alt="" />
            </div>
            <div className="productdisplay-img">
                <img className='productdisplay-main-img'src={product.image} alt="" />
            </div>
    
        </div>
        <div className="productdisplay-right">
            <h1>{product.name}</h1>
            <div className="productdisplay-right-star">
            </div>
            <div className="productdisplay-right-prices">

            </div>

        </div>
      
    </div>
  )
}

export default ProductDisplay;
