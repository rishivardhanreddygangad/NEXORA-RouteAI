import streamlit as st
from route_module import calculate_routes

# =========================================================
# NEXORA RouteAI - Member 3
# Logistics & Authority Dashboard
# =========================================================

st.set_page_config(
    page_title="NEXORA RouteAI",
    page_icon="🏛️",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "delivery_status" not in st.session_state:
    st.session_state["delivery_status"] = "Awaiting Decision"

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 18px;
    color: #666;
    margin-top: 0px;
}

.route-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)
# ---------------- EXTRA UI DESIGN ----------------

st.markdown("""
<style>

div[data-testid="stMetric"] {
    border: 1px solid #dddddd;
    padding: 15px;
    border-radius: 10px;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)



# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🏛️ NEXORA RouteAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Smart Logistics for Northeast India</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("🚚 NEXORA CONTROL")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Delivery Dashboard",
        "Authority Dashboard",
        "Alerts"
    ]
)

st.sidebar.divider()
st.sidebar.success("Member 3")
st.sidebar.caption("Logistics & Dashboard")


# =========================================================
# DELIVERY DASHBOARD
# =========================================================

if page == "Delivery Dashboard":

    st.header("📦 Delivery Management")

    col1, col2, col3 = st.columns(3)

    with col1:
        source = st.text_input(
            "📍 Source",
            "Guwahati"
        )

    with col2:
        destination = st.text_input(
            "🎯 Destination",
            "Remote Village"
        )

    with col3:
        delivery_type = st.selectbox(
            "📦 Delivery Type",
            [
                "Medical Supplies",
                "Food Supplies",
                "Emergency Materials"
            ]
        )

    st.divider()

    # ---------------- VEHICLE ----------------

    st.header("🚚 Vehicle Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        vehicle = st.selectbox(
            "Vehicle",
            [
                "Medical Supply Van",
                "Truck",
                "Emergency Vehicle"
            ]
        )

    with col2:
        driver = st.text_input(
            "👤 Driver",
            "Team Driver"
        )

    with col3:
        delivery_status_input = st.selectbox(
            "Delivery Status",
            [
                "Ready",
                "In Transit",
                "Delivered"
            ]
        )

    st.divider()

    # ---------------- ROUTE ----------------

    st.header("🗺️ Route Recommendation")

    st.write(f"📍 From: {source}")
    st.write(f"🎯 To: {destination}")

    routes, recommended = calculate_routes(
        source,
        destination
    )

    col1, col2 = st.columns(2)

    with col1:
        route_a = routes[0]

        st.warning("⚠️ ROUTE A — HIGH RISK")

        st.write(f"Distance: {route_a['distance']} km")
        st.write(f"Time: {route_a['time']}")
        st.write(f"Road Condition: {route_a['road_condition']}")
        st.write(f"Risk Score: {route_a['risk_score']}/100")

    with col2:
        route_b = routes[1]

        st.success("✅ ROUTE B — RECOMMENDED")

        st.write(f"Distance: {route_b['distance']} km")
        st.write(f"Time: {route_b['time']}")
        st.write(f"Road Condition: {route_b['road_condition']}")
        st.write(f"Risk Score: {route_b['risk_score']}/100")

    st.info(
        f"🤖 NEXORA Recommendation: {recommended['name']} "
        f"selected because it has the lowest risk score "
        f"({recommended['risk_score']}/100)."
    )

    # ---------------- AUTHORITY DECISION ----------------

    st.divider()

    st.header("🧠 NEXORA AI Decision")

    st.info(
        f"Recommended Route: {recommended['name']}\n\n"
        f"Risk Score: {recommended['risk_score']}/100\n\n"
        f"Reason: Lowest risk route selected by NEXORA."
    )

    decision_col1, decision_col2 = st.columns(2)

    with decision_col1:
        approve = st.button(
            "✅ APPROVE DELIVERY",
            use_container_width=True
        )

    with decision_col2:
        reject = st.button(
            "❌ REJECT DELIVERY",
            use_container_width=True
        )

    if approve:
        st.session_state["delivery_status"] = "Approved"

    if reject:
        st.session_state["delivery_status"] = "Rejected"

    authority_status = st.session_state["delivery_status"]

    if authority_status == "Approved":
        st.success("✅ Delivery Approved — Route assigned")

    elif authority_status == "Rejected":
        st.error("❌ Delivery Rejected — Authority review required")

    else:
        st.warning("⏳ Awaiting Authority Decision")

    st.write(
        f"**Current Status:** {authority_status}"
    )

    # ---------------- AUTOMATIC RISK ALERTS ----------------

    st.divider()

    st.header("⚠️ Automatic Risk Alerts")

    risk_score = recommended["risk_score"]

    if risk_score > 70:
        st.error(
            f"🔴 HIGH RISK ALERT\n\n"
            f"Route: {recommended['name']}\n\n"
            f"Risk Score: {risk_score}/100\n\n"
            f"⚠️ Immediate review required."
        )

    elif risk_score > 40:
        st.warning(
            f"🟠 MODERATE RISK\n\n"
            f"Route: {recommended['name']}\n\n"
            f"Risk Score: {risk_score}/100\n\n"
            f"Monitor the delivery closely."
        )

    else:
        st.success(
            f"🟢 LOW RISK\n\n"
            f"Route: {recommended['name']}\n\n"
            f"Risk Score: {risk_score}/100\n\n"
            f"Route is currently within the low-risk range."
        )

    # ---------------- LIVE DELIVERY TRACKING ----------------

    st.divider()

    st.header("📍 Live Delivery Tracking")

    tracking_col1, tracking_col2, tracking_col3 = st.columns(3)

    with tracking_col1:
        st.metric(
            "🚚 Vehicle",
            vehicle
        )

    with tracking_col2:
        st.metric(
            "📦 Delivery Status",
            authority_status
        )

    with tracking_col3:
        st.metric(
            "🛣️ Route",
            recommended["name"]
        )

    progress_values = {
        "Awaiting Decision": 0.00,
        "Approved": 0.65,
        "Rejected": 0.00,
        "Ready": 0.10,
        "In Transit": 0.60,
        "Delivered": 1.00
    }

    progress = progress_values.get(
        authority_status,
        0
    )

    st.progress(progress)

    if authority_status == "Approved":
        st.success(
            "🟢 Vehicle is currently moving toward destination."
        )

    elif authority_status == "Rejected":
        st.error(
            "🔴 Tracking stopped — delivery rejected."
        )

    else:
        st.warning(
            "🟡 Tracking will begin after authority approval."
        )

    # ---------------- LOGISTICS MAP ----------------

    st.divider()

    st.header("📍 Logistics Map")

    st.info(
        f"🛰️ Showing {recommended['name']} — "
        f"NEXORA Route Intelligence"
    )

    route_points = recommended["coordinates"]

    map_data = {
        "lat": [point[0] for point in route_points],
        "lon": [point[1] for point in route_points]
    }

    st.map(
        map_data,
        zoom=9
    )

    # ---------------- LIVE STATUS ----------------

    st.divider()

    st.header("📊 Live Delivery Status")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Delivery",
            delivery_type
        )

    with col2:
        st.metric(
            "🚚 Vehicle",
            vehicle
        )

    with col3:
        st.metric(
            "📍 Status",
            authority_status
        )

    with col4:
        st.metric(
            "⚠️ Risk",
            "HIGH" if risk_score > 70 else "MEDIUM" if risk_score > 40 else "LOW"
        )

    # ---------------- START DELIVERY ----------------

    st.divider()

    if st.button(
        "🚚 START DELIVERY",
        use_container_width=True
    ):
        st.success(
            f"Delivery started successfully!\n\n"
            f"{source} → {destination}"
        )

    # ---------------- DELIVERY ANALYTICS ----------------

    st.divider()

    st.header("📊 Delivery Analytics")

    analytics1, analytics2, analytics3 = st.columns(3)

    with analytics1:
        st.metric(
            "🛣️ Route Distance",
            f"{recommended['distance']} km"
        )

    with analytics2:
        st.metric(
            "⏱️ Estimated Time",
            recommended["time"]
        )

    with analytics3:
        st.metric(
            "⚠️ Risk Score",
            f"{recommended['risk_score']}/100"
        )

    st.write("### 📋 Delivery Summary")

    st.write(f"**Vehicle:** {vehicle}")
    st.write(f"**Driver:** {driver}")
    st.write(f"**Source:** {source}")
    st.write(f"**Destination:** {destination}")
    st.write(f"**Selected Route:** {recommended['name']}")
    st.write(f"**Authority Status:** {authority_status}")

    # ---------------- DELIVERY REPORT ----------------

    st.divider()

    st.header("📄 Delivery Report")

    report = f"""
NEXORA ROUTEAI — DELIVERY REPORT

Vehicle: {vehicle}
Driver: {driver}

Source: {source}
Destination: {destination}

Selected Route: {recommended['name']}
Distance: {recommended['distance']} km
Estimated Time: {recommended['time']}
Risk Score: {recommended['risk_score']}/100

Authority Status: {authority_status}

NEXORA AI Recommendation:
{recommended['name']} selected based on the lowest risk score.
"""

    st.download_button(
        label="📥 Download Delivery Report",
        data=report,
        file_name="NEXORA_Delivery_Report.txt",
        mime="text/plain",
        use_container_width=True
    )


# =========================================================
# AUTHORITY DASHBOARD
# =========================================================

if page == "Authority Dashboard":

    st.header("🏛️ Authority Dashboard")

    st.write(
        "Central monitoring system for logistics operations."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🚚 Active Vehicles",
            "12"
        )

    with col2:
        st.metric(
            "📦 Active Deliveries",
            "28"
        )

    with col3:
        st.metric(
            "⚠️ High Risk Routes",
            "5"
        )

    with col4:
        st.metric(
            "🏘️ Remote Areas",
            "17"
        )

    st.divider()

    st.subheader("📋 Current Logistics Operations")

    operations = {
        "Vehicle": [
            "Vehicle 01",
            "Vehicle 02",
            "Vehicle 03",
            "Vehicle 04"
        ],
        "Destination": [
            "Remote Village A",
            "Remote Village B",
            "Health Centre",
            "Relief Camp"
        ],
        "Status": [
            "In Transit",
            "Ready",
            "In Transit",
            "Delivered"
        ],
        "Risk": [
            "Low",
            "Medium",
            "High",
            "Low"
        ]
    }

    st.dataframe(
        operations,
        use_container_width=True
    )

    st.divider()

    st.subheader("📍 Regional Monitoring")

    st.info(
        "Authority officers can monitor vehicles, "
        "deliveries, route risks and remote-area accessibility "
        "from this dashboard."
    )


# =========================================================
# ALERTS
# =========================================================

if page == "Alerts":

    st.header("🔔 Logistics Alerts")

    st.warning(
        "⚠️ Route A has HIGH disruption risk."
    )

    st.info(
        "🌧️ Heavy rainfall may affect selected routes."
    )

    st.success(
        "✅ Route B is currently recommended."
    )

    st.warning(
        "🚧 Road blockage reported in one remote area."
    )

    st.info(
        "📦 Medical supply delivery is ready to start."
    )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "NEXORA RouteAI | Smart Transportation & Logistics | SIH Prototype"
)