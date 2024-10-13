'use client'

import { useState, useEffect } from "react"
import Chatbot from "./components/ChatBot"
import { Button } from "./components/ui/button"
import { CircleGauge, LogIn, MessageCircle, ShoppingCart, Trash2 } from "lucide-react"
import { Sheet, SheetTrigger, SheetContent, SheetHeader, SheetTitle, SheetDescription } from "./components/ui/sheet"
import { Badge } from "./components/ui/badge"
import Link from "next/link"
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "./components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "./components/ui/select"

interface Product {
  id: number;
  brand: string;
  model: string;
  processor: string;
  ram: number;
  storage: number;
  price: number;
  description: string;
  stars: number;
  stock: number;
  category: string;
}

interface CartItem extends Product {
  quantity: number;
}

export default function Home() {
  const [products, setProducts] = useState<Product[]>([])
  const [displayedProducts, setDisplayedProducts] = useState<Product[]>([])
  const [isChatbotOpen, setIsChatbotOpen] = useState(false)
  const [cart, setCart] = useState<CartItem[]>([])
  const [sortBy, setSortBy] = useState<string>('default')
  const [currentPage, setCurrentPage] = useState(1)
  const productsPerPage = 15

  useEffect(() => {

    const fetchProducts = async () => {

      const response = await fetch('http://127.0.0.1:8000/products', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })

      const data = await response.json()
      setProducts(data)
      setDisplayedProducts(data.slice(0, productsPerPage))
    }

    fetchProducts()
  }, [])

  useEffect(() => {
    sortProducts()
  }, [sortBy, products])

  const sortProducts = () => {
    let sortedProducts = [...products]
    switch (sortBy) {
      case 'category':
        sortedProducts.sort((a, b) => a.category.localeCompare(b.category))
        break
      case 'brand':
        sortedProducts.sort((a, b) => a.brand.localeCompare(b.brand))
        break
      case 'price-asc':
        sortedProducts.sort((a, b) => a.price - b.price)
        break
      case 'price-desc':
        sortedProducts.sort((a, b) => b.price - a.price)
        break
      case 'stars':
        sortedProducts.sort((a, b) => b.stars - a.stars)
        break
      default:
        break
    }
    setDisplayedProducts(sortedProducts.slice(0, currentPage * productsPerPage))
  }

  const loadMore = () => {
    const nextPage = currentPage + 1
    setCurrentPage(nextPage)
    setDisplayedProducts(products.slice(0, nextPage * productsPerPage))
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
                        <h3 className="font-semibold">{item.brand} {item.model}</h3>
                        <p className="text-sm text-gray-500">Quantity: {item.quantity}</p>
                        <p className="text-sm font-semibold">${(item.price * item.quantity).toFixed(2)}</p>
                      </div>
                      <Button variant="destructive" size="icon" onClick={() => removeFromCart(item.id)}>
                        <Trash2 className="h-4 w-4" />
                        <span className="sr-only">Remove {item.brand} {item.model} from cart</span>
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
            <Link href="/dashboard">
              <Button variant="outline" size="icon">
                <CircleGauge className='h-5 w-5'/>
              </Button>
            </Link>
            <Link href="/login">
              <Button variant="outline" size="icon">
                <LogIn className='h-5 w-5'/>
              </Button>
            </Link>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="mb-6 flex justify-end">
          <Select onValueChange={setSortBy}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Sort by" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="default">Default</SelectItem>
              <SelectItem value="category">Category</SelectItem>
              <SelectItem value="brand">Brand</SelectItem>
              <SelectItem value="price-asc">Price: Low to High</SelectItem>
              <SelectItem value="price-desc">Price: High to Low</SelectItem>
              <SelectItem value="stars">Rating</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {displayedProducts.map((product: Product) => (
            <Card key={product.id}>
              <CardHeader>
                <CardTitle>{product.brand} {product.model}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-2xl font-bold">${product.price.toFixed(2)}</p>
                <p className="text-sm text-gray-500">{product.category}</p>
                <p className="text-sm">{product.processor} | {product.ram}GB RAM | {product.storage}GB Storage</p>
                <div className="flex items-center mt-2">
                  {[...Array(5)].map((_, i) => (
                    <svg
                      key={i}
                      className={`w-5 h-5 ${i < product.stars ? 'text-yellow-400' : 'text-gray-300'}`}
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                  ))}
                  <span className="ml-2 text-sm text-gray-500">({product.stars})</span>
                </div>
                <Badge variant={product.stock > 0 ? "secondary" : "destructive"} className="mt-2">
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
        {displayedProducts.length < products.length && (
          <div className="mt-8 flex justify-center">
            <Button onClick={loadMore}>Load More</Button>
          </div>
        )}
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
  )
}