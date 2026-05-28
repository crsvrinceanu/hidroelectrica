"""Local open license shim for the Hidroelectrica integration.

This keeps the integration's existing runtime hooks intact while removing
external license-server checks from this local fork.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

INTEGRATION = "hidroelectrica"
LICENSE_API_URL = ""


class LicenseManager:
    """Compatibility manager that always permits local use."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self._data: dict[str, Any] = {}
        self._status_token: dict[str, Any] = {
            "status": "licensed",
            "valid_until": 0,
            "trial_days_remaining": 0,
        }

    async def async_load(self) -> None:
        """Initialize the local license state."""
        _LOGGER.debug("[Hidroelectrica:License] Local open mode enabled")

    async def async_activate(self, key: str) -> dict[str, Any]:
        """Accept activation attempts without contacting a license server."""
        return {"success": True, "status": "licensed"}

    async def async_check_status(self) -> dict[str, Any]:
        """Return the local status."""
        return {"success": True, "status": "licensed"}

    async def async_heartbeat(self) -> dict[str, Any]:
        """No-op heartbeat kept for compatibility with existing setup code."""
        return await self.async_check_status()

    async def async_notify_event(self, action: str) -> None:
        """Do not send lifecycle telemetry in local open mode."""
        _LOGGER.debug("[Hidroelectrica:License] Ignored lifecycle event: %s", action)

    async def _async_reload_entries(self) -> None:
        """Compatibility no-op; status never changes in local open mode."""

    @property
    def fingerprint(self) -> str:
        """Return an empty fingerprint so removal hooks skip remote notify."""
        return ""

    @property
    def status(self) -> str:
        return "licensed"

    @property
    def is_valid(self) -> bool:
        return True

    @property
    def is_trial_valid(self) -> bool:
        return False

    @property
    def trial_days_remaining(self) -> int:
        return 0

    @property
    def license_type(self) -> str:
        return "open-local"

    @property
    def license_key_masked(self) -> str:
        return ""

    @property
    def activated_at(self) -> datetime | None:
        return None

    @property
    def license_expires_at(self) -> datetime | None:
        return None

    @property
    def check_interval_seconds(self) -> int:
        return 24 * 60 * 60

    @property
    def needs_heartbeat(self) -> bool:
        return False
