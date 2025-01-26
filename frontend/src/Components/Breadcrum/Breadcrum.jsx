import React from 'react'
import './Breadcrum.css'
import arrow_icon from '../Assets/breadcrum arrow icon.png'

const Breadcrum = (props) => {
    const {product} = props;
  return (
    <div className='breadcrum '>
      HOME ---- Cars ----- {product.category}-----{product.name}
    </div>
  )
}

export default Breadcrum
