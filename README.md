# Project Stealth Agent

## 🎯 Core Concept
A full-stack, multi-agent content engine that takes a single text prompt to generate both an optimized YouTube thumbnail and a short teaser/promo video using an asynchronous, Human-in-the-Loop (HITL) architecture.

## 🛠️ Tech Stack & Hosting
* **Frontend:** React (Hosted on **Vercel** — free tier, zero cold starts)
* **Backend:** FastAPI (Hosted on **Render** — free tier, handles background I/O tasks)
* **Database & Storage:** Supabase (Hosted on **Supabase** — permanent free tier Postgres + 500MB asset storage)
* **AI Generation:** Google Gemini 1.5 Flash (Scripting) + Hugging Face Inference API (Image & Video rendering)
* **Notifications:** Resend API or Gmail SMTP (Free email delivery)

## ⚡ Key Technical Mechanics
* **Timeout Elimination:** The frontend requests a job and immediately receives a `job_id` ticket. All long-running API tasks execute strictly as asynchronous background tasks.
* **Human-in-the-Loop (HITL):** Processing halts after thumbnail and script generation. The user reviews/edits the text script completely offline, ensuring zero active server resource consumption during wait time.
* **Asynchronous Delivery:** Once approved, video generation triggers in the background (5–10 minutes). The backend stays active via open network network wait states on Render, updates Supabase upon completion, and fires a notification email containing a direct route redirection link (`/preview/{job_id}`) for playback and download.