# SysDiagX - System Diagnostic Toolkit

**Version:** 2.3.1  
**Last Updated:** May 2025  
**Maintainer:** Core Systems Team – Internal Ops

## Overview

**SysDiagX** is a lightweight cross-platform CLI utility developed for internal use to collect, analyze, and report system-level diagnostics. It supports various UNIX-like systems and is primarily intended for use by DevOps and Infrastructure Engineers.

> 📌 Note: This package is precompiled and bundled with configuration assets. Do **not** modify internal files unless explicitly instructed by the Core Systems Team.

---

## Features

- Collects memory, disk, and CPU usage snapshots
- Aggregates network interface stats and connection logs
- Parses and formats syslog and journal entries for auditing
- Supports offline diagnostics for air-gapped servers
- Compresses diagnostic bundles for secure transmission

---

## Installation

> This is a binary-only distribution. No external dependencies required.

### Linux/macOS:

```bash
tar -xzf sysdiagx-v2.3.1.tar.gz
cd sysdiagx
chmod +x sysdiagx
./sysdiagx --help
