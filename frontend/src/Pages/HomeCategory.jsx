import React,{useContext} from 'react'
import './CSS/HomeCategory.css'
import { HomeContext } from '../Context/HomeContext'
import { RiArrowDropDownLine } from "react-icons/ri";
import Item from '../Components/Item/item';


const HomeCategory = (props) => {
  const {all_product} = useContext(HomeContext);
  return (
    <div className='shop-category'>
      <img className='shopcategory-banner'src={props.banner} alt="" />
      <div className='shopcategory-indexSort'>
        <p>
          <span>Showing 1-3</span> out of 8 cars
        </p>
        <div className='shopcategory-sort'>
          Sort by <RiArrowDropDownLine />
        </div>
      </div>
      <div className='shopcategory-products'>
        {all_product.map((item , i) => {
          if (props.category === item.category){
            return <Item key={i} id={item.id} name={item.name} image={item.image} rent_price={item.rent_price} sale_price={item.sale_price}></Item>
          }

        })}
      </div>
    </div>
  )
}

export default HomeCategory
