## Code the handlers to make the first tests pass

The next step is to implement the first two handlers so that the tests `swap_ui_only` and `swap_wrong_refund` pass.

### Code the `CHECK_ADDRESS` and `GET_PRINTABLE_AMOUNT` handlers and test with `swap_ui_only`

The test `swap_ui_only` stops before sending the `START_SIGNING_TRANSACTION` APDU. That means no coin signature takes place; the only handlers called are [`CHECK_ADDRESS`](../technical_information/coin_application_api/swap_handle_check_address.md) and [`GET_PRINTABLE_AMOUNT`](../technical_information/coin_application_api/swap_handle_get_printable_amount.md).

You can refer to the [sequence diagram](../technical_information/diagram.md) to better see what this test does.

You can use this test to validate that:

- `CHECK_ADDRESS` handler correctly recognizes the `valid_destination_1` address.
- `GET_PRINTABLE_AMOUNT` handler correctly formats the amount for display.

Don't forget to run ragger with the `--golden_run` option when creating or updating the snapshots.

### Test `swap_wrong_refund`

This test sends a refund address that does not belong to the device.

You can use this test to validate that `CHECK_ADDRESS` handler correctly rejects the `fake_refund` address.

## Code the `SIGN_TRANSACTION` handler and the UI bypass

You can now implement the [`SIGN_TRANSACTION`](../technical_information/coin_application_api/sign_transaction/index.md) handler.

You can also implement the UI bypass for the final transaction signature.

Please refer to the [UI bypass documentation](../technical_information/coin_application_api/sign_transaction/ui_bypass.md) carefully.

Please refer to the [Coin application error codes](../technical_information/coin_application_api/sign_transaction/error_codes.md) to learn how to handle a refusal of the final transaction.

All tests should now pass.
