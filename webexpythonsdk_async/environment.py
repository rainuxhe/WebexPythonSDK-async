import os
import warnings

from .config import (
    ACCESS_TOKEN_ENVIRONMENT_VARIABLE,
    LEGACY_ACCESS_TOKEN_ENVIRONMENT_VARIABLES,
)


# Helper Functions
def _get_access_token():
    """Attempt to get the access token from the environment.

    Try using the current and legacy environment variables. If the access token
    is found in a legacy environment variable, raise a deprecation warning.

    Returns:
        The access token found in the environment (str), or None.
    """
    access_token = os.environ.get(ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
    if access_token:
        return access_token

    else:
        for access_token_variable in LEGACY_ACCESS_TOKEN_ENVIRONMENT_VARIABLES:
            access_token = os.environ.get(access_token_variable)
            if access_token:
                env_var_deprecation_warning = PendingDeprecationWarning(
                    "Use of the `{legacy}` environment variable will be "
                    "deprecated in the future.  Please update your "
                    "environment(s) to use the new `{new}` environment "
                    "variable.".format(
                        legacy=access_token,
                        new=ACCESS_TOKEN_ENVIRONMENT_VARIABLE,
                    )
                )
                warnings.warn(env_var_deprecation_warning, stacklevel=2)
                return access_token


# Package Environment Variables
WEBEX_ACCESS_TOKEN = _get_access_token()
