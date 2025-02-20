from enum import IntEnum

from ragger.bip import pack_derivation_path
from ragger.utils import create_currency_config, RAPDU

BOL_PATH = "m/44'/60'/0'/0/0"

BOL_CONF = create_currency_config("BOL", "Boilerplate", ["BOL", 18])
BOL_PACKED_DERIVATION_PATH = pack_derivation_path(BOL_PATH)

class BoilerplateErrors(IntEnum):
    SW_DENY = 0x6985
    SW_SWAP_CHECKING_FAIL = 0xB008

class BoilerplateClient:
    CLA = 0x80

    def __init__(self, backend):
        self._backend = backend

    def send_simple_sign_tx(self, path: str, destination: str, send_amount: int) -> RAPDU:
        packed_path = pack_derivation_path(path)
        tx = bytes.fromhex("deadbabe")

        return self._backend.exchange(self.CLA, 0x04, 0x00, 0x00, packed_path[1:] + tx)
