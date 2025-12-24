--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/swap_entrypoints.h:swap_entry_point_intro"

[`ledger-secure-sdk/lib_standard_app/main.c`](https://github.com/LedgerHQ/ledger-secure-sdk/tree/master/lib_standard_app/main.c)
```C
--8<-- "docs/deps/ledger-secure-sdk/lib_standard_app/main.c:library_app_main"
```

## Rust applications
For Rust applications, the Coin application must handle the command dispatch (the same way the lib_standard_app does in C).

<!-- --8<-- "docs/deps/app-boilerplate-rust/src/main.rs:main_entry_point_intro" -->

[`app-boilerplate-rust/src/main.rs`](https://github.com/LedgerHQ/app-boilerplate-rust/tree/master/src/main.rs)
```Rust
--8<-- "docs/deps/app-boilerplate-rust/src/main.rs:sample_main"
```

[`app-boilerplate-rust/src/swap.rs`](https://github.com/LedgerHQ/app-boilerplate-rust/tree/master/src/swap.rs)
```Rust
--8<-- "docs/deps/app-boilerplate-rust/src/swap.rs:swap_main"
```
