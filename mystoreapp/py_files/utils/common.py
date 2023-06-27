def parse_cart() -> list:
    from flask import request
    import json
    raw_cart = request.args.get('cart') if request.args.get('cart') else None
    parsed_cart = json.loads(raw_cart) if raw_cart else []

    return parsed_cart
