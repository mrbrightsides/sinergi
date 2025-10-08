# 🛠️ SINERGI Developer Guide

Technical documentation for developers working on or extending SINERGI.

---

## 📋 Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Development Setup](#development-setup)
5. [Component Architecture](#component-architecture)
6. [State Management](#state-management)
7. [Data Flow](#data-flow)
8. [Adding New Features](#adding-new-features)
9. [Code Conventions](#code-conventions)
10. [Testing](#testing)
11. [Performance Optimization](#performance-optimization)
12. [Deployment](#deployment)

---

## Architecture Overview

### System Design

SINERGI follows a **modular, component-based architecture** built on Next.js 14 with App Router.

```
┌─────────────────────────────────────────────┐
│           Browser (Client)                   │
│  ┌───────────────────────────────────────┐  │
│  │     React Components                   │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  Feature Modules                 │  │  │
│  │  │  (Learning Hub, Labs, etc.)      │  │  │
│  │  └─────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  State Management                │  │  │
│  │  │  (React Hooks, localStorage)     │  │  │
│  │  └─────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  UI Components                   │  │  │
│  │  │  (shadcn/ui based)               │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────┐
│         Next.js Server                       │
│  ┌───────────────────────────────────────┐  │
│  │     API Routes (/api/proxy)           │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────┐
│       External Services                      │
│  ┌────────────┐  ┌────────────┐            │
│  │ Perplexity │  │  Pyodide   │            │
│  │    API     │  │ (WASM)     │            │
│  └────────────┘  └────────────┘            │
└─────────────────────────────────────────────┘
```

### Key Design Principles

1. **Component Modularity**: Each feature is a self-contained component
2. **Progressive Enhancement**: Core features work without external APIs
3. **Client-Side First**: Most computation happens in browser
4. **Local Data Persistence**: localStorage for progress tracking
5. **Type Safety**: Strict TypeScript throughout

---

## Tech Stack

### Core Framework

- **Next.js 14.2.5** - React framework with App Router
- **React 18.3.1** - UI library
- **TypeScript 5** - Type safety

### UI & Styling

- **Tailwind CSS 3.4.1** - Utility-first CSS
- **Framer Motion 11.11.17** - Animations
- **Lucide React 0.344.0** - Icons
- **class-variance-authority** - Component variants
- **tailwind-merge** - Conditional class merging

### Data Visualization

- **Recharts 2.15.0** - Charts and graphs

### Code Execution

- **Pyodide** - Python runtime in WebAssembly
- Loaded dynamically for Labs and Notebook features

### PDF Generation

- **jsPDF 2.5.2** - PDF creation
- QR code generation for certificates

### AI Integration

- **Perplexity API** - AI assistance
- Proxied through Next.js API route

### Development Tools

- **ESLint** - Linting
- **PostCSS** - CSS processing
- **Autoprefixer** - CSS vendor prefixes

---

## Project Structure

```
sinergi/
├── src/
│   ├── app/                      # Next.js App Router
│   │   ├── page.tsx             # Main entry point
│   │   ├── layout.tsx           # Root layout
│   │   ├── globals.css          # Global styles
│   │   └── api/                 # API routes
│   │       └── proxy/
│   │           └── route.ts     # External API proxy
│   │
│   ├── components/              # React components
│   │   ├── ui/                  # Base UI components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── input.tsx
│   │   │   ├── badge.tsx
│   │   │   ├── progress.tsx
│   │   │   └── ...
│   │   │
│   │   ├── learning-hub.tsx              # Learning modules
│   │   ├── architecture-explorer.tsx     # Architecture viewer
│   │   ├── live-simulator.tsx            # IoT simulator
│   │   ├── hands-on-labs.tsx             # Interactive labs
│   │   ├── notebook-workspace.tsx        # Python notebooks
│   │   ├── dataset-library.tsx           # Dataset management
│   │   ├── business-case-builder.tsx     # ROI calculator
│   │   ├── policy-governance.tsx         # Compliance guides
│   │   ├── analytics-dashboard.tsx       # Progress tracking
│   │   ├── ai-assistant.tsx              # AI chat
│   │   └── quiz-modal.tsx                # Quiz component
│   │
│   └── lib/                     # Utilities and data
│       ├── utils.ts            # Helper functions
│       ├── modules.ts          # Module definitions
│       ├── datasets.ts         # Dataset definitions
│       ├── labs.ts            # Lab content
│       ├── pyodide-loader.ts  # Pyodide initialization
│       └── ai-utils.ts        # AI helper functions
│
├── public/                      # Static assets
│   └── .well-known/
│       └── farcaster.json      # Farcaster manifest
│
├── docs/                        # Documentation
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md
│   ├── API_REFERENCE.md
│   └── DEPLOYMENT_GUIDE.md
│
├── README.md                    # Project overview
├── package.json                 # Dependencies
├── tsconfig.json               # TypeScript config
├── tailwind.config.ts          # Tailwind config
├── next.config.js              # Next.js config
└── .env.local                  # Environment variables
```

---

## Development Setup

### Prerequisites

```bash
node --version  # v18.0.0 or higher
npm --version   # v9.0.0 or higher
```

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/sinergi.git
cd sinergi

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local

# Edit .env.local with your API keys
# PERPLEXITY_API_KEY=your_key_here
```

### Running Development Server

```bash
# Start dev server
npm run dev

# Open browser
# http://localhost:3000
```

### Building for Production

```bash
# Create production build
npm run build

# Test production build
npm start
```

### Linting

```bash
# Run ESLint
npm run lint

# Fix auto-fixable issues
npm run lint:fix
```

---

## Component Architecture

### Feature Component Pattern

Each major feature follows this pattern:

```typescript
'use client'

import { useState, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'

interface FeatureProps {
  onClose: () => void
}

export function FeatureComponent({ onClose }: FeatureProps) {
  // 1. State management
  const [data, setData] = useState<DataType[]>([])
  const [loading, setLoading] = useState<boolean>(false)
  
  // 2. Load persisted data
  useEffect(() => {
    const saved = localStorage.getItem('feature-data')
    if (saved) {
      setData(JSON.parse(saved))
    }
  }, [])
  
  // 3. Save data on changes
  useEffect(() => {
    if (data.length > 0) {
      localStorage.setItem('feature-data', JSON.stringify(data))
    }
  }, [data])
  
  // 4. Event handlers
  const handleAction = async () => {
    setLoading(true)
    try {
      // Perform action
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setLoading(false)
    }
  }
  
  // 5. Render
  return (
    <div className="fixed inset-0 bg-black/95 z-50 overflow-auto">
      <div className="container mx-auto p-6">
        <Card>
          <CardHeader>
            <CardTitle>Feature Title</CardTitle>
            <Button onClick={onClose}>Close</Button>
          </CardHeader>
          <CardContent>
            {/* Feature content */}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
```

### UI Component Structure

Base UI components use class-variance-authority:

```typescript
import * as React from 'react'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md font-medium',
  {
    variants: {
      variant: {
        default: 'bg-purple-600 text-white hover:bg-purple-700',
        outline: 'border border-purple-600 hover:bg-purple-600/10',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-8 px-3 text-sm',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, ...props }, ref) => {
    return (
      <button
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = 'Button'

export { Button, buttonVariants }
```

---

## State Management

### Local State (useState)

For component-specific state:

```typescript
const [isOpen, setIsOpen] = useState<boolean>(false)
const [data, setData] = useState<DataType[]>([])
```

### Persisted State (localStorage)

For user progress and preferences:

```typescript
// Save
useEffect(() => {
  localStorage.setItem('modules-progress', JSON.stringify(progress))
}, [progress])

// Load
useEffect(() => {
  const saved = localStorage.getItem('modules-progress')
  if (saved) {
    setProgress(JSON.parse(saved))
  }
}, [])
```

### Global State Pattern

For cross-feature data sharing:

```typescript
// lib/global-state.ts
export const GlobalState = {
  get: (key: string) => {
    const item = localStorage.getItem(key)
    return item ? JSON.parse(item) : null
  },
  
  set: (key: string, value: any) => {
    localStorage.setItem(key, JSON.stringify(value))
  },
  
  remove: (key: string) => {
    localStorage.removeItem(key)
  }
}

// Usage in components
import { GlobalState } from '@/lib/global-state'

const data = GlobalState.get('shared-data')
GlobalState.set('shared-data', newData)
```

---

## Data Flow

### Learning Progress Flow

```
User completes quiz
    ↓
Quiz component updates score
    ↓
Save to localStorage ('quiz-results')
    ↓
Analytics Dashboard reads from localStorage
    ↓
Display progress metrics
```

### Dataset Sharing Flow

```
User exports dataset from Library
    ↓
Dataset saved to localStorage ('shared-dataset')
    ↓
User opens Labs/Notebook
    ↓
Component checks for shared dataset
    ↓
Auto-loads dataset in code editor
```

### AI Interaction Flow

```
User asks question
    ↓
Component sends to /api/proxy
    ↓
Proxy forwards to Perplexity API
    ↓
Response streamed back to client
    ↓
Display in chat interface
```

---

## Adding New Features

### 1. Create Feature Component

```typescript
// src/components/new-feature.tsx
'use client'

import { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'

interface NewFeatureProps {
  onClose: () => void
}

export function NewFeature({ onClose }: NewFeatureProps) {
  const [state, setState] = useState<string>('')
  
  return (
    <div className="fixed inset-0 bg-black/95 z-50 overflow-auto">
      <div className="container mx-auto p-6">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle>New Feature</CardTitle>
            <Button onClick={onClose} variant="outline">
              Close
            </Button>
          </CardHeader>
          <CardContent>
            {/* Feature implementation */}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
```

### 2. Add to Main Page

```typescript
// src/app/page.tsx

import { NewFeature } from '@/components/new-feature'

export default function Home() {
  const [activeFeature, setActiveFeature] = useState<string | null>(null)
  
  const features = [
    // ... existing features
    {
      id: 'new-feature',
      title: 'New Feature',
      description: 'Feature description',
      icon: IconComponent,
    }
  ]
  
  return (
    <>
      {/* Feature cards */}
      
      {activeFeature === 'new-feature' && (
        <NewFeature onClose={() => setActiveFeature(null)} />
      )}
    </>
  )
}
```

### 3. Add Data Structures (if needed)

```typescript
// src/lib/new-feature-data.ts

export interface NewFeatureData {
  id: string
  name: string
  value: number
}

export const newFeatureData: NewFeatureData[] = [
  { id: '1', name: 'Item 1', value: 100 },
  { id: '2', name: 'Item 2', value: 200 },
]
```

### 4. Add Persistence (if needed)

```typescript
// In component
useEffect(() => {
  const saved = localStorage.getItem('new-feature-state')
  if (saved) {
    setState(JSON.parse(saved))
  }
}, [])

useEffect(() => {
  localStorage.setItem('new-feature-state', JSON.stringify(state))
}, [state])
```

---

## Code Conventions

### TypeScript

```typescript
// ✅ GOOD: Explicit types
interface User {
  id: string
  name: string
  email: string
}

function getUser(id: string): User | null {
  // Implementation
}

// ❌ BAD: Implicit any
function getUser(id) {
  // ...
}
```

### Component Props

```typescript
// ✅ GOOD: Interface for props
interface ButtonProps {
  label: string
  onClick: () => void
  disabled?: boolean
}

function Button({ label, onClick, disabled = false }: ButtonProps) {
  // Implementation
}

// ❌ BAD: No types
function Button({ label, onClick, disabled }) {
  // ...
}
```

### Async Operations

```typescript
// ✅ GOOD: Proper error handling
const loadData = async () => {
  setLoading(true)
  try {
    const response = await fetch('/api/data')
    const data = await response.json()
    setData(data)
  } catch (error) {
    console.error('Failed to load data:', error)
    setError('Failed to load data')
  } finally {
    setLoading(false)
  }
}

// ❌ BAD: No error handling
const loadData = async () => {
  const response = await fetch('/api/data')
  const data = await response.json()
  setData(data)
}
```

### CSS Classes

```typescript
// ✅ GOOD: Use cn() for conditional classes
<div className={cn(
  'base-class',
  isActive && 'active-class',
  variant === 'primary' && 'primary-class'
)}>

// ✅ GOOD: Tailwind utilities
<div className="flex items-center gap-4 p-6 bg-gray-900 rounded-lg">

// ❌ BAD: Inline styles
<div style={{ display: 'flex', padding: '24px' }}>
```

### File Naming

```
✅ GOOD:
- components: kebab-case (learning-hub.tsx)
- utilities: camelCase (aiUtils.ts)
- types: PascalCase (UserTypes.ts)
- constants: UPPER_SNAKE_CASE (API_ENDPOINTS.ts)

❌ BAD:
- Inconsistent naming
- Special characters
- Spaces in filenames
```

---

## Testing

### Unit Tests (Future)

```typescript
// Example test structure
import { render, screen } from '@testing-library/react'
import { Button } from '@/components/ui/button'

describe('Button', () => {
  it('renders button with label', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })
  
  it('calls onClick when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)
    screen.getByText('Click me').click()
    expect(handleClick).toHaveBeenCalledTimes(1)
  })
})
```

### Manual Testing Checklist

- [ ] All features load without errors
- [ ] Data persists across page refreshes
- [ ] Quiz submission works correctly
- [ ] PDF generation successful
- [ ] Python code execution works
- [ ] AI assistants respond properly
- [ ] Progress tracking accurate
- [ ] Mobile responsive
- [ ] Cross-browser compatibility

---

## Performance Optimization

### Code Splitting

```typescript
// Lazy load heavy components
import dynamic from 'next/dynamic'

const HeavyComponent = dynamic(() => import('./heavy-component'), {
  loading: () => <div>Loading...</div>
})
```

### Memoization

```typescript
import { useMemo, useCallback } from 'react'

// Memoize expensive computations
const sortedData = useMemo(() => {
  return data.sort((a, b) => a.value - b.value)
}, [data])

// Memoize callbacks
const handleClick = useCallback(() => {
  // Handler logic
}, [dependencies])
```

### Image Optimization

```typescript
import Image from 'next/image'

// Use Next.js Image component
<Image
  src="/icon.png"
  alt="Icon"
  width={48}
  height={48}
  priority
/>
```

### Bundle Analysis

```bash
# Analyze bundle size
npm install -D @next/bundle-analyzer

# Run analysis
ANALYZE=true npm run build
```

---

## Deployment

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed instructions.

### Quick Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Production deploy
vercel --prod
```

### Environment Variables

Required for production:

```env
PERPLEXITY_API_KEY=your_production_key
NODE_ENV=production
```

---

## API Integration

### Adding New External APIs

1. **Update Proxy Route** (if needed)

```typescript
// src/app/api/proxy/route.ts
// Proxy handles most APIs, but can be extended
```

2. **Create API Client**

```typescript
// src/lib/api-client.ts
export const callExternalAPI = async (endpoint: string, data: any) => {
  const response = await fetch('/api/proxy', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      protocol: 'https',
      origin: 'api.example.com',
      path: endpoint,
      method: 'POST',
      headers: { 'Authorization': 'Bearer token' },
      body: data
    })
  })
  return response.json()
}
```

3. **Use in Component**

```typescript
const result = await callExternalAPI('/v1/endpoint', { data })
```

---

## Contributing

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push to remote
git push origin feature/new-feature

# Create pull request
```

### Commit Message Convention

```
feat: add new feature
fix: fix bug in component
docs: update documentation
style: format code
refactor: refactor component
test: add tests
chore: update dependencies
```

---

## Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Pyodide Documentation](https://pyodide.org/en/stable/)
- [Recharts Documentation](https://recharts.org/)

---

## Support

For technical questions or issues:

- 📧 Email: support@elpeef.com
- 🌐 Web: [ELPEEF](https://elpeef.com)
- 🐛 Issues: [GitHub Issues](https://github.com/mrbrightsides/sinergi/issues)

---

**Happy Coding! 🚀**
