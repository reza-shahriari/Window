import React from 'react'
import './Footer.css'
import footer_logo from '../Assets/logo.png'
import instagram_icon from '../Assets/instagram.jpg'
import facebook_icon from '../Assets/facebook.png'
import whatsapp_icon from '../Assets/whatsapp.png'
import { TiSocialFacebook } from "react-icons/ti";
import { SlSocialInstagram } from "react-icons/sl";
import { SlSocialLinkedin } from "react-icons/sl";

const Footer = () => {
  return (
    <div className='footer'>
        <div className='footer-logo'>
            <img src={footer_logo} height={100} width={150} alt="" />
            <p>WINDOW</p>
        </div>
        <ul className='footer-links'>
            <li>Company</li>
            <li>Office</li>
            <li>About</li>
            <li>Contact</li>
        </ul>
        <div className='footer-social-icon'>
            <div className='footer-icon-container'>
                <SlSocialInstagram />
            </div>
            <div className='footer-icon-container'>
                <TiSocialFacebook />
            </div>
            <div className='footer-icon-container'>
                <SlSocialLinkedin />
            </div>
        </div>
        <div className='footer-copyright'>
            <hr />
            <p>Copyright @ 2025 - All right Reserved</p>

        </div>
      
    </div>
  )
}

export default Footer
