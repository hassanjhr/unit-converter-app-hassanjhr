import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

# Custom CSS for Stylish UI
def set_custom_css():
    st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
        }
        .stApp {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            max-width: 900px;
            margin: auto;
            color: white;
        }
        h1 {
           
            color: black;
            text-align: center;
            padding: 10px;
            border-radius: 5px;
        }
        .conversion-box {
            background-color: #333333;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
            color: white;
        }
        .stButton>button {
            background-color: #ff9800;
            color: black;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }
        input[type=text] {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_custom_css()

# Streamlit UI
st.title(" 🔄 Google Unit Converter App")
st.markdown("---")
st.markdown("### ⚡ Convert Length, Mass, Area, Speed, Time, and Volume Instantly!")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("📌 Choose a category", ["📏 Length", "⚖️ Mass", "📐 Area", "💨 Speed", "⏱️ Time", "🛢️ Volume"])

# Global dictionary for unit conversions
conversions = {
    "📏 Length": {
        "Meters": {"Centimeters": 100, "Kilometers": 0.001, "Miles": 0.000621371},
        "Centimeters": {"Meters": 0.01, "Kilometers": 1e-5},
        "Kilometers": {"Meters": 1000, "Miles": 0.621371},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934}
    },
    "⚖️ Mass": {
        "Kilogram": {"Gram": 1000, "Milligram": 1e6, "Metric Ton": 0.001, "Pound": 2.20462, "Ounce": 35.274},
        "Gram": {"Kilogram": 0.001},
        "Pound": {"Kilogram": 0.453592},
    },
    "📐 Area": {
        "Square Metre": {"Square Kilometre": 1e-6, "Square Centimetre": 10000, "Square Millimetre": 1e6, "Hectare": 1e-4, "Acre": 0.000247105},
    },
    "💨 Speed": {
        "Metre per Second": {"Kilometre per Hour": 3.6, "Mile per Hour": 2.23694, "Foot per Second": 3.28084, "Knot": 1.94384},
    },
    "⏱️ Time": {
        "Second": {"Minute": 1/60, "Hour": 1/3600, "Day": 1/86400, "Week": 1/604800},
        "Minute": {"Second": 60},
        "Hour": {"Minute": 60},
        "Day": {"Hour": 24},
    },
    "🛢️ Volume": {
        "Cubic Metre": {"Litre": 1000, "Millilitre": 1e6, "Gallon (US)": 264.172, "Gallon (UK)": 219.969, "Cubic Inch": 61023.7, "Cubic Foot": 35.3147},
    },
}

def convert_units(category, value, from_unit, to_unit):
    if from_unit in conversions[category] and to_unit in conversions[category][from_unit]:
        return value * conversions[category][from_unit][to_unit]
    return None

st.markdown("---")

from_unit = st.selectbox("🔄 From Unit", list(conversions[category].keys()))
to_unit = st.selectbox("🔄 To Unit", list(conversions[category][from_unit].keys()))

value = st.text_input("✍️ Enter the value to convert (Manually Type the Number)")

if st.button("🚀 Convert"):
    try:
        value = float(value)
        result = convert_units(category, value, from_unit, to_unit)
        if result is not None:
            st.success(f"✅ The result is {result:.2f} {to_unit}")
        else:
            st.error("❌ Invalid conversion.")
    except ValueError:
        st.error("❌ Please enter a valid numeric value.")


