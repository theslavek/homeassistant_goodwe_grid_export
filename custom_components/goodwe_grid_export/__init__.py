import logging

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

import goodwe
import asyncio
import goodwe

DOMAIN = "goodwe_grid_export"
_LOGGER = logging.getLogger(__name__)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    async def set_grid_export(call: ServiceCall):
        ip = call.data.get("ip")
        port = call.data.get("port")
        grid_export = call.data.get("grid_export")

        if grid_export not in (0, 1):
            _LOGGER.error(f"Supported grid_export value is only 0 or 1.")
            return 1

        try:
            inverter = await goodwe.connect(ip, port)
            await inverter.write_setting("grid_export", grid_export)
            _LOGGER.info(f"Grid export set to {grid_export} successfully.")
        except Exception as e:
            _LOGGER.error(f"Failed to set grid export to {grid_export}: {e}")

    hass.services.register(DOMAIN, "set_grid_export", set_grid_export)
    return True
