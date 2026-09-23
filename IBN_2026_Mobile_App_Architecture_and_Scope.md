# IBN London 2026 — Official Event Mobile App
## Complete Product Specification, Technical Architecture & Scope Document
**Event:** Global Indian Business Excellence Awards 2026  
**Organizer:** Indian Business Network (IBN)  
**Venues:** House of Commons (Westminster), Central London, University of Oxford, University of Cambridge, Imperial College London  
**Target Platforms:** iOS (App Store) & Android (Google Play Store)

---

## 1. Executive Summary & Product Vision

The **IBN London 2026** mobile application is a high-security, luxury-grade event companion tailored specifically for an ultra-exclusive cohort of **100 C-Suite leaders, investors, and awardees**.

Unlike generic conference apps, this summit operates across **five days**, in **three cities** (London, Oxford, Cambridge), and inside **the British Parliament (House of Commons)**—a venue governed by strict diplomatic and security protocols.

The app serves three core pillars:
1. **Frictionless VIP Experience:** From visa letters to Cromwell Green security clearance, luxury coach departures, and live schedule updates.
2. **Curated C-Suite Networking:** Facilitating high-value, private bilateral connections without compromising delegate privacy.
3. **Institutional & Legal Compliance:** Managing delegate package payments transparently while strictly maintaining the invitation-only, non-monetary status of the parliamentary ceremony.

---

## 2. Core Functional Modules & Scope

### MODULE 1: Delegate Management & Security Accreditation (Parliament-Ready)

Operating within the Palace of Westminster requires advance security clearance and strict identity verification.

* **KYC & Security Data Collection:**
  * Secure capture of full legal name (matching Passport), nationality, date of birth, passport number, and photograph.
  * Direct export formatted specifically for the Metropolitan Police / Parliamentary Security Authority.
* **Accreditation Tracker:**
  * Live status badge visible to the delegate: `Pending Verification` ➔ `Security Submitted` ➔ `Clearance Approved` ➔ `Digital Pass Activated`.
* **Dynamic Digital Delegate Pass (Anti-Screenshot / Anti-Fraud):**
  * Time-synchronized revolving dynamic QR code for entry checks.
  * **Apple Wallet & Google Wallet Integration:** One-tap add to iOS / Android native wallet for offline entry.
  * Delegate Role Badges: `Award Winner`, `Executive Delegate`, `Keynote Speaker`, `Executive Committee`, `VIP Partner`.
* **Delegate Concierge & Visa Vault:**
  * Instant download of personalized, officially stamped **UK Visa Invitation Support Letters**.
  * Hotel reservation vouchers and airport transfer confirmations stored offline.

---

### MODULE 2: Event & Multi-City Logistics Management

The 5-day programme spans multiple historic cities and institutions. Logistics management is crucial.

* **Interactive 5-Day Master Timeline:**
  * **Day 1 (5 Nov):** House of Commons Awards & Reception (London)
  * **Day 2 (6 Nov):** Black Tie Gala Dinner (London)
  * **Day 3 (7 Nov):** Oxford Business Leadership Forum (Oxford)
  * **Day 4 (8 Nov):** University of Cambridge Campus & Deep-Tech Tour (Cambridge)
  * **Day 5 (9 Nov):** Imperial College London Research & AI Showcase (London)
* **Smart Session Details & Guidance:**
  * **Dress Code Indicator:** E.g., *Parliamentary Formal / Lounge Suit* for Day 1; *Black Tie / Tuxedo* for Day 2; *Business Casual* for Days 3–5.
  * **Security Checkpoints & Gate Guidance:** Specific walking routes, Cromwell Green entrance guidelines, prohibited items list.
* **Inter-City Luxury Coach Transit Tracker:**
  * Live countdown to executive coach departures from central London pickup points to Oxford and Cambridge.
  * Real-time GPS location of official coaches and boarding pass scan.
* **Calendar Sync & Push Notifications:**
  * Native sync to Google Calendar, Apple iCal, and Microsoft Outlook.
  * Urgent security announcements via push notifications (e.g., *"Security Notice: Please arrive at Cromwell Green gates by 13:45 GMT"*).
* **Interactive Forum Tools:**
  * Live anonymous Q&A and polling during the Oxford and Imperial panel discussions.
  * Chatham House Rule toggle indicators during closed-door roundtables.

---

### MODULE 3: Payments & Financial Management (Legally Compliant)

Payment handling must respect both UK tax/corporate regulations and the strict parliamentary rule stating: *"No fee is charged for attendance at the Awards Ceremony, and the invitation is not sold."*

* **Fee Allocation Transparency:**
  * Packages are explicitly itemized: *IBN Business Leadership Programme 2026*, including academic forums (Oxford/Cambridge/Imperial), Gala hospitality, local transport, delegate kits, and executive media.
* **Multi-Currency Global Gateways:**
  * **GBP (£) / EUR (€) / USD ($):** Processed via **Stripe**.
  * **INR (₹):** Processed via **Razorpay** (supporting UPI, Net Banking, and Indian corporate cards).
* **Corporate B2B Invoicing & Tax Compliance:**
  * Automated generation of formal tax invoices with Corporate Name, Tax ID / GSTIN / UK VAT number.
  * Support for Corporate Purchase Orders (PO) and offline Wire Transfer (SWIFT / NEFT) receipts upload with manual committee approval.
* **Tiered & Optional Add-ons:**
  * Executive Delegate Package (Standard)
  * Spouse / Partner Gala Dinner Pass
  * Optional Cambridge & Oxford Private Chauffeur Upgrades

---

### MODULE 4: Advanced C-Suite Scope ("The VIP Game Changers")

To deliver a truly world-class experience worthy of 100 global business leaders:

#### 1. AI-Powered Executive Matchmaker & 1-on-1 Bilateral Scheduler
* Delegates input industry focus, investment sectors, and partnership interests.
* The algorithm suggests high-synergy fellow leaders attending the summit.
* Built-in meeting scheduler allowing delegates to request and confirm 15-minute coffee meetings during designated networking breaks.

#### 2. AI Facial Recognition Event Photo Vault
* Professional event photographers upload thousands of high-res photos throughout the 5 days to an AWS S3 bucket.
* Delegates take a one-time selfie during onboarding.
* Powered by **AWS Rekognition / Face-API**, the app automatically aggregates all photos containing that delegate into their private *"My Moments"* gallery.
* 1-click download of full-resolution RAW/JPEG photos for immediate PR, LinkedIn, and social media posting.

#### 3. Privacy-First C-Suite Direct Chat & Digital Business Card
* Delegates can browse the verified guest directory.
* Direct messaging inside the app without revealing personal phone numbers or email addresses.
* Instant digital business card exchange via **NFC tap** or **QR code scan**.

#### 4. Real-Time Emergency & Concierge Hotline
* One-touch WhatsApp or direct VoIP call to Event Coordinator Subha Austalekshmi and secretariat leads.
* Lost badge / delayed transfer instant support.

---

### MODULE 5: Admin Web Dashboard & Check-In Scanner (For IBN Team)

A companion web portal for the IBN Organising Committee:

* **Real-time Delegate Master Roster:** Searchable, filterable by payment status, security clearance status, and dietary requirements.
* **Parliamentary Manifest Generator:** One-click export of accredited guest list conforming to British Parliament security formats.
* **Gate Check-in Scanner App (Mobile / Tablet):**
  * Staff can scan delegate dynamic QR codes at venue doors in milliseconds.
  * Real-time headcounts (e.g., "74 of 100 delegates currently inside House of Commons").
* **Push Broadcast Console:** Send segmented notifications (e.g., to Award Winners only, or all delegates).

---

## 3. Recommended Technology Stack

| Layer | Recommended Technology | Rationale |
|---|---|---|
| **Mobile App (Frontend)** | **Flutter (Dart)** or **React Native (Expo)** | Single high-performance codebase for iOS and Android, pixel-perfect luxury UI, native 120Hz smooth scrolling, fast time-to-market. |
| **Backend & API** | **Node.js (NestJS)** or **Python (FastAPI)** | Robust RESTful and WebSocket architecture for real-time chat, schedules, and notifications. |
| **Database & Auth** | **Supabase (PostgreSQL)** + **Redis** | Enterprise-grade relational data model with Row-Level Security (RLS), instant Auth with Magic Link / OTP / Biometrics, and Redis for sub-millisecond caching. |
| **Payment Gateways** | **Stripe** + **Razorpay** | Complete international multi-currency coverage (Credit Cards, Apple Pay, Google Pay, UPI, Net Banking). |
| **AI Facial Recognition** | **AWS Rekognition** + **Amazon S3** | Fast, highly accurate face indexing across thousands of summit photos with automated private galleries. |
| **Digital Wallet** | **PassKit / Apple Wallet API** & **Google Wallet API** | Seamless lock-screen passes that automatically pop up when arriving near Westminster. |
| **Push Notifications** | **Firebase Cloud Messaging (FCM)** + **Apple APNs** | Ultra-reliable push delivery across iOS and Android with background sync. |

---

## 4. App Store & Google Play Approval Strategy (Crucial Note)

### Apple App Store Guideline 3.1.1 (In-App Purchases vs Event Goods):
* **Important:** Apple allows external payment gateways (Stripe/Razorpay) **without the 30% Apple commission** for real-world physical events, conference registrations, and travel/hospitality packages.
* The app must clearly present purchases as **"Event & Leadership Programme Registration"** (multi-day physical attendance, hospitality, transport).
* The app should offer a "Public View" with event details and a secure "Delegate Login" to comply with Apple's reviewer testing guidelines (providing dedicated test credentials).

---

## 5. Development Roadmap & Implementation Phases

```
[Phase 1: Architecture & UI/UX]  ──►  [Phase 2: Core Build & Security]  ──►  [Phase 3: Payments & AI Vault]  ──►  [Phase 4: Store Launch & Onsite]
       (Weeks 1-2)                           (Weeks 3-5)                           (Weeks 6-7)                         (Weeks 8-9)
 • Wireframes & Luxury Theme           • Auth & Delegate Directory           • Multi-Currency Payments           • App Store & Play Store Approval
 • Database & API Schema               • Parliament Security KYC flow        • AWS Rekognition Photo Vault       • Staff QR Scanner App
 • Security Clearance workflows        • 5-Day Interactive Itinerary         • Apple/Google Wallet Passes        • Onsite rehearsal & Go-Live
```

---

## 6. Summary of Extended Scope

Beyond a standard conference app, this application delivers:
1. **Diplomatic Security Clearance Module** for the British Parliament.
2. **AI Facial-Recognition Photo Vault** for high-res media distribution.
3. **Inter-City Transit Tracker** for London-Oxford-Cambridge coaches.
4. **Bespoke C-Suite 1-on-1 Meeting Matchmaker**.
5. **Apple Wallet / Google Wallet VIP Passes**.
6. **Legally insulated B2B payment & invoicing architecture**.
