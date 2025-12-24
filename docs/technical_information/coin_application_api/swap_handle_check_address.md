# CHECK_ADDRESS

--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/swap_entrypoints.h:swap_handle_check_address_brief"

---

## C SDK API

[`ledger-secure-sdk/lib_standard_app/swap_entrypoints.h`](https://github.com/LedgerHQ/ledger-secure-sdk/tree/master/lib_standard_app/swap_entrypoints.h)
```C
--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/swap_entrypoints.h:swap_handle_check_address"
```

[`ledger-secure-sdk/lib_standard_app/swap_lib_calls.h`](https://github.com/LedgerHQ/ledger-secure-sdk/tree/master/lib_standard_app/swap_lib_calls.h)
```C
--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/swap_lib_calls.h:check_address_parameters_t"
```

## Example of handle implementation in C Boilerplate

[`app-boilerplate/src/swap/handle_check_address.c`](https://github.com/LedgerHQ/app-boilerplate/blob/master/src/swap/handle_check_address.c)
```C
--8<-- "docs/deps/app-boilerplate/src/swap/handle_check_address.c"
```

---

## Rust SDK API

[`ledger-device-rust-sdk/ledger_device_sdk/src/libcall/swap.rs`](https://github.com/LedgerHQ/ledger-device-rust-sdk/tree/master/ledger_device_sdk/src/libcall/swap.rs)
```Rust
--8<-- "docs/deps/ledger-device-rust-sdk/ledger_device_sdk/src/libcall/swap.rs:get_check_address_params"



--8<-- "docs/deps/ledger-device-rust-sdk/ledger_device_sdk/src/libcall/swap.rs:CheckAddressParams"
```

---

## Example of handle implementation in Rust Boilerplate

[`app-boilerplate-rust/src/swap.rs`](https://github.com/LedgerHQ/app-boilerplate-rust/tree/master/src/swap.rs)
```Rust
--8<-- "docs/deps/app-boilerplate-rust/src/swap.rs:check_address"
```
