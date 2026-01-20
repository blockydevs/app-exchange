## C SDK API

[`ledger-secure-sdk/lib_standard_app/swap_entrypoints.h`](https://github.com/LedgerHQ/ledger-secure-sdk/tree/master/lib_standard_app/swap_entrypoints.h)
```C
--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/swap_entrypoints.h:swap_copy_transaction_parameters"
```

[`ledger-secure-sdk/lib_standard_app/swap_lib_calls.h`](https://github.com/LedgerHQ/ledger-secure-sdk/tree/master/lib_standard_app/swap_lib_calls.h)
```C
--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/swap_lib_calls.h:create_transaction_parameters_t"
```

---

## Example of handle implementation in C Boilerplate

[`app-boilerplate/src/swap/handle_swap_sign_transaction.c`](https://github.com/LedgerHQ/app-boilerplate/blob/master/src/swap/handle_swap_sign_transaction.c)
```C
--8<-- "docs/deps/app-boilerplate/src/swap/handle_swap_sign_transaction.c:swap_copy_transaction_parameters"
```

---

## Rust SDK API

[`ledger-device-rust-sdk/ledger_device_sdk/src/libcall/swap.rs`](https://github.com/LedgerHQ/ledger-device-rust-sdk/tree/master/ledger_device_sdk/src/libcall/swap.rs)
```Rust
--8<-- "docs/deps/ledger-device-rust-sdk/ledger_device_sdk/src/libcall/swap.rs:sign_tx_params"



--8<-- "docs/deps/ledger-device-rust-sdk/ledger_device_sdk/src/libcall/swap.rs:CreateTxParams"
```

---

## Implementation in Rust Boilerplate

Unlike the C SDK where the Coin application defines the copy parameter callback, the Rust SDK directly exposes this function that returns a usable `CreateTxParams` struct.

As such its usage is a straightforward oneliner in the swap_main function.
