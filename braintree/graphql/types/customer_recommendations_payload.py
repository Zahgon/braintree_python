from typing import Dict, List, Any, Optional
from braintree.exceptions.server_error import ServerError
from braintree.graphql.enums.recommended_payment_option import RecommendedPaymentOption
from braintree.graphql.unions.customer_recommendations import CustomerRecommendations
from braintree.graphql.types.payment_options import PaymentOptions
from braintree.graphql.types.payment_recommendation import PaymentRecommendation
from braintree.util.experimental import Experimental

@Experimental
# This class is Experiemental and may change in future releases.
class CustomerRecommendationsPayload:
    """
    Represents the customer recommendations information associated with a PayPal customer session.
    """

    def __init__(self, session_id: str = None, is_in_paypal_network: bool = None, recommendations: CustomerRecommendations = None, response: Dict[str, Any] = None):
        if response:
            # Constructor for response map
            self.session_id = self._get_value(response, "generateCustomerRecommendations.sessionId")
            self.is_in_paypal_network = self._get_value(response, "generateCustomerRecommendations.isInPayPalNetwork")
            self.recommendations = self._extract_recommendations(response)
        else:
            # Constructor for direct values
            self.session_id = session_id
            self.is_in_paypal_network = is_in_paypal_network
            self.recommendations = recommendations

    def _extract_recommendations(self, response: Dict[str, Any]) -> CustomerRecommendations:
        """
        Extract recommendations from the GraphQL response.
        
        Args:
            response: The GraphQL response containing recommendations data
            
        Returns:
            CustomerRecommendations object with payment options
        
        Raises:
            ServerError: If there's an error parsing the response
        """
        pass

    @staticmethod
    def _get_value(response: Dict[str, Any], key: str) -> Any:
        """
        Get a nested value from a dictionary using dot notation.
        
        Args:
            response: The dictionary to extract values from
            key: Dot notation path to the desired value
            
        Returns:
            The value at the specified path
            
        Raises:
            ServerError: If the key doesn't exist in the dictionary
        """
        pass

    @staticmethod
    def _pop_value(response: Dict[str, Any], key: str) -> Any:
        """
        Get a value from a dictionary with error handling.
        
        Args:
            response: The dictionary to extract a value from
            key: The key to look up
            
        Returns:
            The value associated with the key
            
        Raises:
            ServerError: If the key doesn't exist in the dictionary
        """
        pass
