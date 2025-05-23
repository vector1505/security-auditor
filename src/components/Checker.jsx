import React from "react";

export default function Checker(){

  function push(){
    console.log("Works");
  }
    
    return (
    <div className="flex items-center justify-center p-4 bg-gradient-to-b from-gray-900 to-gray-800"> 
      <div className="w-full max-w-4xl rounded-lg bg-gray-800/50 backdrop-blur-sm p-8 shadow-xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">Free website security checker</h1>
          <p className="text-lg text-gray-300">
            Enter a website URL and check it for Malware, Viruses, Blacklisted status, malicious code, etc
          </p>
        </div>

        <div className="flex flex-col md:flex-row gap-4">
          <input
            type="text"
            placeholder="example.com"
            className="flex-1 px-6 py-4 rounded-lg text-lg bg-gray-100 border-0 focus:ring-2 focus:ring-gray-400 focus:outline-none"
          />
          <button
            type="button"
            className="px-8 py-4 rounded-lg bg-white hover:bg-gray-200 text-gray-800 font-semibold text-lg transition-colors cursor-pointer"
            onClick={push}
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  );
}
