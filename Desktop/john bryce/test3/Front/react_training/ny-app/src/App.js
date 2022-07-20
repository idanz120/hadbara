import { useState } from 'react';
import './App.css';
import prods from './MyDB';
import './MyCart';
import MyCart from './MyCart';

function App() {
  const [myprods, setMyprods] = useState(prods)
  const [price, setPrice] = useState(0)
  const [desc, setdesc] = useState("")
  const [cart, setcart] = useState([])
  const SERVER_URL='http://localhost:3004/prods'
  const DJANGO ='http://127.0.0.1:8000/'
  const addPoduct=() =>{
    setMyprods([
      ...myprods,
      {
        "desc":desc,
        "price": price
      }
    ])
    console.log(myprods)

 

  }

  const delFromCart=(i)=>{
      console.log(i)
      setcart(cart.filter(x => x.desc != cart[i].desc))
  }
  const loadCart= async()=>{
   setMyprods(await fetch(SERVER_URL).then(response => response.json()))
    
    

    console.log(localStorage.getItem("cart"))
  }
  const addToCart=async(i) =>{
    setcart([ ...cart,myprods[i]])
     console.table(cart)
  }
  const test=async()=>{
   let res= await fetch(DJANGO).then(response => response.json())
   console.log(res)
  }
  return (
    <div className="App">
      <button onClick={()=>test()}>test</button>
      <button onClick={()=>loadCart()}>Load</button>
      <MyCart del={delFromCart} cart={cart}></MyCart>
      <hr></hr>
      <button onClick={() => addPoduct()}>Add</button>
      Price:<input onChange={(e) => setPrice(e.target.value)}/>
      Desc:<input onChange={(e) => setdesc(e.target.value)}/>
      {myprods.map((item,ind) =><div key={ind}>{item.desc} {""} {item.price} <button onClick={() =>addToCart(ind)}>Buy</button></div>)}
    </div>
  );
}

export default App;
