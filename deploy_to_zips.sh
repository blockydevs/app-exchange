#!/bin/bash
# This script is used to pack builded bin's and debug files into zip files
# for each device.
# It assumes that the build process has already been completed and the
# necessary files are present in the specified directories.
rm -rf zips
mkdir -p zips
# List of devices

apt-get update
apt-get install -y zip

declare -A SDK_ENVS=(
  [nanosp]="NANOSP_SDK"
  [nanox]="NANOX_SDK"
  [flex]="FLEX_SDK"
  [stax]="STAX_SDK"
)


DEVICES=("nanosp" "nanox" "flex" "stax")
# List of directories for each device
for device in "${DEVICES[@]}"; do
    sdk_env="${SDK_ENVS[$device]}"
    sdk_path="${!sdk_env}"

    if [[ -z "$sdk_path" ]]; then
        echo "Environment variable $sdk_env is not set. Skipping build for $device."
        continue
    fi

    echo "Building for $device using SDK: $sdk_path"
    BOLOS_SDK="$sdk_path" make DEBUG=1

    # Create a zip file for the device
    zip_file="${device}_build.zip"
    echo "Creating zip file: $zip_file"
    mkdir -p "zips/$device"
    cp "bin/app.elf" "bin/app.apdu" "bin/app.hex" "bin/app.sha256" "debug/app.map" "debug/app.asm" "zips/$device/"
    cd "zips/$device" || exit 1
    zip -r "$zip_file" "app.elf" "app.apdu" "app.hex" "app.sha256" "app.map" "app.asm"
    cd - || exit 1
    cp "zips/$device/$zip_file" "zips/"
    # Clean up the temporary directory
    rm -rf "zips/$device"
    # Check if the zip file was created successfully
    if [[ $? -ne 0 ]]; then
        echo "Failed to create zip file for $device."
        exit 1
    fi
    echo "Zip file for $device created successfully: $zip_file"
done

chmod -R 777 zips