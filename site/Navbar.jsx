import React, { useContext, useState } from 'react'
import './Navbar.css'
import cart_icon from '../Assets/shopping-cart-icon.png'
import logo from '../Assets/logo.png'
import {Link} from 'react-router-dom'
import { HomeContext } from '../../Context/HomeContext'
const Navbar = () => {

    const[menu,setMenu] =  useState("Home");

    const {getTotalCartItem} = useContext(HomeContext);

  return (
    <div className='navbar'>
        <div className='nav-logo'>
            <img src={logo} height={66.6} width={100} alt="" />
            <p>WINDOW</p>
        </div>
        <ul className='nav-menu'>
            <li onClick={()=>{setMenu("Home")}}><Link style={{textDecoration : 'none'}} to="/Home">Home</Link>{menu==="Home"? <hr/>:<></>}</li>
            <li onClick={()=>{setMenu("Rent")}}><Link style={{textDecoration : 'none'}} to="/Rent">Rent</Link>{menu==="Rent"? <hr/>:<></>}</li>
            <li onClick={()=>{setMenu("Sale")}}><Link style={{textDecoration : 'none'}} to="/Sale">Sale</Link>{menu==="Sale"? <hr/>:<></>}</li>
            <li onClick={()=>{setMenu("Upload")}}><Link style={{textDecoration : 'none'}} to="/Upload">Upload</Link>{menu==="Upload"? <hr/>:<></>}</li>
        </ul>
        <div className='nav-login-cart'>
            <Link to="/Login"><button>Login</button></Link>
            <Link to="Cart"><img src={cart_icon} height={30} width={30} alt="" /></Link>
            <div className='nav-cart-count'>{getTotalCartItem()}</div>
        </div>
      
    </div>
  )
}

export default Navbar
