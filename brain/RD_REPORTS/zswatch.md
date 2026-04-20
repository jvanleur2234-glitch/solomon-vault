# R&D Report: ZSWatch — Open Source Smartwatch

**Repo:** github.com/ZSWatch/ZSWatch
**Stars:** 3.2K | **License:** GPL-3.0 | **Lang:** C (97.7%)

## What It Is
ZSWatch is a complete open-source smartwatch built from scratch — both hardware AND firmware. Built on Zephyr RTOS.

## Hardware Specs
- **Chip:** Nordic nRF5340 (128 MHz dual-core, 512KB RAM, 1MB flash)
- **Display:** 240x240 round IPS touchscreen, 1.28"
- **Sensors:** IMU (BMI270), pressure (BMP581), magnetometer, light, microphone
- **Extras:** 64MB external flash, BLE, USB-C
- **Dev Kit:** WatchDK ($99) — same chip/sensors in larger form factor for dev

## Why It Fits Be Like You! OS
- Hardware designs are open (KiCad PCB files)
- Runs Zephyr RTOS — same OS layer that could host Solomon OS agents
- BLE communication → could pair with Solomon Air for phone-free connectivity
- App framework is extensible → Solomon Skills as watch apps
- Health sensors → continuous biometric data for AI personalization

## Link Fit
★★★★★ — #wearables #hardware #solomon-air #future

## Forked
Local at /home/workspace/ZSWatch/ (direct clone after fork timeout)
