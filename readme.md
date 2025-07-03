# eDot Automation Testing Setup

This guide will help you set up your environment for running both web and mobile automation tests for the eDot project.

## 1. Install Python

Download and install Python 3.9 or later from [python.org](https://www.python.org/downloads/).

Verify installation:
```sh
python3 --version
```

## 2. Install Project Requirements

Install pip if not already installed, then install dependencies:
```sh
pip install -r requirements.txt
```

## 3. Set Up Android Emulator

- Install [Android Studio](https://developer.android.com/studio).
- Open Android Studio and go to **Tools > Device Manager**.
- Create a new virtual device (emulator) with your desired configuration (e.g., Pixel 4, Android 11).


## 4. Run the Emulator

Start the emulator from Android Studio or via terminal:
```sh
emulator -avd <your_emulator_name>
```

## 5. Install the App on the Emulator

You can install your APK using:
```sh
adb install /path/to/your/app.apk
```
Replace `/path/to/your/app.apk` with the actual path to your APK file.


## 6. Run Appium Server

Install Appium globally (if not already installed):
```sh
npm install -g appium
```

Start the Appium server:
```sh
appium
```
or for Appium 2.x:
```sh
appium server
```

## 7. Run the Tests

**Web Tests:**
```sh
pytest tests/web_tests
```
**Mobile Tests:**
```sh
pytest tests/mobile_tests
```

Or run both in sequence:
```sh
chmod +x run_all_tests.sh
./run_all_tests.sh
```

## Notes

- Make sure your emulator is running before starting Appium and running mobile tests.
- Update any configuration files (such as `config.py`) with your credentials or environment-specific values as needed.



