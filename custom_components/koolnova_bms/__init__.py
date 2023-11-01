"""The koolnova BMS modbus integration."""  # pylint: disable=invalid-name

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType

from homeassistant.const import CONF_HOST, CONF_PORT, CONF_NAME, CONF_DEVICE_ID

from .const import DOMAIN
#from .wfrac.device import Device

_LOGGER = logging.getLogger(__name__)

COMPONENT_TYPES = ["sensor", "climate", "select"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """ Set up koolnova from a config entry. """

    _LOGGER.info('async_setup_entry')
#    if DOMAIN not in hass.data:
#        hass.data[DOMAIN] = []
#
#    device: str = entry.data[CONF_HOST]
#    name: str = entry.data[CONF_NAME]
#    device_id: str = entry.data[CONF_DEVICE_ID]
#    operator_id: str = entry.data[CONF_OPERATOR_ID]
#    port: int = entry.data[CONF_PORT]
#    airco_id: str = entry.data[CONF_AIRCO_ID]

#    try:
#        api = Device(hass, name, device, port, device_id, operator_id, airco_id)
#        await api.update()  # initial update to get fresh values
#        hass.data[DOMAIN].append(api)
#    except Exception as ex:  # pylint: disable=broad-except
#        _LOGGER.warning("Something whent wrong setting up device [%s] %s", device, ex)
#
#    for component in COMPONENT_TYPES:
#        hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, component))
#
#    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    _LOGGER.info('async_unload_entry')
#    if unloaded := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
#        hass.data[DOMAIN].pop(entry.entry_id)
#    return unloaded

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    _LOGGER.info('async_reload_entry')
#    await async_unload_entry(hass, entry)
#    await async_setup_entry(hass, entry)

async def async_remove_entry(hass, entry: ConfigEntry) -> None:
    """Handle removal of an entry."""
    _LOGGER.info('async_remove_entry')
#    for device in hass.data[DOMAIN]:
#        temp_device: Device = device
#        if temp_device.host == entry.data[CONF_HOST]:
#            try:
#                await temp_device.delete_account()
#                _LOGGER.info(
#                        "Deleted operator ID [%s] from airco [%s]",
#                        temp_device.operator_id,
#                        temp_device.airco_id,
#                        )
#                hass.data[DOMAIN].remove(temp_device)
#            except Exception as ex:  # pylint: disable=broad-except
#                _LOGGER.warning(
#                        "Something whent wrong deleting account from airco [%s] %s",
#                        temp_device.name,
#                        ex,
#                        )