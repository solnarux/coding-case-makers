import Image from "next/image";
import Header from "./components/Header";
import ProductsGrid from "./components/ProductsGrid";
import ChatBot from "./components/ChatBot";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Header/>
      <ProductsGrid/>
      <ChatBot/>
    </div>
  );
}
