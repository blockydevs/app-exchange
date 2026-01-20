## Enable the SWAP feature

For Rust applications, SWAP support needs to be enabled in your application's entry point, as Rust applications handle their own command dispatch (unlike C applications where `lib_standard_app` handles this automatically).

## Add SWAP entry points in main.rs

You will need to:

- Split the application boot flow to handle different start modes (Exchange or Dashboard)
- Dispatch SWAP commands to the handler when in Exchange mode

Please refer to the [`app-boilerplate-rust/src/main.rs`](https://github.com/LedgerHQ/app-boilerplate-rust/tree/master/src/main.rs) for an example of the boot flow split.

Please also refer to the Rust [entry point documentation](../../technical_information/coin_application_api/entry_point.md) for detailed code examples.

## Add stub SWAP handlers

For now, we will implement the handlers in the simplest possible way (yesmen handlers that accept everything).

Add the following file to your application (it is recommended to follow the Boilerplate file structure):
```sh
$> ls app-boilerplate-rust/src/
main.rs  swap.rs  ...
```

In your `swap.rs` file, you should have a `swap_main()` function that dispatches to the three handler functions. For more information about what the handlers do, refer to the [handler documentation](../../technical_information/coin_application_api/index.md).
