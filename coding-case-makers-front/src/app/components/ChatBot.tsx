'use client'

import React, { useState, useEffect } from 'react'
import { X, Loader2, MessageCircle, Minus } from 'lucide-react'
import { Button } from '../components/ui/button'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '../components/ui/card'
import { Input } from '../components/ui/input'

interface ChatbotProps {
  onClose: () => void
}

export default function Chatbot({ onClose }: ChatbotProps) {
  const [messages, setMessages] = useState<{ text: string; isUser: boolean }[]>([
    { text: "Hello! How may I help you, ask me anything.", isUser: false }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [isMinimized, setIsMinimized] = useState(false)
  const [hasNewMessage, setHasNewMessage] = useState(false)

  useEffect(() => {
    // Scroll to bottom of message container when new message is added
    const messageContainer = document.getElementById('message-container')
    if (messageContainer) {
      messageContainer.scrollTop = messageContainer.scrollHeight
    }
  }, [messages])

  const handleSend = async () => {
    if (input.trim() === '') return

    // Add the user's message
    setMessages(prev => [...prev, { text: input, isUser: true }])
    setInput('')

    setLoading(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/chatbot-rag', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: input }),
      })
      const data = await response.json()
      
      setMessages(prev => [...prev, { text: data.answer, isUser: false }])

      setHasNewMessage(true)
    } catch (error) {
      setMessages(prev => [...prev, { text: "Something went wrong, please try again.", isUser: false }])
    } finally {
      setLoading(false)
    }
  }

  const toggleMinimize = () => {
    setIsMinimized(!isMinimized)
    if (!isMinimized) {
      setHasNewMessage(false)
    }
  }

  if (isMinimized) {
    return (
      <Button
        className="fixed bottom-4 right-4 p-2"
        onClick={toggleMinimize}
        aria-label="Maximize chatbot"
      >
        <MessageCircle className="h-6 w-6" />
        {hasNewMessage && (
          <span className="absolute top-0 right-0 block h-3 w-3 rounded-full bg-red-500" />
        )}
      </Button>
    )
  }

  return (
    <Card className="fixed bottom-20 right-4 w-80 h-96 flex flex-col">
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle>Makers ChatBot</CardTitle>
        <div className="flex">
          <Button variant="ghost" size="icon" onClick={toggleMinimize} aria-label="Minimize chatbot">
            <Minus className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" onClick={onClose} aria-label="Close chatbot">
            <X className="h-4 w-4" />
          </Button>
        </div>
      </CardHeader>
      <CardContent className="flex-grow overflow-y-auto" id="message-container">
        {messages.map((message, index) => (
          <div key={index} className={`mb-2 ${message.isUser ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block p-2 rounded-lg ${message.isUser ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}>
              {message.text}
            </span>
          </div>
        ))}
        {loading && (
          <div className="text-left mb-2">
            <span className="inline-block p-2 rounded-lg bg-gray-200">
              <Loader2 className="animate-spin h-4 w-4 inline-block mr-2" /> Typing...
            </span>
          </div>
        )}
      </CardContent>
      <CardFooter>
        <form onSubmit={(e) => { e.preventDefault(); handleSend(); }} className="flex w-full">
          <Input 
            value={input} 
            onChange={(e) => setInput(e.target.value)} 
            placeholder="Type your message..."
            className="flex-grow mr-2"
          />
          <Button type="submit" disabled={loading}>Send</Button>
        </form>
      </CardFooter>
    </Card>
  )
}