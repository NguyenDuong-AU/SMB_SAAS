# TODO.md

## Phase 0 – Foundations
- [ ] **Setup core system architecture**
  - [ ] Multi-tenant auth (OAuth2/OIDC, RBAC: Owner, Admin, Staff, Client).
  - [ ] Tenant + user data model with row-level security.
  - [ ] Event bus/queue (Redis/NATS) with `events` table sink.
  - [ ] Base config schema (per-tenant JSON).
  - [ ] Messaging adapters: Email (SMTP), SMS (Twilio), basic logging only for v1.
  - [ ] Payment integration (Stripe) for SaaS billing.
  - [ ] Observability: structured logs, OpenTelemetry traces, tenant-tagged.
- [ ] **Dev environment**
  - [ ] Docker Compose with backend (FastAPI/NestJS), Postgres, Redis, worker.
  - [ ] Seed data for tenants/users.
  - [ ] Feature flag system for module rollout.

---

## Phase 1 – Fast ROI Modules
1. **Speed-to-Lead**
   - [ ] Endpoint `/v1/leads` to ingest web form/ads.
   - [ ] Validate → create CRM contact → AI auto-reply → booking link → 15-min follow-up.
   - [ ] Edge: spam filter, after-hours routing.
   - [ ] KPIs: response time, booking rate.
2. **Show-Up Saver**
   - [ ] Appointment reminders (T-minus schedule).
   - [ ] Confirmation prompt → reschedule link if no confirm.
   - [ ] Edge: timezone handling, double-booking guard.
   - [ ] KPIs: no-show %, confirm %.
3. **Reactivation Engine**
   - [ ] Trigger inactivity (60/90 days).
   - [ ] Personalized AI check-in → spaced follow-ups → escalate to human.
   - [ ] Edge: opt-out compliance, suppression list.
   - [ ] KPIs: reactivation rate, revenue revived.

---

## Phase 2 – Cash Flow Modules
4. **Smart Proposals**
   - [ ] Trigger: CRM deal stage = “Proposal”.
   - [ ] Generate PDF/HTML → e-sign link → send → track opens.
   - [ ] Edge: multi-versioning, legal clauses.
   - [ ] KPIs: open rate, close rate.
5. **Invoice Auto-Flow**
   - [ ] Trigger: accepted proposal/job done.
   - [ ] Create + send invoice → reminders → reconcile payments.
   - [ ] Edge: partial/failure handling.
   - [ ] KPIs: DSO, 7-day paid %.

---

## Phase 3 – Client Experience Modules
6. **Onboarding Autopilot**
   - [ ] Trigger: payment received.
   - [ ] Welcome email/video → kickoff scheduling → client portal access.
   - [ ] Edge: missing info capture, stalled checklist.
   - [ ] KPIs: time-to-kickoff, checklist completion.
7. **Loyalty / NPS**
   - [ ] Trigger: job complete/purchase.
   - [ ] Send NPS/feedback form → coupon/referral link.
   - [ ] Edge: incentive abuse guard, review compliance.
   - [ ] KPIs: NPS score, referral rate.

---

## Phase 4 – Growth Modules
8. **Outbound Lead Machine**
   - [ ] Seed list/scraping → AI one-liners → throttle sends → tag replies.
   - [ ] Edge: compliance, bounce handling.
   - [ ] KPIs: reply %, booked calls.
9. **AI Draft Assistant**
   - [ ] Trigger: content/report/proposal update.
   - [ ] Draft → fact-check → send to reviewer → track edits.
   - [ ] Edge: hallucination control, citation mode.
   - [ ] KPIs: turnaround time, revision count.
10. **Client Portal**
    - [ ] Unified view: proposals, invoices, bookings, checklists.
    - [ ] RBAC for clients.
    - [ ] Edge: SSO for larger tenants.
    - [ ] KPIs: login rate, support tickets reduced.

---

## Phase X – Cross-Cutting
- [ ] **Testing**
  - [ ] Unit tests per module pipeline.
  - [ ] Flow tests with sandbox APIs.
  - [ ] Smoke tests per tenant template.
- [ ] **KPIs dashboard**
  - [ ] Aggregate per module (response times, conversion %, revenue revived).
- [ ] **Docs**
  - [ ] README for dev setup.
  - [ ] API reference (per-tenant endpoints).
  - [ ] Niche template packs (Trades, Health, Agencies, Retail).
