import React from 'react'
import './Popular.css'
import data_product from '../Assets/data'
import Item from '../Item/item'

const Popular = () => {
  return (
    <div>
      <h1>POPULAR IN RENT</h1>
      <hr />
      <div className='popular-item'>
        {data_product.map((item,i)=>{
            return <Item key={i} id={item.id} name={item.name} image={item.image} rent_price={item.rent_price} sale_price={item.sale_price}></Item>

        })}
      </div>
    </div>
  )
}

export default Popular
