import streamlit as st
import qrcode
from io import BytesIO
import time  # Import time for simulating processing

# Page Configuration
st.set_page_config(page_title="QR Code Generator", layout="centered")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #E9E8E8;  /* Purple background */
            color: black;  /* Text color */
        }
        [data-testid="stSidebar"] .stTextInput>div>div>input {
            background-color: white; /* Input box background */
            color: black; /* Input text color */
        }
    </style>
""", unsafe_allow_html=True)

# Apply custom CSS for white warning box
st.markdown("""
    <style>
        div.stAlert {
            background-color: white !important;
            color: black !important;
            border: 1px solid #FFC107 !important; /* Keeps the warning look */
            padding: 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)



# Custom CSS for better styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #E6D9A2, #8967B3);
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: white;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
# st.markdown('<p class="title">🔳 QR Code Generator</p>', unsafe_allow_html=True)
# st.markdown('<p class="subtitle">Enter text or a URL to generate a QR code.</p>', unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns([1, 6])  # Adjust width ratio as needed

# Display the image in the first column
with col1:
    st.image("qr.png", width=100)

# Display the title in the second column
with col2:

    st.title("QR Code Generator")

   
st.write("Enter text or a URL to generate a QR code.")


# Sidebar Input
st.sidebar.header("🛠️Customize Your QR Code")
text = st.sidebar.text_input("Enter text or URL:", placeholder="Type here...")

# QR Code Generation
if text:
    with st.spinner("Generating QR Code..."):  # Show processing animation
        time.sleep(2)  # Simulating processing time

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Convert to Image
    img = qr.make_image(fill="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Display QR Code
    st.image(img_bytes, caption="📸 Generated QR Code", use_container_width=False)

    # Download Button
    st.download_button(
        label="⬇️ Download QR Code",
        data=img_bytes,
        file_name="qrcode.png",
        mime="image/png"
    )
    st.write("Hope  You  Enjoy  Using   This   App😊")
else:
    st.warning("🤖 Please enter some text to generate a QR code.")





















# import streamlit as st
# import requests

# Streamlit App Title
# st.title("🍽️ Recipe Finder")
# st.write("Enter an ingredient to find recipes!")

# User Input
# ingredient = st.text_input("Enter an ingredient (e.g., chicken, tomato):")

# if ingredient:
#     API_URL = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
#     response = requests.get(API_URL)
    
#     if response.status_code == 200:
#         data = response.json()
#         meals = data.get("meals")

#         if meals:
#             for meal in meals:
#                 st.subheader(meal["strMeal"])  
#                 st.image(meal["strMealThumb"], width=300) 
                
                # Full Recipe Button
    #             recipe_url = f"https://www.themealdb.com/meal/{meal['idMeal']}"
    #             st.markdown(f"[👉 Full Recipe]({recipe_url})", unsafe_allow_html=True)
                
    #     else:
    #         st.error("No recipes found. Try another ingredient.")
    # else:
    #     st.error("Failed to fetch recipes. Try again later.")






























# import streamlit as st
# import request

# Set page config to add a custom title and favicon (icon in browser tab)
# st.set_page_config(
#     page_title="Recipe Finder",  # Title that appears in the browser tab
#     page_icon="/assets/book.png" , # Path to your favicon file (local or URL)
#     layout="centered"  # Optional: Choose layout (centered, wide)
# )

# Your Streamlit app content
# st.title("🍽️  Welcome to Recipe Finder!")
# st.write("Find delicious recipes based on the ingredients you have!")

# Input ingredients
# ingredients = st.text_input("Enter an ingredient to find recipes!  (e.g., chicken, tomato):")


# if ingredient:
#     API_URL = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
#     response = requests.get(API_URL)
#     if response.status_code == 200:
#         data = response.json()
#         if data['meals']:
#             for meal in data['meals']:
#                 st.subheader(meal['strMeal'])
#                 st.image(meal['strMealThumb'])
#                 st.write(f"Recipe ID: {meal['idMeal']}")
#         else:
#             st.write("No recipes found for this ingredient.")
#     else:
#         st.write("Error fetching data from TheMealDB.")







# Example Recipe Finder
# st.set_page_config(page_title="")
# st.title("Recipe Finder")


# Button to trigger recipe search
# if st.button("Find Recipes") and ingredients:

# Example of a recipe search API (replace with actual API or web scraping)
    # response = requests.get(f"={ingredients}")
    # recipes = response.json()    



# http://www.recipepuppy.com/api/