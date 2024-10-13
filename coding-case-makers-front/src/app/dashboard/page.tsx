'use client'
import React from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "../components/ui/chart"
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend, PieChart, Pie, Cell } from 'recharts'
import { ArrowUpIcon, ArrowDownIcon, Package2Icon, TruckIcon, UsersIcon, DollarSignIcon } from 'lucide-react'

// Sample data for charts
const stockData = [
  { category: "T-Shirts", inStock: 120, lowStock: 30, outOfStock: 10 },
  { category: "Jeans", inStock: 80, lowStock: 20, outOfStock: 5 },
  { category: "Shoes", inStock: 100, lowStock: 25, outOfStock: 15 },
  { category: "Accessories", inStock: 200, lowStock: 50, outOfStock: 20 },
]

const salesData = [
  { month: "Jan", sales: 1000 },
  { month: "Feb", sales: 1500 },
  { month: "Mar", sales: 1200 },
  { month: "Apr", sales: 1800 },
  { month: "May", sales: 2000 },
  { month: "Jun", sales: 2400 },
]

const categoryDistribution = [
  { name: "T-Shirts", value: 35 },
  { name: "Jeans", value: 25 },
  { name: "Shoes", value: 20 },
  { name: "Accessories", value: 20 },
]

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042']

export default function AdminDashboard() {
  return (
    <div className="flex-1 space-y-4 p-8 pt-6">
      <div className="flex items-center justify-between space-y-2">
        <h2 className="text-3xl font-bold tracking-tight">Dashboard</h2>
      </div>
      <Tabs defaultValue="overview" className="space-y-4">
        <TabsList>
          <TabsTrigger value="overview">Overview</TabsTrigger>
        </TabsList>
        <TabsContent value="overview" className="space-y-4">
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">
                  Total Revenue
                </CardTitle>
                <DollarSignIcon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">$45,231.89</div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">
                  Total Products
                </CardTitle>
                <Package2Icon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">2350</div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Orders</CardTitle>
                <TruckIcon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">12,234</div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">
                  Active Users
                </CardTitle>
                <UsersIcon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">573</div>
              </CardContent>
            </Card>
          </div>
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
            <Card className="col-span-4">
              <CardHeader>
                <CardTitle>Stock Overview</CardTitle>
              </CardHeader>
              <CardContent className="pl-2">
                <ChartContainer config={{
                  inStock: {
                    label: "In Stock",
                    color: "hsl(var(--chart-1))",
                  },
                  lowStock: {
                    label: "Low Stock",
                    color: "hsl(var(--chart-2))",
                  },
                  outOfStock: {
                    label: "Out of Stock",
                    color: "hsl(var(--chart-3))",
                  },
                }} className="h-[300px]">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={stockData}>
                      <XAxis dataKey="category" />
                      <YAxis />
                      <Tooltip content={<ChartTooltipContent />} />
                      <Legend />
                      <Bar dataKey="inStock" stackId="a" fill="var(--color-inStock)" />
                      <Bar dataKey="lowStock" stackId="a" fill="var(--color-lowStock)" />
                      <Bar dataKey="outOfStock" stackId="a" fill="var(--color-outOfStock)" />
                    </BarChart>
                  </ResponsiveContainer>
                </ChartContainer>
              </CardContent>
            </Card>
            <Card className="col-span-3">
              <CardHeader>
                <CardTitle>Sales Overview</CardTitle>
                <CardDescription>
                  Monthly sales performance
                </CardDescription>
              </CardHeader>
              <CardContent className="pl-2">
                <ChartContainer config={{
                  sales: {
                    label: "Sales",
                    color: "hsl(var(--chart-1))",
                  },
                }} className="h-[300px]">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={salesData}>
                      <XAxis dataKey="month" />
                      <YAxis />
                      <Tooltip content={<ChartTooltipContent />} />
                      <Bar dataKey="sales" fill="var(--color-sales)" />
                    </BarChart>
                  </ResponsiveContainer>
                </ChartContainer>
              </CardContent>
            </Card>
          </div>
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
            <Card className="col-span-4">
              <CardHeader>
                <CardTitle>Recent Sales</CardTitle>
                <CardDescription>
                  You made 265 sales this month.
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-8">
                  {[
                    { name: "Olivia Martin", email: "olivia.martin@email.com", amount: "+$1,999.00" },
                    { name: "Jackson Lee", email: "jackson.lee@email.com", amount: "+$39.00" },
                    { name: "Isabella Nguyen", email: "isabella.nguyen@email.com", amount: "+$299.00" },
                    { name: "William Kim", email: "will@email.com", amount: "+$99.00" },
                    { name: "Sofia Davis", email: "sofia.davis@email.com", amount: "+$39.00" },
                  ].map((sale, index) => (
                    <div key={index} className="flex items-center">
                      <div className="space-y-1">
                        <p className="text-sm font-medium leading-none">{sale.name}</p>
                        <p className="text-sm text-muted-foreground">
                          {sale.email}
                        </p>
                      </div>
                      <div className="ml-auto font-medium">{sale.amount}</div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
            <Card className="col-span-3">
              <CardHeader>
                <CardTitle>Product Category Distribution</CardTitle>
                <CardDescription>
                  Breakdown of product categories
                </CardDescription>
              </CardHeader>
              <CardContent className="pl-2">
                <ChartContainer config={{
                  category: {
                    label: "Category",
                    color: "hsl(var(--chart-1))",
                  },
                }} className="h-[300px]">
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={categoryDistribution}
                        cx="50%"
                        cy="50%"
                        labelLine={false}
                        outerRadius={80}
                        fill="#8884d8"
                        dataKey="value"
                      >
                        {categoryDistribution.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                      </Pie>
                      <Tooltip content={<ChartTooltipContent />} />
                      <Legend />
                    </PieChart>
                  </ResponsiveContainer>
                </ChartContainer>
              </CardContent>
            </Card>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  )
}