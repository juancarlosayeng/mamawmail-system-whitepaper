> **Annex A — IFPP Message Packet Specification and Stateless Transport Behavior**  
> *The Intelligent Fractal Propagation Protocol (IFPP) — A Protocol Originating from the MAMAWMAIL Project Whitepaper*  
> **Author:** Engr. Juan Carlos G. Ayeng  
> **Location:** Bacolod City, Philippines  
> **Date:** October 15, 2025  
> **Version:** 1.0  
> **License:** CC BY-NC-ND 4.0  
> [Temporary during Development]  
>
> **Description:** This annex defines the IFPP message packet structure and stateless transport behavior for use in the MAMAWMAIL decentralized communication system. It serves as a canonical developer and evaluator reference for NLnet and open research review.
---
<hr>


# Annex A — IFPP Message Packet Specification and Stateless Transport Behavior

(“IFPP Message Packet Specification and Stateless Transport Layer Behavior (No-Socket, No-Session Transports)”)

## A.1. Overview

The Intelligent Fractal Propagation Protocol (IFPP) redefines the transport behavior of digital messages across heterogeneous, self-forming swarms of devices. Unlike TCP/IP, which depends on sockets, sessions, and acknowledgments, IFPP employs stateless, event-driven exchanges designed for autonomous relay environments.

Each IFPP message is composed of three interdependent yet independently storable components:

- **Ephemeral Header** – transient bootstrap and authentication data.  
- **AI Metadata** – dynamic, self-evolving contextual information for learning and traceability.  
- **Eternal Message Core** – immutable encrypted payload representing the true message.

All IFPP transmissions occur without sockets or streams, using one-shot, signed, self-destructing datagrams exchanged over any available carrier (UDP, Bluetooth, Wi-Fi, TCP/IP bridge).  
Every device acts as a temporary router, verifier, and teacher, ensuring network resilience and self-healing.

---

## A.2. IFPP Message Structure

| Component | Description | Storage Class | Example Size | Persistence | Contents |
|------------|-------------|----------------|----------------|--------------|-----------|
| **Ephemeral Header** | Transient routing + identity data | Volatile | 1–2 KB | Milliseconds | Fractal Hop ID, Device UUID, Seed Hash, Angel Team Instantiation Token |
| **AI Metadata** | Progressive swarm intelligence data | Semi-volatile | 2–5 KB | Per-hop | Hop Digest, Traceback Map, Gabriel Extracts, Device UUID Pairings |
| **Eternal Message Core** | Immutable encrypted message | Persistent | 10 KB–10 MB | Permanent | Encrypted Payload, Swarm Public/Private Key Pair, Sender/Receiver IDs |

### A.2.1. Ephemeral Header (Seed Data)

- **Fractal Hop ID** – a1, a1b1, a1b2, etc.; universal fractal identifier of message lineage.  
- **Device UUID** – locally unique, cryptographically bound to physical hardware.  
- **Seed Hash** – derived from swarm public key + device private key; ensures authenticity.  
- **Angel Team Token** – minimal code seed to instantiate 7-Angel Team on next device.  
- **Source/Destination Digest** – public identifiers for routing & visual confirmation.

### A.2.2. AI Metadata

- **Hop Digest** – signed record of hop UUIDs and fractal branch IDs.  
- **Partial Learning Snapshot** – per-hop data appended by device AI (not fully transmitted).  
- **Traceback Index** – reverse-linking of all known devices encountered.  
- **Federated Learning Extract** – summary vector for Gabriel’s swarm model updates.

🟣 **Transmission Rule:**  
AI Metadata is appended locally and only partial, hashed versions are sent per hop.  
The complete metadata graph exists collectively across the swarm — no single node holds it all.

### A.2.3. Eternal Message Core

- **Encrypted Payload** – sealed content using sender’s private and receiver’s public key.  
- **Core Signature** – immutable signature of source identity + Sacred Persistence marker.  
- **Swarm Key Pair (SPK/SRK)** – ephemeral keypair per swarm propagation wave.  
- **Integrity Anchors** – Gabriel’s checksum across metadata and header lineage.

🟡 **Decryption Rule:**  
Only the true destination device may access the Eternal Core, based on matching Swarm Receiver Key (SRK).  
Non-destination devices forward based on header checks only.

---

## A.3. Mode 1 — App → UDP (Stateless Datagram)

**Flow:**

App (Team Leader)  
↓  
Encode Message Packet (Ephemeral + Metadata + Core)  
↓  
Liaison Angel → selects UDP interface  
↓  
Create ephemeral datagram (no session)  
↓  
sendto(device_ip, random_port)  
↓  
Point Angel (receiver) verifies trust hash  
↓  
Destroy socket immediately

**Behavior:**

- No connect() or 3-way handshake  
- Random ephemeral port  
- Receiver spawns micro-listener (milliseconds), authenticates, self-destructs  

**Analogy:**  
A signed flare tossed across the sky — visible long enough to verify, then gone.

---

## A.4. Mode 2 — App → Bluetooth (Low Energy / Classic)

**Flow:**

App (Team Leader)  
↓  
Liaison Angel scans for nearby Bluetooth devices  
↓  
Recon verifies candidate in Gabriel’s hash registry  
↓  
Point Angel creates short-lived L2CAP or GATT channel  
↓  
Transmit IFPP packet  
↓  
Immediate disconnect

**Behavior:**

- No pairing or bonding required  
- Uses BLE advertisement or GATT write for envelope  
- Encryption handled entirely by IFPP layer  

**Analogy:**  
A sealed note passed hand-to-hand — no lingering connection.

---

## A.5. Mode 3 — App → Wi-Fi (Ad-hoc or Mesh)

**Flow:**

App (Team Leader)  
↓  
Liaison Angel joins ad-hoc / Wi-Fi Direct mesh  
↓  
Recon detects IFPP-broadcast devices  
↓  
Point Angel selects candidate; sends via broadcast frame  
↓  
Receiver decodes frame; validates UUID  
↓  
If not destination → forward fractally

**Behavior:**

- Operates outside/above IP  
- Stateless, broadcast-capable  
- Ideal for enclosed mesh or swarm networks  

**Analogy:**  
A crowd passing coded notes — each node decides instantly to keep or forward.

---

## A.6. Mode 4 — App → TCP/IP Bridge (Legacy Compatibility)

**Flow:**

App (Team Leader)  
↓  
Liaison Angel routes to IFPP–TCP bridge  
↓  
Bridge wraps IFPP packet inside TCP payload  
↓  
Send via standard socket  
↓  
Remote bridge unwraps packet → passes to Liaison

**Behavior:**

- Maintains socket only within bridge layer  
- Used for transitional systems or public internet hops  

**Analogy:**  
A pigeon carrying a USB stick — TCP/IP carries IFPP intact through legacy space.

---

## A.7. Unified Event-Driven Model

All transports use the same lightweight event engine:

```python
def on_candidate_detected(device):
    if verify_digest(device):
        emit("handshake_ready", device)

def on_handshake_ready(device):
    eph_key = Point_Angel.create_ephemeral_key(device)
    Liaison_Angel.transmit(device, build_ifpp_packet(eph_key))

def on_packet_received(packet):
    if verify_packet(packet):
        Team_Leader_Angel.decide_next_action(packet)
```
          

## A.8. Comparative Transport Table

| Mode | Carrier | Persistent? | Energy | Typical Use | Notes |
|------|----------|-------------|--------|--------------|--------|
| **UDP** | Datagram | ❌ | 🔋 Medium | Internet hops | Stateless, self-authenticating |
| **Bluetooth** | BLE/GATT | ❌ | 🔋 Low | Disaster or local mesh | No pairing required |
| **Wi-Fi** | Mesh / Direct | ❌ | 🔋 Medium | Swarm propagation | IP-optional |
| **TCP/IP Bridge** | Socket | ✅ (bridge only) | 🔋 High | Legacy compatibility | For old systems only |

---

## A.9. Development Status and Future Revision

This annex defines the current working model of IFPP’s message packet structure and transport logic.  
The system is under active development and will evolve as field tests validate performance, device compatibility, and swarm integrity.

**Planned improvements include:**
- Integration with adaptive swarm load-balancing  
- AI-driven hop optimization and energy cost reduction  
- Open SDK for third-party encapsulation libraries  

When additional collaborators, engineers, and test nodes become available, each transport mode will undergo rigorous unit testing, performance benchmarking, and security evaluation.  
All modifications will be reflected in future versions of this annex.




  ---

## 11.1 Ephemeral Header (example JSON)

```json
{
  "message_id": "sha3-512:...",
  "fractal_hop_id": "A1B3",
  "fractal_depth": 3,
  "parent_hop_id": "A1B",
  "hop_count": 5,
  "source_pubkey_fpr": "ed25519:ab12...",
  "prev_device_pubkey_fpr": "ed25519:cd34...",
  "next_candidate_list": ["ed25519:ef56", "ed25519:gh78"],
  "blob_id": "blob-2025-10-13-0001",
  "manifest_id": "man-2025-10-13-01",
  "bootstrap_nonce_id": "nonce-0001",
  "been_here_digest": "sha3-256:4a3f...",
  "ai_digest": "sha3-256:9f1b...",
  "hop_hash_seed": "sha3-256:7z...",
  "sacred_persistence": true,
  "flags": {
    "ack_requested": true,
    "push_mode": false
  },
  "signature": "ed25519:..."
}
```

## 11.2 Payload Sidecar (example)

```json  
{
  "blob_id": "blob-2025-10-13-0001",
  "message_id": "sha3-512:...",
  "content_type": "text/plain",
  "pre_encryption_digest": "sha3-256:...",
  "encryption": {
    "algorithm": "XChaCha20-Poly1305",
    "key_id": "sesh-2025-10-13-01",
    "nonce": "..."
  },
  "display_header": {
    "from_label": "Alice",
    "to_label": "Bob"
  },
  "fractal_seed": "A",
  "integrity_core_hash": "sha3-512:..."
}
```


## 11.3 AI Hop Delta (example)

```json  
{
  "message_id": "sha3-512:...",
  "current_fhi": "A1B3",
  "prev_fhi": "A1B2",
  "device_pubkey_fpr": "ed25519:cd34...",
  "hop_perf_delta": {
    "latency_ms": 22,
    "rssi": -56
  },
  "integrity_flag": true,
  "learning_delta_digest": "sha3-256:..."
}
```
