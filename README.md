-------
| REPO LINKS |
|----- |
| [MAMAWMAIL RESEARCH INITIATIVE](https://github.com/Mamawmail-Research-Initiative) : Github Organization  |
| [Intelligent Fractal Propagation Protocol](https://github.com/juancarlosayeng/mamawmail-intelligent-fractal-propagation-protocol-whitepaper) : IFPP Whitepaper  |
| [Mamawmail SYSTEM Whitepaper](https://github.com/juancarlosayeng/mamawmail-system-whitepaper) : IFPP Implementation/Application Whitepaper  |
| [Mamawmail](https://github.com/juancarlosayeng/mamawmail) : IFPP Implementation  |
-------

UPDATED: October 28 2025

### IFPP + MAMAWMAIL WHITEPAPER CURRENT STRUCTURE 

 
1. [x] [Intelligent Fractal Propagation Protocol Whitepaper](https://github.com/juancarlosayeng/mamawmail-system-whitepaper/blob/main/docs/The%20Intelligent%20Fractal%20Propagation%20Protocol%20(IFPP)%20A%20Protocol%20Originating%20from%20the%20MAMAWMAIL%20Project%20Whitepaper%20%E2%80%94%20September%2022%202025%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.pdf) 
   1. [x] Annex A [IFPP MESSAGE PACKET SPECIFICATION AND STATELESS TRANSPORT BEHAVIOR](https://github.com/juancarlosayeng/mamawmail-system-whitepaper/blob/main/docs/Annex_A-IFPP_Message_Packet_Specification_and_Stateless_Transport_Behavior_Beta_102025.pdf)
   2. [ ] Annex B  - ONGOING - [IFPP PHYSICAL TRANSFER AND CARRIER LAYER EXPRESSIONS](https://github.com/juancarlosayeng/mamawmail/blob/main/docs/Annex_B-IFPP_Physical_Transfer_and_Carrier_Layer_Expressions.md)
   3. [ ] Annex C - ONGOING - <b>Archangel Gabriel [AI]: Swarm Supra-Entity and Integrity Sentinel</b> 
  
      
2. [ ] Mamawmail Whitepaper - [ONOING/Unfinished](https://github.com/juancarlosayeng/mamawmail-intelligent-fractal-propagation-protocol-whitepaper/blob/main/docs/MAMAWMAIL%20-%20%20A%20Decentralized%20Communication%20System%20Updated%20Whitepaper%20%E2%80%94%20September%2027%202025%20(Original%20June%2020%202025)%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.docx](https://github.com/juancarlosayeng/mamawmail-system-whitepaper/blob/main/docs/MAMAWMAIL%20-%20%20A%20Decentralized%20Communication%20System%20Updated%20Whitepaper%20%E2%80%94%20September%2027%202025%20(Original%20June%2020%202025)%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.docx))
   
  <br><br><br>
 SAMPLE ONGOING RESEARCH - adding more annexes, sections and research
## ANNEX-B Table: Projected Computational and Transmission Costs

This section quantifies the expected energy, storage, and bandwidth requirements during a full IFPP hop cycle between two devices.
The estimates are based on current-generation mobile hardware (ARM A53–A76 class CPUs, 4 GB RAM, 10 MB/s equivalent link) and optimized cryptographic operations (SHA3–256 and XChaCha20-Poly1305).
Values are averages designed for modeling and comparative evaluation with TCP/IP message delivery.
 <br>
| Stage                         | Description                                 | Device A (Sender)                                            | Device B (Receiver)    | Typical Duration | Notes                            |
|-------------------------------|---------------------------------------------|--------------------------------------------------------------|------------------------|------------------|----------------------------------|
| 1 – Payload Receipt           | App → Team Leader message load              |    8 KB RAM, 0.3 MB I/O                                      | -                      | 1ms              | No crypto; memory copy only      |
| 2 – Intel ↔ Gabriel           |    Candidate discovery, AI digest   sync    | 0.5 KB TX / 1 KB RX (≈1.5 KB total)                          | 0.5 KB RX / 1 KB TX    | 2–5 ms           |    Short JSON digest exchange    |
| 3 – Liaison Device Engagement | Candidate signal probe                      | < 2 KB RF signal frames                                      | 2 KB probe response    | 3-7 ms           | BLE/Wi-Fi beacon or UDP ping     |
| 4 – Point Binding             | Object binding + hash computation           | 32 KB RAM (SHA3) ≈ 2 ms CPU                                  | -                      | 2 ms             | 0.002 Wh compute cost            |
| 5 – Heavy Weapons Security    | Security update & verification              | 1 MB read + 64 KB write (≈2 MB I/O)                          | -                      | 15-25 ms         | Most expensive CPU stage (8%)    |
| 6 – Pre-Interaction Sync      | Angel team coordination                     | 128 KB RAM                                                   | 128 KB RAM             | 1 ms             | Negligible bandwidth             |
| 7 – Candidate Evaluation      | 3-node scoring and prioritization           |    1.5 MB RAM compute                                        | -                      | 5 ms             | Local AI inference vectorization |
| 8 – Recon Scouting            | Probe and verification on 3 targets         | 3 × 512 B TX                                                 | 3 × 512 B RX           | 8 ms             | Maintains micro-links            |
|    9 – Hop Decision           | Team Leader + Gabriel evaluation            | 64 KB RAM                                                    | -                      | <1 ms            | Decision matrix merge            |
| 10 – Security Instantiation   | Pre-arrival sandbox deploy                  | -                                                            | 0.5 MB disk write      | 5 ms             | Security sweep initialization    |
| 11 – Message Transfer         | Three-burst transmission                    | 2 KB (Ephemeral) + 4 KB (Metadata) + 10 KB (Core) = 16 KB TX | 16 KB RX               | 1-2 ms           | One-shot burst; no ACK cycle     |
| 12 – Post-Hop Deploy          | Angel re-spawn logic                        | 16 KB RAM                                                    | 32 KB RAM              | 2ms              | Code copy + hash verify          |
| 13 – Hop Confirm ↔ Gabriel    |    Hop status confirmation                  | 1 KB TX / RX                                                 | 1 KB TX / RX           | 1 ms             | Swarm ledger update              |
| 14 – All-Clear Signal         | Passive Gabriel confirmation                | -                                                            | < 0.1 KB RX            | Variable         | Triggered remotely               |
| 15 – Self-Deletion            | Memory release and cleanup                  |    32 KB RAM                                                 | -                      | 0.5 ms           | Garbage collection event         |
| 16 – Cycle Re-Instantiation   | Angel reload on next device                 | -                                                            | 64 KB RAM + 0.5 MB I/O | 2 ms             | Fresh process spawn              |


### Aggregate Resource Cost per Hop (One Device Pair)
| Metric                                         | Device A (Sender) | Device B (Receiver) |     Combined Total     |
|------------------------------------------------|-------------------|---------------------|------------------------|
|    Storage footprint (volatile + temp disk)    | ≈ 2.8 MB          | ≈ 1.1 MB            |    ≈ 3.9 MB            |
| Bandwidth usage (TX + RX combined)             | ≈ 25 KB           | ≈ 25 KB             | ≈ 50 KB per hop        |
| Energy draw                                    | ≈ 0.07 Wh         | ≈ 0.05 Wh           |    ≈ 0.12 Wh total     |
| Compute time (active CPU)                      | ≈ 70 ms           | ≈ 40 ms             | ≈ 110 ms total         |

<br><br><br><br>
## TCP/IP Transmission Baseline (10 KB Payload Example)
| Stage                    | Process                              | Device A (Sender) | Device B (Receiver) | Typical Duration |
|--------------------------|--------------------------------------|-------------------|---------------------|------------------|
| 1 – 3-Way Handshake      | SYN, SYN-ACK, ACK (3 packets × 60 B) | 180 B TX/RX       | 180 B TX/RX         | 15–30 ms         |
| 2 – TLS Handshake        | ECDHE + Certificate exchange         | 4 KB TX + 4 KB RX | 4 KB TX + 4 KB RX   | 120–200 ms       |
| 3 – Payload Transmission | 10.5 KB TX                           | 10.5 KB RX        | 10–20 ms            |                  |
| 4 – ACK & Keepalive      | 1 KB TX / RX                         | 1 KB TX / RX      | 5 ms                |                  |
| 5 – Session Close        | 0.5 KB TX / RX                       | 0.5 KB TX / RX    | 5 ms                |                  |

### Aggregate Cost (10 KB TCP Payload)
| Metric                             | Device A (Sender) | Device B (Receiver) |     Combined Total     |
|------------------------------------|-------------------|---------------------|------------------------|
| Bandwidth usage (over the air)     | 25 KB             | 25 KB               | ≈ 50 KB total          |
| Bandwidth usage (TX + RX combined) | 150–260 ms        | -                   | ≈ 200 ms average       |
| Energy draw                        | ≈ 0.30 Wh         | ≈ 0.25 Wh           | ≈ 0.55 Wh total        |
| Socket duration                    | 250 ms            | 250 ms              | -                      |

### Analytical Comparison
| Category           | IFPP [Per Hop]             | TCP/IP [10kb Message] | Relative Efficiency               |
|--------------------|----------------------------|-----------------------|-----------------------------------|
| Storage (volatile) | 3.9 MB                     | 4.0 MB                | ≈ Parity                          |
| Energy Draw        | 0.12 Wh                    | 0.55 Wh               | 4.5× more efficient               |
| Latency            | 110 ms                     | 200 ms                | ≈ 2× faster                       |
| Bandwidth          | 50 KB                      | 50 KB                 | Equal (IFPP includes AI metadata) |
| Security Overhead  | Self-authenticating digest | TLS cert chain        | ≈ 80% lighter                     |

<br>

## Interpretive Commentary  

### Compute Efficiency:
> IFPP’s event-driven architecture replaces persistent sockets with short-lived microtransactions, cutting power consumption by up to 75%.  

### Reduced Latency:
> Hop decisions overlap with Gabriel synchronization, enabling sub-100 ms behavior within three-hop swarm radius.  

### Stable Memory Pressure:  
> Because each angelic module self-deletes post-hop, per-device memory load remains constant even during heavy network churn.

### Security Simplicity:
> Eliminates TLS certificate dependencies — authentication occurs directly through device key digests.  

### Scalability Trend:
> As devices adopt multi-core AI accelerators (ARMv9 / RISC-V), IFPP’s efficiency gains scale sub-linearly with hop count, meaning greater network size yields higher relative throughput per watt.


<br><br><br><br>




<hr>

UPDATED: October 14 2025

🧩 New Annex Added 

Annex A — IFPP Message Packet Specification and Stateless Transport Behavior
Defines the three-part IFPP message structure (Ephemeral Header, AI Metadata, Eternal Message Core) and outlines stateless, no-socket transport modes via UDP, Bluetooth, Wi-Fi, and TCP/IP bridge.

📘 Preview:
“Each IFPP message is composed of three interdependent yet independently storable components:
— Ephemeral Header – transient bootstrap and authentication data.
— AI Metadata – dynamic, self-evolving contextual information for learning and traceability.
— Eternal Message Core – immutable encrypted payload representing the true message.”


<details>
<summary>🧩 Annex A — IFPP Message Packet Specification and Stateless Transport Behavior</summary>

> Defines the three-part IFPP message structure (Ephemeral Header, AI Metadata, Eternal Message Core).  
>  
> 🔗 [Read Full Annex A (Markdown)](docs/Annex_A-IFPP_Message_Packet_Specification.md)  
> 📄 [Download PDF Version](docs/Annex_A-IFPP_Message_Packet_Specification.pdf)

</details>

<hr>

UPDATED: October 1 2025

# Submitted New IFPP Whitepaper to NLNET. 
- Separated IFPP from Mamawmail into its own Whitepaper.
<br><br>
- Github Repo about to be updated after finishing Mawmawmail Whitepaper.
<br><br>

-----------------------------------------------------
UPDATED: August 24 2025

Part of the Mamawmail Research Initiative – system-level design and theory.
-----------------------------------------------------
## Mamawmail Research Initiative – License Overview

The Mamawmail Research Initiative is a combined effort of theoretical research,  
system architecture design, and practical software implementation.  

It is organized into three connected repositories, each with its own license.  
The whitepapers provide the **research foundation** and theoretical framework,  
while the implementation repository translates those ideas into a working system.  

| Repository                                                | License                              | Purpose                                                   |
| --------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------- |
| **mamawmail-intelligent-propagation-protocol-whitepaper** | CC BY-SA 4.0 (open research license) | Formal description of the Intelligent Fractal Propagation Protocol (IFPP), mathematical models, and comparisons |
| **mamawmail-system-whitepaper**                           | AGPL-3.0 (Community) + Commercial    | Broader system design, AI integrations, and saturation singularity theory |
| **mamawmail**                                             | AGPL-3.0 (Community) + Commercial    | Practical implementation of the Mamawmail system (Community & Enterprise editions) |



--------------------------------------------------

INITIAL README
[June 20 2025 Version]
# MAMAWMAIL  
**An AI-Assisted Decentralized Messaging Protocol Using Fractal Propagation**
<br><br>
# UPDATE SUMMARY
<br><br>
**August 20, 2025**  
<br><br>
<br>
*Intelligent Fractal Propagation Protocol [I.F.P.P] Technical Specification Defnition
<br><br>
<table align="center">
  <tr>
    <th align="center" style="font-size:20px;">I.F.P.P. Formal Description</th>
    <th align="center" style="font-size:20px;">I.F.P.P. Simplified Description</th>
  </tr>  
<tr>
<td width="50%" valign="top" >
<br>“In the initial propagation phase, nodes exhibit a fanout of \(k\), resulting in exponential reachability growth until the maximum fractal depth \(D\) is reached. For illustrative purposes, we select \(k=3\), a value chosen heuristically to approximate network saturation in a 1000-node environment without excessive redundancy. 
<br><br>This parameter is not fixed: in future iterations, the branching factor will be treated as a variable informed by network conditions and adaptive optimization.  
<br><br>In early simulations, IFPP behavior can be modeled within a TCP/IP framework for clarity of illustration, although the protocol itself is transport-agnostic.   
<br><br>Conceptually, equivalent behaviors could be observed in a theoretical UDP system or a Bluetooth mesh of 1000 devices.   
<br><br>These references are not implementations but testbeds for understanding propagation dynamics.”
<br><br><br><br>
</td>
<td width="50%" valign="top">
<br>“At the start, each device passes the message on to three others. 
  <br>This creates a branching, tree-like spread that grows very quickly, reaching most of the network in just a few steps. 
  <br><br>We chose the number three as a simple starting point because, in a group of about 1,000 devices, it lets the message spread widely without creating too many unnecessary duplicates. 
  <br><br>In later versions, this number will not be fixed — the system can adjust how many neighbors to pass the message to depending on how crowded or quiet the network is. 
  <br><br><br>For early testing, we can show this spreading pattern on common computer networks like the Internet (TCP/IP) or even imagine it working over wireless links such as Bluetooth. 
  <br><br>These examples are not finished systems, but just ways to picture how the spreading process works.”
<br><br><br><br>
</td>
</tr>
</table>
<br><br>
<br><br>
-------------------------
<br><br>
<br><br>



# UPDATE SUMMARY
<br><br>
**June 20, 2025**  

## Abstract  

MAMAWMAIL is a decentralized, peer-to-peer messaging protocol that enables encrypted communication without relying on central servers or permanent infrastructure. Messages are distributed using a fractal propagation model, where packets branch through nearby devices and self-delete upon successful forwarding or delivery. The system integrates lightweight routing intelligence and prepares for optional AI-based learning, allowing it to optimize delivery paths over time.

MAMAWMAIL is designed to be censorship-resistant, infrastructure-free, and resilient — ideal for use in disaster zones, offline environments, and sensitive field operations.

---

## Project Goals

- Enable secure, serverless messaging via local device relays (Bluetooth, Wi-Fi Direct, UDP)
- Create a propagation model that is self-pruning, resilient, and scalable
- Integrate lightweight peer learning to improve routing decisions over time
- Support future extensions such as group messaging and swarm optimization
- Offer a modular open-source reference for mesh-based communication systems

---

## Key Features

- Fractal message propagation (3-way hops, with up to 5-depth tree spread)
- Encrypted headers and payloads, recipient-only decryption
- Self-deletion of message copies after successful hop or delivery
- Local peer scorecards with optional AI-ready routing intelligence
- Optional aggregators for private swarms (enterprise, research, or tactical)
- Fully offline-capable; runs over Bluetooth, Wi-Fi Direct, or LAN-based UDP

---

## Use Cases

- **Disaster zones** – Communication where signal towers are down
- **Military/tactical ops** – Secure field coordination without infrastructure
- **Censorship-resistant environments** – Encrypted, trace-resistant delivery
- **Industrial intranets** – Messaging within ships, factories, hospitals
- **Education & research** – Teaching decentralized systems and AI routing

---

## Project Structure
mamawmail_core/ → Core logic, message routing, and fractal propagation
daemon/ → Lightweight background service for peer discovery and relay
docs/ → Diagrams, whitepaper (Markdown and PDF), system specs
test_net/ → Scripts and configurations for test scenarios
README.md → This overview file




---

## Licensing and IP

- **Source Code**: [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.html) – ensures all modifications remain open-source  
- **Whitepaper & Docs**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) – no commercial use or derivatives without explicit permission  
- **Commercial Deployment**: Reserved – contact the author for enterprise or field licensing options  
- **Author**: J.C. Ayeng (2023–2025)

---

## Contributions

We welcome:

- Developers (Python, Android, P2P networking)
- Mesh system testers and field simulation volunteers
- Researchers in swarm logic, federated learning, and offline-first communication

Please open issues, submit pull requests, or share ideas and field use cases.

---

## Contact & Attribution

**Author**: J.C. Ayeng (Juan Carlos G. Ayeng)  
**Email**: [jcgayeng@protonmail.com](mailto:jcgayeng@protonmail.com)  
**Whitepaper**: _Coming soon on arXiv_  

**Citation**:  
> Ayeng, J.C. (2025). *MAMAWMAIL: A Fractal, Serverless, Self-Optimizing Communication Protocol.*

© 2025 J.C. Ayeng. This whitepaper is licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).














