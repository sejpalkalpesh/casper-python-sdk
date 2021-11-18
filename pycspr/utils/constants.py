import collections

# Data structure representing numerical constraints.
NumericConstraints = collections.namedtuple("NumericConstraints", ["LENGTH", "MIN", "MAX"])

# Default number of motes to pay for standard payments.
STANDARD_PAYMENT_FOR_NATIVE_TRANSFERS = int(1e8)

# Default number of motes to pay for standard delegation.
STANDARD_PAYMENT_FOR_DELEGATION = int(3e9)

# Default number of motes to pay for standard delegation withdrawal.
STANDARD_PAYMENT_FOR_DELEGATION_WITHDRAWAL = int(3e9)

# Default number of motes to pay for standard auction bid.
STANDARD_PAYMENT_FOR_AUCTION_BID = int(3e9)

# Default number of motes to pay for standard auction bid withdrawal.
STANDARD_PAYMENT_FOR_AUCTION_BID_WITHDRAWAL = int(3e9)

# Default deploy time to live.
DEFAULT_DEPLOY_TTL = "30m"

# Default deploy gas price.
DEFAULT_GAS_PRICE = 1

# Maximum deploy time to live = 1 day.
DEPLOY_TTL_MS_MAX = 1000 * 60 * 60 * 24
