from typing import Callable, Dict, List, Any

# A simple in-memory event bus
# This can be replaced with a more robust system like RabbitMQ or Redis Pub/Sub in the future.
_subscribers: Dict[str, List[Callable]] = {}

def subscribe(event_type: str, fn: Callable):
    """Subscribe a function to a specific event type."""
    if event_type not in _subscribers:
        _subscribers[event_type] = []
    _subscribers[event_type].append(fn)
    print(f"Function {fn.__name__} subscribed to event '{event_type}'")


def post_event(event_type: str, *args, **kwargs: Any):
    """Post an event to all subscribed functions."""
    if event_type not in _subscribers:
        return

    print(f"Posting event '{event_type}' with args: {args} and kwargs: {kwargs}")
    for fn in _subscribers[event_type]:
        try:
            fn(*args, **kwargs)
        except Exception as e:
            print(f"Error handling event '{event_type}' in function {fn.__name__}: {e}")

# Example Usage:
#
# from core.events import subscribe, post_event
#
# def handle_sale_created(sale_data: dict):
#     print(f"Handling sale created event: {sale_data}")
#
# subscribe("sale_created", handle_sale_created)
#
# # In another part of the code, e.g., in the POS service after a sale is completed:
# post_event("sale_created", sale_data={"id": 1, "total": 100.0})
