"""Sensor platform for iaqualinkRobots integration — Enhanced with full API telemetry."""

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

ICON_MAP = {
    # === ORIGINAL SENSORS ===
    "serial_number":       "mdi:barcode",
    "device_type":         "mdi:robot",
    "cycle_start_time":    "mdi:clock-start",
    "cycle_duration":      "mdi:timer-sand",
    "cycle":               "mdi:format-list-numbered",
    "battery_level":       "mdi:battery",
    "total_hours":         "mdi:timer",
    "canister":            "mdi:recycle",
    "error_state":         "mdi:alert-circle",
    "temperature":         "mdi:thermometer",
    "time_remaining_human":"mdi:clock-outline",
    "time_remaining":      "mdi:timer",
    "estimated_end_time":  "mdi:calendar-clock",
    "model":               "mdi:information-outline",
    "fan_speed":           "mdi:fan",
    "activity":            "mdi:robot-vacuum",
    "status":              "mdi:connection",
    "stepper":             "mdi:stairs",
    "stepper_adj_time":    "mdi:timer-plus",
    "base_cycle_duration": "mdi:timer-sand",
    "stepper_adjustment_minutes": "mdi:timer-plus-outline",
    "adjusted_cycle_duration": "mdi:timer",
    # === EBOX DATA (Hardware) ===
    "ebox_control_box_sn": "mdi:chip",
    "ebox_cleaner_sn":     "mdi:identifier",
    "ebox_power_supply_sn":"mdi:power-plug",
    "ebox_sensor_block_sn":"mdi:memory",
    "ebox_motor_block_sn": "mdi:engine",
    "ebox_control_box_pn": "mdi:barcode-scan",
    "ebox_cleaner_pn":     "mdi:barcode-scan",
    "robot_firmware":      "mdi:update",
    # === CYCLE DURATIONS ===
    "duration_water":      "mdi:waves",
    "duration_quick":      "mdi:lightning-bolt",
    "duration_smart":      "mdi:brain",
    "duration_deep":       "mdi:broom",
    "duration_custom":     "mdi:tune",
    "duration_first_smart":"mdi:numeric-1-circle",
    # === SCHEDULE ===
    "schedule_mon_enabled":"mdi:calendar-check",
    "schedule_mon_program":"mdi:playlist-play",
    "schedule_mon_time":   "mdi:clock-outline",
    "schedule_tue_enabled":"mdi:calendar-check",
    "schedule_tue_program":"mdi:playlist-play",
    "schedule_tue_time":   "mdi:clock-outline",
    "schedule_wed_enabled":"mdi:calendar-check",
    "schedule_wed_program":"mdi:playlist-play",
    "schedule_wed_time":   "mdi:clock-outline",
    "schedule_thu_enabled":"mdi:calendar-check",
    "schedule_thu_program":"mdi:playlist-play",
    "schedule_thu_time":   "mdi:clock-outline",
    "schedule_fri_enabled":"mdi:calendar-check",
    "schedule_fri_program":"mdi:playlist-play",
    "schedule_fri_time":   "mdi:clock-outline",
    "schedule_sat_enabled":"mdi:calendar-check",
    "schedule_sat_program":"mdi:playlist-play",
    "schedule_sat_time":   "mdi:clock-outline",
    "schedule_sun_enabled":"mdi:calendar-check",
    "schedule_sun_program":"mdi:playlist-play",
    "schedule_sun_time":   "mdi:clock-outline",
    # === HARDWARE SENSORS (from shadow) ===
    "pressure_sensor_state":"mdi:gauge",
    "compass_sensor_state": "mdi:compass",
    "error_code":           "mdi:alert-circle-outline",
    "internal_temp":        "mdi:thermometer-alert",
}

# Unit of measurement map
UNIT_MAP = {
    "battery_level":       "%",
    "total_hours":         "h",
    "canister":            "%",
    "temperature":         "°C",
    "cycle_duration":      "min",
    "time_remaining":      "min",
    "time_remaining_human": None,
    "stepper_adj_time":    "min",
    "base_cycle_duration": "min",
    "stepper_adjustment_minutes": "min",
    "adjusted_cycle_duration": "min",
    # Cycle durations
    "duration_water":      "min",
    "duration_quick":      "min",
    "duration_smart":      "min",
    "duration_deep":       "min",
    "duration_custom":     "min",
    "duration_first_smart":"min",
    # Hardware sensors
    "internal_temp":       "°C",
}

# Device class map for HA native device classes
DEVICE_CLASS_MAP = {
    "temperature":         SensorDeviceClass.TEMPERATURE,
    "internal_temp":       SensorDeviceClass.TEMPERATURE,
}

# State class for entities that track numeric measurement values
STATE_CLASS_MAP = {
    "total_hours":         SensorStateClass.TOTAL_INCREASING,
    "temperature":         SensorStateClass.MEASUREMENT,
    "internal_temp":       SensorStateClass.MEASUREMENT,
}

# All possible sensors — grouped by category
ALL_SENSOR_TYPES = [
    # --- Core sensors (original) ---
    ("serial_number",       "Serial Number"),
    ("device_type",         "Device Type"),
    ("cycle_start_time",    "Cycle Start Time"),
    ("cycle_duration",      "Cycle Duration"),
    ("cycle",               "Cycle"),
    ("battery_level",       "Battery Level"),
    ("total_hours",         "Total Hours"),
    ("canister",            "Canister Level"),
    ("error_state",         "Error State"),
    ("temperature",         "Temperature"),
    ("time_remaining_human","Time Remaining"),
    ("time_remaining",      "Time Remaining (Minutes)"),
    ("estimated_end_time",  "Estimated End Time"),
    ("model",               "Model"),
    ("fan_speed",           "Fan Speed"),
    ("activity",            "Activity"),
    ("status",              "Status"),
    ("stepper",             "Time Adjustments"),
    ("stepper_adj_time",    "Adjustment Increment"),
    ("base_cycle_duration", "Original Duration"),
    ("stepper_adjustment_minutes", "Time Added/Removed"),
    ("adjusted_cycle_duration", "Total Duration"),
    # --- Hardware (eboxData) ---
    ("ebox_control_box_sn", "Control Box Serial"),
    ("ebox_cleaner_sn",     "Cleaner Serial"),
    ("ebox_power_supply_sn","Power Supply Serial"),
    ("ebox_sensor_block_sn","Sensor Block Serial"),
    ("ebox_motor_block_sn", "Motor Block Serial"),
    ("ebox_control_box_pn", "Control Box Part No."),
    ("ebox_cleaner_pn",     "Cleaner Part No."),
    ("robot_firmware",      "Robot Firmware"),
    # --- Cycle Durations (configured timers) ---
    ("duration_water",      "Duration: Waterline"),
    ("duration_quick",      "Duration: Quick"),
    ("duration_smart",      "Duration: Smart"),
    ("duration_deep",       "Duration: Deep"),
    ("duration_custom",     "Duration: Custom"),
    ("duration_first_smart","Duration: First Smart"),
    # --- Weekly Schedule ---
    ("schedule_mon_enabled","Schedule Mon Enabled"),
    ("schedule_mon_program","Schedule Mon Program"),
    ("schedule_mon_time",   "Schedule Mon Time"),
    ("schedule_tue_enabled","Schedule Tue Enabled"),
    ("schedule_tue_program","Schedule Tue Program"),
    ("schedule_tue_time",   "Schedule Tue Time"),
    ("schedule_wed_enabled","Schedule Wed Enabled"),
    ("schedule_wed_program","Schedule Wed Program"),
    ("schedule_wed_time",   "Schedule Wed Time"),
    ("schedule_thu_enabled","Schedule Thu Enabled"),
    ("schedule_thu_program","Schedule Thu Program"),
    ("schedule_thu_time",   "Schedule Thu Time"),
    ("schedule_fri_enabled","Schedule Fri Enabled"),
    ("schedule_fri_program","Schedule Fri Program"),
    ("schedule_fri_time",   "Schedule Fri Time"),
    ("schedule_sat_enabled","Schedule Sat Enabled"),
    ("schedule_sat_program","Schedule Sat Program"),
    ("schedule_sat_time",   "Schedule Sat Time"),
    ("schedule_sun_enabled","Schedule Sun Enabled"),
    ("schedule_sun_program","Schedule Sun Program"),
    ("schedule_sun_time",   "Schedule Sun Time"),
    # --- Hardware Sensors (from device shadow) ---
    ("pressure_sensor_state","Pressure Sensor"),
    ("compass_sensor_state", "Compass Sensor"),
    ("error_code",           "Error Code"),
    ("internal_temp",        "Internal Temperature"),
]

# Sensors only available for VR/Vortrax robots
VR_ONLY_SENSORS = {
    "ebox_control_box_sn", "ebox_cleaner_sn", "ebox_power_supply_sn",
    "ebox_sensor_block_sn", "ebox_motor_block_sn", "ebox_control_box_pn",
    "ebox_cleaner_pn", "robot_firmware",
    "duration_water", "duration_quick", "duration_smart",
    "duration_deep", "duration_custom", "duration_first_smart",
    "schedule_mon_enabled", "schedule_mon_program", "schedule_mon_time",
    "schedule_tue_enabled", "schedule_tue_program", "schedule_tue_time",
    "schedule_wed_enabled", "schedule_wed_program", "schedule_wed_time",
    "schedule_thu_enabled", "schedule_thu_program", "schedule_thu_time",
    "schedule_fri_enabled", "schedule_fri_program", "schedule_fri_time",
    "schedule_sat_enabled", "schedule_sat_program", "schedule_sat_time",
    "schedule_sun_enabled", "schedule_sun_program", "schedule_sun_time",
    "pressure_sensor_state", "compass_sensor_state",
    "error_code", "internal_temp",
}


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensors for an entry, filtering based on robot type."""
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]
    client = data["client"]

    device_type = client._device_type
    
    if device_type == "cyclobat":
        # Include all original sensors for cyclobat (no VR-only telemetry)
        sensor_types = [
            (key, name) for key, name in ALL_SENSOR_TYPES
            if key not in VR_ONLY_SENSORS
        ]
    elif device_type == "i2d_robot":
        # Exclude specified sensors for i2d robots
        excluded_sensors = {"cycle_duration", "cycle_start_time", "model", "temperature", "battery_level"}
        excluded_sensors.update(VR_ONLY_SENSORS)
        sensor_types = [
            (key, name) for key, name in ALL_SENSOR_TYPES
            if key not in excluded_sensors
        ]
    elif device_type in ("vr", "vortrax"):
        # VR and Vortrax get ALL sensors including telemetry
        sensor_types = [
            (key, name) for key, name in ALL_SENSOR_TYPES
            if key != "battery_level"
        ]
    else:
        # For other types, exclude battery and VR-only telemetry
        sensor_types = [
            (key, name) for key, name in ALL_SENSOR_TYPES
            if key != "battery_level" and key not in VR_ONLY_SENSORS
        ]

    entities = [
        AqualinkSensor(coordinator, client, key, name)
        for key, name in sensor_types
    ]
    async_add_entities(entities)


class AqualinkSensor(CoordinatorEntity, SensorEntity):
    """Representation of a sensor tied to the vacuum data coordinator."""

    def __init__(self, coordinator, client, key, name):
        super().__init__(coordinator)
        self.coordinator = coordinator
        self.client = client
        self._key = key
        self._last_value = None

        self._attr_unique_id = f"{client.robot_id}_{key}"
        self._attr_icon = ICON_MAP.get(key)
        self._attr_should_poll = False
        
        # Set unit if defined
        unit = UNIT_MAP.get(key)
        if unit:
            self._attr_native_unit_of_measurement = unit
        
        # Set device class if defined
        device_class = DEVICE_CLASS_MAP.get(key)
        if device_class:
            self._attr_device_class = device_class
            
        # Set state class if defined
        state_class = STATE_CLASS_MAP.get(key)
        if state_class:
            self._attr_state_class = state_class
        
        # Set translation key for entity name
        self._attr_translation_key = key
        self._attr_has_entity_name = True

    @property
    def native_value(self):
        """Return the current value with resilient handling."""
        if self.coordinator.data:
            error_state = self.coordinator.data.get("error_state")
            if error_state in ["no_data", "update_failed", "setup_cancelled", "connection_failed"]:
                cached_value = getattr(self, '_last_value', None)
                if cached_value is not None:
                    return cached_value
            
            current_value = self.coordinator.data.get(self._key)
            
            # Handle value translation for display
            if self._key == "fan_speed" and current_value:
                fan_speed_display_map = {
                    "floor_only": "Floor only",
                    "wall_only": "Wall only", 
                    "walls_only": "Walls only",
                    "floor_and_walls": "Floor and walls",
                    "smart_floor_and_walls": "SMART Floor and walls"
                }
                current_value = fan_speed_display_map.get(current_value, current_value)
            
            elif self._key == "activity" and current_value:
                activity_display_map = {
                    "cleaning": "Cleaning",
                    "error": "Error",
                    "idle": "Idle",
                    "returning": "Returning",
                    "docking": "Docking",
                    "paused": "Paused"
                }
                current_value = activity_display_map.get(current_value, current_value)
            
            elif self._key == "status" and current_value:
                status_display_map = {
                    "connected": "Connected",
                    "disconnected": "Disconnected",
                    "offline": "Offline",
                    "online": "Online"
                }
                current_value = status_display_map.get(current_value, current_value)
            
            if current_value is not None and current_value != "unknown":
                self._last_value = current_value
                return current_value
            else:
                cached_value = getattr(self, '_last_value', None)
                if cached_value is not None:
                    return cached_value
                return current_value
        else:
            return getattr(self, '_last_value', None)

    @property
    def available(self):
        """Keep sensors available as long as we have data."""
        return self.coordinator.data is not None

    @property
    def device_info(self):
        model = "Unknown"
        if self.coordinator.data:
            model = self.coordinator.data.get("model", "Unknown")
            
        return {
            "identifiers": {(DOMAIN, self.client.robot_id)},
            "name": getattr(self.coordinator, "_title", self.client.robot_id),
            "manufacturer": "Zodiac",
            "model": model,
        }

    @property
    def entity_category(self):
        """Set entity category for diagnostic sensors."""
        from homeassistant.helpers.entity import EntityCategory
        # Hardware info and firmware are diagnostic
        if self._key.startswith("ebox_") or self._key.endswith("_firmware"):
            return EntityCategory.DIAGNOSTIC
        # Schedule info is configuration
        if self._key.startswith("schedule_"):
            return EntityCategory.DIAGNOSTIC
        return None
