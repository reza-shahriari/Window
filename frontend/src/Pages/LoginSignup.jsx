import React, { useState } from "react";
import './CSS/LoginSignup.css'
import { FaUser } from "react-icons/fa";
import { FaLock } from "react-icons/fa";
import { FaEnvelope } from "react-icons/fa";
import { FaRegIdCard } from "react-icons/fa";

const LoginSignup = () => {

  return (
   <div className="Loginsignup">
    <div className="loginsignup-container">
      <h1>Sign Up</h1>
      <div className="loginsignup-fields">
        <input type="text" placeholder="Username " />
        <input type="email" placeholder="Email Address" />
        <input type="password" placeholder="Password" />
      </div>
      <button>Continue</button>
      <p className="loginsignup-login">Already have an account? <span>Login Here</span></p>
      <div className="loginsignup-agree">
        <input type="checkbox" name='' id='' />
        <p>By continuing, i agree to the terms of use & privacy policy</p>
      </div>
    </div>
   </div>
)
    
}

export default LoginSignup
