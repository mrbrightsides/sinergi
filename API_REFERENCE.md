# 📡 SINERGI API Reference

Complete reference for all APIs and integrations used in SINERGI.

---

## 📋 Table of Contents

1. [API Proxy](#api-proxy)
2. [Perplexity AI API](#perplexity-ai-api)
3. [Pyodide Python Runtime](#pyodide-python-runtime)
4. [LocalStorage API](#localstorage-api)
5. [Data Structures](#data-structures)
6. [Utility Functions](#utility-functions)

---

## API Proxy

### Overview

The API proxy (`/api/proxy`) is a Next.js API route that forwards requests to external APIs, handling CORS and adding necessary headers.

### Endpoint

```
POST /api/proxy
```

### Request Format

```typescript
interface ProxyRequest {
  protocol: string        // 'https' or 'http'
  origin: string         // API domain (e.g., 'api.perplexity.ai')
  path: string           // API endpoint path (e.g., '/chat/completions')
  method: string         // HTTP method: 'GET' | 'POST' | 'PUT' | 'DELETE'
  headers: Record<string, string>  // Request headers (always include, use {} if none)
  body?: any             // Request body (omit if not needed)
}
```

### Example: Perplexity API Call

```typescript
const response = await fetch('/api/proxy', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    protocol: 'https',
    origin: 'api.perplexity.ai',
    path: '/chat/completions',
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json',
    },
    body: {
      model: 'llama-3.1-sonar-small-128k-online',
      messages: [
        {
          role: 'system',
          content: 'You are a helpful AI assistant.'
        },
        {
          role: 'user',
          content: 'Explain IoT in simple terms.'
        }
      ]
    }
  })
})

const data = await response.json()
```

### Response

The proxy returns the response from the external API as-is.

```typescript
{
  // External API response
  id: string
  choices: Array<{
    message: {
      role: string
      content: string
    }
  }>
  // ... other fields
}
```

### Error Handling

```typescript
try {
  const response = await fetch('/api/proxy', { /* ... */ })
  
  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`)
  }
  
  const data = await response.json()
} catch (error) {
  console.error('Proxy request failed:', error)
}
```

---

## Perplexity AI API

### Overview

Perplexity AI powers the AI Assistant and Coding Helper features.

### Base Configuration

```typescript
const PERPLEXITY_CONFIG = {
  baseURL: 'https://api.perplexity.ai',
  model: 'llama-3.1-sonar-small-128k-online',
  apiKey: process.env.PERPLEXITY_API_KEY
}
```

### AI Learning Assistant

**System Prompt:**
```
You are an AI learning assistant for SINERGI, an educational platform about AI, IoT, and Big Data. Provide clear, concise, and educational responses. Use examples when helpful.
```

**Request Example:**

```typescript
const askAI = async (question: string) => {
  const response = await fetch('/api/proxy', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      protocol: 'https',
      origin: 'api.perplexity.ai',
      path: '/chat/completions',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: {
        model: 'llama-3.1-sonar-small-128k-online',
        messages: [
          {
            role: 'system',
            content: 'You are an AI learning assistant...'
          },
          {
            role: 'user',
            content: question
          }
        ]
      }
    })
  })
  
  const data = await response.json()
  return data.choices[0].message.content
}
```

### AI Coding Helper

**System Prompt:**
```
You are an AI coding assistant specializing in Python, data analysis, IoT, and machine learning. Help debug code, explain concepts, and provide solutions. Be concise and practical.
```

**Request Example:**

```typescript
const getCodingHelp = async (code: string, issue: string) => {
  const prompt = `I have this code:\n\`\`\`python\n${code}\n\`\`\`\n\nIssue: ${issue}\n\nPlease help.`
  
  // Same structure as AI Assistant
  // but with coding-specific system prompt
}
```

### Rate Limits

- Free tier: 5 requests per minute
- Pro tier: 50 requests per minute
- Handle rate limits gracefully with retry logic

```typescript
const callWithRetry = async (fn: () => Promise<any>, retries = 3) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn()
    } catch (error) {
      if (i === retries - 1) throw error
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)))
    }
  }
}
```

---

## Pyodide Python Runtime

### Overview

Pyodide runs Python 3.10 in the browser via WebAssembly. Used in Labs and Notebook Workspace.

### Loading Pyodide

```typescript
// lib/pyodide-loader.ts

let pyodideInstance: any = null

export const loadPyodide = async () => {
  if (pyodideInstance) return pyodideInstance
  
  if (typeof window !== 'undefined') {
    const pyodide = await (window as any).loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.23.4/full/'
    })
    
    // Load common packages
    await pyodide.loadPackage(['numpy', 'pandas', 'scikit-learn'])
    
    pyodideInstance = pyodide
    return pyodide
  }
  
  return null
}
```

### Executing Python Code

```typescript
import { loadPyodide } from '@/lib/pyodide-loader'

const runPython = async (code: string) => {
  try {
    const pyodide = await loadPyodide()
    
    // Capture stdout
    let output = ''
    pyodide.runPython(`
      import sys
      from io import StringIO
      sys.stdout = StringIO()
    `)
    
    // Run user code
    await pyodide.runPythonAsync(code)
    
    // Get output
    output = pyodide.runPython('sys.stdout.getvalue()')
    
    return { success: true, output }
  } catch (error: any) {
    return { success: false, error: error.message }
  }
}
```

### Loading Datasets in Python

```typescript
const loadDatasetInPython = async (pyodide: any, data: any[]) => {
  // Convert JS data to Python
  pyodide.globals.set('data_json', JSON.stringify(data))
  
  await pyodide.runPythonAsync(`
    import pandas as pd
    import json
    
    data = json.loads(data_json)
    df = pd.DataFrame(data)
  `)
  
  return true
}
```

### Available Python Packages

Pre-loaded packages:
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `scikit-learn` - Machine learning
- `matplotlib` - Plotting (limited in browser)

Additional packages can be loaded:

```python
# In Python code
import micropip
await micropip.install('package-name')
```

---

## LocalStorage API

### Overview

All user progress, preferences, and data are stored in browser's localStorage.

### Storage Keys

```typescript
// Module Progress
'modules-progress': ModuleProgress[]

// Quiz Results
'quiz-results': QuizResult[]

// Lab Progress
'labs-progress': LabProgress[]

// Notebooks
'notebooks': Notebook[]

// Shared Dataset
'shared-dataset': Dataset | null

// Simulator Data
'simulator-devices': SimulatorDevice[]

// Analytics
'learning-analytics': AnalyticsData

// Business Cases
'business-cases': BusinessCase[]
```

### Data Structures

#### ModuleProgress

```typescript
interface ModuleProgress {
  moduleId: string
  completed: boolean
  score?: number
  completedAt?: string
  timeSpent: number
  badge?: 'bronze' | 'silver' | 'gold'
}
```

#### QuizResult

```typescript
interface QuizResult {
  moduleId: string
  moduleName: string
  score: number
  totalQuestions: number
  answers: {
    questionId: string
    userAnswer: string
    correct: boolean
  }[]
  completedAt: string
  timeSpent: number
}
```

#### Notebook

```typescript
interface Notebook {
  id: string
  name: string
  cells: {
    id: string
    type: 'code' | 'markdown'
    content: string
    output?: string
  }[]
  createdAt: string
  updatedAt: string
}
```

#### AnalyticsData

```typescript
interface AnalyticsData {
  totalModules: number
  completedModules: number
  totalQuizzes: number
  averageScore: number
  totalTimeSpent: number
  streak: number
  lastActivity: string
  activityByDay: {
    date: string
    modules: number
    timeSpent: number
  }[]
  performanceByCategory: {
    category: string
    score: number
    count: number
  }[]
}
```

### Storage Helper Functions

```typescript
// lib/storage.ts

export const Storage = {
  get: <T>(key: string): T | null => {
    if (typeof window === 'undefined') return null
    const item = localStorage.getItem(key)
    return item ? JSON.parse(item) : null
  },
  
  set: <T>(key: string, value: T): void => {
    if (typeof window === 'undefined') return
    localStorage.setItem(key, JSON.stringify(value))
  },
  
  remove: (key: string): void => {
    if (typeof window === 'undefined') return
    localStorage.removeItem(key)
  },
  
  clear: (): void => {
    if (typeof window === 'undefined') return
    localStorage.clear()
  }
}
```

### Usage Example

```typescript
import { Storage } from '@/lib/storage'

// Save progress
const progress: ModuleProgress = {
  moduleId: 'module-1',
  completed: true,
  score: 85,
  completedAt: new Date().toISOString(),
  timeSpent: 1200,
  badge: 'silver'
}

const allProgress = Storage.get<ModuleProgress[]>('modules-progress') || []
allProgress.push(progress)
Storage.set('modules-progress', allProgress)

// Load progress
const savedProgress = Storage.get<ModuleProgress[]>('modules-progress')
```

---

## Data Structures

### Learning Modules

```typescript
// lib/modules.ts

export interface Module {
  id: string
  title: string
  category: 'IoT' | 'BigData' | 'AI' | 'Integration' | 'Governance'
  difficulty: 'beginner' | 'intermediate' | 'advanced'
  duration: string
  description: string
  content: string
  codeExample?: string
  quiz: Quiz
}

export interface Quiz {
  questions: Question[]
}

export interface Question {
  id: string
  question: string
  options: string[]
  correctAnswer: number
  explanation: string
  difficulty: 'easy' | 'medium' | 'hard'
}
```

### Datasets

```typescript
// lib/datasets.ts

export interface Dataset {
  id: string
  name: string
  category: string
  description: string
  rows: number
  columns: string[]
  sampleData: Record<string, any>[]
  useCases: string[]
  industry: string
}
```

### Labs

```typescript
// lib/labs.ts

export interface Lab {
  id: string
  title: string
  difficulty: 'beginner' | 'intermediate' | 'advanced'
  duration: string
  description: string
  objectives: string[]
  instructions: string
  starterCode: string
  solution?: string
  hints: string[]
}
```

---

## Utility Functions

### cn() - Class Name Utility

```typescript
// lib/utils.ts

import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// Usage
<div className={cn(
  'base-class',
  isActive && 'active-class',
  error && 'error-class'
)}>
```

### formatDuration()

```typescript
export function formatDuration(seconds: number): string {
  const hours = Math.floor(seconds / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  
  if (hours > 0) {
    return `${hours}h ${minutes}m`
  }
  return `${minutes}m`
}

// Usage
formatDuration(3750) // "1h 2m"
formatDuration(120)  // "2m"
```

### formatDate()

```typescript
export function formatDate(dateString: string): string {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

// Usage
formatDate('2024-01-15T10:30:00Z') // "Jan 15, 2024"
```

### generateId()

```typescript
export function generateId(): string {
  return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`
}

// Usage
const notebookId = generateId() // "1704123456789-a3f9k2m1p"
```

### calculateScore()

```typescript
export function calculateScore(
  correct: number,
  total: number
): number {
  return Math.round((correct / total) * 100)
}

// Usage
const score = calculateScore(4, 5) // 80
```

### getBadge()

```typescript
export function getBadge(
  score: number
): 'bronze' | 'silver' | 'gold' | null {
  if (score >= 90) return 'gold'
  if (score >= 80) return 'silver'
  if (score >= 60) return 'bronze'
  return null
}

// Usage
const badge = getBadge(85) // "silver"
```

### exportToCSV()

```typescript
export function exportToCSV(
  data: Record<string, any>[],
  filename: string
): void {
  if (data.length === 0) return
  
  // Get headers
  const headers = Object.keys(data[0])
  
  // Create CSV content
  const csvContent = [
    headers.join(','),
    ...data.map(row =>
      headers.map(header =>
        JSON.stringify(row[header] ?? '')
      ).join(',')
    )
  ].join('\n')
  
  // Download
  const blob = new Blob([csvContent], { type: 'text/csv' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = filename
  link.click()
  URL.revokeObjectURL(url)
}

// Usage
exportToCSV(deviceData, 'sensor-data.csv')
```

---

## Error Handling

### Standard Error Response

```typescript
interface ErrorResponse {
  error: string
  message: string
  statusCode: number
}
```

### Error Handling Pattern

```typescript
const fetchData = async () => {
  try {
    const response = await fetch('/api/endpoint')
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`)
    }
    
    const data = await response.json()
    return { success: true, data }
  } catch (error) {
    console.error('Error fetching data:', error)
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error'
    }
  }
}
```

---

## Rate Limiting & Best Practices

### Debouncing API Calls

```typescript
import { useCallback, useEffect, useRef } from 'react'

const useDebounce = (callback: Function, delay: number) => {
  const timeoutRef = useRef<NodeJS.Timeout>()
  
  return useCallback((...args: any[]) => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current)
    }
    
    timeoutRef.current = setTimeout(() => {
      callback(...args)
    }, delay)
  }, [callback, delay])
}

// Usage
const debouncedSearch = useDebounce((query: string) => {
  // API call
}, 500)
```

### Caching Responses

```typescript
const cache = new Map<string, { data: any; timestamp: number }>()

const fetchWithCache = async (url: string, ttl = 300000) => {
  const cached = cache.get(url)
  
  if (cached && Date.now() - cached.timestamp < ttl) {
    return cached.data
  }
  
  const response = await fetch(url)
  const data = await response.json()
  
  cache.set(url, { data, timestamp: Date.now() })
  return data
}
```

---

## WebSocket (Future)

### Planned Real-time Features

```typescript
// Future implementation
class RealtimeConnection {
  private ws: WebSocket | null = null
  
  connect(url: string) {
    this.ws = new WebSocket(url)
    
    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data)
      this.handleMessage(data)
    }
  }
  
  send(data: any) {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data))
    }
  }
  
  disconnect() {
    this.ws?.close()
  }
  
  private handleMessage(data: any) {
    // Handle incoming messages
  }
}
```

---

## Additional Resources

- [Next.js API Routes](https://nextjs.org/docs/api-routes/introduction)
- [Perplexity API Docs](https://docs.perplexity.ai/)
- [Pyodide Documentation](https://pyodide.org/en/stable/)
- [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)

---

## Support

For API-related questions:

- 📧 Email: api@sinergi.dev
- 📖 Docs: [docs.sinergi.dev/api](https://docs.sinergi.dev/api)
- 💬 Discord: [#api-support](https://discord.gg/sinergi)

---

**Last Updated:** 2024-01-15
