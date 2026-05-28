# Hidroelectrica Home Assistant - Open Local

Custom Home Assistant integration for Hidroelectrica Romania.

This repository contains a local open variant of the Hidroelectrica integration. It keeps the existing API integration flow and removes external license-server checks for local use.

## Features

- Hidroelectrica account setup through Home Assistant config flow.
- Sensors for bill status, balance, invoices, consumption, payments, meter indexes and self-reading window.
- Additional promoted sensors for numeric values such as balance, invoice total, current-month consumption and yearly totals.
- Button support for submitting meter readings where the account supports it.

## Installation

Copy the integration folder into Home Assistant:

```bash
mkdir -p /config/custom_components
cp -r custom_components/hidroelectrica /config/custom_components/
ha core restart
```

Or clone directly on a Home Assistant server:

```bash
cd /config
git clone https://github.com/YOUR_USER/hidroelectrica-ha-open-local.git /tmp/hidroelectrica-ha-open-local
cp -r /tmp/hidroelectrica-ha-open-local/custom_components/hidroelectrica /config/custom_components/
ha core restart
```

## HACS custom repository

After this repo is pushed to GitHub:

1. Open HACS.
2. Go to Integrations.
3. Open Custom repositories.
4. Add the GitHub repository URL.
5. Select category `Integration`.
6. Install and restart Home Assistant.

## Notes

- This is a custom integration and depends on Hidroelectrica/iHidro API behavior.
- Keep your Home Assistant secrets and credentials out of this repository.
- This fork is intended for personal/local Home Assistant use.

## License

MIT. This repository preserves the original integration attribution and license notice.
