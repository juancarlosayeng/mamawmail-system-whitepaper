
'''
probabilistic_showcase.py

Module: Probabilistic Broadcast Protocol – Showcase Simulation
--------------------------------------------------------------

Simulates basic **Probabilistic Broadcast** protocol on a random network topology using NetworkX.
Designed for 1-seed "storyboard" runs to visually illustrate protocol behavior.  

Responsible for:
    - Initializing graph topology and parameters
    - Injecting a single message source (seed)
    - Forwarding messages with probability `p_forward`
    - Tracking delivery time, number of transmissions, duplicates, and overhead
    - Producing visualization frames for animation or GIF rendering

Part of the Comparative Protocol Simulations suite for IFPP (Intelligent Fractal Propagation Protocol).  
This file focuses on **visual clarity** rather than statistical rigor.

Usage:
    Run directly as a Python script for side-by-side demo against other protocols.
    Produces logs + images to be compiled into an animation.

Author:
    Engr. Juan Carlos G. Ayeng  
    Bacolod City, The Philippines  
    © 2025

Version:
    0.1.0

License:
    MIT License (see LICENSE file)

Related:
    - flooding_showcase.py / flooding_stats.py: Flooding comparison
    - gossip_showcase.py / gossip_stats.py: Gossip-style comparison
    - spray_wait_showcase.py / spray_wait_stats.py: Limited-replication comparison
    - ifpp_showcase.py / ifpp_stats.py: Intelligent Fractal Propagation Protocol
    - whitepaper: https://github.com/juancarlosayeng/mamawmail-whitepaper

Last updated:
    August 20, 2025
'''

# ===============================
# protocol_eval/showcase/probabilistic_showcase.py
# ===============================

import random
import networkx as nx
import matplotlib.pyplot as plt
from base import network_init, simulator, metrics, visualize
from protocols import probabilistic   # <- specific protocol

# -------------------------------
# Config
# -------------------------------
PROTOCOL_NAME = "Probabilistic"
MODE = "showcase"        # showcase | stat
SEED_COUNT = 1           # can be 1, 5, 20
NUM_NODES = 100
GRAPH_TYPE = "random_geometric"
SIM_TICKS = 20
RUNS = 1 if MODE == "showcase" else 50
P_FORWARD = 0.6          # probability of forwarding (tunable)

# -------------------------------
# Main Execution
# -------------------------------
def main():
    results = []

    for run in range(RUNS):
        # Initialize graph
        G, positions = network_init.create_graph(NUM_NODES, GRAPH_TYPE)

        # Select seeds
        seeds = random.sample(list(G.nodes), SEED_COUNT)

        # Run simulation
        history, deliveries = simulator.run(
            G,
            protocol=probabilistic.protocol,
            seeds=seeds,
            ticks=SIM_TICKS,
            p_forward=P_FORWARD
        )

        # Record metrics
        m = metrics.compute(deliveries, G, seeds, ticks=SIM_TICKS)
        results.append(m)

        # Showcase visualization (first run only)
        if MODE == "showcase" and run == 0:
            visualize.animate(
                G, positions, history,
                title=f"{PROTOCOL_NAME} ({SEED_COUNT} seed, p={P_FORWARD})"
            )

    # Output stats
    if MODE == "stat":
        metrics.save_csv(results, f"results/csv/{PROTOCOL_NAME}_{SEED_COUNT}seeds.csv")

    print(f"{PROTOCOL_NAME} finished ({MODE}, {SEED_COUNT} seeds, p={P_FORWARD}).")

if __name__ == "__main__":
    main()
