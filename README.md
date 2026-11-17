# 🚗 APPSC AMVI Master Preparation & CBT Portal
### Andhra Pradesh Assistant Motor Vehicle Inspectors in A.P. Transport Subordinate Service
**Official Examination Preparation Platform for Paper-I & Paper-II**

---

## 📌 Executive Summary

This portal is a full-featured, responsive, production-ready interactive web application designed specifically for aspirants preparing for the **Assistant Motor Vehicle Inspector (AMVI)** recruitment in the **A.P. Transport Subordinate Service** conducted by the **Andhra Pradesh Public Service Commission (APPSC)**.

It is architected to run immediately in your local environment, while also coming pre-configured with Docker and Kubernetes manifests for seamless deployment to production Kubernetes clusters and custom domains.

---

## 🌟 Key Features & Tabs

### 1. 📋 Job Overview & Exam Patterns
- **Role:** Assistant Motor Vehicle Inspector (Executive Cadre), A.P. Transport Subordinate Service.
- **Pay Scale:** ₹48,440 – ₹1,37,220 (Revised Pay Scales RPS 2022).
- **Educational Qualifications:** Degree in Mechanical / Automobile Engineering OR Diploma in Automobile Engineering (DAE) from State Board of Technical Education and Training (SBTET), AP.
- **Driving License & HTV Experience:** Valid Driving License with Heavy Transport Vehicle (HTV/HMV) endorsement and 3+ years experience. Special concession for female candidates (LMV allowed, acquire HTV within 2 years).
- **Physical Standards:** Male: Height ≥ 165 cm, Chest ≥ 86.3 cm (+5 cm expansion). Female: Height ≥ 157.5 cm. Visual acuity: 6/6 distant, 0.5 near, no colour blindness.
- **Exam Pattern (CBRT):** 300 Questions, 300 Marks, 300 Minutes.
  - **Paper-I:** General Studies & Mental Ability (150 Qs, 150 Marks, Degree Standard).
  - **Paper-II:** Automobile / Mechanical Engineering (150 Qs, 150 Marks, Diploma Standard).
  - **Negative Marking:** **1/3rd (0.33 marks)** deducted for every wrong answer.

### 2. 📚 Phase 1: Paper-I Syllabus (General Studies & Mental Ability)
- Complete coverage of all 10 core units:
  1. Events of National & International Importance
  2. Current Affairs (International, National & Andhra Pradesh)
  3. General Science & IT Applications (EV Batteries, BMS, Telematics)
  4. Modern Indian & Andhra Pradesh History (Freedom Struggle, Potti Sreeramulu fast, 1953 Andhra State)
  5. Indian Polity & Governance (Writs, 73rd/74th Amendments, e-Governance, VAHAN/SARATHI)
  6. Indian & AP Economy (Socio-economic survey, logistics, ports)
  7. Geography of India & AP (River Godavari/Krishna, Polavaram)
  8. Disaster Management & Sustainable Mobility
  9. Logical Reasoning, Analytical Ability & Data Interpretation
  10. AP Reorganisation Act, 2014 (Section 90 Polavaram, River Boards, Asset Division)
- **Interactive Checklist:** Mark completed topics; progress percentages are saved to your browser's local storage.

### 3. ⚙️ Phase 2: Paper-II Syllabus (Automobile & Mechanical Engineering)
- Complete coverage of all 6 technical units (Diploma Standard):
  1. Automotive Engines & Thermodynamics (Otto/Diesel cycles, CRDI, MPFI, BS-VI SCR/DEF/DPF)
  2. Automotive Chassis, Transmission & Drivetrain (Clutches, Synchromesh balking ring, Differential, Axles)
  3. Steering Geometry, Suspension & Brakes (Camber, Caster, KPI, Scrub Radius, Air Unloader Valves, ABS)
  4. Automotive Electrical & Electronics (Lead-acid battery, Alternator, CAN bus, Sensors)
  5. Motor Vehicles Act 1988, Amendments 2019 & CMVR (Fitness Form 38, Section 185 drunk driving, Section 194 overload)
  6. Applied Mechanical Sciences, SOM & Workshop Technology (Bending, Torsion, Bernoulli)

### 4. 📑 Previous Model Papers & Trend Analysis
- In-depth trend reviews of **2023, 2019, and 2012** APPSC AMVI papers.
- Topic weightage blueprint highlighting high-yield recurring focus areas.

### 5. ✍️ Model Exams Simulator (Computer Based Test - CBRT)
- Real-world simulation matching the APPSC online exam screen:
  - **Model Exam 1:** Paper-I Full Test (General Studies & Mental Ability)
  - **Model Exam 2:** Paper-II Full Test (Automobile Engineering / Mechanical)
  - **Model Exam 3:** Combined Grand Mock Test (Paper-I + Paper-II)
- **Smart Dynamic Practice:** Separate 150-question Paper-I and Paper-II tests; each attempt prioritizes previously missed questions, then unseen questions.
- Live countdown timer with low-time visual alerts.
- APPSC 5-state Question Palette:
  - 🟢 Green: Answered
  - 🔴 Red: Not Answered
  - 🟣 Purple: Marked for Review
  - 🟠 Orange: Answered & Marked for Review
  - ⚪ Gray: Not Visited
- Standard exam actions: *Save & Next*, *Clear Response*, *Mark for Review & Next*, *Previous*, and *Submit Exam*.

### 6. 📊 Exam Results & Dual-Language Explanations (English + Telugu)
- **Automatic Scorecard:** Net Score, Correct (+1.00), Incorrect (-0.33), Unattempted (0), Accuracy %, Time Taken.
- **Bilingual Solutions:** Every question features a comprehensive:
  - 📘 **English Explanation** (Technical reasoning, equations, constitutional articles).
  - 📙 **తెలుగు వివరణ (Telugu Explanation)** (Natural, clear Telugu with correct terminology).
- **Solution Filtering:** Filter by *All*, *Incorrect Only* (for high-yield mistake revision), *Correct*, or *Unattempted*.
- **Language Toggle:** View Both (English + Telugu), English Only, or Telugu Only.

### 7. 💡 High-Yield Formula Cheat Sheet & MVA Rules
- Quick revision formulas for thermal efficiencies ($\eta_{otto}$, $\eta_{diesel}$), Brake Power, Simple Bending $(M/I = \sigma/y = E/R)$, Torsion $(T/J = \tau/r = G\theta/L)$, Steering Included Angle, and critical Motor Vehicles Act legal limits.

---

## 🚀 How to Run Locally

### Option 1: Direct Shell Launcher (Recommended)
Open your terminal in this directory and execute:
```bash
./run_local.sh
```
Then open your browser at: **`http://localhost:8080`**

### Option 2: Using Python 3
```bash
python3 -m http.server 8080
```
Open your browser at: **`http://localhost:8080`**

### Option 3: Using Node.js
```bash
npx serve -l 8080 .
# or
npm start
```

## 🌐 Free Hosting with GitHub Pages

This is a static website and can be deployed free with GitHub Pages.

1. Create a **public** GitHub repository for the project and push the site files to its `main` branch.
2. In the repository, open **Settings → Pages** and set the build/deployment source to **GitHub Actions**.
3. The included `.github/workflows/pages.yml` workflow deploys `index.html`, `css/`, and `js/` after each push to `main`. You can also start it from the repository's **Actions** tab with **Run workflow**.
4. When the deployment completes, open the URL shown in the workflow run or under **Settings → Pages**. It normally has the form `https://<github-user>.github.io/<repository-name>/`.

The workflow publishes only the website files; local scripts, Docker/Kubernetes files, and scratch content are not included in the Pages artifact.

---

## 🐳 Running with Docker Locally

To run with Docker:
```bash
# Build the container image
docker build -t appsc-amvi-portal:latest .

# Run the container
docker run -d -p 8080:80 --name amvi-portal appsc-amvi-portal:latest
```
Access at **`http://localhost:8080`**.

Using Docker Compose:
```bash
docker compose up -d
```

---

## ☸️ Deploying to Kubernetes Production Clusters & Custom Domain

Pre-configured Kubernetes manifests are provided inside the `k8s/` directory:

1. **Tag and push image to your container registry:**
   ```bash
   docker tag appsc-amvi-portal:latest your-registry.com/appsc-amvi-portal:v1.0.0
   docker push your-registry.com/appsc-amvi-portal:v1.0.0
   ```

2. **Update image and domain in manifests:**
   - In `k8s/deployment.yaml`, update `image: your-registry.com/appsc-amvi-portal:v1.0.0`.
   - In `k8s/ingress.yaml`, replace `amvi-prep.yourdomain.com` with your production domain or subdomain.

3. **Deploy to your Kubernetes cluster:**
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   kubectl apply -f k8s/ingress.yaml
   ```

4. **Verify cluster status:**
   ```bash
   kubectl get pods -l app=appsc-amvi-portal
   kubectl get svc appsc-amvi-service
   kubectl get ingress appsc-amvi-ingress
   ```

---

## 📂 Project Structure

```
ap-break-ins-tool/
├── index.html              # Main Single Page Application interface
├── css/
│   └── styles.css          # Modern, responsive styles & CBRT UI layout
├── js/
│   ├── app.js              # UI controller, tab switching, events, solutions renderer
│   ├── examEngine.js       # CBRT test engine, timer, palette state & scoring logic
│   ├── questionBank.js     # Bilingual question bank with English & Telugu explanations
│   └── syllabusData.js     # Official syllabus, exam overview, blueprints & formulas
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment (2 replicas, health checks)
│   ├── service.yaml        # Kubernetes ClusterIP Service
│   └── ingress.yaml        # Kubernetes Ingress with TLS/SSL for custom domain
├── Dockerfile              # Lightweight Nginx Alpine production image
├── docker-compose.yml      # Local / containerized orchestration
├── nginx.conf              # Production Nginx config with gzip & caching
├── package.json            # Node.js project definition & scripts
├── run_local.sh            # One-click local runner script
└── README.md               # Complete documentation
```
