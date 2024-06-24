# homeassistant_goodwe_grid_export

## TL;DR;
Custom component for enabling/disabling grid_export parameter on a GoodWe inverter.

## Installation

1. Copy the custom_components/goodwe_grid_export directory to the custom_components directory in your Home Assistant configuration directory.

2. Add the custom component to your Home Assistant `configuration.yaml`:
    ```commandline
    goodwe_grid_export:
    ```

3. Restart Home Assistant to load the new component.

4. Use the Home Assistant services UI to call `goodwe_grid_export.set_grid_export` with the necessary parameters (ip, port, limit).

## Example Automation
```commandline
alias: "FVE - turn off grid export"
description: ""
trigger:
  - platform: time
    at: "18:00:00"
condition: []
action:
  - service: goodwe_grid_export.set_grid_export
    data:
      ip: 192.168.1.10
      port: 8899
      grid_export: 0
```
