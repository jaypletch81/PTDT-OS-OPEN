ptdt-os/
│
├── core/
│   ├── ptdt_os_v3.py        # Final open-core GoldenKernel/GoldenReport
│   ├── crypto/              # If you include v3.0 crypto edition
│   └── __init__.py
│
├── adapters/
│   ├── brain_adapter.py     # Placeholder interfaces for Neuralink, EEG, etc.
│   ├── ai_training_adapter.py
│   ├── robotics_adapter.py
│   ├── vehicle_adapter.py
│   └── quantum_adapter.py
│
├── examples/
│   ├── run_open_core.py     # Simple working demo
│   ├── multi_domain_demo.py
│   └── README.md
│
├── docs/
│   ├── OVERVIEW.md          # High-level explanation of PTDT theory
│   ├── SAFETY_SPEC.md       # Δ, dΔ/dt spec documented
│   ├── GLOSSARY.md
│   └── ROADMAP.md
│
├── tests/
│   ├── test_kernel.py
│   ├── test_adapters.py
│   └── __init__.py
│
├── LICENSE
├── README.md
└── CHANGELOG.md
