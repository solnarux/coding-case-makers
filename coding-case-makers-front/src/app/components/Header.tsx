import { ShoppingCart } from 'lucide-react'
import { Button } from '@/app/components/ui/button'
import React from 'react'

export default function Header() {
  return (
    <header className="bg-white shadow-sm">
    <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
      <h1 className="text-2xl font-bold text-gray-900">My Store</h1>
      <Button variant="outline" size="icon">
        <ShoppingCart className="h-5 w-5" />
        <span className="sr-only">View cart</span>
      </Button>
    </div>
  </header>
  )
}
