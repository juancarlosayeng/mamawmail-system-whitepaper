UPDATED: October 28 2025

### IFPP + MAMAWMAIL WHITEPAPER CURRENT STRUCTURE 

 
1. [x] [Intelligent Fractal Propagation Protocol Whitepaper](https://github.com/juancarlosayeng/mamawmail-system-whitepaper/blob/main/docs/The%20Intelligent%20Fractal%20Propagation%20Protocol%20(IFPP)%20A%20Protocol%20Originating%20from%20the%20MAMAWMAIL%20Project%20Whitepaper%20%E2%80%94%20September%2022%202025%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.pdf) 
   1. [x] Annex A [IFPP MESSAGE PACKET SPECIFICATION AND STATELESS TRANSPORT BEHAVIOR](https://github.com/juancarlosayeng/mamawmail-system-whitepaper/blob/main/docs/Annex_A-IFPP_Message_Packet_Specification_and_Stateless_Transport_Behavior_Beta_102025.pdf)
   2. [ ] Annex B - ONGOING - <b>IFPP PHYSICAL TRANSFER AND CARRIER LAYER EXPRESSIONS</b>  
   3. [ ] Annex C - ONGOING - <b>Archangel Gabriel [AI]: Swarm Supra-Entity and Integrity Sentinel</b> 
  
      
2. [ ] Mamawmail Whitepaper - ONOING

   
 




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














