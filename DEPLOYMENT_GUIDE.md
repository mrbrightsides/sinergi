# 🚀 SINERGI Deployment Guide

Complete guide for deploying SINERGI to production.

---

## 📋 Table of Contents

1. [Deployment Options](#deployment-options)
2. [Vercel Deployment](#vercel-deployment)
3. [Netlify Deployment](#netlify-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Self-Hosted Deployment](#self-hosted-deployment)
6. [Environment Variables](#environment-variables)
7. [Pre-Deployment Checklist](#pre-deployment-checklist)
8. [Post-Deployment Tasks](#post-deployment-tasks)
9. [Monitoring & Maintenance](#monitoring--maintenance)
10. [Troubleshooting](#troubleshooting)

---

## Deployment Options

### Recommended: Vercel ⭐

**Best for:**
- Next.js applications (native support)
- Quick deployments
- Automatic HTTPS
- Global CDN
- Serverless functions

**Pros:**
- Zero configuration for Next.js
- Automatic preview deployments
- Free tier available
- Excellent performance

**Cons:**
- Limited customization
- Vendor lock-in

---

### Alternative: Netlify

**Best for:**
- Simple hosting
- Static exports
- Form handling

**Pros:**
- Easy setup
- Good free tier
- Built-in form handling

**Cons:**
- Less optimized for Next.js
- Limited serverless capabilities

---

### Advanced: Docker

**Best for:**
- Custom infrastructure
- Complete control
- Multi-service deployments

**Pros:**
- Full control
- Portable
- Scalable

**Cons:**
- Requires DevOps knowledge
- More maintenance

---

### Expert: Self-Hosted

**Best for:**
- Enterprise deployments
- Specific compliance requirements
- Custom infrastructure

**Pros:**
- Complete control
- Cost-effective at scale
- Custom configurations

**Cons:**
- Requires infrastructure expertise
- Higher maintenance
- Manual scaling

---

## Vercel Deployment

### Quick Deploy (5 minutes)

#### Method 1: GitHub Integration

1. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/yourusername/sinergi.git
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Select your GitHub repository
   - Click "Import"

3. **Configure**
   - Framework Preset: Next.js (auto-detected)
   - Build Command: `npm run build` (default)
   - Output Directory: `.next` (default)
   - Install Command: `npm install` (default)

4. **Add Environment Variables**
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   NODE_ENV=production
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app is live! 🎉

#### Method 2: Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login**
   ```bash
   vercel login
   ```

3. **Deploy to preview**
   ```bash
   vercel
   ```

4. **Deploy to production**
   ```bash
   vercel --prod
   ```

### Vercel Configuration File

Create `vercel.json` in project root:

```json
{
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "regions": ["iad1"],
  "env": {
    "PERPLEXITY_API_KEY": "@perplexity-api-key"
  },
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Frame-Options",
          "value": "SAMEORIGIN"
        },
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        }
      ]
    }
  ]
}
```

### Custom Domain

1. **Add Domain in Vercel**
   - Go to Project Settings → Domains
   - Add your domain (e.g., sinergi.dev)

2. **Configure DNS**
   
   **If using Vercel nameservers:**
   ```
   Vercel will provide nameservers
   Update at your domain registrar
   ```

   **If using external DNS:**
   ```
   Type: A
   Name: @
   Value: 76.76.21.21

   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

3. **Wait for SSL**
   - HTTPS certificate auto-generated
   - Takes 5-10 minutes

### Preview Deployments

Every push to a branch creates a preview:

```bash
git checkout -b feature/new-feature
git push origin feature/new-feature
# Vercel automatically creates preview URL
```

---

## Netlify Deployment

### Deploy via Git

1. **Push to Git**
   ```bash
   git push origin main
   ```

2. **Connect to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Click "Add new site" → "Import from Git"
   - Select repository

3. **Configure Build**
   ```
   Build command: npm run build
   Publish directory: .next
   ```

4. **Environment Variables**
   - Go to Site settings → Environment variables
   - Add `PERPLEXITY_API_KEY`

5. **Deploy**
   - Click "Deploy site"
   - Wait for build to complete

### Netlify CLI

```bash
# Install
npm install -g netlify-cli

# Login
netlify login

# Initialize
netlify init

# Deploy
netlify deploy --prod
```

### netlify.toml Configuration

```toml
[build]
  command = "npm run build"
  publish = ".next"

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
```

---

## Docker Deployment

### Dockerfile

Create `Dockerfile` in project root:

```dockerfile
# Build stage
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source
COPY . .

# Build application
RUN npm run build

# Production stage
FROM node:18-alpine AS runner

WORKDIR /app

# Copy necessary files
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

# Expose port
EXPOSE 3000

# Set environment
ENV NODE_ENV=production
ENV PORT=3000

# Start application
CMD ["npm", "start"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  sinergi:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - PERPLEXITY_API_KEY=${PERPLEXITY_API_KEY}
    restart: unless-stopped
    volumes:
      - ./logs:/app/logs
```

### Build and Run

```bash
# Build image
docker build -t sinergi:latest .

# Run container
docker run -d \
  -p 3000:3000 \
  -e PERPLEXITY_API_KEY=your_key \
  --name sinergi \
  sinergi:latest

# Or use docker-compose
docker-compose up -d
```

### Docker Hub Deployment

```bash
# Tag image
docker tag sinergi:latest yourusername/sinergi:latest

# Push to Docker Hub
docker push yourusername/sinergi:latest

# Pull and run on server
docker pull yourusername/sinergi:latest
docker run -d -p 3000:3000 yourusername/sinergi:latest
```

---

## Self-Hosted Deployment

### Prerequisites

- Ubuntu 20.04+ or similar Linux distribution
- Node.js 18+
- Nginx (reverse proxy)
- PM2 (process manager)
- SSL certificate (Let's Encrypt)

### Server Setup

#### 1. Install Node.js

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Verify
node --version
npm --version
```

#### 2. Install PM2

```bash
sudo npm install -g pm2
```

#### 3. Install Nginx

```bash
sudo apt install -y nginx
```

#### 4. Clone Repository

```bash
cd /var/www
sudo git clone https://github.com/yourusername/sinergi.git
cd sinergi
sudo npm install
```

#### 5. Build Application

```bash
# Set environment variables
export PERPLEXITY_API_KEY=your_api_key

# Build
sudo npm run build
```

#### 6. Configure PM2

Create `ecosystem.config.js`:

```javascript
module.exports = {
  apps: [{
    name: 'sinergi',
    script: 'npm',
    args: 'start',
    cwd: '/var/www/sinergi',
    instances: 'max',
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'production',
      PORT: 3000,
      PERPLEXITY_API_KEY: 'your_api_key'
    }
  }]
}
```

Start with PM2:

```bash
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

#### 7. Configure Nginx

Create `/etc/nginx/sites-available/sinergi`:

```nginx
server {
    listen 80;
    server_name sinergi.dev www.sinergi.dev;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/sinergi /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 8. SSL Certificate (Let's Encrypt)

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d sinergi.dev -d www.sinergi.dev

# Auto-renewal (already set up by certbot)
sudo certbot renew --dry-run
```

### Monitoring

```bash
# PM2 monitoring
pm2 monit

# PM2 logs
pm2 logs sinergi

# System resources
htop

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

---

## Environment Variables

### Required Variables

```env
# Perplexity AI API Key (required for AI features)
PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxxx

# Node Environment
NODE_ENV=production
```

### Optional Variables

```env
# Port (default: 3000)
PORT=3000

# API Rate Limiting
API_RATE_LIMIT=100

# Feature Flags
ENABLE_AI_FEATURES=true
ENABLE_ANALYTICS=true
```

### Setting Environment Variables

#### Vercel

```bash
vercel env add PERPLEXITY_API_KEY production
```

Or via dashboard: Project Settings → Environment Variables

#### Netlify

Via dashboard: Site Settings → Environment Variables

#### Docker

```bash
docker run -e PERPLEXITY_API_KEY=your_key sinergi
```

Or in docker-compose.yml

#### PM2

In `ecosystem.config.js` env section

---

## Pre-Deployment Checklist

### Code Quality

- [ ] All TypeScript errors resolved
- [ ] ESLint warnings fixed
- [ ] Build completes successfully
- [ ] No console.log statements in production code

### Testing

- [ ] All features tested manually
- [ ] Quiz submission works
- [ ] PDF generation functional
- [ ] Python code execution works
- [ ] AI assistants respond
- [ ] Data persistence works
- [ ] Cross-browser tested (Chrome, Firefox, Safari)
- [ ] Mobile responsive tested

### Security

- [ ] API keys not hardcoded
- [ ] Environment variables set
- [ ] HTTPS configured
- [ ] Security headers added
- [ ] CORS properly configured

### Performance

- [ ] Images optimized
- [ ] Bundle size acceptable (<500KB initial)
- [ ] Lighthouse score >90

### Content

- [ ] All text reviewed
- [ ] Links working
- [ ] Documentation complete
- [ ] README updated

---

## Post-Deployment Tasks

### 1. Verify Deployment

```bash
# Check if site is live
curl -I https://your-domain.com

# Check API proxy
curl -X POST https://your-domain.com/api/proxy \
  -H "Content-Type: application/json" \
  -d '{"test": true}'
```

### 2. Test Features

- Open each feature module
- Complete a quiz
- Generate a PDF
- Run Python code
- Test AI assistant
- Export dataset

### 3. Monitor Performance

```bash
# Check response times
curl -w "@curl-format.txt" -o /dev/null -s https://your-domain.com
```

Create `curl-format.txt`:
```
time_namelookup:  %{time_namelookup}\n
time_connect:  %{time_connect}\n
time_starttransfer:  %{time_starttransfer}\n
time_total:  %{time_total}\n
```

### 4. Set Up Monitoring

**Vercel:**
- Built-in analytics in dashboard
- Real-time logs available

**Self-Hosted:**
```bash
# Install monitoring tools
pm2 install pm2-logrotate
pm2 set pm2-logrotate:max_size 10M
pm2 set pm2-logrotate:retain 7
```

### 5. Configure Backups

```bash
# Backup script for self-hosted
#!/bin/bash
BACKUP_DIR="/backups/sinergi"
DATE=$(date +%Y%m%d)

# Create backup
tar -czf $BACKUP_DIR/sinergi-$DATE.tar.gz /var/www/sinergi

# Keep only last 7 backups
find $BACKUP_DIR -name "sinergi-*.tar.gz" -mtime +7 -delete
```

Schedule with cron:
```bash
# Daily backup at 2 AM
0 2 * * * /path/to/backup-script.sh
```

---

## Monitoring & Maintenance

### Health Checks

Create health check endpoint:

```typescript
// src/app/api/health/route.ts
export async function GET() {
  return Response.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  })
}
```

### Logging

```bash
# PM2 logs
pm2 logs --lines 100

# Nginx access logs
sudo tail -f /var/log/nginx/access.log | grep -v "health"

# Nginx error logs
sudo tail -f /var/log/nginx/error.log
```

### Performance Monitoring

```bash
# Server resources
htop
df -h  # Disk usage
free -m  # Memory

# Application metrics
pm2 monit
```

### Updates

```bash
# Pull latest code
cd /var/www/sinergi
git pull origin main

# Install dependencies
npm install

# Rebuild
npm run build

# Restart
pm2 restart sinergi
```

### Database Maintenance

Since SINERGI uses localStorage (client-side), no database maintenance needed. For future database integration:

```sql
-- Example maintenance queries
VACUUM ANALYZE;  -- PostgreSQL
OPTIMIZE TABLE table_name;  -- MySQL
```

---

## Troubleshooting

### Build Fails

**Problem:** `npm run build` fails

**Solutions:**
```bash
# Clear cache
rm -rf .next node_modules
npm install
npm run build

# Check Node version
node --version  # Should be 18+

# Check for TypeScript errors
npx tsc --noEmit
```

### Port Already in Use

**Problem:** `Error: Port 3000 is already in use`

**Solutions:**
```bash
# Find process using port
lsof -i :3000

# Kill process
kill -9 <PID>

# Or use different port
PORT=3001 npm start
```

### API Proxy Errors

**Problem:** Perplexity API calls fail

**Solutions:**
```bash
# Check environment variable
echo $PERPLEXITY_API_KEY

# Test API directly
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.1-sonar-small-128k-online","messages":[{"role":"user","content":"test"}]}'

# Check proxy route exists
ls -la src/app/api/proxy/route.ts
```

### SSL Certificate Issues

**Problem:** HTTPS not working

**Solutions:**
```bash
# Renew certificate
sudo certbot renew

# Check certificate status
sudo certbot certificates

# Force renewal
sudo certbot renew --force-renewal

# Check Nginx config
sudo nginx -t
```

### Out of Memory

**Problem:** Application crashes with OOM

**Solutions:**
```bash
# Increase Node memory limit
NODE_OPTIONS="--max-old-space-size=4096" npm start

# Or in PM2 ecosystem.config.js
node_args: '--max-old-space-size=4096'

# Check memory usage
pm2 monit
free -m
```

### Slow Performance

**Problem:** Application is slow

**Solutions:**
```bash
# Enable gzip in Nginx
# Add to /etc/nginx/nginx.conf
gzip on;
gzip_types text/plain text/css application/json application/javascript;

# Check bundle size
npm run build
ls -lh .next/static

# Optimize images
# Use next/image component

# Enable caching
# Add cache headers in next.config.js
```

### PM2 Process Dies

**Problem:** PM2 process keeps stopping

**Solutions:**
```bash
# Check logs
pm2 logs sinergi --err

# Increase restart delay
pm2 restart sinergi --exp-backoff-restart-delay=100

# Check system resources
df -h  # Disk space
free -m  # Memory

# Update PM2
pm2 update
```

---

## Rollback Procedures

### Vercel

```bash
# Via CLI
vercel rollback

# Via Dashboard
# Go to Deployments → Select previous deployment → Promote
```

### Self-Hosted

```bash
# Restore from backup
cd /var/www
sudo tar -xzf /backups/sinergi/sinergi-20240115.tar.gz

# Restart application
pm2 restart sinergi
```

### Docker

```bash
# Pull previous version
docker pull yourusername/sinergi:previous-tag

# Stop current container
docker stop sinergi

# Start previous version
docker run -d -p 3000:3000 --name sinergi yourusername/sinergi:previous-tag
```

---

## Scaling

### Vertical Scaling

**Increase server resources:**
- CPU: 2→4 cores
- RAM: 2GB→8GB
- Storage: As needed

### Horizontal Scaling

**Load balancer configuration:**

```nginx
upstream sinergi_backend {
    server 10.0.1.10:3000;
    server 10.0.1.11:3000;
    server 10.0.1.12:3000;
}

server {
    location / {
        proxy_pass http://sinergi_backend;
    }
}
```

### CDN Integration

**Vercel:** Built-in global CDN

**Self-Hosted:** Use Cloudflare

```nginx
# Nginx cache configuration
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g;

location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 1h;
}
```

---

## Cost Estimates

### Vercel (Recommended)

- **Hobby Plan:** Free
  - 100GB bandwidth
  - Unlimited websites
  - Automatic HTTPS

- **Pro Plan:** $20/month
  - 1TB bandwidth
  - Team collaboration
  - Advanced analytics

### Self-Hosted (AWS/DigitalOcean)

- **t3.small:** $15-20/month
  - 2 vCPUs
  - 2GB RAM
  - Suitable for moderate traffic

- **t3.medium:** $30-40/month
  - 2 vCPUs
  - 4GB RAM
  - Better for higher traffic

### Domain & SSL

- **Domain:** $10-15/year
- **SSL:** Free (Let's Encrypt)

---

## Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Netlify Documentation](https://docs.netlify.com/)
- [Next.js Deployment](https://nextjs.org/docs/deployment)
- [Docker Documentation](https://docs.docker.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [PM2 Documentation](https://pm2.keymetrics.io/docs/)

---

## Support

For deployment assistance:

- 📧 Email: deploy@sinergi.dev
- 💬 Discord: [#deployment-help](https://discord.gg/sinergi)
- 📖 Docs: [docs.sinergi.dev/deployment](https://docs.sinergi.dev/deployment)

---

**Deploy with Confidence! 🚀**

Last Updated: 2024-01-15
