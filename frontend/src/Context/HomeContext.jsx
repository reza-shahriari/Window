import React,{createContext, use, useState} from "react";
import all_product from "../Components/Assets/all_product";

export const HomeContext = createContext(null);

const getDefaultCart = ()=>{
    let cart = {};
    for (let index = 1; index < all_product.length +1; index++) {
        cart[index] = 0;
    }
    return cart;
}

export const HomeContextProvider = (props) => {

    const [cartItems,setCartItems] = useState(getDefaultCart());

    const getTotalCartAmount = () =>{
        let totalAmount = 0;
        for(const item in cartItems){
            if (cartItems[item] > 0){
                let itemInfo = all_product.find((product) => product.id === Number(item));
                if (itemInfo.category ==='Rent'){
                    totalAmount += cartItems[item] * (Number(itemInfo.rent_price)); 
                }
                else{
                    totalAmount += cartItems[item] * (Number(itemInfo.sale_price));
                }
            }
        }
        return totalAmount;
    }

    const getTotalCartItem = () => {
        let totalItem = 0;
        for(const item in cartItems){
            if (cartItems[item] > 0){
                totalItem += cartItems[item]
            }
        }
        return totalItem
    }

    const addToCart = (itemId) =>{
        setCartItems((prev)=>({...prev,[itemId]:prev[itemId]+1}))
        console.log(cartItems)
    }
    const removeFromCart = (itemId) =>{
        setCartItems((prev)=>({...prev,[itemId]:prev[itemId]-1}))
    }    
    const contextValue = {all_product,cartItems,addToCart,removeFromCart,getTotalCartAmount,getTotalCartItem};



    return(
        <HomeContext.Provider value={contextValue}>
            {props.children}
        </HomeContext.Provider>
    )
}

export default HomeContextProvider;