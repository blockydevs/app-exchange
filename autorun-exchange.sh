@ -0,0 +1,42 @@
#!/bin/bash

if [[ "$1" == "setup" ]]; then
  pip install -r test/python/requirements.txt --break-system-packages
fi

# Map devices to environment variable names for SDKs
declare -A SDK_ENVS=(
  [nanosp]="NANOSP_SDK"
  [nanox]="NANOX_SDK"
  [flex]="FLEX_SDK"
  [stax]="STAX_SDK"
)

# List of Ledger devices
DEVICES=("flex" "stax")

#make clean
if [[ "$1" != "test" ]]; then
  # Build for each device
  for device in "${DEVICES[@]}"; do
    sdk_env="${SDK_ENVS[$device]}"
    sdk_path="${!sdk_env}"

    if [[ -z "$sdk_path" ]]; then
      echo "Environment variable $sdk_env is not set. Skipping build for $device."
      continue
    fi

    echo "Building for $device using SDK: $sdk_path"
    BOLOS_SDK="$sdk_path" make DEBUG=1 TEST_PUBLIC_KEY=1 -j8 || exit 1
    #cp ../app-hedera/build/$device/bin/app.elf test/python/lib_binaries/hedera_$device.elf
  done
fi

echo > log.log
# Run tests for each device
for device in "${DEVICES[@]}"; do
  echo "=================================================================================================================================="
  echo "Running tests for $device..."
  pytest --tb=short -v --device "$device" -k "test_hedera"  --golden_run -s 2>>log.log
done