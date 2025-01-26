import React from 'react'
import './NewCollections.css'
import new_collection from '../Assets/new_collections'
import Item from '../Item/item'

const NewCollections = () => {
  return (
    <div className='new-collections'>
        <h1>New Cars</h1>
        <hr />
        <div className='collections'>
            {new_collection.map((item , i) => {
                return <Item key={i} id={item.id} name={item.name} image={item.image} rent_price={item.rent_price} sale_price={item.sale_price}></Item>
            })}
        </div>
      
    </div>
  )
}

export default NewCollections
