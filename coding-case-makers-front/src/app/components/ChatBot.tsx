'use client'
import React, { useState } from 'react'
import { X } from 'lucide-react'
import { Button } from './ui/button'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from './ui/card'
import { Input } from './ui/input'

// Dummy product data (same as in store-page.tsx)
const products = [
  { id: 1, name: 'T-Shirt', price: 19.99, stock: 50 },
  { id: 2, name: 'Jeans', price: 49.99, stock: 30 },
  { id: 3, name: 'Sneakers', price: 79.99, stock: 20 },
  { id: 4, name: 'Hat', price: 14.99, stock: 40 },
]


export default function Chatbot() {
  const [messages, setMessages] = useState<{ text: string; isUser: boolean }[]>([
    { text: "Hello! How can I help you with our inventory?", isUser: false }
  ])
  const [input, setInput] = useState('')

  const handleSend = () => {
    if (input.trim() === '') return

    setMessages(prev => [...prev, { text: input, isUser: true }])
    setInput('')

    // Simple logic to respond to user queries
    const response = generateResponse(input)
    setTimeout(() => {
      setMessages(prev => [...prev, { text: response, isUser: false }])
    }, 500)
  }

  const generateResponse = (query: string) => {
    const lowerQuery = query.toLowerCase()
    if (lowerQuery.includes('price')) {
      const product = products.find(p => lowerQuery.includes(p.name.toLowerCase()))
      return product 
        ? `The price of ${product.name} is $${product.price.toFixed(2)}.` 
        : "I'm sorry, I couldn't find that product. Can you please specify the product name?"
    } else if (lowerQuery.includes('stock') || lowerQuery.includes('inventory')) {
      const product = products.find(p => lowerQuery.includes(p.name.toLowerCase()))
      return product 
        ? `We currently have ${product.stock} ${product.name}(s) in stock.` 
        : "I'm sorry, I couldn't find that product. Can you please specify the product name?"
    } else {
      return "I'm sorry, I didn't understand that. You can ask me about product prices or stock levels."
    }
  }

  return (
    <Card className="fixed bottom-20 right-4 w-80 h-96 flex flex-col">
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle>Store Assistant</CardTitle>
        <Button variant="ghost" size="icon">
          <X className="h-4 w-4" />
        </Button>
      </CardHeader>
      <CardContent className="flex-grow overflow-y-auto">
        {messages.map((message, index) => (
          <div key={index} className={`mb-2 ${message.isUser ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block p-2 rounded-lg ${message.isUser ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}>
              {message.text}
            </span>
          </div>
        ))}
      </CardContent>
      <CardFooter>
        <form onSubmit={(e) => { e.preventDefault(); handleSend(); }} className="flex w-full">
          <Input 
            value={input} 
            onChange={(e) => setInput(e.target.value)} 
            placeholder="Type your message..."
            className="flex-grow mr-2"
          />
          <Button type="submit">Send</Button>
        </form>
      </CardFooter>
    </Card>
  )
}