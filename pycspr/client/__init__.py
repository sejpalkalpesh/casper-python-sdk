from pycspr.client.connection_info import NodeConnectionInfo
from pycspr.client.deploys import DeploysClient as _DeploysClient
from pycspr.client.events import NodeEventChannelType
from pycspr.client.events import NodeEventType
from pycspr.client.events import EventsClient as _EventsClient
from pycspr.client.queries import QueriesClient as _QueriesClient
from pycspr.utils.constants import NODE_REST_ENDPOINTS
from pycspr.utils.constants import NODE_RPC_ENDPOINTS
from pycspr.utils.constants import NODE_SSE_ENDPOINTS



class NodeClient():
    """Exposes a set of (categorised) functions for interacting  with a node.
    
    """
    NODE_REST_ENDPOINTS: set = NODE_REST_ENDPOINTS
    NODE_RPC_ENDPOINTS: set = NODE_RPC_ENDPOINTS
    NODE_SSE_ENDPOINTS: set = NODE_SSE_ENDPOINTS

    def __init__(self, connection_info: NodeConnectionInfo):
        """Instance constructor.

        :param connection_info: Information required to connect to a node.
        
        """
        self.deploys = _DeploysClient(connection_info)
        self.events = _EventsClient(connection_info)
        self.queries = _QueriesClient(connection_info)