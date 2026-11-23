<!-- retrieval: {"source_ids":["public:commit:01bb88e61f9e5ba666d02a274da97e9b4075e71d","public:commit:0b5d56cccdd3440a82bf036ce69a0bc68ecf2710","public:commit:183cc29c981ae685e3d1a52653630dd28596aa98","public:commit:24ed88df7d64309630d8125b4875e4fa9facf059","public:commit:396345a6397b8eeff1079a470c136bd320648241","public:commit:4f392a0d119b979b8dc8885c4d127e7703834a55","public:commit:589bbb938296acad5176f3821e9387a26b3b8abb","public:commit:6221371622bf32842ea27821b12cf7885b933a60","public:commit:6f1bf0b809365567817779c3bfdc52673f5a3208","public:commit:75aa43f8842209c2b47d8bba754ea1e2fa50fb13","public:commit:7669ec98cfb6f0c83f90a292eb2dd58968ab35f6","public:commit:8ba0c4e85d6cf3cfd1f28374ec7e901bf30ea0f3","public:commit:9beada2e6fcfa58a73fb148cdcc8e5b209c61fa0","public:commit:a6ffa333b8d03bf9a8974c94da275ac2e9b9c32b","public:commit:b440a31bbd688b8ad6a2ad96aa35f403cc39221a","public:commit:cf78cd46d4db4240666f955496dec5ddabf05411","public:commit:d54dede957925a6a901da0240e0d4ba9fbb57b66","public:commit:da2dbff757b5b049f0e005625c89c3e7a371a97b","public:commit:daee0a89b98432c903cab887308660d8d1f9097a","public:commit:df59864bf6c268ff48b3ec973c805df61accefc4","public:commit:e6c954227100828b75a65893d4d0576ee26af972","public:commit:f1c81922ec248dc715125af0f7c9216e13f84085","public:commit:f78f736251fbf0c4b01d58ad7011ac717acc7fab"],"source_type":"public","date":"2024-01-31..2026-05-02","topics":["ffi","build","performance","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="remote-development-toolchain-consistency-shell-boundaries-and-host-key-portability"></a>
# Remote development: toolchain consistency, shell boundaries and host-key portability {#remote-development-toolchain-consistency-shell-boundaries-and-host-key-portability}

## Decision chain {#decision-chain}
The root-through-profile sequence (01–03) builds a reproducible-enough development baseline by selecting Python/Debian, LLVM, libc++, CMake, Conan and Ninja in one Dockerfile and carrying a matching Conan profile. The qualifier matters: initial Conan/pip floated, the image tag was not digest pinned, and CMake's x86_64 download limits architecture. Later compiler bumps (15→16, 16→20) briefly left Conan's recorded compiler version behind. Commits 16 and 21 repair those identities; a compiler executable and Conan settings are coupled inputs to package selection. The transition from Docker ENV to account .bashrc (13–14) changes environment scope, with user-local Python scripts on PATH. SSH and noninteractive tools cannot be assumed to see identical shell startup files.

The initial Compose setup directly binds host SSH material into the user directory and publishes SSH plus UDP 19132. In 22, a comprehensive hardening and maintenance pass replaces SSH binding with a named volume and ssh-copy-id onboarding, persists the Conan cache, validates sudo configuration, pins Conan, and brings docs up to date. Its build workflow is a two-stage hadolint→Buildx gate with layer cache and superseded-run cancellation. These checks concern image construction and linting, not successful remote IDE login or a functioning game server. The process-existence healthcheck is weaker than an SSH handshake or end-to-end developer smoke test.

Commit 23 deliberately reverses the named SSH volume approach. The message explains that Docker Desktop on Windows/macOS exposes mount modes OpenSSH rejects. It mounts host material elsewhere, copies it into the container filesystem, applies ownership/modes, skips host-specific config, then execs sshd. It also enforces LF endings to prevent Windows checkout line endings breaking shell scripts. This is a concrete portability mechanism with explicit costs: it exposes host private keys to any container compromise, and the published Compose port remains all-interface by default. The code comment promises regular-file copying, but the loop only checks existence; a directory can reach nonrecursive cp under set -e. Repeated starts do not remove keys deleted on the host. Those are static review cautions, not demonstrated incidents.

## How to use this evidence {#how-to-use-this-evidence}
When diagnosing a remote-development failure, separate four layers: image dependency availability, declared compiler/package identity, shell/session environment, and host-filesystem permission translation. Check the actual failure layer before adding broad privileges or broad key copying. For a new setup, verify least-privilege credentials and network binding rather than copying these historical defaults. The source's security warning is part of its design, not proof the default is safe.

## Provenance, alternatives and limits {#provenance-alternatives-and-limits}
The two late commits explicitly credit Claude Opus 4.7 (1M context). Preserve shared authorship. The intermediate named-volume plus public-key onboarding approach is a real examined alternative, not a hypothetical design. Runtime scripts, containers, CI and SSH were not executed. Credential-guard redactions are individually recorded; masked lines were neither reconstructed nor bypassed. The image OCI license label says Apache-2.0 while this repository's root license remains MIT, also corroborated by the organization license table. Treat that inconsistency as a packaging metadata review item, not a legal determination.

## Complete per-SHA navigation {#complete-per-sha-navigation}

- [01 daee0a89b984 — Initial commit](dossiers/01-daee0a89b98432c903cab887308660d8d1f9097a.md)
- [02 589bbb938296 — feat: add Dockerfile](dossiers/02-589bbb938296acad5176f3821e9387a26b3b8abb.md)
- [03 6f1bf0b80936 — feat: add conan profile](dossiers/03-6f1bf0b809365567817779c3bfdc52673f5a3208.md)
- [04 183cc29c981a — feat: add docker-compose.yml](dossiers/04-183cc29c981ae685e3d1a52653630dd28596aa98.md)
- [05 b440a31bbd68 — docs: update README.md](dossiers/05-b440a31bbd688b8ad6a2ad96aa35f403cc39221a.md)
- [06 f78f736251fb — docs: update README.md](dossiers/06-f78f736251fbf0c4b01d58ad7011ac717acc7fab.md)
- [07 d54dede95792 — refactor: rename files](dossiers/07-d54dede957925a6a901da0240e0d4ba9fbb57b66.md)
- [08 01bb88e61f9e — feat: create ci.yml](dossiers/08-01bb88e61f9e5ba666d02a274da97e9b4075e71d.md)
- [09 24ed88df7d64 — refactor: rename ci.yml to build.yml](dossiers/09-24ed88df7d64309630d8125b4875e4fa9facf059.md)
- [10 0b5d56cccdd3 — Update Dockerfile](dossiers/10-0b5d56cccdd3440a82bf036ce69a0bc68ecf2710.md)
- [11 7669ec98cfb6 — Add new port mapping to docker-compose.yml](dossiers/11-7669ec98cfb6f0c83f90a292eb2dd58968ab35f6.md)
- [12 da2dbff757b5 — Add build-essential package to Dockerfile](dossiers/12-da2dbff757b5b049f0e005625c89c3e7a371a97b.md)
- [13 df59864bf6c2 — feat: configure Clang as the default C++ and C compiler using environment variables](dossiers/13-df59864bf6c268ff48b3ec973c805df61accefc4.md)
- [14 6221371622bf — feat: set environment variables in .bashrc](dossiers/14-6221371622bf32842ea27821b12cf7885b933a60.md)
- [15 8ba0c4e85d6c — chore: update LLVM version to 16](dossiers/15-8ba0c4e85d6cf3cfd1f28374ec7e901bf30ea0f3.md)
- [16 396345a6397b — fix: conan profile](dossiers/16-396345a6397b8eeff1079a470c136bd320648241.md)
- [17 9beada2e6fcf — chore: update CMake to version 4.0.3](dossiers/17-9beada2e6fcfa58a73fb148cdcc8e5b209c61fa0.md)
- [18 e6c954227100 — feat: update base image to python:3.12-slim-bookworm](dossiers/18-e6c954227100828b75a65893d4d0576ee26af972.md)
- [19 cf78cd46d4db — chore: add clang-tools installation to Dockerfile](dossiers/19-cf78cd46d4db4240666f955496dec5ddabf05411.md)
- [20 4f392a0d119b — chore: update LLVM version to 20 in Dockerfile](dossiers/20-4f392a0d119b979b8dc8885c4d127e7703834a55.md)
- [21 a6ffa333b8d0 — chore: update LLVM to 20 and CMake to 4.2.3](dossiers/21-a6ffa333b8d03bf9a8974c94da275ac2e9b9c32b.md)
- [22 75aa43f88422 — chore: harden Dockerfile, modernize compose, refresh docs and CI](dossiers/22-75aa43f8842209c2b47d8bba754ea1e2fa50fb13.md)
- [23 f1c81922ec24 — feat: copy host SSH material via entrypoint with strict perms](dossiers/23-f1c81922ec248dc715125af0f7c9216e13f84085.md)
