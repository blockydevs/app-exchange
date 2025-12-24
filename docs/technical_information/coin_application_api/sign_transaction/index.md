To handle the `SIGN_TRANSACTION` command, the coin application must first copy the whitelisted
parameters validated in the Exchange application UI, then resume the normal boot process with the
following differences:

- No main menu UI must be displayed at startup flow
- Simple transactions matching the parameters given by Exchange must be signed without prompting
the UI a second time
- Simple transactions not matching the parameters given by Exchange must be rejected
- Complex transactions must be rejected
- Upon transaction signature / refusal, the Coin Application must return to Exchange with the
result code to let Exchange display the success / failure screen.
- Transactions rejected because they do not match the Exchange validated parameters must use
the common error code data.
