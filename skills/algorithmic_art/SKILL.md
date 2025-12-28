---
name: algorithmic_art
router_kit: FullStackKit
description: p5.js ile generative art, flow fields ve interactive visuals oluşturma rehberi.
metadata:
  skillport:
    category: design
    tags: [algorithmic art, architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - creative
---

# 🎨 Algorithmic Art

> p5.js ile generative art rehberi.

---

## 📋 Temel Yapı

```javascript
function setup() {
  createCanvas(800, 600);
  background(20);
}

function draw() {
  // Animation loop
}
```

---

## 🔧 Temel Şekiller

```javascript
// Çizgi
line(x1, y1, x2, y2);

// Dikdörtgen
rect(x, y, width, height);

// Elips
ellipse(x, y, width, height);

// Nokta
point(x, y);

// Renkler
fill(r, g, b, alpha);
stroke(r, g, b);
noFill();
noStroke();
```

---

## 🌀 Flow Fields

```javascript
let flowField = [];
let cols, rows;
let scale = 20;

function setup() {
  createCanvas(800, 600);
  cols = floor(width / scale);
  rows = floor(height / scale);
  
  // Create flow field
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      let angle = noise(x * 0.1, y * 0.1) * TWO_PI;
      flowField.push(p5.Vector.fromAngle(angle));
    }
  }
}
```

---

## ✨ Particle Systems

```javascript
class Particle {
  constructor() {
    this.pos = createVector(random(width), random(height));
    this.vel = createVector(0, 0);
    this.acc = createVector(0, 0);
  }
  
  update() {
    this.vel.add(this.acc);
    this.vel.limit(4);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }
  
  show() {
    point(this.pos.x, this.pos.y);
  }
}
```

---

## 🎲 Seeded Randomness

```javascript
// Reproducible randomness
randomSeed(42);
noiseSeed(42);

// Perlin noise
let n = noise(x, y);

// Random range
let r = random(0, 100);
```

---

## 🖱️ Interactivity

```javascript
function mouseMoved() {
  // Mouse position: mouseX, mouseY
}

function mousePressed() {
  // Click handler
}

function keyPressed() {
  if (key === 's') {
    saveCanvas('artwork', 'png');
  }
}
```

---

*Algorithmic Art v1.0*
