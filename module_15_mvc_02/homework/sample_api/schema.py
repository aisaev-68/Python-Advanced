schema = {
    "properties": {
        "rooms": {
            "items": {
                "$id": "#/properties/rooms/items",
                "anyOf": [
                    {
                        "type": "object",
                        "required": [
                            "roomId",
                            "floor",
                            "guestNum",
                            "beds",
                            "price"
                        ],
                        "properties": {
                            "roomId": {
                                "type": "integer"
                            },
                            "floor": {
                                "type": "integer"
                            },
                            "guestNum": {
                                "type": "integer"
                            },
                            "beds": {
                                "type": "integer"
                            },
                            "price": {
                                "type": "integer"
                            }
                        }
                    }
                ]
            }
        }
    }
}