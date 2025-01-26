import React, { useContext } from 'react'
import {all_product} from '../Components/Assets/all_product'
import {Product2} from '../Components/Product2/Product2'
import { HomeContext } from '../Context/HomeContext'
import {CartItem} from '../Components/CartItems/CartItems'
import './CSS/Cart.css'

export const Cart = () => {
  const {cartItems , getTotalCartAmount} = useContext(HomeContext);
  const totalAmount = getTotalCartAmount();
  return (
    <div className='cart'>
      <div>
        <h1>Your Cart Items</h1>
      </div>
      <div className='cartItems'>
        {all_product.map((product) => {
          if(cartItems[product.id] !== 0){
            return <CartItem data={product}/>
          }
        })}
      </div>
     {totalAmount > 0 ? ( 
      <div className="checkout">
        <p> Subtotal : $ {totalAmount}</p>
        <button> Continue Shopping </button>
        <button> Checkout </button>
      </div>
     ) : (
        <h1>Your Cart is Empty</h1>
     )}  

    </div>
  )
}

export default Cart
