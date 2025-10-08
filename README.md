# 🌟 SINERGI - AI, IoT & Big Data Learning Platform

<div align="center">

![SINERGI Platform](https://img.shields.io/badge/SINERGI-Educational%20Platform-purple?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?style=for-the-badge&logo=typescript)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An Interactive Educational Platform Demonstrating the Synergy of AI, IoT, and Big Data**

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [✨ Features](#-key-features) • [🎯 Target Audience](#-target-audience)

</div>

---

## 📋 Table of Contents

- [About SINERGI](#-about-sinergi)
- [Key Features](#-key-features)
- [Target Audience](#-target-audience)
- [Quick Start](#-quick-start)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About SINERGI

**SINERGI** (Synergy of Intelligent Networks, Edge computing, Real-time analytics, Governance, and Innovation) is a comprehensive educational and sandbox demonstration platform that showcases the transformative power of AI, IoT, and Big Data in modern information systems.

### Why SINERGI?

In today's rapidly evolving tech landscape, understanding the intersection of AI, IoT, and Big Data is crucial. SINERGI provides:

- **Interactive Learning**: Hands-on modules with real code execution
- **Real-World Simulations**: Live IoT device simulations with real-time data
- **Practical Experience**: Jupyter-like notebook workspace for experimentation
- **Industry Datasets**: 10+ curated datasets from various industries
- **AI-Powered Assistance**: Integrated AI tutors and coding helpers
- **Professional Outputs**: Generate certifications and business case reports

---

## ✨ Key Features

### 🎓 Learning Hub
- **12 Comprehensive Modules** covering beginner to advanced topics
- Interactive quizzes with instant feedback
- Progress tracking and achievement system
- Difficulty levels: Easy, Medium, Hard
- Real code examples with syntax highlighting

### 🏗️ Architecture Explorer
- Visual interactive architecture diagrams
- Deep-dive into each component (IoT Layer, Data Layer, AI Layer, Edge Computing)
- Technology recommendations and best practices
- Real-world implementation patterns

### 🔄 Live Simulator
- Real-time IoT device simulations
- Multiple device types: Temperature sensors, Smart meters, GPS trackers, Industrial machines
- Live data streaming with MQTT protocol
- Anomaly detection and alerts
- Data export capabilities

### 🧪 Hands-on Labs
- 6 Practical labs with step-by-step guides
- Real Python code execution via Pyodide
- Labs cover: IoT basics, data processing, ML integration, real-time analytics
- Code editor with syntax highlighting
- Import datasets directly from Dataset Library

### 📓 Notebook Workspace
- Jupyter-like interactive environment
- Real Python execution in browser
- Pre-loaded libraries: pandas, numpy, scikit-learn, matplotlib
- Save and manage multiple notebooks
- Import datasets for analysis

### 📊 Dataset Library
- **10 Industry Datasets** including:
  - Manufacturing Equipment Sensors
  - Patient Vital Signs Monitoring
  - Smart City Traffic Analytics
  - Financial Transaction Stream
  - Smart Agriculture IoT Data
  - Supply Chain Tracking Data
- Search and filter capabilities
- CSV export functionality
- Direct integration with Labs and Notebooks

### 💼 Business Case Builder
- ROI Calculator with customizable parameters
- Professional PDF report generation
- QR code embedded reports
- Scenario analysis (Conservative, Moderate, Aggressive)
- Cost-benefit breakdown

### 📜 Policy & Governance
- Comprehensive governance frameworks
- GDPR, HIPAA, ISO compliance guides
- Best practices for data privacy and security
- Industry-specific regulations
- Professional certification generation

### 📈 Analytics Dashboard
- **Comprehensive Progress Tracking**
- Quiz performance analytics
- Time tracking per module
- Learning streaks and consistency metrics
- Category-based performance breakdown
- 7-day activity visualization
- Personalized insights and recommendations
- Export analytics data

### 🤖 AI Features
- **AI Learning Assistant**: Get explanations, examples, and learning guidance
- **AI Coding Helper**: Debug code, get suggestions, and learn best practices
- Powered by Perplexity API
- Context-aware responses

---

## 🎯 Target Audience

### 🎓 Undergraduate Students
Perfect for students learning about IoT, Big Data, AI, and Information Systems

### 💻 IT Professionals
Upskill in modern tech stacks and architectural patterns

### 📊 Product Managers
Understand technical capabilities and make informed decisions

### 🏛️ Policymakers
Learn about governance, compliance, and ethical considerations

### 🚀 Startups & Innovators
Explore possibilities and build business cases for IoT/AI solutions

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sinergi.git
   cd sinergi
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env.local
   ```
   
   Add your API keys:
   ```env
   PERPLEXITY_API_KEY=your_api_key_here
   ```

4. **Run the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. **Open your browser**
   ```
   http://localhost:3000
   ```

### First Steps

1. 🎓 Start with **Learning Hub** - Complete Module 1 (Introduction to IoT)
2. 🏗️ Explore **Architecture Explorer** - Understand the system components
3. 🔄 Try **Live Simulator** - See real-time IoT data in action
4. 🧪 Complete a **Hands-on Lab** - Build your first IoT data processor
5. 📈 Check **Analytics Dashboard** - Track your progress

---

## 🧰 Technology Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Smooth animations
- **Recharts** - Data visualization
- **Lucide React** - Icon library

### Code Execution
- **Pyodide** - Python runtime in WebAssembly
- **CodeMirror** - Code editor with syntax highlighting

### AI Integration
- **Perplexity API** - AI-powered assistance and learning

### Data & State Management
- **React Hooks** - State management
- **LocalStorage** - Progress persistence
- **Context API** - Global state

### PDF Generation
- **jsPDF** - Professional report generation
- **QR Code** - Certificate verification

### Real-time Simulation
- **WebSocket-ready** - For future real-time features
- **MQTT concepts** - IoT protocol demonstrations

---

## 📁 Project Structure

```
sinergi/
├── src/
│   ├── app/
│   │   ├── page.tsx              # Main application entry
│   │   └── layout.tsx            # Root layout
│   ├── components/
│   │   ├── ui/                   # Reusable UI components
│   │   ├── learning-hub.tsx      # Learning modules
│   │   ├── architecture-explorer.tsx
│   │   ├── live-simulator.tsx
│   │   ├── hands-on-labs.tsx
│   │   ├── notebook-workspace.tsx
│   │   ├── dataset-library.tsx
│   │   ├── business-case-builder.tsx
│   │   ├── policy-governance.tsx
│   │   ├── analytics-dashboard.tsx
│   │   ├── ai-assistant.tsx
│   │   └── quiz-modal.tsx
│   ├── lib/
│   │   ├── modules.ts            # Learning module data
│   │   ├── datasets.ts           # Dataset definitions
│   │   ├── labs.ts              # Lab content
│   │   └── utils.ts             # Utility functions
│   └── styles/
│       └── globals.css          # Global styles
├── public/
│   └── .well-known/
│       └── farcaster.json       # Farcaster integration
├── docs/
│   ├── USER_GUIDE.md            # User documentation
│   ├── DEVELOPER_GUIDE.md       # Developer documentation
│   ├── API_REFERENCE.md         # API documentation
│   └── DEPLOYMENT_GUIDE.md      # Deployment guide
├── README.md                     # This file
├── package.json
├── tsconfig.json
└── tailwind.config.ts
```

---

## 📖 Documentation

- **[User Guide](./USER_GUIDE.md)** - Complete guide for end users
- **[Developer Guide](./DEVELOPER_GUIDE.md)** - Technical documentation for developers
- **[API Reference](./API_REFERENCE.md)** - API endpoints and integrations
- **[Deployment Guide](./DEPLOYMENT_GUIDE.md)** - How to deploy SINERGI

---

## 🎨 Design Philosophy

### Neon Glow Web3 Aesthetic
- Dark theme with vibrant purple/cyan neon accents
- Glassmorphism effects
- Smooth animations and transitions
- Modern, futuristic UI

### User Experience
- Intuitive navigation
- Progressive disclosure
- Real, tangible outputs (no mockups)
- Cross-feature integration
- Persistent progress tracking

### Educational Approach
- Learn by doing
- Immediate feedback
- Real code execution
- Industry-relevant examples
- Gamification elements

---

## 🌟 Roadmap

### Current Version: 1.0
- ✅ 12 Learning modules with quizzes
- ✅ Architecture Explorer
- ✅ Live IoT Simulator
- ✅ 6 Hands-on Labs
- ✅ Notebook Workspace
- ✅ 10 Industry Datasets
- ✅ Business Case Builder
- ✅ Policy & Governance
- ✅ Analytics Dashboard
- ✅ AI Assistant & Coding Helper

### Future Enhancements
- 🔄 Multi-user collaboration
- 🔄 Social learning features
- 🔄 More advanced labs
- 🔄 Video tutorials
- 🔄 Certification programs
- 🔄 Community marketplace for notebooks
- 🔄 Real hardware integration guides
- 🔄 Mobile app

---

## 🤝 Contributing

We welcome contributions! Whether it's:
- 🐛 Bug reports
- ✨ Feature requests
- 📝 Documentation improvements
- 🔧 Code contributions

Please see our [Contributing Guidelines](./CONTRIBUTING.md) for details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Next.js](https://nextjs.org/)
- AI powered by [Perplexity](https://www.perplexity.ai/)
- Python execution via [Pyodide](https://pyodide.org/)
- Icons by [Lucide](https://lucide.dev/)
- UI components inspired by [shadcn/ui](https://ui.shadcn.com/)

---

## 📞 Support

- 📧 Email: support@elpeef.com
- 🌐 Web: [elpeef.com](https://elpeef.com)

---

<div align="center">

**Built with ❤️ for the future of education**

[⬆ Back to Top](#-sinergi---ai-iot--big-data-learning-platform)

</div>
