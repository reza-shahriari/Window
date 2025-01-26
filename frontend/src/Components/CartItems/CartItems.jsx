import React, { useContext } from 'react'
import { HomeContext } from '../../Context/HomeContext';

export const CartItem = (props) => {
    const {id,name,category,model,rent_price,sale_price,image} = props.data
    const {cartItems , addToCart , removeFromCart} = useContext(HomeContext);


  return (
    <div className='cartItem'>
        <img src={image} alt="" />
        <div className='description'>
            <p>
                <b>{name}</b>
            </p>
            <p>{rent_price}</p>
            <p>{sale_price}</p>
            <div className="countHandler">
                <button onClick={() => removeFromCart(id)}> - </button>
                <input value={cartItems[id]} />
                <button onClick={() => addToCart(id)}> + </button>
            </div>
        </div>
      
    </div>
  )
}

export default CartItem
