Before proceeding with the SWAP integration, ensure that your application follows the steps below.

Although these steps may seem unrelated to the SWAP feature, they significantly simplify the integration process, to the point that no support is provided if you skip them.

You should use the [app-boilerplate](https://github.com/LedgerHQ/app-boilerplate) or [app-boilerplate-rust](https://github.com/LedgerHQ/app-boilerplate-rust) as an example. Depending on the date of your fork from the Boilerplate application, most of these steps may already be done.

## C applications

### Standard Makefile

In order to use the SWAP feature on C applications, your Makefile needs to use the [Standard Makefile](https://github.com/LedgerHQ/ledger-secure-sdk/blob/master/Makefile.standard_app).
Ensure that, like the [Boilerplate Makefile](https://github.com/LedgerHQ/app-boilerplate/blob/master/Makefile), your Makefile contains:
```Makefile
include $(BOLOS_SDK)/Makefile.standard_app
```

### Standard application files

In order to use the SWAP feature on C applications, your codebase must use the [Standard application format](https://github.com/LedgerHQ/ledger-secure-sdk/tree/master/lib_standard_app).

Ensure that, like the [Boilerplate Makefile](https://github.com/LedgerHQ/app-boilerplate/blob/master/Makefile), the `DISABLE_STANDARD_APP_FILES` is **not** set to `1`:

## C and Rust applications

### Split test structure

Ensure that your tests directory follows the structure below:
```sh
$> ls app-boilerplate/tests/
application_client/
README.md
standalone/
swap/
```

You can look at the Boilerplate (or Rust Boilerplate it's the same) [tests structure](https://github.com/LedgerHQ/app-boilerplate/blob/master/tests/).

--8<-- "docs/deps/app-boilerplate/tests/README.md"
