'use client'
import { useState } from "react";
import Chatbot from "./components/ChatBot";
import { Button } from "./components/ui/button";
import { LogIn, MessageCircle, ShoppingCart, Trash2 } from "lucide-react";
import { Sheet, SheetTrigger, SheetContent, SheetHeader, SheetTitle, SheetDescription } from "./components/ui/sheet";
import { Badge } from "./components/ui/badge";
import Link from "next/link";
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "./components/ui/card";


export default function Home() {

  const products = [
    { id: 1, name: 'T-Shirt', price: 19.99, stock: 50 },
    { id: 2, name: 'Jeans', price: 49.99, stock: 30 },
    { id: 3, name: 'Sneakers', price: 79.99, stock: 20 },
    { id: 4, name: 'Hat', price: 14.99, stock: 40 },
  ]
  
  const [isChatbotOpen, setIsChatbotOpen] = useState(false)
  const [cart, setCart] = useState<CartItem[]>([])

  interface CartItem extends Product {
    quantity: number;
  }
  
  interface Product {
    id: number;
    name: string;
    price: number;
    stock: number;
  }

  const addToCart = (product: Product) => {
    setCart(prevCart => {
      const existingItem = prevCart.find(item => item.id === product.id)
      if (existingItem) {
        return prevCart.map(item =>
          item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item
        )
      }
      return [...prevCart, { ...product, quantity: 1 }]
    })
  }

  const removeFromCart = (productId: number) => {
    setCart(prevCart => prevCart.filter(item => item.id !== productId))
  }

  const getTotalItems = () => {
    return cart.reduce((total, item) => total + item.quantity, 0)
  }

  const getTotalPrice = () => {
    return cart.reduce((total, item) => total + item.price * item.quantity, 0)
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow-sm">
          <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
            <h1 className="text-2xl font-bold text-gray-900">Makers Tech Store</h1>
            <div className="flex flex-row gap-2">
            <Sheet>
              <SheetTrigger asChild>
                <Button variant="outline" size="icon" className="relative">
                  <ShoppingCart className="h-5 w-5" />
                  {getTotalItems() > 0 && (
                    <Badge variant="destructive" className="absolute -top-2 -right-2 px-2 py-1 text-xs">
                      {getTotalItems()}
                    </Badge>
                  )}
                  <span className="sr-only">Open cart</span>
                </Button>
              </SheetTrigger>
              <SheetContent>
                <SheetHeader>
                  <SheetTitle>Your Cart</SheetTitle>
                  <SheetDescription>
                    {cart.length === 0 ? "Your cart is empty" : `${getTotalItems()} items in your cart`}
                  </SheetDescription>
                </SheetHeader>
                <div className="mt-8">
                  {cart.map(item => (
                    <div key={item.id} className="flex justify-between items-center mb-4">
                      <div>
                        <h3 className="font-semibold">{item.name}</h3>
                        <p className="text-sm text-gray-500">Quantity: {item.quantity}</p>
                        <p className="text-sm font-semibold">${(item.price * item.quantity).toFixed(2)}</p>
                      </div>
                      <Button variant="destructive" size="icon" onClick={() => removeFromCart(item.id)}>
                        <Trash2 className="h-4 w-4" />
                        <span className="sr-only">Remove {item.name} from cart</span>
                      </Button>
                    </div>
                  ))}
                </div>
                {cart.length > 0 && (
                  <div className="mt-8">
                    <p className="font-semibold text-lg mb-4">Total: ${getTotalPrice().toFixed(2)}</p>
                    <Button className="w-full">Proceed to Checkout</Button>
                  </div>
                )}
              </SheetContent>
            </Sheet>
            <Link href="/login">
            <Button variant="outline" size="icon">
              <LogIn className='h-5 w-5'/>
            </Button>
            </Link>
            </div>
          </div>
        </header>
        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {products.map((product : Product) => (
            <Card key={product.id}>
              <CardHeader>
                <CardTitle>{product.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-2xl font-bold">${product.price.toFixed(2)}</p>
                <Badge variant={product.stock > 0 ? "secondary" : "destructive"}>
                  {product.stock > 0 ? `${product.stock} in stock` : 'Out of stock'}
                </Badge>
              </CardContent>
              <CardFooter>
                <Button className="w-full" onClick={() => addToCart(product)} disabled={product.stock === 0}>
                  Add to Cart
                </Button>
              </CardFooter>
            </Card>
          ))}
        </div>
      </main>

      {isChatbotOpen ? 
      <Chatbot onClose={() => setIsChatbotOpen(false)} /> :       
        <div className="fixed bottom-4 right-4">
        <Button onClick={() => setIsChatbotOpen(!isChatbotOpen)}>
          <MessageCircle className="h-5 w-5 mr-2" />
          Chat with Us
        </Button>
      </div>
      }
    </div>
  );
}
