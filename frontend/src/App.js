import './App.css';
import Navbar from './Components/Navbar/Navbar';
import {BrowserRouter,Routes, Route} from 'react-router-dom';
import HomeCategory from './Pages/HomeCategory';
import Product from './Pages/Product';
import LoginSignup from './Pages/LoginSignup';
import Home from './Pages/Home';
import Cart from './Pages/Cart';
import Upload from './Pages/Upload';
import Footer from './Components/Footer/Footer';
import rent_banner from '../src/Components/Assets/rent banner.png'
import sale_banner from '../src/Components/Assets/sale banner.png'


/*          <Route path='/productId' element={<Product/>}></Route>
*/
function App() { 
  return (
    <div>
      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path='/Home' element={<Home/>}/>
        <Route path='/Rent' element={<HomeCategory banner = {rent_banner} category="Rent"/>}/>
        <Route path='/Sale' element={<HomeCategory banner = {sale_banner} category="Sale"/>}/>
        <Route path="/Product" element={<Product/>}>
          <Route path=':ProductID' element={<Product/>}/>
        </Route>
        <Route path='/cart' element={<Cart/>}/>
        <Route path='/Login' element={<LoginSignup/>}/>
        <Route path='/Upload' element={<Upload/>}/>
      </Routes>
      <Footer></Footer>
      </BrowserRouter>
    </div>
  );
}

export default App;
