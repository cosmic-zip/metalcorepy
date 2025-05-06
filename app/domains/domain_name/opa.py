from functools import wraps
from ninja.errors import HttpError
from infrastructure.opa_client import OPAClient

opa = OPAClient()

# This is a sample function
def opa_check(policy_path: str):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            input_data = {
                "user": str(request.user),
                "path": request.path,
                "method": request.method,
                "query": request.GET.dict(),
            }
            allowed = opa.evaluate_policy(policy_path, input_data)
            if not allowed:
                raise HttpError(403, "Access Denied by OPA Policy")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
