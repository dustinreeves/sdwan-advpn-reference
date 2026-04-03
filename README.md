# Ansible Jinja Templates for SD-WAN/ADVPN

This repository provides Jinja-based FortiGate CLI templates and an **Ansible-native** renderer.
It is focused on building and validating SD-WAN/ADVPN configurations directly from project data,
without external management platform dependencies.

## Routing Design Flavors

Two design flavors are provided:

- **BGP per Overlay** (`bgp-per-overlay/`)
- **BGP on Loopback** (`bgp-on-loopback/`)

Each flavor contains equivalent structure and template stages.

## Repository Structure

Within each flavor directory:

- `??-Edge-*.j2`, `??-Hub-*.j2` — core underlay/overlay/routing templates.
- `projects/Project*.j2` — project-level data model template(s).
- `projects/inventory.json` — per-device variables and device grouping.
- `optional/*.j2` — optional security and SD-WAN templates.
- `pre-run/*.j2` — bootstrap templates for platform-specific first-time setup.
- `rendered/` — sample rendered outputs.

Renderer assets:

- `ansible/render_config.yml` — main Ansible playbook.
- `ansible/render_device_group.yml` — group rendering workflow.
- `ansible/render_single_device.yml` — per-device rendering workflow.

## Prerequisites

- Ansible (2.12+ recommended)
- `ansible.utils` collection (for `ipaddr` Jinja filter used by templates)

Install collection if needed:

```bash
ansible-galaxy collection install ansible.utils
```

## Rendering with Ansible

Basic usage:

```bash
ansible-playbook ansible/render_config.yml -e flavor=bgp-on-loopback
```

Full parameterized usage:

```bash
ansible-playbook ansible/render_config.yml \
  -e flavor=<flavor_dir> \
  -e inventory=<inventory_file> \
  -e project=<project_template> \
  -e outdir=<output_dir> \
  -e skip_optional=true
```

Defaults:

- `inventory`: `<flavor>/projects/inventory.json`
- `project`: `<flavor>/projects/Project.j2`
- `outdir`: `out`
- `skip_optional`: `false`

## Project Customization Workflow

1. Pick one flavor (`bgp-on-loopback` or `bgp-per-overlay`).
2. Edit the project template (`projects/Project.j2` or `Project.nocert.j2`).
3. Populate per-device variables in `projects/inventory.json`.
4. Run the Ansible renderer.
5. Validate rendered output under your selected output directory.

## Project Template Reference

Detailed parameter documentation is in:

- [`Project_Template_Reference.md`](./Project_Template_Reference.md)

## Example Topology

All provided samples refer to:

![](example_project.png)
