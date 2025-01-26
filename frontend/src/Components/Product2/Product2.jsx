import React, { useContext } from 'react'
import './Product2.css'
import { HomeContext } from '../../Context/HomeContext';
export const Product2 = (props) => {
    const {id,name,category,model,rent_price,sale_price,image} = props.data;
    const {addToCart , cartItems} = useContext(HomeContext)
    const cartItemAmount = cartItems[id]
  return (
    <div className='product'>
        <img src={image} alt="" />
        <div className='description'>
            <p><b>{name}</b></p>
            <p>{rent_price}</p>
            <p>{sale_price}</p>
        </div>
        <button className='addToCartBttn' onClick={() => addToCart(id)}>Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}</button>
    </div>
  )
}

export default Product2
