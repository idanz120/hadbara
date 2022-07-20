import React from 'react'

const MyCart = (props) => {
  const saveCart=()=>{
    localStorage.setItem("cart",JSON.stringify(props.cart))
  }
  return (
    <div>{props.cart.length >0 &&<div> {props.cart.map((item,ind) =><div key={ind}>{item.desc} {""} {item.price}
      <button onClick={() => props.del(ind)}>Rmove</button>
     </div>)}
     </div>}
     <button onClick={()=>saveCart()}>Save</button>
    </div>
  )
}

export default MyCart