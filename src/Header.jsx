import React from "react"

function Header(){
    return(
        <>
        <div className="flex justify-around sticky top-2 bg-[rgba(255,255,255,0.5)]  text-white my-0 p-10">
            <div className="flex justify-center items-center text-4xl font-sans text-white font-black">G U A R D I F Y</div>
            <div className="flex gap-5">
            <button className="flex justify-center text-2xl font-sans font-semibold items-center rounded opacity-40 bg-gray-600 m-1 p-2 cursor-pointer">Knowledgebase</button>
            <button className="flex justify-center text-2xl font-sans font-semibold items-center rounded opacity-40 bg-gray-600 m-1 p-2 cursor-pointer">Support</button>
            </div>
            
        </div>
        </>
    )
}


export default Header;