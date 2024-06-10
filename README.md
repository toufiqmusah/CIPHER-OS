# CIPHER-OS: Pi-Pico Weather Station + ML Predictions

## Overview
CIPHER-OS is a microcontroller-based weather station that utilizes a Raspberry Pi Pico and MicroPython to collect environmental data such as temperature and humidity. This project not only monitors real-time environmental conditions, and also employs a simple linear regression model to predict future weather trends.

## Hardware Requirements
- **Raspberry Pi Pico**: The core microcontroller for data collection and processing.
- **DHT11 Sensor**: Used for measuring temperature and moisture content in the air.

## Software Requirements
- **MicroPython**
- **LR Module**: Found in this repo.

## Usage
- **Data Collection**: The device collects temperature and humidity data at predefined intervals.
- **Data Prediction**:
  - The collected data is used to train a linear regression model.
  - The model predicts future environmental conditions based on historical data.

## Contributing
Feel free to fork this project and contribute to its development. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Potato code, by the way.

## License
[MIT License](LICENSE.txt)

## Authors
- Toufiq – https://github.com/toufiqmusah
- Federal - https://github.com/Federal-Sedinam

## Acknowledgments
- PicoML - https://www.youtube.com/watch?v=9JeTxW0rgHI
- https://github.com/charlie2951/ML_micropython
