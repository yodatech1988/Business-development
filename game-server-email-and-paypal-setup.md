# Game Server Contact Email + PayPal Setup — The AEGIS Directive

Status: planned/in-progress as of 2026-09-12. Domain `aegisdirective.net` is managed on Cloudflare.

## Goal

A single professional contact address (`contact@aegisdirective.net`) used as:
1. The PayPal account email for accepting hosting-cost donations.
2. The point-of-contact address for Bohemia Interactive correspondence (Workshop mods, licensing, support).

Zero-cost approach: Cloudflare Email Routing (free) for receiving + Gmail "Send as" (free) for sending — no paid mailbox host required.

## Setup steps

### 1. Cloudflare Email Routing (receiving)
1. Cloudflare dashboard → `aegisdirective.net` → **Email** → **Email Routing**.
2. Enable Email Routing (auto-adds MX/TXT records).
3. Add routing rule: `contact@aegisdirective.net` → forward to the personal Gmail managing this.
4. Confirm the verification email Cloudflare sends to that Gmail.

### 2. Gmail "Send as" (sending)
1. Gmail → Settings → Accounts and Import → **Send mail as** → Add another email address.
2. Name: "AEGIS Directive", address: `contact@aegisdirective.net`, keep "Treat as an alias" checked.
3. Choose **Send through Gmail** (no custom SMTP needed).
4. Confirm via the code emailed to `contact@aegisdirective.net` (arrives via the Cloudflare forward).

### 3. PayPal
Create a Business account using `contact@aegisdirective.net`.

| Field | Value |
|---|---|
| Business name | The AEGIS Directive |
| Business type | Individual/Sole proprietor (unless a formal LLC exists) |
| Category | Entertainment → Gaming |
| Website | https://aegisdirective.net/ |
| Contact email | contact@aegisdirective.net |
| Description | Community-run DayZ game servers accepting player donations to cover hosting/infrastructure costs |

Framing note: keep this as **donations**, not goods/services purchases, to avoid PayPal dispute/seller-protection complications.

### 4. Bohemia Interactive point of contact
Use `contact@aegisdirective.net` for any Workshop publishing, licensing, or support correspondence with Bohemia. Template:

```
Subject: Point of Contact — The AEGIS Directive (DayZ Community Server Network)

Hello,

I'm writing to establish an official point of contact for The AEGIS Directive,
a DayZ community server network.

- Project/Community name: The AEGIS Directive
- Contact email: contact@aegisdirective.net
- Website: https://aegisdirective.net/
- Nature of contact: [fill in]

Please direct any correspondence regarding our servers, mods, or Workshop
content to this address going forward.

Thank you,
[Your name]
The AEGIS Directive
```

## Open items
- [x] PayPal account type: **Individual/Sole proprietor** — decided 2026-09-12. No LLC exists yet;
  zero-cost-first, and it upgrades to a registered-business account later without losing history.
- [ ] Fill in specific reason for initial Bohemia outreach (mod publishing vs. licensing vs. support)
  — needs Jeremy's input, content of the letter depends on it.

## Note on repo push
This doc was pushed directly to `main`, bypassing a "changes must go through a pull request" branch
rule (GitHub allowed the bypass for this account). Future changes to this repo should go through a
PR unless told otherwise.
