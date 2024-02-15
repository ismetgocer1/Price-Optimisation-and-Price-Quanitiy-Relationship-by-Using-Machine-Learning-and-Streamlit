import streamlit as st
import pandas as pd
import pickle

# CSS Stillerini Ekleyin
def set_css():
    st.markdown(
        """
        <style>
        .stNumberInput, .stTextInput {
            margin-top: -25px;    /* Kutuların üst etiketlere olan boşluğunu azalt */
            margin-bottom: -5px;  /* Kutuların alt etiketlere olan boşluğunu azalt */
        }
        .stNumberInput > div > div, .stTextInput > div > div {
            padding-top: 0px;    /* Kutu içi üst boşluğu azalt */
            padding-bottom: 0px; /* Kutu içi alt boşluğu azalt */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
st.sidebar.title("Price Optimisation and Price - Quantity Relationship Machine Learning Algorithms")

# Her sayfa için bir fonksiyon tanımlayın
def teorik():
    st.title('Price Optimisation')
    
    st.markdown("""
    **Not:** This analysis is done on a per ASIN basis.    

    **R = P – C ** 
    
    **R: Revenue (USD) **
    
    **P: Price (USD) **
    
    **C: Cost (USD) ** 
    
    P = Selling price of the product in Canada
    
    C = Purchase price of product from US + OneAMZ Intermediate Wharehouse Handling Fee + Amazon Fee

    As can be seen in the bottom graph, there is an inverted U-shaped relationship between revenue and price.
    """)
    # Resmi göster
    #st.image("/mnt/data/image.png", use_column_width=True)
    st.image("resim.jpg",  width=500)
    # Metni göster
    st.markdown("""
<style>
.red-text { color: red; }
</style>

Now let's turn this inverted U-shaped relationship into an equation:

<span class="red-text">R = β₀ + β₁P + β₂P² + β₃Q + β₄BSRSub + β₅SellerNumbers + β₆Rating + β₇ReviewNumbers</span><br><br>

In this model, the most important part for price optimization is; <span class="red-text">R = β₀ + β₁P + β₂P²</span>. Other variables are included in the model as additional explanatory variables .<br><br>

After estimating this model with Machine Learning algorithms, the partial derivative of R with respect to P is taken and set equal to zero. This is because in an inverted U-shaped function, at the point where income is maximum, the slope of the tangent (1st derivative) will be equal to zero.<br><br>

<span class="red-text">R' = β₁ + 2β₂P = 0</span><br><br>

<span class="red-text">P = -β₁ / (2β₂)</span><br><br>

Thus, the income-maximizing price (P), i.e. the optimum price level, will be found.
""", unsafe_allow_html=True)
    
# Fiyat Optimizasyon Sayfasını Tanımlayın
def price_optimization_page():
    selected_asin = st.sidebar.selectbox("Select an ASIN", ["B00FS3VJAO", "B0779LHFMF", "B0811VD9MY"])

    # Ürün Bilgilerini Göster
    if selected_asin == "B00FS3VJAO":
        st.image("B00FS3VJAO.jpg", caption="Product Photo", width=180)
        # Kullanıcı girdilerini al
        input_data = {}
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**Purchase Price from the US($):**")
            input_data['us_purchase_price'] = st.number_input('', value=39.99 )  
        with col3:
            st.markdown("**Sales Price at Canada($):**")
            input_data['us_sellin_price'] = st.number_input('', value=56.65)
        with col5:
            st.markdown("**Amazon Fee($):**")
            input_data['amazon_fee'] = st.number_input('', value=17.16)
    
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        with col7:
            st.markdown("**Wharehouse Handling Fee($):**")
            input_data['oneamz_fee'] = st.number_input('', value=42.78)  
        with col9:
            st.markdown("**Sub Category Sales Rank:**")
            input_data['Sub_Sales_Rank'] = st.number_input('', value=4)
        with col11:
            st.markdown("**Daily Sales Number:**")
            input_data['daily_sales'] = st.number_input('', value=48)
        col13, col14, col15, col16,col17,col18 = st.columns(6)
        with col13:
            st.markdown("**Rewiew Number:**")
            input_data['mnumber_of_reviews'] = st.number_input('', value=8904)
        with col15:
            st.markdown("**Seller Number:**")
            input_data['number_of_floods'] = st.number_input('', value=1)
        with col17:
            st.markdown("**Rating:**")
            input_data['rating'] = st.number_input('', value=4.2)
        col19, col20, col21, col22,col23,col24 = st.columns(6)
        with col19:
            st.markdown("**Optimum Selling Price Calculated for Canada($):**")
            input_data['optimum_price'] = st.number_input('', value=114.41)
        with col21:
            st.markdown("**Net Profit for Seller($):**")
            input_data['Remaining_Profit_to_OneAMZ_Seller'] = st.number_input('', value=22.59)
        with col23:
            st.markdown("**Net Profit Ratio of Seller(%):**")
            input_data['Net_Profit_Remaining_for_OneAMZ_Seller'] = st.number_input('', value=24.60)
        
        
       
     # Ürün Bilgilerini Göster
    elif selected_asin == "B0779LHFMF":
        st.image("B0779LHFMF.jpg", caption="Product Photo", width=180)
        # Kullanıcı girdilerini al
        input_data = {}
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**Purchase Price from the US($):**")
            input_data['us_purchase_price'] = st.number_input('', value=32.99 )  
        with col3:
            st.markdown("**Sales Price at Canada($):**")
            input_data['us_sellin_price'] = st.number_input('', value=34.62)
        with col5:
            st.markdown("**Wharehouse Handling Fee($):**")
            input_data['amazon_fee'] = st.number_input('', value=10.12)
    
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        with col7:
            st.markdown("**Wharehouse Handling Fee($)):**")
            input_data['oneamz_fee'] = st.number_input('', value=15.75)  
        with col9:
            st.markdown("**Sub Category Sales Rank:**")
            input_data['Sub_Sales_Rank'] = st.number_input('', value=4)
        with col11:
            st.markdown("**Daily Sales Number:**")
            input_data['daily_sales'] = st.number_input('', value=174)
        col13, col14, col15, col16,col17,col18 = st.columns(6)
        with col13:
            st.markdown("**Rewiew Number:**")
            input_data['mnumber_of_reviews'] = st.number_input('', value=42352)
        with col15:
            st.markdown("**Seller Number:**")
            input_data['number_of_floods'] = st.number_input('', value=2)
        with col17:
            st.markdown("**Rating:**")
            input_data['rating'] = st.number_input('', value=4.4)
        col19, col20, col21, col22,col23,col24 = st.columns(6)
        with col19:
            st.markdown("**Optimum Selling Price Calculated for Canada($):**")
            input_data['optimum_price'] = st.number_input('', value=67.46)
        with col21:
            st.markdown("**Net Profit for Seller($):**")
            input_data['Remaining_Profit_to_OneAMZ_Seller'] = st.number_input('', value=11.60)
        with col23:
            st.markdown("**Net Profit Ratio of Seller(%):**")
            input_data['Net_Profit_Remaining_for_OneAMZ_Seller'] = st.number_input('', value=20.77)
            
        
         # Ürün Bilgilerini Göster
    elif selected_asin == "B0811VD9MY":
        st.image("B0811VD9MY.jpg", caption="Ürün Resmi", width=160)
        # Kullanıcı girdilerini al
        input_data = {}
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**Purchase Price from the US($):**")
            input_data['us_purchase_price'] = st.number_input('', value=13.39)  
        with col3:
            st.markdown("**Sales Price at Canada($):**")
            input_data['us_sellin_price'] = st.number_input('', value=10.1)
        with col5:
            st.markdown("**Amazon Fee($):**")
            input_data['amazon_fee'] = st.number_input('', value=6.10)
    
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        with col7:
            st.markdown("**Wharehouse Handling Fee($):**")
            input_data['oneamz_fee'] = st.number_input('$', value=13.53)  
        with col9:
            st.markdown("**Sub Category Sales Rank:**")
            input_data['Sub_Sales_Rank'] = st.number_input('', value=25)
        with col11:
            st.markdown("**Daily Sales Number:**")
            input_data['daily_sales'] = st.number_input('', value=3)
        col13, col14, col15, col16,col17,col18 = st.columns(6)
        with col13:
            st.markdown("**Rewiew Number:**")
            input_data['mnumber_of_reviews'] = st.number_input('', value=69)
        with col15:
            st.markdown("**Seller Number:**")
            input_data['number_of_floods'] = st.number_input('', value=18)
        with col17:
            st.markdown("**Rating:**")
            input_data['rating'] = st.number_input('', value=2.7)
        col19, col20, col21, col22,col23,col24 = st.columns(6)
        with col19:
            st.markdown("**Optimum Selling Price Calculated for Canada($):**")
            input_data['optimum_price'] = st.number_input('', value=40.69)
        with col21:
            st.markdown("**Net Profit for Seller($):**")
            input_data['Remaining_Profit_to_OneAMZ_Seller'] = st.number_input('', value=5.08)
        with col23:
            st.markdown("**Net Profit Ratio of Seller(%):**")
            input_data['Net_Profit_Remaining_for_OneAMZ_Seller'] = st.number_input('', value=14.26)

def Fiyat_Miktar_İlişkisi():
    st.title('Price-Quantity Relation')
    
    st.markdown("""
    **About Dataset:**

    - Q: Quantity (
    - P: Price 

    **Model: P = β₀ + β₁ * Q**
    """)

    # Grafik dosyanızın adını ve yolunu güncelleyin
    st.image("resim33.png", caption="Price - Quantity Graph", width=600)
    
    st.markdown("""
    **Demand Law in Economics:** As the price of a product decreases, the quantity demanded will increase.. 
    
    This analysis conducted for B00FS3VJAO ASIN number product as an example. 
    """)

# Sayfa 4 Fonksiyonu
def page4():
    st.title('Price - Quantity')
    
    # Grafik dosyanızın adını ve yolunu güncelleyin
    st.image("B00FS3VJAO.jpg", caption="B00FS3VJAO", width=100)
    st.image("resim44.png", caption="B00FS3VJAO", width=600)
    
    # Denklemi kırmızı ve büyük fontla, ortalanmış şekilde göster
    st.markdown("""
    <h3 style="color:red; text-align:center;">Q = 286.92 - 2.38*P</h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Price($):**")
        price = st.number_input('', value=10.00)
        
    miktar=286.92-2.38*price
        
    with col2:
        st.markdown("**Quantity:**")
        st.info(miktar)  

# Sidebar Menüsü
def sidebar_navigation():
    page = st.sidebar.radio('Chose a Page:', ('Price Optimisation Theorical Framework', 'Price Optimisation Application', 'Price - Quantity Relation Theorical Framework', 'Price - Quantity Relation Application'))

    if page == 'Price Optimisation Theorical Framework':
        teorik()
    elif page == 'Price Optimisation Application':
        price_optimization_page()
    elif page == 'Price - Quantity Relation Theorical Framework':
        Fiyat_Miktar_İlişkisi()  # Burada uygun fonksiyon çağrısını yapın.
    elif page == 'Price - Quantity Relation Application':
        page4()

# Ana fonksiyon
def main():
    set_css()
    sidebar_navigation()

# Ana fonksiyonu çağırın
if __name__ == "__main__":
    main()
