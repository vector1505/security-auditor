import React from "react";

function Mainsite(){
    return(
        <>
            <div className="flex justify-start items-baseline my-10 bg-[url(src/assets/image.png)]">
                <div className="flex flex-col justify-start gap-20 px-50">
                    <div className="flex justify-start  items-baseline font-extrabold text-white text-4xl">Revolutionizing Security</div>
                    <div className="flex justify-start items-baseline font-medium text-white text-2xl text-left">Our platform redefines web security intelligence. By autonomously scanning for vulnerabilities, threats, and misconfigurations,
We empower businesses to identify risks before they escalate - delivering precision, speed, and unmatched insight in securing the digital frontier.</div>
                <button className="flex justify-center items-center bg-white hover:bg-gray-300 rounded-lg h-[50px] w-[200px] cursor-pointer">Try Now</button>
                </div>
            </div>
        </>
    )
}

export default Mainsite