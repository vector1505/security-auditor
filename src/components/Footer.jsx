import React from "react";

export default function ProtectionFeatures() {
  const features = [
    {
      title: "Security Check",
      description:
        "Seamless connectivity between drones and ground autobots for efficient...",
    },
    {
      title: "Sample text 2",
      description:
        "Seamless connectivity between drones and ground autobots for efficient...",
    },
    {
      title: "Sample text 3",
      description:
        "AI-driven sensors analyze surroundings, optimizing routes and avoiding...",
    },
  ];

  return (
    <div className="bg-gradient-to-b from-gray-800 to-gray-700 text-white py-16 px-4">
      <div className="max-w-6xl mx-auto text-center">
        <h2 className="text-3xl md:text-4xl font-semibold mb-12">
          How Guardify protects you from malicious sites?
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-gray-700/40 p-6 rounded-xl backdrop-blur-sm shadow-md text-left"
            >
              <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
              <p className="text-gray-300 text-sm line-clamp-2">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
