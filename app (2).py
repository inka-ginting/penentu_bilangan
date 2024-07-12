import streamlit as st

# Dictionary berisi daftar unsur kimia dan massa relatif atomnya
atomic_masses = {
    "Hidrogen": 1.008,
    "Helium": 4.0026,
    "Lithium": 6.94,
    "Boron": 10.81,
    "Carbon": 12.011,
    "Nitrogen": 14.007,
    "Oxygen": 15.999,
    "Neon": 20.180,
    "Sodium": 22.990,
    "Magnesium": 24.305,
    "Aluminum": 26.982,
    "Silicon": 28.085,
    "Phosphorus": 30.974,
    "Sulfur": 32.06,
    "Chlorine": 35.45,
    "Potassium": 39.098,
    "Calcium": 40.078,
}

# Set judul aplikasi Streamlit
st.title('Aplikasi Penentuan Massa Relatif Atom')

# Deskripsi aplikasi
st.write('Aplikasi ini membantu Anda menentukan massa relatif atom dari unsur kimia.')

try:
    # Pilihan unsur kimia dari dropdown
    selected_element = st.selectbox("Pilih unsur kimia:", list(atomic_masses.keys()))

    # Tampilkan massa relatif atom untuk unsur yang dipilih
    mass_relative = atomic_masses[selected_element]
    st.write(f"Massa relatif atom dari {selected_element} adalah {mass_relative}.")
except KeyError:
    st.error("Unsur kimia yang Anda pilih tidak ditemukan dalam database.")

# Menambahkan footer atau informasi tambahan
st.write("")
st.write("Sumber data: National Institute of Standards and Technology (NIST)")



