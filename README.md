MAMAWMAIL: An AI-Assisted Decentralized Messaging Protocol Using Fractal Propagation

Abstract

MAMAWMAIL is a decentralized, peer-to-peer messaging protocol that delivers encrypted messages without central servers or permanent infrastructure. Using a fractal propagation model, messages branch through nearby devices and self-clean upon successful delivery. It integrates lightweight routing intelligence and prepares for optional AI-based learning to optimize delivery paths over time. MAMAWMAIL is designed to be censorship-resistant, infrastructure-free, and suitable for use in disaster zones, offline environments, and sensitive field operations.




Project Goals

Enable secure, serverless messaging using local device relays (Bluetooth, Wi-Fi Direct, UDP)

Create a propagation system that is self-pruning, resilient, and scalable

Add lightweight peer learning to improve routing over time

Support future extensions like group messaging and swarm optimization

Provide a modular open-source reference for mesh-based communication systems




Key Features
Fractal message propagation (3-way hops, 5-depth maximum)

Encrypted headers and message payloads

Self-deletion after successful hop or device match

Local peer scorecard and optional routing intelligence

Optional aggregator support for private swarms (enterprise, research, military)

Designed for offline, hostile, or disconnected environments





Use Cases
Disaster zone communication without signal

Military field coordination in disconnected areas

Censorship resistance in restricted networks

Messaging inside factories, ships, or campuses

Educational use for decentralized learning and AI swarm modeling




Project Structure
mamawmail_core/: Core logic, message routing, and fractal logic

daemon/: Lightweight background service for peer discovery and relay

docs/: Diagrams, whitepaper (Markdown and PDF), system specs

test_net/: Scripts and configurations for test scenarios

readme.md: This overview file



## 🔐 Licensing and IP

- **Source Code**: [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.html) – ensures all modifications stay open
- **Whitepaper & Docs**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) – no commercial use or derivatives without permission
- **Commercial Deployment**: Reserved – contact author for field/enterprise/commercial licensing
- **Author**: J.C. Ayeng (2023–2025)





Contributions
We welcome early testers, peer-to-peer developers, offline-first system contributors, and mesh researchers. Please open issues, submit pull requests, or suggest test cases.



Contact & Attribution
Author: JC Ayeng [Juan Carlos G Ayeng]

Whitepaper:  

Contact: [jcgayeng@protonmail.com]

Cite as: MAMAWMAIL: A Fractal, Serverless, Self-Optimizing Communication Protocol

© 2025 J.C. Ayeng. This whitepaper is licensed under CC BY-NC-ND 4.0.
