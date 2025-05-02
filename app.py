import streamlit as st

# Read plate number from query params
query_params = st.experimental_get_query_params()
plate = query_params.get("plate", [None])[0]

if plate:
    st.title("🚨 Traffic Fine Alert")
    st.markdown(f"**Vehicle Number:** {plate}")
    st.warning("You have been detected riding without a helmet.")
    st.info("As per traffic rules, a fine has been imposed.")

    if "paid" not in st.session_state:
        st.session_state.paid = False

    if not st.session_state.paid:
        if st.button("💳 Pay Now"):
            st.session_state.paid = True
            st.success("✅ You have paid your fine. Drive safe!")
    else:
        st.success("✅ You have already paid your fine.")
else:
    st.info("No vehicle plate detected.")
