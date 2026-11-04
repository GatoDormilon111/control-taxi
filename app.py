import streamlit as st

st.set_page_config(page_title="Control Diario Taxista", page_icon="🚕", layout="centered")

st.title("🚕 Control de Ganancias y Costos")
st.write("Calcula tu ganancia neta real descontando comisiones, combustible y desgaste.")

# Entradas de datos
col1, col2 = st.columns(2)

with col1:
    ingreso_bruto = st.number_input("Ingreso Bruto (S/.)", min_value=0.0, value=150.0, step=10.0)
    km_recorridos = st.number_input("Km Recorridos", min_value=0.0, value=80.0, step=5.0)

with col2:
    gasto_combustible = st.number_input("Combustible (S/.)", min_value=0.0, value=35.0, step=5.0)
    comision_pct = st.slider("Comisión App (%)", min_value=0, max_value=35, value=20)

# Parámetro de desgaste/mantenimiento
tasa_desgaste = st.number_input("Fondo Desgaste por Km (S/.)", min_value=0.05, max_value=0.50, value=0.15, step=0.01)

# Cálculos
comision_monto = ingreso_bruto * (comision_pct / 100)
costo_mantenimiento = km_recorridos * tasa_desgaste
costos_totales = gasto_combustible + comision_monto + costo_mantenimiento
ganancia_neta = ingreso_bruto - costos_totales

costo_por_km = (costos_totales / km_recorridos) if km_recorridos > 0 else 0
margen_por_km = (ganancia_neta / km_recorridos) if km_recorridos > 0 else 0

st.divider()

# Métricas destacadas
st.subheader("Balance del Día")
m1, m2 = st.columns(2)
m1.metric(label="Ganancia Neta Real", value=f"S/. {ganancia_neta:.2f}")
m2.metric(label="Margen por Km", value=f"S/. {margen_por_km:.2f}/km")

with st.expander("Ver desglose de costos detallado"):
    st.write(f"- **Comisión retenida:** S/. {comision_monto:.2f}")
    st.write(f"- **Combustible:** S/. {gasto_combustible:.2f}")
    st.write(f"- **Reserva mantenimiento:** S/. {costo_mantenimiento:.2f}")
    st.write(f"- **Costo operativo total:** S/. {costos_totales:.2f}")
