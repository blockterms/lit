from lit.format import verify_sig
from lit.network.fees import set_fee_cache_time
from lit.network.rates import SUPPORTED_CURRENCIES, set_rate_cache_time
from lit.network.services import set_service_timeout
from lit.wallet import Key, PrivateKey, PrivateKeyTestnet, wif_to_key

__version__ = '0.4.2'
