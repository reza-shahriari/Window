import React, { useContext } from 'react'
import './Item.css'
import { Link } from 'react-router-dom'
import { HomeContext } from '../../Context/HomeContext'

const Item = (props) => {
  const {addToCart} = useContext(HomeContext);
  return (
    <div className='item'>
        <Link to={`/product/${props.id}`}><img src={props.image} alt="" /></Link>
        <p>{props.name}</p>
        <div className='item-prices'>
            <div className='item-price-rent'>
                {props.rent_price}
            </div>
            <div className='item-price-sale'>
                {props.sale_price}
            </div>
        </div>
     
    </div>
  )
}

export default Item
