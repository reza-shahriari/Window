import React from 'react'
import './Hero.css';
import fast_icon from '../Assets/fast.png';
import affordable_icon from '../Assets/affordable.png'
import reliable_icon from '../Assets/reliabel.png'
import back_img from "../Assets/rolls3.png"

const Hero = () => {
  return (
    <div className='hero'>
      <div className="hero-left">
        <h2>WINDOW</h2>
        <div>
            <div className='hero-fast-icon'>
                <p>Fast</p>
            </div>

            <div className='hero-affordable-icon'>
                <p>Affordable</p>
            </div>

            <div className='hero-reliable-icon'>
                <p>Reliable</p>
            </div>
            
        </div>

        <div className="hero-start-btn">
            <div>Let's Drive Now</div>
        </div>
      </div>
      <div className="hero-right">
      </div>
    </div>
  )
}

export default Hero
