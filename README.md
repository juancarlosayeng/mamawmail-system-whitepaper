# MAMAWMAIL  
**An AI-Assisted Decentralized Messaging Protocol Using Fractal Propagation**

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














