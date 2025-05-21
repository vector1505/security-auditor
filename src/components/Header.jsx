import React from "react"

function Header(){
    return(
        <>
        <div className="flex justify-around sticky top-2 bg-[rgba(31,41,55,0.95)]  text-white my-0 p-10">
            <div className="flex justify-center items-center text-4xl font-sans text-white font-black">G U A R D I F Y</div>
            <div className="flex gap-15">
            <button className="flex justify-center text-2xl font-sans font-bold items-center rounded-lg opacity-40 bg-gray-900 m-1 p-5 cursor-pointer">Knowledgebase</button>
            <button className="flex justify-center text-2xl font-sans font-bold items-center rounded-lg opacity-40 bg-gray-900 m-1 p-5 cursor-pointer">Support</button>
            </div>
            
        </div>
        </>
    )
}


export default Header;