import pytest
from .apps.exchange_test_runner import ExchangeTestRunner, ALL_TESTS_EXCEPT_MEMO_AND_FEES, ALL_TESTS_EXCEPT_MEMO_THORSWAP_AND_FEES
from .apps import cal as cal

from .apps.boilerplate import BoilerplateClient, BoilerplateErrors

# ExchangeTestRunner implementation for Near
class BoilerplateTests(ExchangeTestRunner):

    currency_configuration = cal.BOL_CURRENCY_CONFIGURATION
    valid_destination_1 = "speculos.testnet"
    valid_destination_memo_1 = ""
    valid_destination_2 = "ledger.testnet"
    valid_destination_memo_2 = ""
    valid_refund = "c4f5941e81e071c2fd1dae2e71fd3d859d462484391d9a90bf219211dcbb320f"
    valid_refund_memo = ""
    valid_send_amount_1 = 1234560000000000000000000000
    valid_send_amount_2 = 500000000000000000000000
    valid_fees_1 = 0
    valid_fees_2 = 0
    fake_refund = "abcdabcd"
    fake_refund_memo = "bla"
    fake_payout = "abcdabcd"
    fake_payout_memo = "bla"
    signature_refusal_error_code = BoilerplateErrors.SW_SWAP_CHECKING_FAIL

    def perform_final_tx(self, destination, send_amount, fees, memo):
        BoilerplateClient(self.backend).send_simple_sign_tx(path="m/44'/397'/0'/0'/1'",
                                                    destination=destination,
                                                    send_amount=send_amount)

        # TODO : assert signature validity


# Use a class to reuse the same Speculos instance
class TestsBoilerplate:

    @pytest.mark.parametrize('test_to_run', ALL_TESTS_EXCEPT_MEMO_THORSWAP_AND_FEES)
    def test_boilerplate(self, backend, exchange_navigation_helper, test_to_run):
        BoilerplateTests(backend, exchange_navigation_helper).run_test(test_to_run)