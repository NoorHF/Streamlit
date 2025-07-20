import streamlit as st
import numpy as np
import joblib

st.title('Expresso Churn Prediction')

REGION = st.selectbox("REGION", [
    'FATICK', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK',
    'THIES', 'SAINT-LOUIS', 'KOLDA', 'KAFFRINE',
    'DIOURBEL', 'ZIGUINCHOR', 'MATAM', 'SEDHIOU', 'KEDOUGOU'
])

TENURE = st.number_input("TENURE")
MONTANT = st.number_input("MONTANT")
FREQUENCE_RECH = st.number_input("FREQUENCE_RECH")
REVENUE = st.number_input("REVENUE")
ARPU_SEGMENT = st.number_input("ARPU_SEGMENT")
FREQUENCE = st.number_input("FREQUENCE")
DATA_VOLUME = st.number_input("DATA_VOLUME")
ON_NET = st.number_input("ON_NET")
ORANGE = st.number_input("ORANGE")
TIGO = st.number_input("TIGO")
ZONE1 = st.number_input("ZONE1")
ZONE2 = st.number_input("ZONE2")
MRG = st.number_input("MRG")
REGULARITY = st.number_input("REGULARITY")
TOP_PACK = st.number_input("TOP_PACK")
FREQ_TOP_PACK = st.number_input("FREQ_TOP_PACK")

region_map = {
    'FATICK': 0, 'DAKAR': 1, 'LOUGA': 2, 'TAMBACOUNDA': 3, 'KAOLACK': 4,
    'THIES': 5, 'SAINT-LOUIS': 6, 'KOLDA': 7, 'KAFFRINE': 8,
    'DIOURBEL': 9, 'ZIGUINCHOR': 10, 'MATAM': 11, 'SEDHIOU': 12, 'KEDOUGOU': 13
}
region_encoded = region_map.get(REGION, -1)

test_data = np.array([
    region_encoded, TENURE, MRG, TOP_PACK, MONTANT, FREQUENCE_RECH, REVENUE,
    ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO, ZONE1, ZONE2,
    REGULARITY, FREQ_TOP_PACK
]).reshape(1, -1)

model = joblib.load(r'C:\Users\batta\Desktop\Streamlit\model.pkl')

if st.button('Predict'):
    prediction = model.predict(test_data)
    if prediction[0] == 1:
        st.error("This client is likely to churn.")
    else:
        st.success("This client is likely to stay.")
