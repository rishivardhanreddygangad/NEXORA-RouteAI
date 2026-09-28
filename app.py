import streamlit as st
import pandas as pd
import joblib
# Load SKRYPTORA AI Risk Model
risk_model = joblib.load("risk_model.pkl")
# -----------------------------
# SKRYPTORA GLOBAL STATE
# -----------------------------

if "delivery" not in st.session_state:
    st.session_state.delivery = {
        "delivery_id": "SKY-001",
        "customer": "Customer A",
        "source": "Guwahati",
        "destination": "Remote Village A",
        "product": "Medical Supplies",
        "vehicle": "Truck",
        "cargo_weight": 500,
        "priority": "Emergency",
        "route": "Route B",
        "risk": "Low",
        "status": "Pending Approval",
        "progress": 0,
        "driver": "Driver 01",
        "tracking": "GPS Online",
        "hazard": "No Hazard",
        "case_status": "No Case"
    }

delivery = st.session_state.delivery
# =========================================================
# SKRYPTORA
# =========================================================

st.set_page_config(
    page_title="SKRYPTORA",
    page_icon="🚚",
    layout="wide"
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🚚 SKRYPTORA")
st.sidebar.caption("Smart Logistics Intelligence Platform")

role = st.sidebar.selectbox(
    "Select Role",
    ["Customer", "Driver", "Admin"]
)

# =========================================================
# PAGE SELECTION
# =========================================================

if role == "Customer":

    pages = [
        "Customer Home",
        "Create Delivery",
        "Track Delivery",
        "Feedback & Return"
    ]

elif role == "Driver":

    pages = [
        "Driver Home",
        "Assigned Delivery",
        "Route Recommendation",
        "Live Tracking",
        "Hazard Response"
    ]

else:

    pages = [
        "Admin Dashboard",
        "Delivery Approval",
        "Operations Monitoring",
        "Alerts",
        "Support & Escalation"
    ]

page = st.sidebar.radio(
    "Navigation",
    pages
)

# =========================================================
# TEST PAGE
# =========================================================

if page == "Admin Dashboard":

    st.title("🏛️ SKRYPTORA Admin Dashboard")

    st.subheader("Smart Logistics Operations Center")

    st.write(
        "Monitor deliveries, AI route decisions, "
        "vehicle status, environmental risks and "
        "operational alerts."
    )

    st.divider()

    # =================================================
    # OPERATIONS OVERVIEW
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📦 Total Deliveries",
            "24"
        )

    with col2:

        st.metric(
            "🚚 Active Vehicles",
            "18"
        )

    with col3:

        st.metric(
            "🟢 Safe Deliveries",
            "20"
        )

    with col4:

        st.metric(
            "🚨 Active Alerts",
            "4"
        )

    st.divider()

    # =================================================
    # DELIVERY OPERATIONS
    # =================================================

    st.subheader("📦 Delivery Operations")

    operations = pd.DataFrame({
        "Delivery ID": [
            "SKY-001",
            "SKY-002",
            "SKY-003",
            "SKY-004"
        ],
        "Destination": [
            "Remote Village A",
            "District Hospital",
            "Hill Area B",
            "Agri Center"
        ],
        "Vehicle": [
            "Truck",
            "Van",
            "Mini Truck",
            "Truck"
        ],
        "Status": [
            "In Transit",
            "Approved",
            "Risk Alert",
            "Delivered"
        ],
        "Risk": [
            "Low",
            "Low",
            "High",
            "Low"
        ]
    })

    st.dataframe(
        operations,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =================================================
    # AI MONITORING
    # =================================================

    st.subheader("🤖 AI Logistics Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "🧠 AI Route Engine: ACTIVE"
        )

        st.write(
            "Route accessibility analysis"
        )

        st.write(
            "Vehicle suitability analysis"
        )

        st.write(
            "Environmental risk assessment"
        )

        st.write(
            "Alternative route recommendation"
        )

    with col2:

        st.info(
            "🌧️ Environmental Monitoring: ACTIVE"
        )

        st.write(
            "Rainfall monitoring"
        )

        st.write(
            "Flood-risk detection"
        )

        st.write(
            "Landslide-risk detection"
        )

        st.write(
            "Road blockage monitoring"
        )

    st.divider()

    # =================================================
    # REGIONAL MONITORING
    # =================================================

    st.subheader("🗺️ Regional Monitoring")

    regional_location = pd.DataFrame({
        "latitude": [
            26.1445,
            26.2000,
            26.0500
        ],
        "longitude": [
            91.7362,
            91.7500,
            91.7000
        ]
    })

    st.map(
        regional_location,
        zoom=9
    )

    st.caption(
        "📍 Demonstration monitoring points — Northeast region"
    )

    st.divider()

    # =================================================
    # ADMIN ACTION
    # =================================================

    st.subheader("⚙️ Administrative Action")

    selected_delivery = st.selectbox(
        "Select Delivery",
        [
            "SKY-001",
            "SKY-002",
            "SKY-003",
            "SKY-004"
        ]
    )

    action = st.selectbox(
        "Action",
        [
            "Monitor",
            "Approve",
            "Reject",
            "Request Driver Update",
            "Escalate Risk"
        ]
    )

    if st.button(
        "⚡ EXECUTE ACTION",
        use_container_width=True
    ):

        if action == "Approve":

            st.success(
                f"✅ {selected_delivery} approved successfully."
            )

        elif action == "Reject":

            st.error(
                f"❌ {selected_delivery} rejected."
            )

        elif action == "Escalate Risk":

            st.warning(
                f"🚨 Risk escalation created for {selected_delivery}."
            )

        else:

            st.info(
                f"Action '{action}' applied to {selected_delivery}."
            )

elif page == "Customer Home":

    st.title("👤 SKRYPTORA Customer Portal")

    st.subheader("🚚 Smart Logistics at Your Service")

    st.write(
        "Create deliveries, track shipments, monitor risks "
        "and report delivery issues from one platform."
    )

    st.divider()

    # =================================================
    # CUSTOMER DASHBOARD
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Active Deliveries",
            "1"
        )

    with col2:
        st.metric(
            "🚚 In Transit",
            "1"
        )

    with col3:
        st.metric(
            "🛡️ Risk Level",
            "Low"
        )

    with col4:
        st.metric(
            "⭐ Rating",
            "4.8/5"
        )

    st.divider()

    # =================================================
    # CURRENT DELIVERY
    # =================================================

    st.subheader("📦 Current Delivery")

    delivery_data = {
        "Delivery ID": "SKY-001",
        "Pickup": "Guwahati",
        "Destination": "Remote Village A",
        "Product": "Medical Supplies",
        "Vehicle": "Truck",
        "Status": "🚚 In Transit",
        "Route": "Route B"
    }

    st.table(delivery_data)

    st.divider()

    # =================================================
    # DELIVERY PROGRESS
    # =================================================

    st.subheader("📊 Delivery Progress")

    st.progress(65)

    st.write(
        "🚚 Delivery is currently 65% complete."
    )

    st.info(
        "📍 Driver location is being monitored through "
        "LIVE / LAST-KNOWN tracking."
    )

    st.divider()

    # =================================================
    # QUICK ACTIONS
    # =================================================

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            "📦 Create a new delivery\n\n"
            "Use **Create Delivery** from the sidebar."
        )

    with col2:

        st.info(
            "📍 Track your delivery\n\n"
            "Use **Track Delivery** from the sidebar."
        )

    with col3:

        st.info(
            "⭐ Give feedback\n\n"
            "Use **Feedback & Return** after delivery."
        )

    st.divider()

    # =================================================
    # SAFETY ALERT
    # =================================================

    st.subheader("🚨 Safety & Route Alert")

    st.success(
        "🟢 No active hazard detected on the recommended route."
    )

    st.caption(
        "SKRYPTORA continuously evaluates route accessibility "
        "and environmental risks for safer delivery."
    )

elif page == "Driver Home":

    st.title("🚚 SKRYPTORA Driver Portal")

    st.subheader("Driver Operations Dashboard")

    st.write(
        "Manage assigned deliveries, monitor route safety "
        "and respond to logistics alerts."
    )

    st.divider()

    # =================================================
    # DRIVER STATUS
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Assigned Deliveries",
            "1"
        )

    with col2:
        st.metric(
            "🚚 Vehicle",
            "Truck"
        )

    with col3:
        st.metric(
            "🛡️ Route Risk",
            "Low"
        )

    with col4:
        st.metric(
            "📡 GPS",
            "Online"
        )

    st.divider()

    # =================================================
    # ASSIGNED DELIVERY
    # =================================================

    st.subheader("📦 Assigned Delivery")

    delivery_data = {
        "Delivery ID": "SKY-001",
        "Customer": "Customer A",
        "Pickup": "Guwahati",
        "Destination": "Remote Village A",
        "Product": "Medical Supplies",
        "Cargo": "500 kg",
        "Priority": "🚨 Emergency"
    }

    st.table(delivery_data)

    st.divider()
# =================================================
    # VEHICLE STATUS
    # =================================================

    st.subheader("🚚 Vehicle Status")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "✅ Vehicle Suitable"
        )

        st.write(
            "Vehicle: Truck"
        )

        st.write(
            "Maximum Capacity: 5000 kg"
        )

        st.write(
            "Current Cargo: 500 kg"
        )

    with col2:

        st.info(
            "🔧 Vehicle Inspection"
        )

        inspection = st.selectbox(
            "Vehicle Condition",
            [
                "Ready",
                "Needs Inspection",
                "Maintenance Required"
            ]
        )

        if inspection == "Ready":

            st.success(
                "Vehicle is ready for delivery."
            )

        elif inspection == "Needs Inspection":

            st.warning(
                "Vehicle inspection required before departure."
            )

        else:

            st.error(
                "Vehicle maintenance required."
            )

    st.divider()

    # =================================================
    # ROUTE INFORMATION
    # =================================================

    st.subheader("🧭 AI Recommended Route")

    route_data = {
        "Selected Route": "Route B",
        "Distance": "145 km",
        "Estimated Time": "4h 30m",
        "Road Condition": "Good",
        "Risk Level": "🟢 Low"
    }

    st.table(route_data)

    st.success(
        "🤖 SKRYPTORA recommends Route B based on "
        "accessibility and risk analysis."
    )

    st.divider()

    # =================================================
    # START DELIVERY
    # =================================================

    st.subheader("🚀 Delivery Control")

    if st.button(
        "🚀 START DELIVERY",
        use_container_width=True
    ):

        st.success(
            "🚚 Delivery started successfully!"
        )

        st.info(
            "📡 Live tracking has been activated."
        )

        st.warning(
            "⚠️ Continue monitoring route and environmental alerts."
        )

    st.divider()

    # =================================================
    # DRIVER SAFETY
    # =================================================

    st.subheader("🛡️ Driver Safety")

    st.success(
        "🟢 No active hazard detected."
    )

    st.info(
        "SKRYPTORA will notify the driver if a road blockage, "
        "flood, landslide or other route hazard is detected."
    )

    st.title("🚚 SKRYPTORA Driver Portal")

    st.success("Driver Portal is working.")
elif page == "Create Delivery":

    st.title("📦 Create Delivery Request")

    st.subheader("Customer Delivery Details")

    col1, col2 = st.columns(2)

    with col1:

        customer = st.text_input(
            "👤 Customer Name",
            "Customer A"
        )

        source = st.text_input(
            "📍 Pickup Location",
            "Guwahati"
        )

        destination = st.text_input(
            "🎯 Destination",
            "Remote Village A"
        )

        product = st.selectbox(
            "📦 Product",
            [
                "Medical Supplies",
                "Food Supplies",
                "Construction Material",
                "Agricultural Produce",
                "General Goods"
            ]
        )

    with col2:

        vehicle = st.selectbox(
            "🚚 Vehicle Type",
            [
                "Truck",
                "Mini Truck",
                "Van",
                "Emergency Vehicle"
            ]
        )

        cargo_weight = st.number_input(
            "⚖️ Cargo Weight (kg)",
            min_value=1,
            value=500
        )

        priority = st.selectbox(
            "🚨 Delivery Priority",
            [
                "Normal",
                "High",
                "Emergency"
            ]
        )

        instructions = st.text_area(
            "📝 Special Instructions",
            "Remote-area delivery"
        )

    st.divider()

    # =================================================
    # ENVIRONMENT
    # =================================================

    st.subheader("🌧️ Environment & Disaster Risk")

    environment = st.selectbox(
        "Select Current Environmental Condition",
        [
            "Normal Conditions",
            "Heavy Rainfall",
            "Flood Risk",
            "Landslide Risk",
            "Road Blockage",
            "Connectivity Loss"
        ]
    )

    # =================================================
    # SUBMIT
    # =================================================

    if st.button(
        "🚀 SUBMIT DELIVERY REQUEST",
        use_container_width=True
    ):

        # =================================================
        # VEHICLE ANALYSIS
        # =================================================

        vehicle_capacity = {
            "Truck": 5000,
            "Mini Truck": 2000,
            "Van": 1000,
            "Emergency Vehicle": 1500
        }

        capacity = vehicle_capacity[vehicle]

        if cargo_weight <= capacity:

            vehicle_status = "Suitable"

        else:

            vehicle_status = "Not Suitable"

        # =================================================
        # ENVIRONMENT FEATURES
        # =================================================

        environment_features = {

            "Normal Conditions": {
                "rainfall": 0,
                "road_condition": 1,
                "landslide_risk": 0,
                "flood_risk": 0,
                "connectivity": 90
            },

            "Heavy Rainfall": {
                "rainfall": 70,
                "road_condition": 2,
                "landslide_risk": 30,
                "flood_risk": 40,
                "connectivity": 60
            },

            "Flood Risk": {
                "rainfall": 90,
                "road_condition": 3,
                "landslide_risk": 40,
                "flood_risk": 80,
                "connectivity": 40
            },

            "Landslide Risk": {
                "rainfall": 80,
                "road_condition": 3,
                "landslide_risk": 80,
                "flood_risk": 30,
                "connectivity": 50
            },

            "Road Blockage": {
                "rainfall": 50,
                "road_condition": 3,
                "landslide_risk": 60,
                "flood_risk": 40,
                "connectivity": 50
            },

            "Connectivity Loss": {
                "rainfall": 30,
                "road_condition": 2,
                "landslide_risk": 20,
                "flood_risk": 20,
                "connectivity": 20
            }
        }

        features = environment_features[environment]

        # =================================================
        # CARGO PRIORITY
        # =================================================

        priority_value = {
            "Normal": 1,
            "High": 2,
            "Emergency": 3
        }

        cargo_priority = priority_value[priority]

        # =================================================
        # AI INPUT
        # =================================================

        ai_input = pd.DataFrame([{

            "rainfall": features["rainfall"],

            "road_condition": features["road_condition"],

            "landslide_risk": features["landslide_risk"],

            "flood_risk": features["flood_risk"],

            "connectivity": features["connectivity"],

            "cargo_priority": cargo_priority

        }])

        # =================================================
        # AI PREDICTION
        # =================================================

        prediction = risk_model.predict(ai_input)[0]

        risk_labels = {
            0: "LOW",
            1: "MEDIUM",
            2: "HIGH"
        }

        risk_level = risk_labels[int(prediction)]

        # =================================================
        # CONFIDENCE
        # =================================================

        if hasattr(risk_model, "predict_proba"):

            probabilities = risk_model.predict_proba(ai_input)[0]

            confidence = max(probabilities) * 100

        else:

            confidence = 0

        # =================================================
        # ROUTE DECISION
        # =================================================

        if risk_level == "HIGH":

            recommended_route = "Route C"

        elif risk_level == "MEDIUM":

            recommended_route = "Route B"

        else:

            recommended_route = "Route B"

        # =================================================
        # SAVE DELIVERY
        # =================================================

        st.session_state.delivery.update({

            "customer": customer,

            "source": source,

            "destination": destination,

            "product": product,

            "vehicle": vehicle,

            "cargo_weight": cargo_weight,

            "priority": priority,

            "route": recommended_route,

            "risk": risk_level,

            "status": "Pending Approval",

            "progress": 0,

            "hazard": environment

        })

        # =================================================
        # SUCCESS
        # =================================================

        st.success(
            f"✅ Delivery "
            f"{st.session_state.delivery['delivery_id']} "
            f"created successfully!"
        )

        st.divider()

        # =================================================
        # REQUEST SUMMARY
        # =================================================

        st.subheader("📋 Request Summary")

        summary = {

            "Customer": customer,

            "Pickup": source,

            "Destination": destination,

            "Product": product,

            "Vehicle": vehicle,

            "Cargo": f"{cargo_weight} kg",

            "Priority": priority,

            "Status": "Pending Approval"

        }

        st.table(summary)

        st.divider()

        # =================================================
        # VEHICLE ANALYSIS
        # =================================================

        st.subheader("🚚 Vehicle Analysis")

        if vehicle_status == "Suitable":

            st.success(
                f"✅ Vehicle Suitable — "
                f"Capacity: {capacity} kg"
            )

        else:

            st.error(
                f"❌ Vehicle Not Suitable — "
                f"Capacity: {capacity} kg"
            )

        vehicle_analysis = {

            "Vehicle": vehicle,

            "Maximum Capacity": f"{capacity} kg",

            "Cargo Weight": f"{cargo_weight} kg",

            "Vehicle Status": vehicle_status

        }

        st.table(vehicle_analysis)

        st.divider()

        # =================================================
        # ROUTE ANALYSIS
        # =================================================

        st.subheader("🧭 Route Analysis")

        routes = pd.DataFrame({

            "Route": [
                "Route A",
                "Route B",
                "Route C"
            ],

            "Distance": [
                "120 km",
                "145 km",
                "160 km"
            ],

            "Travel Time": [
                "3h 45m",
                "4h 30m",
                "5h 10m"
            ],

            "Road Condition": [
                "Poor",
                "Good",
                "Moderate"
            ],

            "Risk": [
                "🔴 High",
                "🟢 Low",
                "🟡 Medium"
            ],

            "AI Score": [
                "78/100",
                "92/100",
                "84/100"
            ]

        })

        st.dataframe(
            routes,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            f"🤖 AI Recommended Route: "
            f"{recommended_route}"
        )

        st.divider()

        # =================================================
        # AI RISK PREDICTION
        # =================================================

        st.subheader("🤖 AI Risk Prediction")

        st.metric(
            "AI Predicted Risk",
            risk_level,
            f"Confidence: {confidence:.1f}%"
        )

        st.dataframe(
            ai_input,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            f"SKRYPTORA AI analyzed environmental conditions, "
            f"connectivity and cargo priority."
        )

        st.divider()

        # =================================================
        # AI DECISION ENGINE
        # =================================================

        st.subheader("🤖 AI Decision Engine")

        if vehicle_status == "Not Suitable":

            st.error("⛔ DELIVERY HOLD")

            st.warning(
                "Cargo weight exceeds the selected "
                "vehicle capacity."
            )

        elif risk_level == "HIGH":

            st.error("🚨 HIGH RISK DETECTED")

            st.warning(
                "SKRYPTORA recommends reviewing "
                "an alternative route."
            )

            st.info(
                "🧭 Alternative Route: Route C"
            )

        elif risk_level == "MEDIUM":

            st.warning("⚠️ MEDIUM RISK")

            st.info(
                "Route B can be used with "
                "continuous monitoring."
            )

        else:

            st.success(
                "✅ DELIVERY CONDITIONS ACCEPTABLE"
            )

            st.info(
                "🤖 SKRYPTORA recommends Route B."
            )

        st.divider()

        # =================================================
        # FINAL AI SUMMARY
        # =================================================

        st.subheader("🧠 Final AI Analysis")

        ai_summary = {

            "Vehicle": vehicle_status,

            "Recommended Route": recommended_route,

            "Environmental Risk": risk_level,

            "Hazard": environment,

            "Delivery Priority": priority,

            "AI Confidence": f"{confidence:.1f}%"

        }

        st.table(ai_summary)

        st.success(
            "✅ AI analysis completed. "
            "Next step: Admin Delivery Approval."
        )
#==================================
# skryptora delivery approval
# ==================================                                                                                              elif page == "Track Delivery":
elif page == "Track Delivery":
    st.title("📍 Track Delivery")
    
    st.subheader("🚚 Delivery Tracking")

    col1, col2 = st.columns(2)

    with col1:

        delivery_id = st.text_input(
            "🆔 Delivery ID",
            "SKY-001"
        )

        driver_name = st.text_input(
            "👤 Driver",
            "Driver A"
        )

    with col2:

        vehicle_number = st.text_input(
            "🚚 Vehicle Number",
            "AS-01-AB-1234"
        )

        tracking_status = st.selectbox(
            "📡 Tracking Status",
            [
                "Preparing",
                "Approved",
                "In Transit",
                "Near Destination",
                "Delivered"
            ],
            index=2
        )

    st.divider()

    # =================================================
    # DELIVERY STATUS
    # =================================================

    st.subheader("📦 Delivery Status")

    status_steps = {
        "Preparing": 0,
        "Approved": 25,
        "In Transit": 50,
        "Near Destination": 75,
        "Delivered": 100
    }

    progress = status_steps[tracking_status]

    st.progress(progress / 100)

    st.metric(
        "Delivery Progress",
        f"{progress}%"
    )

    if tracking_status == "Preparing":

        st.info("📦 Delivery request is being prepared.")

    elif tracking_status == "Approved":

        st.info("✅ Delivery approved. Driver can start the journey.")

    elif tracking_status == "In Transit":

        st.warning("🚚 Delivery is currently in transit.")

    elif tracking_status == "Near Destination":

        st.warning("📍 Vehicle is approaching the destination.")

    else:

        st.success("🎉 Delivery completed successfully.")

    st.divider()

    # =================================================
    # LIVE / LAST-KNOWN LOCATION
    # =================================================

    st.subheader("📡 Live / Last-Known Location")

    tracking_mode = st.radio(
        "Tracking Mode",
        [
            "LIVE GPS",
            "LAST-KNOWN LOCATION"
        ],
        horizontal=True
    )

    if tracking_mode == "LIVE GPS":

        st.success(
            "🟢 GPS connection active"
        )

        current_location = pd.DataFrame({
            "latitude": [26.1445],
            "longitude": [91.7362]
        })

        st.map(current_location)

    else:

        st.warning(
            "🟡 Live signal unavailable. "
            "Showing the driver's last-known location."
        )

        last_location = pd.DataFrame({
            "latitude": [26.1445],
            "longitude": [91.7362]
        })

        st.map(last_location)

    st.divider()

    # =================================================
    # DELIVERY INFORMATION
    # =================================================

    st.subheader("📋 Delivery Information")

    delivery_info = {
        "Delivery ID": delivery_id,
        "Driver": driver_name,
        "Vehicle": vehicle_number,
        "Status": tracking_status,
        "Tracking Mode": tracking_mode
    }

    st.table(delivery_info)

    st.info(
        "🧠 SKRYPTORA supports live tracking and "
        "last-known-location tracking for low-connectivity regions."
    )
elif page == "Feedback & Return":

    st.title("⭐ Feedback & Return")

    st.subheader("📦 Delivery Feedback")

    col1, col2 = st.columns(2)

    with col1:

        delivery_id = st.text_input(
            "🆔 Delivery ID",
            "SKY-001"
        )

        rating = st.slider(
            "⭐ Delivery Rating",
            1,
            5,
            5
        )

    with col2:

        issue_type = st.selectbox(
            "📋 Issue Type",
            [
                "No Issue",
                "Damaged Product",
                "Wrong Product",
                "Missing Product",
                "Late Delivery",
                "Product Quality Issue",
                "Other"
            ]
        )

        return_required = st.selectbox(
            "🔄 Return Required?",
            [
                "No",
                "Yes"
            ]
        )

    feedback = st.text_area(
        "📝 Customer Feedback",
        placeholder="Describe your delivery experience or issue..."
    )

    st.divider()

    if st.button(
        "📤 SUBMIT FEEDBACK",
        use_container_width=True
    ):

        st.success(
            "✅ Feedback submitted successfully!"
        )

        st.subheader("📋 Feedback Summary")

        feedback_data = {
            "Delivery ID": delivery_id,
            "Rating": f"{rating}/5",
            "Issue": issue_type,
            "Return Required": return_required,
            "Feedback": feedback if feedback else "No additional comments"
        }

        st.table(feedback_data)

        st.divider()

        # =================================================
        # RETURN / ISSUE PROCESS
        # =================================================

        if issue_type != "No Issue" or return_required == "Yes":

            st.warning(
                "⚠️ Customer issue detected."
            )

            st.subheader("🔄 Return & Support Process")

            st.info(
                "1️⃣ Product issue registered"
            )

            st.info(
                "2️⃣ Dealer interaction required"
            )

            st.info(
                "3️⃣ Admin support review"
            )

            st.info(
                "4️⃣ Case resolution"
            )

            st.success(
                "📨 Support case created successfully."
            )

            st.write(
                "Case Status: **Open**"
            )

        else:

            st.success(
                "🎉 No return or support case required."
            )

        st.divider()

        # =================================================
        # CUSTOMER EXPERIENCE
        # =================================================

        st.subheader("🤝 Customer Experience")

        if rating >= 4 and issue_type == "No Issue":

            st.success(
                "😊 Thank you! Your positive feedback "
                "helps improve SKRYPTORA."
            )

        elif rating <= 2:

            st.warning(
                "⚠️ Your feedback has been marked for "
                "customer-support review."
            )

        else:

            st.info(
                "Thank you for helping us improve the service."
            )

elif page == "Assigned Delivery":

    st.title("📦 Assigned Delivery")

    st.subheader("🚚 Delivery Assignment")

    # =================================================
    # DELIVERY DETAILS
    # =================================================

    delivery_details = {
        "Delivery ID": "SKY-001",
        "Customer": "Customer A",
        "Pickup Location": "Guwahati",
        "Destination": "Remote Village A",
        "Product": "Medical Supplies",
        "Cargo Weight": "500 kg",
        "Priority": "🚨 Emergency",
        "Approval Status": "✅ Approved"
    }

    st.table(delivery_details)

    st.divider()

    # =================================================
    # ASSIGNMENT STATUS
    # =================================================

    st.subheader("📋 Assignment Status")

    assignment = st.selectbox(
        "Driver Response",
        [
            "Pending Acceptance",
            "Accepted",
            "Rejected"
        ]
    )

    if assignment == "Pending Acceptance":

        st.warning(
            "⏳ Delivery is waiting for driver acceptance."
        )

    elif assignment == "Accepted":

        st.success(
            "✅ Delivery accepted by driver."
        )

        st.info(
            "🧭 Continue to Route Recommendation "
            "to review the AI-selected route."
        )

    else:

        st.error(
            "❌ Delivery rejected by driver."
        )

    st.divider()

    # =================================================
    # DELIVERY REQUIREMENTS
    # =================================================

    st.subheader("📋 Delivery Requirements")

    requirements = [
        "Vehicle capacity must be sufficient",
        "Driver must verify cargo",
        "AI-recommended route should be reviewed",
        "Environmental alerts must be monitored",
        "GPS / last-known tracking should remain active"
    ]

    for requirement in requirements:

        st.write(
            f"☑️ {requirement}"
        )

    st.divider()

    # =================================================
    # ACCEPT DELIVERY
    # =================================================

    if st.button(
        "✅ ACCEPT & CONTINUE",
        use_container_width=True
    ):

        st.success(
            "🚚 Delivery accepted successfully!"
        )

        st.info(
            "Next: Open **Route Recommendation** "
            "to review the AI route."
        )

elif page == "Route Recommendation":

    st.title("🧭 AI Route Recommendation")

    st.subheader("🤖 SKRYPTORA Route Intelligence")

    st.write(
        "SKRYPTORA compares route distance, travel time, "
        "road condition and environmental risk."
    )

    st.divider()

    # =================================================
    # ROUTE OPTIONS
    # =================================================

    st.subheader("🛣️ Available Routes")

    routes = pd.DataFrame({
        "Route": [
            "Route A",
            "Route B",
            "Route C"
        ],
        "Distance": [
            "120 km",
            "145 km",
            "160 km"
        ],
        "Travel Time": [
            "3h 45m",
            "4h 30m",
            "5h 10m"
        ],
        "Road Condition": [
            "Poor",
            "Good",
            "Moderate"
        ],
        "Risk": [
            "🔴 High",
            "🟢 Low",
            "🟡 Medium"
        ],
        "AI Score": [
            "78/100",
            "92/100",
            "84/100"
        ]
    })

    st.dataframe(
        routes,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =================================================
    # AI RECOMMENDATION
    # =================================================

    st.subheader("🏆 AI Recommendation")

    recommended_route = "Route B"

    st.success(
        f"🟢 Recommended Route: {recommended_route}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Distance",
            "145 km"
        )

    with col2:

        st.metric(
            "Travel Time",
            "4h 30m"
        )

    with col3:

        st.metric(
            "AI Score",
            "92/100"
        )

    st.info(
        "Route B is recommended because it provides "
        "better road conditions and lower risk."
    )

    st.divider()

    # =================================================
    # DRIVER CONFIRMATION
    # =================================================

    st.subheader("🚚 Driver Route Confirmation")

    selected_route = st.radio(
        "Select route for delivery",
        [
            "Route A",
            "Route B",
            "Route C"
        ],
        index=1
    )

    if selected_route == recommended_route:

        st.success(
            "✅ Driver selected the AI-recommended route."
        )

    else:

        st.warning(
            "⚠️ Driver selected a different route "
            "from the AI recommendation."
        )

    st.divider()

    if st.button(
        "🧭 CONFIRM ROUTE",
        use_container_width=True
    ):

        st.success(
            f"✅ {selected_route} confirmed for delivery."
        )

        st.info(
            "📡 Route is ready for live tracking."
        )

        st.warning(
            "🚨 Continue monitoring environmental "
            "and disaster alerts during delivery."
        )

elif page == "Live Tracking":

    st.title("📡 Live / Last-Known Tracking")

    st.subheader("🚚 Vehicle Tracking")

    # =================================================
    # DELIVERY STATUS
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🆔 Delivery",
            "SKY-001"
        )

    with col2:
        st.metric(
            "🚚 Vehicle",
            "Truck"
        )

    with col3:
        st.metric(
            "📊 Progress",
            "65%"
        )

    with col4:
        st.metric(
            "🛡️ Risk",
            "Low"
        )

    st.divider()

    # =================================================
    # TRACKING MODE
    # =================================================

    st.subheader("📡 Tracking Connection")

    tracking_mode = st.radio(
        "Select Tracking Mode",
        [
            "LIVE GPS",
            "LAST-KNOWN LOCATION"
        ],
        horizontal=True
    )

    if tracking_mode == "LIVE GPS":

        st.success(
            "🟢 GPS connection active"
        )

        st.write(
            "Vehicle location is being updated."
        )

    else:

        st.warning(
            "🟡 GPS signal unavailable"
        )

        st.info(
            "Showing the vehicle's last-known location."
        )

    st.divider()

    # =================================================
    # MAP
    # =================================================

    st.subheader("🗺️ Vehicle Location")

    vehicle_location = pd.DataFrame({
        "latitude": [26.1445],
        "longitude": [91.7362]
    })

    st.map(
        vehicle_location,
        zoom=10
    )

    st.caption(
        "📍 Demonstration vehicle location — Guwahati region"
    )

    st.divider()

    # =================================================
    # ROUTE STATUS
    # =================================================

    st.subheader("🧭 Current Route")

    route_status = {
        "Current Route": "Route B",
        "Destination": "Remote Village A",
        "Distance Remaining": "50 km",
        "Estimated Remaining Time": "1h 40m",
        "Road Condition": "Good",
        "Route Risk": "🟢 Low"
    }

    st.table(route_status)

    st.divider()

    # =================================================
    # DELIVERY PROGRESS
    # =================================================

    st.subheader("📊 Delivery Progress")

    progress = 65

    st.progress(
        progress / 100
    )

    st.write(
        f"🚚 Delivery progress: **{progress}%**"
    )

    st.write(
        "Pickup → Route Confirmed → In Transit → "
        "Near Destination → Delivered"
    )

    st.divider()

    # =================================================
    # LIVE ALERT
    # =================================================

    st.subheader("🚨 Live Route Alert")

    alert = st.selectbox(
        "Simulate Current Condition",
        [
            "No Alert",
            "Heavy Rainfall",
            "Road Blockage",
            "Flood Risk",
            "Landslide Risk",
            "Connectivity Loss"
        ]
    )

    if alert == "No Alert":

        st.success(
            "🟢 No active route alerts."
        )

    elif alert == "Connectivity Loss":

        st.warning(
            "🟡 Connectivity loss detected."
        )

        st.info(
            "SKRYPTORA has switched to "
            "LAST-KNOWN LOCATION mode."
        )

    else:

        st.error(
            f"🚨 {alert} detected!"
        )

        st.warning(
            "SKRYPTORA recommends checking "
            "the alternative route."
        )

    st.divider()

    # =================================================
    # TRACKING SUMMARY
    # =================================================

    st.subheader("📋 Tracking Summary")

    tracking_summary = {
        "Delivery": "SKY-001",
        "Tracking": tracking_mode,
        "Progress": "65%",
        "Current Route": "Route B",
        "Destination": "Remote Village A",
        "Alert": alert
    }

    st.table(tracking_summary)

elif page == "Hazard Response":

    st.title("🚨 Hazard Response")

    st.subheader("🛡️ Real-Time Hazard Detection")

    st.write(
        "SKRYPTORA monitors delivery conditions and "
        "helps drivers respond to sudden route hazards."
    )

    st.divider()

    # =================================================
    # HAZARD SELECTION
    # =================================================

    hazard = st.selectbox(
        "🚨 Current Road / Environmental Condition",
        [
            "No Hazard",
            "Heavy Rainfall",
            "Flood Risk",
            "Landslide Risk",
            "Road Blockage",
            "Bridge Blockage",
            "Connectivity Loss"
        ]
    )

    st.divider()

    # =================================================
    # HAZARD RESPONSE
    # =================================================

    if hazard == "No Hazard":

        st.success(
            "🟢 No active hazard detected."
        )

        st.info(
            "Delivery can continue on the confirmed route."
        )

    elif hazard == "Connectivity Loss":

        st.warning(
            "🟡 Connectivity loss detected."
        )

        st.info(
            "SKRYPTORA will use the driver's "
            "last-known location until connectivity returns."
        )

        st.info(
            "📡 Offline / low-signal monitoring mode activated."
        )

    else:

        st.error(
            f"🚨 HAZARD DETECTED: {hazard}"
        )

        st.warning(
            "⚠️ Current route may no longer be safe."
        )

        st.divider()

        # =================================================
        # ALTERNATIVE ROUTE
        # =================================================

        st.subheader("🧭 Alternative Route Recommendation")

        st.success(
            "🟢 SKRYPTORA recommends switching to Route C."
        )

        alternative_route = {
            "Previous Route": "Route B",
            "Hazard": hazard,
            "Alternative Route": "Route C",
            "Distance": "160 km",
            "Estimated Time": "5h 10m",
            "Risk": "🟡 Medium"
        }

        st.table(alternative_route)

        st.info(
            "🤖 AI selected the alternative route "
            "to avoid the detected hazard."
        )

        st.divider()

        # =================================================
        # DRIVER ACTION
        # =================================================

        st.subheader("🚚 Driver Action")

        action = st.radio(
            "Select Action",
            [
                "Switch to Alternative Route",
                "Wait for Further Instructions",
                "Request Emergency Support"
            ]
        )

        if st.button(
            "🚨 CONFIRM ACTION",
            use_container_width=True
        ):

            if action == "Switch to Alternative Route":

                st.success(
                    "✅ Route changed to Route C."
                )

                st.info(
                    "📡 Live tracking continues on the alternative route."
                )

            elif action == "Wait for Further Instructions":

                st.warning(
                    "⏸️ Delivery temporarily paused."
                )

            else:

                st.error(
                    "🆘 Emergency support request registered."
                )

        st.divider()

        # =================================================
        # ALERT NOTIFICATION
        # =================================================

        st.subheader("📢 Alert Notification")

        st.warning(
            f"⚠️ {hazard} detected on the current delivery route."
        )

        st.write(
            "Notification recipients:"
        )

        st.write("👤 Customer")
        st.write("🚚 Driver")
        st.write("🏛️ Admin / Authority")
elif page == "Delivery Approval":

    # =========================================================
    # AI-BASED DELIVERY APPROVAL
    # =========================================================

    st.subheader("🤖 AI Approval Analysis")

    current_risk = delivery["risk"]
    current_route = delivery["route"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Risk Level",
            current_risk
        )

    with col2:
        st.metric(
            "Recommended Route",
            current_route
        )

    with col3:
        st.metric(
            "Vehicle Status",
            "Suitable"
        )

    st.divider()

    # =========================================================
    # AI ASSESSMENT
    # =========================================================

    if current_risk == "LOW":

        st.success(
            "🟢 AI Assessment: Delivery conditions are suitable."
        )

    elif current_risk == "MEDIUM":

        st.warning(
            "🟡 AI Assessment: Moderate risk detected. "
            "Admin review is recommended."
        )

    else:

        st.error(
            "🔴 AI Assessment: High risk detected. "
            "Admin must review the delivery carefully."
        )

    st.divider()

    # =========================================================
    # DELIVERY REQUEST
    # =========================================================

    st.subheader("📦 Delivery Request")

    delivery_data = {
        "Delivery ID": delivery["delivery_id"],
        "Customer": delivery["customer"],
        "Pickup": delivery["source"],
        "Destination": delivery["destination"],
        "Product": delivery["product"],
        "Cargo": f'{delivery["cargo_weight"]} kg',
        "Priority": f'🚨 {delivery["priority"]}'
    }

    st.table(delivery_data)

    st.divider()

    # =========================================================
    # VEHICLE ANALYSIS
    # =========================================================

    st.subheader("🚚 Vehicle Analysis")

    vehicle_data = {
        "Vehicle": delivery["vehicle"],
        "Maximum Capacity": "5000 kg",
        "Cargo Weight": f'{delivery["cargo_weight"]} kg',
        "Suitability": "✅ Suitable"
    }

    st.table(vehicle_data)

    st.divider()

    # =========================================================
    # ROUTE ANALYSIS
    # =========================================================

    st.subheader("🧭 AI Route Analysis")

    route_data = {
        "Recommended Route": current_route,
        "Distance": "145 km",
        "Estimated Time": "4h 30m",
        "Road Condition": "Good",
        "AI Score": "92/100"
    }

    st.table(route_data)

    st.divider()

    # =========================================================
    # ENVIRONMENTAL RISK
    # =========================================================

    st.subheader("🌧️ Environmental Risk")

    if current_risk == "LOW":

        st.success(
            "🟢 Low environmental risk."
        )

    elif current_risk == "MEDIUM":

        st.warning(
            "🟡 Moderate risk. Continuous monitoring recommended."
        )

    else:

        st.error(
            "🔴 High risk. Alternative route or delivery hold recommended."
        )

    st.divider()

    # =========================================================
    # ADMIN DECISION
    # =========================================================

    st.subheader("🏛️ Admin Decision")

    decision = st.radio(
        "Select Decision",
        [
            "Approve Delivery",
            "Hold for Review",
            "Reject Delivery"
        ]
    )

    if st.button(
        "⚡ CONFIRM ADMIN DECISION",
        use_container_width=True
    ):

        if decision == "Approve Delivery":

            delivery["status"] = "Approved"

            st.success(
                "✅ DELIVERY APPROVED"
            )

            st.info(
                f"🚚 Driver can now accept the assigned delivery "
                f"and begin {delivery['route']}."
            )

        elif decision == "Hold for Review":

            delivery["status"] = "Pending Approval"

            st.warning(
                "⏸️ DELIVERY ON HOLD"
            )

            st.info(
                "Additional safety or route information is required."
            )

        else:

            delivery["status"] = "Rejected"

            st.error(
                "❌ DELIVERY REJECTED"
            )

            st.info(
                "The delivery request will not proceed."
            )

    st.divider()

    # =========================================================
    # APPROVAL WORKFLOW
    # =========================================================

    st.subheader("🔄 Approval Workflow")

    st.write("📦 Customer Request")
    st.write("↓")
    st.write("🤖 AI Vehicle + Route + Risk Analysis")
    st.write("↓")
    st.write("🏛️ Admin Review")
    st.write("↓")
    st.write("✅ Approval / ⏸️ Hold / ❌ Rejection")
    st.write("↓")
    st.write("🚚 Driver Assignment")


elif page == "Operations Monitoring":


    st.title("📊 Operations Monitoring")
    st.caption("Real-time monitoring of deliveries, vehicles, routes and risk conditions")

    # -----------------------------
    # OPERATIONS DATA
    # -----------------------------
    operations_data = pd.DataFrame({
        "Delivery ID": [
            "SKY-001",
            "SKY-002",
            "SKY-003",
            "SKY-004"
        ],
        "Customer": [
            "Customer A",
            "District Hospital",
            "Hill Area B",
            "Agri Center"
        ],
        "Driver": [
            "Driver 01",
            "Driver 02",
            "Driver 03",
            "Driver 04"
        ],
        "Vehicle": [
            "Truck",
            "Van",
            "Mini Truck",
            "Truck"
        ],
        "Destination": [
            "Remote Village A",
            "District Hospital",
            "Hill Area B",
            "Agri Center"
        ],
        "Status": [
            "In Transit",
            "Approved",
            "Risk Alert",
            "Delivered"
        ],
        "Progress": [
            65,
            0,
            35,
            100
        ],
        "Risk": [
            "Low",
            "Low",
            "High",
            "Low"
        ]
    })

    # -----------------------------
    # SUMMARY
    # -----------------------------
    total = len(operations_data)
    active = len(
        operations_data[
            operations_data["Status"].isin(
                ["Approved", "In Transit", "Risk Alert"]
            )
        ]
    )
    completed = len(
        operations_data[
            operations_data["Status"] == "Delivered"
        ]
    )
    high_risk = len(
        operations_data[
            operations_data["Risk"] == "High"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Deliveries", total)
    col2.metric("Active Operations", active)
    col3.metric("Completed", completed)
    col4.metric("High Risk", high_risk)

    st.divider()

    # -----------------------------
    # FILTER
    # -----------------------------
    st.subheader("🔎 Delivery Monitoring")

    selected_status = st.selectbox(
        "Filter by Status",
        [
            "All",
            "Approved",
            "In Transit",
            "Risk Alert",
            "Delivered"
        ]
    )

    if selected_status == "All":
        filtered_data = operations_data
    else:
        filtered_data = operations_data[
            operations_data["Status"] == selected_status
        ]

    st.dataframe(
        filtered_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------
    # SELECT DELIVERY
    # -----------------------------
    st.subheader("📦 Delivery Details")

    selected_delivery = st.selectbox(
        "Select Delivery",
        operations_data["Delivery ID"]
    )

    delivery = operations_data[
        operations_data["Delivery ID"] == selected_delivery
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Delivery ID:**", delivery["Delivery ID"])
        st.write("**Customer:**", delivery["Customer"])
        st.write("**Driver:**", delivery["Driver"])
        st.write("**Vehicle:**", delivery["Vehicle"])
        st.write("**Destination:**", delivery["Destination"])

    with col2:
        st.write("**Status:**", delivery["Status"])
        st.write("**Risk Level:**", delivery["Risk"])
        st.write("**Progress:**", f'{delivery["Progress"]}%')

        st.progress(
            int(delivery["Progress"]) / 100
        )

    st.divider()

    # -----------------------------
    # ROUTE & VEHICLE STATUS
    # -----------------------------
    st.subheader("🛣️ Route & Vehicle Status")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "🤖 AI Route Recommendation\n\n"
            "Current Route: Route B\n\n"
            "Distance: 145 km\n\n"
            "Travel Time: 4h 30m\n\n"
            "Road Condition: Good\n\n"
            "Risk: Low"
        )

    with col2:
        st.success(
            "🚚 Vehicle Status\n\n"
            "Vehicle: Truck\n\n"
            "Capacity: 5000 kg\n\n"
            "Cargo: 500 kg\n\n"
            "Vehicle Condition: Ready\n\n"
            "GPS: Online"
        )

    st.divider()

    # -----------------------------
    # REGIONAL MAP
    # -----------------------------
    st.subheader("🗺️ Regional Operations Map")

    map_data = pd.DataFrame({
        "latitude": [
            26.1445,
            26.2000,
            26.3000,
            26.1000
        ],
        "longitude": [
            91.7362,
            91.8000,
            91.6500,
            91.9000
        ]
    })

    st.map(
        map_data,
        zoom=9
    )

    st.divider()

    # -----------------------------
    # ADMIN ACTION
    # -----------------------------
    st.subheader("⚙️ Admin Action")

    action = st.selectbox(
        "Select Action",
        [
            "Monitor Delivery",
            "Request Driver Update",
            "Escalate Risk",
            "Approve Route Change",
            "Contact Support"
        ]
    )

    if st.button("Execute Action"):

        if action == "Escalate Risk":
            st.warning(
                "⚠️ Risk escalation sent to the operations team."
            )

        elif action == "Request Driver Update":
            st.info(
                "📡 Driver location and status update requested."
            )

        elif action == "Approve Route Change":
            st.success(
                "🛣️ Alternative route change approved."
            )

        elif action == "Contact Support":
            st.info(
                "📞 Support team has been notified."
            )

        else:
            st.success(
                "✅ Delivery is being monitored."
            )

    st.divider()

    st.success(
        "SKRYPTORA AI Operations Engine: "
        "Delivery + Vehicle + Route + Risk monitoring active."
    )

elif page == "Alerts":

    st.title("🚨 Risk & Disaster Alerts")
    st.caption(
        "AI-powered monitoring of hazards affecting logistics operations"
    )

    # -----------------------------
    # ACTIVE ALERTS
    # -----------------------------
    alerts_data = pd.DataFrame({
        "Alert ID": [
            "ALT-001",
            "ALT-002",
            "ALT-003",
            "ALT-004"
        ],
        "Hazard": [
            "Heavy Rainfall",
            "Road Blockage",
            "Landslide Risk",
            "Connectivity Loss"
        ],
        "Affected Area": [
            "Guwahati Sector",
            "Hill Route B",
            "Remote Hill Area",
            "Remote Village A"
        ],
        "Severity": [
            "Medium",
            "High",
            "High",
            "Medium"
        ],
        "Affected Delivery": [
            "SKY-001",
            "SKY-003",
            "SKY-003",
            "SKY-001"
        ],
        "Recommended Action": [
            "Monitor Route",
            "Switch Route",
            "Stop / Re-route",
            "Use Last-Known Location"
        ]
    })

    # -----------------------------
    # SUMMARY
    # -----------------------------
    high_alerts = len(
        alerts_data[alerts_data["Severity"] == "High"]
    )

    medium_alerts = len(
        alerts_data[alerts_data["Severity"] == "Medium"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Active Alerts",
        len(alerts_data)
    )

    col2.metric(
        "High Severity",
        high_alerts
    )

    col3.metric(
        "Medium Severity",
        medium_alerts
    )

    st.divider()

    # -----------------------------
    # ALERT TABLE
    # -----------------------------
    st.subheader("📋 Active Risk Alerts")

    st.dataframe(
        alerts_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------
    # SELECT ALERT
    # -----------------------------
    st.subheader("🔍 Alert Investigation")

    selected_alert = st.selectbox(
        "Select Alert",
        alerts_data["Alert ID"]
    )

    alert = alerts_data[
        alerts_data["Alert ID"] == selected_alert
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Alert ID:**", alert["Alert ID"])
        st.write("**Hazard:**", alert["Hazard"])
        st.write("**Affected Area:**", alert["Affected Area"])

    with col2:

        st.write("**Severity:**", alert["Severity"])
        st.write(
            "**Affected Delivery:**",
            alert["Affected Delivery"]
        )
        st.write(
            "**Recommended Action:**",
            alert["Recommended Action"]
        )

    # -----------------------------
    # SEVERITY WARNING
    # -----------------------------
    if alert["Severity"] == "High":

        st.error(
            "🚨 HIGH RISK: Immediate operational attention required."
        )

    else:

        st.warning(
            "⚠️ MEDIUM RISK: Continue monitoring environmental conditions."
        )

    st.divider()

    # -----------------------------
    # AI RESPONSE
    # -----------------------------
    st.subheader("🤖 AI Risk Response")

    if alert["Hazard"] == "Road Blockage":

        st.info(
            "AI Recommendation:\n\n"
            "1. Detect blocked road\n"
            "2. Stop current route\n"
            "3. Search alternative route\n"
            "4. Notify driver\n"
            "5. Notify customer\n"
            "6. Update admin dashboard"
        )

    elif alert["Hazard"] == "Landslide Risk":

        st.info(
            "AI Recommendation:\n\n"
            "1. Restrict movement through affected zone\n"
            "2. Identify safer route\n"
            "3. Alert driver\n"
            "4. Update delivery ETA\n"
            "5. Escalate if no safe route exists"
        )

    elif alert["Hazard"] == "Connectivity Loss":

        st.info(
            "AI Recommendation:\n\n"
            "Switch to LAST-KNOWN LOCATION mode "
            "and continue monitoring until connectivity returns."
        )

    else:

        st.info(
            "AI Recommendation:\n\n"
            "Continue monitoring weather and route conditions."
        )

    st.divider()

    # -----------------------------
    # EMERGENCY ACTION
    # -----------------------------
    st.subheader("🚑 Emergency Response")

    action = st.selectbox(
        "Select Emergency Action",
        [
            "Notify Driver",
            "Notify Customer",
            "Switch to Alternative Route",
            "Stop Delivery",
            "Escalate to Authority",
            "Activate Emergency Support"
        ]
    )

    if st.button("🚨 Execute Emergency Action"):

        if action == "Notify Driver":

            st.success(
                "📡 Emergency alert sent to the driver."
            )

        elif action == "Notify Customer":

            st.success(
                "📱 Customer has been notified about the risk."
            )

        elif action == "Switch to Alternative Route":

            st.success(
                "🛣️ AI alternative route activated: Route C."
            )

        elif action == "Stop Delivery":

            st.error(
                "⛔ Delivery temporarily stopped for safety."
            )

        elif action == "Escalate to Authority":

            st.warning(
                "🏛️ Alert escalated to the responsible authority."
            )

        else:

            st.error(
                "🚑 Emergency support request activated."
            )

    st.divider()

    # -----------------------------
    # DISASTER WORKFLOW
    # -----------------------------
    st.subheader("🌐 Disaster Response Workflow")

    st.write(
        "Hazard Detection → Risk Analysis → "
        "Route Recalculation → Driver Alert → "
        "Customer Notification → Admin/Authority Escalation"
    )

    st.success(
        "SKRYPTORA continuously monitors logistics risks "
        "and supports safer delivery decisions."
    )

elif page == "Support & Escalation":

    st.title("🆘 Support & Escalation")
    st.caption(
        "Customer issues, returns, dealer interaction and emergency case management"
    )

    # -----------------------------
    # SUPPORT CASE DATA
    # -----------------------------
    support_data = pd.DataFrame({
        "Case ID": [
            "CASE-001",
            "CASE-002",
            "CASE-003",
            "CASE-004"
        ],
        "Delivery ID": [
            "SKY-001",
            "SKY-002",
            "SKY-003",
            "SKY-004"
        ],
        "Customer": [
            "Customer A",
            "Customer B",
            "Customer C",
            "Customer D"
        ],
        "Issue": [
            "Damaged Product",
            "Late Delivery",
            "Route Emergency",
            "No Issue"
        ],
        "Priority": [
            "High",
            "Medium",
            "Critical",
            "Low"
        ],
        "Dealer": [
            "Dealer A",
            "Dealer B",
            "Dealer C",
            "Dealer D"
        ],
        "Status": [
            "Open",
            "Under Review",
            "Escalated",
            "Resolved"
        ]
    })

    # -----------------------------
    # SUMMARY
    # -----------------------------
    total_cases = len(support_data)

    open_cases = len(
        support_data[
            support_data["Status"] == "Open"
        ]
    )

    escalated_cases = len(
        support_data[
            support_data["Status"] == "Escalated"
        ]
    )

    resolved_cases = len(
        support_data[
            support_data["Status"] == "Resolved"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Cases",
        total_cases
    )

    col2.metric(
        "Open Cases",
        open_cases
    )

    col3.metric(
        "Escalated",
        escalated_cases
    )

    col4.metric(
        "Resolved",
        resolved_cases
    )

    st.divider()

    # -----------------------------
    # CASE TABLE
    # -----------------------------
    st.subheader("📋 Support Cases")

    st.dataframe(
        support_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------
    # SELECT CASE
    # -----------------------------
    st.subheader("🔍 Case Investigation")

    selected_case = st.selectbox(
        "Select Case",
        support_data["Case ID"]
    )

    case = support_data[
        support_data["Case ID"] == selected_case
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Case ID:**", case["Case ID"])
        st.write("**Delivery ID:**", case["Delivery ID"])
        st.write("**Customer:**", case["Customer"])
        st.write("**Issue:**", case["Issue"])

    with col2:

        st.write("**Priority:**", case["Priority"])
        st.write("**Dealer:**", case["Dealer"])
        st.write("**Status:**", case["Status"])

    # -----------------------------
    # PRIORITY ALERT
    # -----------------------------
    if case["Priority"] == "Critical":

        st.error(
            "🚨 CRITICAL CASE: Immediate escalation required."
        )

    elif case["Priority"] == "High":

        st.warning(
            "⚠️ HIGH PRIORITY: Admin review required."
        )

    else:

        st.info(
            "ℹ️ Standard support case."
        )

    st.divider()

    # -----------------------------
    # DEALER INTERACTION
    # -----------------------------
    st.subheader("🏪 Dealer Interaction")

    dealer_action = st.selectbox(
        "Dealer Action",
        [
            "Request Product Verification",
            "Request Replacement",
            "Confirm Product Availability",
            "Request Delivery Update",
            "No Dealer Action"
        ]
    )

    if st.button("📨 Contact Dealer"):

        st.success(
            f"Dealer action requested: {dealer_action}"
        )

    st.divider()

    # -----------------------------
    # ADMIN CASE ACTION
    # -----------------------------
    st.subheader("⚙️ Admin Case Action")

    case_action = st.selectbox(
        "Select Case Action",
        [
            "Keep Case Open",
            "Assign Support Team",
            "Escalate Case",
            "Approve Replacement",
            "Approve Return",
            "Resolve Case"
        ]
    )

    if st.button("✅ Execute Case Action"):

        if case_action == "Keep Case Open":

            st.info(
                "📂 Case remains open for further investigation."
            )

        elif case_action == "Assign Support Team":

            st.success(
                "👨‍💼 Support team assigned to this case."
            )

        elif case_action == "Escalate Case":

            st.warning(
                "🚨 Case escalated to senior administration."
            )

        elif case_action == "Approve Replacement":

            st.success(
                "🔄 Product replacement approved."
            )

        elif case_action == "Approve Return":

            st.success(
                "📦 Product return approved."
            )

        else:

            st.success(
                "✅ Case marked as resolved."
            )

    st.divider()

    # -----------------------------
    # ESCALATION LEVEL
    # -----------------------------
    st.subheader("🚨 Escalation Management")

    escalation_level = st.selectbox(
        "Escalation Level",
        [
            "Level 1 - Support Team",
            "Level 2 - Dealer",
            "Level 3 - Operations Admin",
            "Level 4 - Emergency Authority"
        ]
    )

    if st.button("🚨 Escalate"):

        st.warning(
            f"Case {selected_case} escalated to "
            f"{escalation_level}."
        )

    st.divider()

    # -----------------------------
    # COMPLETE SUPPORT WORKFLOW
    # -----------------------------
    st.subheader("🔄 Support Resolution Workflow")

    st.write(
        "Customer Feedback → Issue Detection → "
        "Case Registration → Dealer Interaction → "
        "Admin Review → Escalation if Required → "
        "Return / Replacement → Case Resolution"
    )

    st.success(
        "SKRYPTORA Support & Escalation system is active."
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "SKRYPTORA | AI-Powered Smart Logistics Accessibility "
    "& Delivery Management | SIH 2026 Prototype"
)