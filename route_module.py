 #NEXORA RouteAI
# Member 1 - Route Intelligence Module
    
def calculate_routes(source, destination):
    print(f"Calculating route from {source} to {destination}...")

    distance_factor = len(source) + len(destination)
    route_a_distance = 100 + distance_factor
    route_b_distance = route_a_distance + 25

    route_a_time = f"{route_a_distance / 32:.1f} hr"
    route_b_time = f"{route_b_distance / 32:.1f} hr"

    routes = [
        {
            "name": "Route A",
            "source": source,
            "destination": destination,
            "distance": route_a_distance,
            "time": route_a_time,
            "road_condition": "Poor",
            "risk_score": 82,
            "coordinates": [
                [26.1445, 91.7362],
                [26.2500, 91.9000],
                [26.5000, 92.1000]
            ]
        },
        {
            "name": "Route B",
            "source": source,
            "destination": destination,
            "distance": route_b_distance,
            "time": route_b_time,
            "road_condition": "Good",
            "risk_score": 25,
            "coordinates": [
                [26.1445, 91.7362],
                [26.2500, 91.9000],
                [26.5000, 92.1000]
            ]
        }
    ]

    # Lowest risk route
    recommended = min(
        routes,
        key=lambda route: route["risk_score"]
    )

    return routes, recommended


def show_route_information(source, destination):
    routes, recommended = calculate_routes(
        source,
        destination
    )

    print("\n================================")
    print("     NEXORA ROUTE INTELLIGENCE")
    print("================================")

    print("Source      :", source)
    print("Destination :", destination)

    print("\nAVAILABLE ROUTES")
    print("----------------")

    for route in routes:
        print(
            f'{route["name"]} | '
            f'{route["distance"]} km | '
            f'{route["time"]} | '
            f'Road: {route["road_condition"]} | '
            f'Risk: {route["risk_score"]}/100'
        )

    print("\n================================")
    print("🏆 RECOMMENDED ROUTE")
    print("================================")

    print("Route       :", recommended["name"])
    print("Distance    :", recommended["distance"], "km")
    print("Time        :", recommended["time"])
    print("Road        :", recommended["road_condition"])
    print("Risk Score  :", recommended["risk_score"], "/100")

    print("\nReason:")
    print("NEXORA selected the route with the lowest risk.")


if __name__ == "__main__":
    source = "Guwahati"
    destination = "Remote Village"

    show_route_information(
        source,
        destination
    )