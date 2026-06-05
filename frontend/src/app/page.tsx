"use client";

import { useState } from "react";
import { Send, BrainCircuit, Database, Network } from "lucide-react";
import { motion } from "framer-motion";

export default function Home() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([
    { role: "assistant", content: "Hello! I am CogniMind AI. How can I assist you today?" },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    setMessages((prev) => [...prev, { role: "user", content: userMessage }]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/api/v1/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage, user_id: "default_user" }),
      });

      const data = await response.json();
      setMessages((prev) => [...prev, { role: "assistant", content: data.response }]);
    } catch (error) {
      console.error("Error communicating with backend:", error);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Sorry, I am having trouble connecting to my memory systems right now." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen bg-[#0f1115] text-white">
      {/* Sidebar */}
      <aside className="w-64 glass border-r border-gray-800 flex flex-col hidden md:flex">
        <div className="p-6 flex items-center gap-3">
          <BrainCircuit className="w-8 h-8 text-blue-500 animate-glow" />
          <h1 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
            CogniMind
          </h1>
        </div>
        <div className="flex-1 px-4 py-2 space-y-4">
          <div className="space-y-2">
            <h2 className="text-xs uppercase text-gray-500 font-semibold tracking-wider">Memory Systems</h2>
            <div className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-800 cursor-pointer transition">
              <Database className="w-4 h-4 text-emerald-400" />
              <span className="text-sm">Vector DB (Pinecone)</span>
            </div>
            <div className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-800 cursor-pointer transition">
              <Network className="w-4 h-4 text-purple-400" />
              <span className="text-sm">Knowledge Graph</span>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Chat Area */}
      <main className="flex-1 flex flex-col relative">
        <div className="flex-1 overflow-y-auto p-4 md:p-8 space-y-6">
          {messages.map((msg, i) => (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3 }}
              key={i}
              className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
            >
              <div
                className={`max-w-[80%] rounded-2xl p-4 shadow-lg ${
                  msg.role === "user"
                    ? "bg-blue-600 text-white"
                    : "glass text-gray-200 border border-gray-700/50"
                }`}
              >
                {msg.content}
              </div>
            </motion.div>
          ))}
          {loading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex justify-start"
            >
              <div className="max-w-[80%] rounded-2xl p-4 glass border border-gray-700/50 flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce" />
                <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce delay-75" />
                <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce delay-150" />
              </div>
            </motion.div>
          )}
        </div>

        {/* Input Area */}
        <div className="p-4 md:p-6 bg-[#0f1115]/80 backdrop-blur-md border-t border-gray-800">
          <div className="max-w-4xl mx-auto relative">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSend()}
              placeholder="Ask CogniMind..."
              className="w-full bg-gray-900 border border-gray-700 rounded-full py-4 pl-6 pr-14 text-white focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition shadow-inner"
            />
            <button
              onClick={handleSend}
              disabled={loading}
              className="absolute right-2 top-2 bottom-2 aspect-square flex items-center justify-center bg-blue-600 hover:bg-blue-500 rounded-full transition disabled:opacity-50"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
