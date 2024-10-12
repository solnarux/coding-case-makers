import React from 'react'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from './ui/card'
import { Badge } from './ui/badge'
import { Button } from './ui/button'

export default function ProductsGrid() {
    const products = [
        { id: 1, name: 'T-Shirt', price: 19.99, stock: 50 },
        { id: 2, name: 'Jeans', price: 49.99, stock: 30 },
        { id: 3, name: 'Sneakers', price: 79.99, stock: 20 },
        { id: 4, name: 'Hat', price: 14.99, stock: 40 },
    ]

  return (
    <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {products.map((product) => (
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
            <Button className="w-full">Add to Cart</Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  </main>
  )
}
