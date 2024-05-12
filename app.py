import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header
from streamlit_elements import elements, mui, nivo
from streamlit_echarts import st_echarts 
import streamlit_echarts
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

def horizontal_line():
    st.markdown('<hr>', unsafe_allow_html=True)
    
def enter():
    st.markdown('<br>', unsafe_allow_html=True)
    
def logo_link(link, path_img, width):
    st.markdown(
        """<div style="display: grid; place-items: center;">
        <a href="{}">
        <img src="data:image/png;base64,{}" width="{}">
        </a></div>""".format(
            link,
            base64.b64encode(open(path_img, "rb").read()).decode(),
            width,
        ),
        unsafe_allow_html=True,
    )    
   
st.set_page_config(
    page_title='MoF - Kemiskinan Jawa Barat',
    layout='wide'
)

with st.sidebar:
    st.markdown("""
        <div style='text-align: center; font-size:24px'>
            <b>
            Kemiskinan Jawa Barat <br>
            </b>
        </div>
    """, unsafe_allow_html=True)
    
    enter()

    logo_link('', r'img/logo-jabar.png', 125)
    enter()
    horizontal_line()

    selected = option_menu(menu_title=None, 
                          options=["Home", 'IPM', 'Trend IHK', 'Pekerja'], 
                          icons=['house'], 
                          menu_icon="cast", default_index=0
                        )
    
    horizontal_line()
    
    st.markdown("""
        <div style='text-align: center; font-size:24px'>
            <b>Created By</b> 
        </div>
    """, unsafe_allow_html=True)
    # enter()
    st.markdown("""
        <div style='text-align: center; font-size:20px'>
            Sherly Santiadi
            <br>
            Marselius Agus Dhion
        </div>
    """, unsafe_allow_html=True)

    horizontal_line()
    
    st.markdown("""
        <div style='text-align: center; font-size:20px'>
            <b>Data Source</b> <br>
            BPS Jawa Barat
        </div>
    """, unsafe_allow_html=True)
    
    
    # st.write('[Source Data]')


    
if selected == 'Home':
    # colored_header(
    #     label="Kemiskinan di Jawa Barat (General)",
    #     description="",
    #     color_name="orange-70",
    # )
    
    # enter()
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b> Metrics Year 2022 vs 2021</b>
        </div>
    """, unsafe_allow_html=True)   
    horizontal_line()
    
    enter()
     
    df = pd.read_csv(r'data/csv/metrics.csv')
    
    def metric_cards_1():
        _, _, metric_idx_p1, metric_idx_penduduk, metric_idx_p2, _, _ = st.columns([2,2,3,3,3,2,2])                
        
        # Indeks Kedalaman Kemiskinan (P1)
        idx_before = df[df['Tahun'] == 2021]['Indeks Kedalaman Kemiskinan'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Indeks Kedalaman Kemiskinan'].mean()
        delta_idx = idx_latest - idx_before
        metric_idx_p1.metric(label="Indeks Kedalaman Kemiskinan (P1)", value=round(idx_latest, 2), delta=round(delta_idx, 2))
        
        # Indeks Keparahan Kemiskinan (P2)
        idx_before = df[df['Tahun'] == 2021]['Indeks Keparahan Kemiskinan'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Indeks Keparahan Kemiskinan'].mean()
        delta_idx = idx_latest - idx_before
        metric_idx_p2.metric(label="Indeks Keparahan Kemiskinan (P2)", value=round(idx_latest, 2), delta=round(delta_idx, 2))
        
        # Jumlah Penduduk Miskin
        idx_before = df[df['Tahun'] == 2021]['Jumlah Penduduk Miskin'].sum()
        idx_latest = df[df['Tahun'] == 2022]['Jumlah Penduduk Miskin'].sum()
        delta_idx = idx_latest - idx_before
        metric_idx_penduduk.metric(label="Jumlah Penduduk Miskin (Ribu)", value=round(idx_latest, 2), delta=round(delta_idx, 0))

        style_metric_cards(background_color='#0E1117', border_radius_px=20)
        
    def metric_cards_2():
        _, metric_idx_kesehatan, metric_ipm, metric_idx_pendidikan, metric_idx_pengeluaran, _ = st.columns([1,1,1,1,1,1])                
        
        # Indeks Kesehatan
        idx_before = df[df['Tahun'] == 2021]['Indeks Kesehatan'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Indeks Kesehatan'].mean()
        delta_idx = idx_latest - idx_before
        metric_idx_kesehatan.metric(label="Indeks Kesehatan", value=round(idx_latest, 2), delta=round(delta_idx, 2))
        
        # Indeks Pembangunan Manusia
        idx_before = df[df['Tahun'] == 2021]['Indeks Pembangunan Manusia'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Indeks Pembangunan Manusia'].mean()
        delta_idx = idx_latest - idx_before
        metric_ipm.metric(label="Indeks Pembangunan Manusia", value=round(idx_latest, 2), delta=round(delta_idx, 2))
        
        # Indeks Pendidikan
        idx_before = df[df['Tahun'] == 2021]['Indeks Pendidikan'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Indeks Pendidikan'].mean()
        delta_idx = idx_latest - idx_before
        metric_idx_pendidikan.metric(label="Indeks Pendidikan", value=round(idx_latest, 2), delta=round(delta_idx, 2))
        
        # Indeks Pengeluaran
        idx_before = df[df['Tahun'] == 2021]['Indeks Pengeluaran'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Indeks Pengeluaran'].mean()
        delta_idx = idx_latest - idx_before
        metric_idx_pengeluaran.metric(label="Indeks Pengeluaran", value=round(idx_latest, 2), delta=round(delta_idx, 2))
        
        style_metric_cards(background_color='#0E1117', border_radius_px=20)
        
    metric_cards_1()
    metric_cards_2()
    
    enter()
    
    horizontal_line()    
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b>Perbandingan Kemiskinan antar Kota/Kab. di Jawa Barat (2017-2023) </b>
        </div>
    """, unsafe_allow_html=True)   
    horizontal_line()
              
    # Load dataset
    df = pd.read_csv(r'data/csv/metrics.csv')

    _, col_filter_wilayah, col_filter_features, _ = st.columns([1, 7, 7, 1])

    with col_filter_wilayah:
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique(), default=['Bandung', 'Kota Bandung'])
        filtered_df = df[df['Wilayah Jawa Barat'].isin(selected_regions)]
        filtered_df = filtered_df[~filtered_df['Tahun'].isin([2015, 2016, 2023])]

    # Calculate "Jumlah Penduduk Miskin" mean for selected regions
    sum_penduduk_miskin = [round(value, 2) for value in filtered_df.groupby('Tahun')['Jumlah Penduduk Miskin'].sum().tolist()]

    with col_filter_features:
        selected_features_columns = st.multiselect('Select features for line chart',
                                                ['Indeks Kesehatan', 'Indeks Pembangunan Manusia',
                                                    'Indeks Pendidikan', 'Indeks Pengeluaran'],
                                                default=['Indeks Kesehatan', 'Indeks Pembangunan Manusia',
                                                            'Indeks Pendidikan', 'Indeks Pengeluaran'])

        # Calculate mean for selected features columns
        mean_selected_features = filtered_df.groupby('Tahun')[selected_features_columns].mean().reset_index()
        for column in selected_features_columns:
            mean_selected_features[column] = mean_selected_features[column].round(2)

    # Remove duplicate values from 'Tahun' column
    filtered_df = filtered_df.drop_duplicates(subset=['Tahun'])
    x_axis_data = filtered_df['Tahun'].tolist()

    # Generate series for line chart based on selected features
    line_series = []
    for column in selected_features_columns:
        series_data = {
            "name": column,
            "type": "line",
            "yAxisIndex": 1,
            "data": mean_selected_features[column].tolist(),  # Use mean value of selected column data
            "lineStyle": {"width": 4},
            "symbolSize": 8,
            "tooltip": {"formatter": "{b}: {c}"},  # Format tooltip to display rounded value
        }
        line_series.append(series_data)

    # ECharts options
    options = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "crossStyle": {"color": "#999"}},
            "backgroundColor": "rgba(50,50,50,0.7)",
            "textStyle": {"color": "white"}
        },
        "legend": {
            "data": ["Jumlah Penduduk Miskin"] + selected_features_columns,
            "textStyle": {
                "color": "white",
                "fontSize": 14,
            },
            "orient": "horizontal"
        },
        "xAxis": [
            {
                "type": "category",
                "data": x_axis_data,
                "axisPointer": {"type": "shadow"},
                "axisLabel": {"color": "white"},
                "splitLine": {"show": True}
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "Penduduk Miskin",
                "min": 0,
                "max": max(sum_penduduk_miskin) * 1.5,
                "interval": max(sum_penduduk_miskin) // 2,
                "axisLabel": {"formatter": "{value} Jiwa", "color": "white"},
                "nameTextStyle": {
                    "color": "white",
                    "fontWeight": "bolder",
                    "align": "right"
                },
                "axisTick": {
                    "alignWithLabel": True
                },
                "splitLine": {"show": False}
            },
            {
                "type": "value",
                "name": "Indeks",
                "min": 0,
                "max": 100,
                "interval": 20,
                "axisLabel": {"formatter": "{value}", "color": "white"},
                "nameTextStyle": {
                    "color": "white",
                    "fontWeight": "bolder",
                    "align": "left"
                },
                "axisTick": {
                    "alignWithLabel": True
                },
            },
        ],
        "series": [
            {
                "name": "Jumlah Penduduk Miskin",
                "type": "bar",
                "data": sum_penduduk_miskin,
                "tooltip": {"formatter": "{b}: {c}"},  # Format tooltip to display rounded value
            },
            *line_series  # Add series for line chart based on selected features
        ],
    }

    st_echarts(options, height="400px")    
    
    enter()

    horizontal_line()    
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b>Matriks Ranking Indeks Wilayah Jawa Barat 2022</b>
        </div>
    """, unsafe_allow_html=True)   
    horizontal_line()

    
    df = pd.read_csv(r'data/csv/metrics.csv')  
    df.drop(['Tingkat Angkatan Kerja (%)', 'Tingkat Pengangguran (%)', 'Jumlah Penduduk Miskin'], inplace=True, axis=1)
    df.columns = df.columns.str.replace(' ', '_')
    df = df[df['Tahun'] == 2022]
        
    # Menghitung nilai Q1 dan Q3 dari kolom Indeks Kedalaman Kemiskinan
    Q1_kemiskinan = df['Indeks_Kedalaman_Kemiskinan'].quantile(0.25)
    Q3_kemiskinan = df['Indeks_Kedalaman_Kemiskinan'].quantile(0.75)

    # Menghitung nilai Q1 dan Q3 dari kolom Indeks Keparahan Kemiskinan
    Q1_keparahan = df['Indeks_Keparahan_Kemiskinan'].quantile(0.25)
    Q3_keparahan = df['Indeks_Keparahan_Kemiskinan'].quantile(0.75)

    # Membuat kode JavaScript untuk gaya sel
    cellStyle = JsCode(
        r"""
        function(params) {
            var style = {};
            var value = params.value;
            var field = params.colDef.field;
            
            if (field == 'Indeks_Kesehatan' || field == 'Indeks_Pendidikan' || field == 'Indeks_Pembangunan_Manusia' || field == 'Indeks_Pengeluaran') {
                if (value >= 80) {
                    style['background-color'] = 'green';
                } else if (value <= 60) {
                    style['background-color'] = 'red';
                } else if (value > 60 && value < 80) {
                    style['background-color'] = '#D88C00';
                }
            } else if (field == 'Indeks_Kedalaman_Kemiskinan') {
                if (value <= """ + str(Q1_kemiskinan) + """) {
                    style['background-color'] = 'green';
                } else if (value >= """ + str(Q3_kemiskinan) + """) {
                    style['background-color'] = 'red';
                } else {
                    style['background-color'] = '#D88C00';
                }
            } else if (field == 'Indeks_Keparahan_Kemiskinan') {
                if (value <= """ + str(Q1_keparahan) + """) {
                    style['background-color'] = 'green';
                } else if (value >= """ + str(Q3_keparahan) + """) {
                    style['background-color'] = 'red';
                } else {
                    style['background-color'] = '#D88C00';
                }
            }
            
            // Tambahkan properti font-size di sini
            style['font-size'] = '14px'; // Misalnya, ukuran teks 14px
            return style;
        }
        """
    )

    grid_options = GridOptionsBuilder.from_dataframe(df).build()
    grid_options['defaultColDef']['cellStyle'] = cellStyle
    AgGrid(df, gridOptions=grid_options, allow_unsafe_jscode=True, key='grid1')
    
    with st.expander('Legend Color'):
        col_1_legend, col_2_legend, col_3_legend = st.columns(3)
    
        with col_1_legend:
            legend_html = """
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 20px; height: 20px; background-color: green; margin-right: 5px;"></div>
                <div>Nilai >= 80</div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 20px; height: 20px; background-color: red; margin-right: 5px;"></div>
                <div>Nilai <= 60</div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 20px; height: 20px; background-color: #D88C00; margin-right: 5px;"></div>
                <div>Nilai di antara 60 dan 80</div>
            </div>
            """
            st.markdown("**Indeks Kesehatan, Pembangunan Manusia, Pendiddikan & Pengeluaran**")
            st.markdown(legend_html, unsafe_allow_html=True)
        
        with col_2_legend:
            legend_html_kemiskinan = f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 20px; height: 20px; background-color: green; margin-right: 5px;"></div>
                <div>Nilai <= Q1 ({Q1_kemiskinan:.2f})</div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 20px; height: 20px; background-color: red; margin-right: 5px;"></div>
                <div>Nilai >= Q3 ({Q3_kemiskinan:.2f})</div>
            </div>
            <div style="display: flex; align-items: center;">
                <div style="width: 20px; height: 20px; background-color: #D88C00; margin-right: 5px;"></div>
                <div>Nilai di antara Q1 dan Q3</div>
            </div>
            """
            
            st.markdown("**Indeks Kedalaman Kemiskinan**")
            st.markdown(legend_html_kemiskinan, unsafe_allow_html=True)


        with col_3_legend:
            legend_html_keparahan = f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="width: 20px; height: 20px; background-color: green; margin-right: 5px;"></div>
                    <div>Nilai <= Q1 ({Q1_keparahan:.2f})</div>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="width: 20px; height: 20px; background-color: red; margin-right: 5px;"></div>
                    <div>Nilai >= Q3 ({Q3_keparahan:.2f})</div>
                </div>
                <div style="display: flex; align-items: center;">
                    <div style="width: 20px; height: 20px; background-color: #D88C00; margin-right: 5px;"></div>
                    <div>Nilai di antara Q1 dan Q3</div>
                </div>
            """
            st.markdown("**Indeks Keparahan Kemiskinan**")
            st.markdown(legend_html_keparahan, unsafe_allow_html=True)
    
    enter();enter();enter()
    
    # st.markdown("""
    #     <div style='text-align: center; font-size:32px'>
    #         <b>Five Top & Bottom Regions</b>
    #     </div>
    # """, unsafe_allow_html=True)   
    
    col_header, col_filter_index = st.columns([3,1])
    
    with col_header:
        colored_header(
            label="Five Top & Bottom Regions",
            description="",
            color_name="orange-70",
        )
        
    with col_filter_index:
        selected_feature = st.selectbox(
            "Select features",
            ('Indeks Kesehatan', 'Indeks Pembangunan Manusia', 'Indeks Pendidikan', 'Indeks Pengeluaran', 'Indeks Kedalaman Kemiskinan', 'Indeks Keparahan Kemiskinan'), index=0)


    enter()
    
    col_top_5, col_bottom_5, col_expl_index  = st.columns([2,2,3])
    
    with col_top_5:
            st.markdown("""
                <div style='text-align: center; font-size:24px'>
                    <b>Top 5 Regions</b>
                </div>
            """, unsafe_allow_html=True)   
            enter()
            df = pd.read_csv(r'data/csv/metrics.csv')  
            df = df[['Wilayah Jawa Barat', 'Tahun', selected_feature]]
            df_2022 = df[df['Tahun'] == 2022]
            df_sorted = df_2022.sort_values(by=selected_feature, ascending=False)
            top_5_df = df_sorted.head().reset_index(drop=True)

            st.dataframe(top_5_df)
                   
    with col_bottom_5:
            st.markdown("""
                <div style='text-align: center; font-size:24px'>
                    <b>Bottom 5 Regions</b>
                </div>
            """, unsafe_allow_html=True)   
            enter()            
            df = pd.read_csv(r'data/csv/metrics.csv')  
            df = df[['Wilayah Jawa Barat', 'Tahun', selected_feature]]
            df_2022 = df[df['Tahun'] == 2022]
            df_sorted = df_2022.sort_values(by=selected_feature, ascending=False)
            bottom_5_df = df_sorted.tail().reset_index(drop=True)

            st.dataframe(bottom_5_df)
                
    with col_expl_index:
        # enter()
        if selected_feature == 'Indeks Kesehatan':
            with st.expander('Program yang dapat dilakukan', expanded=True):
                st.markdown('<b>Disclaimer: Khusus Indeks Kesehatan</b>', unsafe_allow_html=True)
                st.write('''
                        Berikut adalah program-program yang telah direalisasikan pada tahun 2021.
                        Sehingga berdampak pada peningkatan kesehatan tahun 2022 pada Kota/Kabupaten Bekasi:
                        ''')
                st.write("""
                        - Intervensi dan konvergensi tentang stunting di Kabupaten Bekasi.
                        - Jaminan kesehatan masyarakat miskin melalui PBI, BPJS dan Jamkesda.
                        - Peningkatan Puskesmas Pembantu menjadi Puskesmas.
                        - Akreditasi Puskesmas
                        - Peningkatan upaya kesehatan masyarakat melalui promotive, preventif dan kuratif ketenagakerjaan
                        """)
                
                st.write('Referensi: https://www.bekasikab.go.id/ini-dia-43-program-prioritas-kabupaten-bekasi-tahun-2021')
            
        
if selected == 'IPM':  
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:30px'>
            <b>IPM per Komponen (2017 - 2023)</b>
        </div>
    """, unsafe_allow_html=True)  
    horizontal_line()
       
    df = pd.read_csv('data/csv/IPM_Menurut_Komponen_2015_2023.csv')
    
    _, col_filter_ipm, _ = st.columns([1,2,1])
    
    with col_filter_ipm:       
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique(), default=['Kota Bandung', 'Cianjur'])
    
    df = df[df['Wilayah Jawa Barat'].isin(selected_regions)]
    df = df[df['Kategori'] != 'Pengeluaran Per Kapita']
    df = df[~df['Tahun'].isin([2015, 2016])] 

    # Filter hanya kolom 'Usia Harapan Hidup' untuk bar chart
    df_bar = df[df['Kategori'] == 'Usia Harapan Hidup']

    # Filter kolom 'Rata Rata Lama Sekolah' dan 'Harapan Lama Sekolah' untuk line chart
    df_line = df[(df['Kategori'] == 'Rata Rata Lama Sekolah') | (df['Kategori'] == 'Harapan Lama Sekolah')]

    data_series = []

    # Data untuk bar chart
    data_series.append({
        "name": 'Usia Harapan Hidup',
        "type": "bar",
        "barGap": 0,
        "data": list(df_bar['Value']),
        "yAxisIndex": 0,  # Menggunakan y-axis pertama
        "emphasis": {"focus": "series"},
        "label": {
            "show": False  # Menyembunyikan nilai pada bar chart
        },
        "barWidth": 100,  # Mengatur lebar bar chart
    })

    # Data untuk line chart
    for kategori, group in df_line.groupby('Kategori'):
        data_series.append({
            "name": kategori,
            "type": "line",
            "data": list(group['Value']),
            "yAxisIndex": 1,  # Menggunakan y-axis kedua
            "emphasis": {"focus": "series"},
            "lineStyle": {
                "width": 4  # Memperbesar ketebalan garis pada line chart
            },
            "label": {
                "show": False  # Menyembunyikan nilai pada line chart
            },
            "symbolSize": 8,  # Memperbesar marker pada line chart
        })

    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "xAxis": [{"type": "category", "axisTick": {"show": False}, "data": df_line['Tahun'].unique().tolist(),
                "axisLabel": {"fontSize": 14, "color": "white"}}],
        "yAxis": [
            {"type": "value", "name": "Usia Harapan Hidup", "position": "left",
            "axisLabel": {"fontSize": 14, "color": "white"}, "max": 100, "interval":25,
            "nameTextStyle": {"color": "white"}},  # Menyesuaikan warna teks sumbu y pertama
            {"type": "value", "name": "Lama Sekolah", "position": "right",
            "axisLabel": {"fontSize": 14, "color": "white"}, "max":20, "interval":5,
            "nameTextStyle": {"color": "white"}}  # Menyesuaikan warna teks sumbu y kedua
        ],
        "series": data_series,
        "color": ["#1f77b4", "#ff7f0e", "#2ca02c"],
        "label": {"show": True, "color": "#FFFFFF"}
    }

    st_echarts(options, height="600px")
    
    col_expl_ipm_top, col_expl_ipm_bottom = st.columns(2)
    
    with col_expl_ipm_top:
        with st.expander('Insight (Kota Bandung)', expanded=True):
            st.write(f"""
                    - Mulai dari 2017 - 2023, :blue[Kota Bandung] merupakan wilayah dengan :blue[Rata-rata Usia Harapan Hidup (UHH) tertinggi sebesar 74 tahun].
                    - Pada tahun 2023, :orange[Kota Bandung memiliki Harapan Lama Sekolah (HLS) mencapai 14.24 tahun], artinya rata-rata anak usia 7 tahun 
                    yang masuk jenjang pendidikan formal memiliki :orange[peluang untuk bersekolah selama 14.24 tahun atau setara dengan Diploma 3].
                    - Pada 2023, :green[Rata-rata Lama Sekolah (RLS) penduduk berusia 25 tahun ke atas adalah 11.06 tahun], hal ini masih kurang dari :red[target seharusnya yaitu 12 tahun].
                     """)
            
    with col_expl_ipm_bottom:
        with st.expander('Insight (Kota Cianjur)', expanded=True):
            st.write(f"""
                    - Mulai dari 2017 - 2023, :blue[Kota Cianjur] merupakan wilayah dengan :blue[Rata-rata Usia Harapan Hidup (UHH) terendah sebesar 70 tahun].
                    - Pada tahun 2023, :orange[Kota Cianjur memiliki Harapan Lama Sekolah (HLS) mencapai nilai 12.03 tahun], artinya rata-rata anak usia 7 tahun 
                    yang masuk jenjang pendidikan formal memiliki :orange[peluang untuk bersekolah selama 12.03 tahun atau setara dengan Diploma 1].
                    - Pada 2023, :green[Rata-rata Lama Sekolah (RLS) penduduk usia 25 tahun ke atas adalah 7.22 tahun], hal ini masih kurang dari :red[target seharusnya yaitu 7 tahun].
                     """)

 
if selected == 'Trend IHK':
    with st.container(): 
        horizontal_line()
        st.markdown("""
            <div style='text-align: center; font-size:30px'>
                <b>Trend & Jumlah IHK - 2020-2024</b>
            </div>
        """, unsafe_allow_html=True)     
        horizontal_line()
        
        ihk_col1, ihk_col2 = st.columns(2)
        
        with ihk_col1:
            enter()
            
            # Trend IHK per Pengeluaran (Tahun)
            df = pd.read_csv('data/csv/IHK per Pengeluaran.csv')

            # Group by Kelompok Pengeluaran IHK and Tahun and calculate the mean IHK Value
            df_grouped = df.pivot_table(index="Kelompok Pengeluaran IHK", columns="Tahun", values="IHK Value", aggfunc="mean")

            # Calculate the mean and round the values
            df_grouped["mean"] = df_grouped.mean(axis=1).round(2)
            df_grouped = df_grouped.sort_values(by="mean", ascending=True)
            df_grouped = df_grouped.drop(columns="mean")

            option = {
                "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
                "legend": {"textStyle": {"fontSize": 14, "color": "white"}},
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "xAxis": {"type": "value", "axisLabel": {"fontSize": 14, "color": "white"}},
                "yAxis": {"type": "category", "data": df_grouped.index.tolist(), "axisLabel": {"fontSize": 12, "color": "white"}},
                "series": [
                    {"name": str(year), 
                    "emphasis": {"focus": "series"},
                    "type": "bar", "stack": "mean", "label": {"show": True}, "data": df_grouped[year].round(2).tolist()}
                    for year in df_grouped.columns
                ],
                "label": {"show": True, "color": "black", "fontSize":14, "fontWeight":"bold"}
            }

            st_echarts(option, height=600)
            
        with ihk_col2:
            
            selected_pengeluaran_ihk = st.multiselect('Select Kelompok Pengeluaran IHK', df['Kelompok Pengeluaran IHK'].unique(), default=['Pendidikan', 'Kesehatan', 'Perawatan Pribadi & Jasa Lainnya'])

            # Trend IHK per Pengeluaran (Bulan)
            df = pd.read_csv('data/csv/IHK per Pengeluaran.csv')
            df = df[df['Kelompok Pengeluaran IHK'].isin(selected_pengeluaran_ihk)]
               
            # Menyesuaikan format Bulan_Tahun menjadi string
            df['Bulan_Tahun'] = df['Bulan_Tahun'].str.replace('-', ' ')
            df['Bulan_Tahun'] = pd.to_datetime(df['Bulan_Tahun'], format='%B %Y').astype(str)

            categories = df['Kelompok Pengeluaran IHK'].unique()
            grouped_data = df.groupby('Kelompok Pengeluaran IHK')

            echart_config = {
                "tooltip": {"trigger": "axis"},
                "legend": {"data": categories.tolist(), "textStyle": {"fontSize": 14, "color": "white"}},
                "xAxis": {"type": "category",
                          "data": df['Bulan_Tahun'].unique().tolist(),
                          "axisLabel": {"fontSize": 12, "color": "white"}
                          },
                "yAxis": {"type": "value",
                        "max": 120,
                        "min": 95,
                        "axisLabel": {"fontSize": 12, "color": "white"}
                        },
                "series": [],
            }

            # data series untuk setiap kategori
            for category in categories:
                category_data = grouped_data.get_group(category)
                series_data = {"name": category, "type": "line", "data": category_data['IHK Value'].tolist(), "smooth": True}
                echart_config["series"].append(series_data)

            st_echarts(echart_config, height="600px")
            
        with st.expander('Insight', expanded=True):
            st.write("""
                    Trend IHK pada dashboard dapat dilihat mengalami peningkatan yang cukup signifikan dikarenakan pertumbuhan ekonomi pada kuartal IV 2023 sebesar 5,05% dan mengalami penurunan dibandingkan tahun 2022 sekitar 5,31%. 
                    
                    Hal itu disebabkan oleh beberapa faktor seperti: 
                    - Melambatnya konsumsi rumah tangga menjadi 4,5 persen (yoy) pada 2023-01-01 dibanding 2023-02-01 sebesar 5,1 persen (yoy). Terutama disebabkan melemahnya :orange[(tertundanya) daya beli kelas menengah ke atas], serta relatif :orange[terbatasnya kenaikan konsumsi segmen berpenghasilan rendah di tengah kenaikan belanja sosial dan politik menjelang pemilihan umum (pemilu)].
                    - Perlambatan investasi menjadi 5,0 persen (yoy) pada 2023-01-01, dibandingkan 5,8 persen pada 2023-02-01. :orange[Investasi mesin dan peralatan serta kendaraan bermotor mengalami perlambatan seiring melemahnya ekspor dan investasi asing langsung] (foreign direct investment/FDI), sementara investasi bangunan dan infrastruktur relatif bertahan didukung belanja modal pemerintah
                    - Melambatnya kinerja ekspor-impor. Kontribusi net ekspor terhadap pertumbuhan PDB menurun menjadi 0,4 percentage point (ppt) pada Q4 2023 dari 0,5 ppt pada Q3 2023. Hal ini mencerminkan :orange[peningkatan impor lebih tinggi ketimbang ekspor] seiring perlambatan ekonomi global dan harga komoditas yang melemah.
                     """)
            st.write("Source: https://www.example.com")
            
                  
if selected == 'Pekerja':

    colored_header(
        label="Tingkat Angkatan Kerja vs Pengangguran (%)",
        description="",
        color_name="orange-70",
    )
    
    enter()
    
    col_filter_wilayah, col_filter_year = st.columns(2)
    
    df = pd.read_csv(r"data/csv/df_merge_idx.csv")
    
    with col_filter_wilayah:
        # Filter by region
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique(), default=['Bandung', 'Garut', 'Tasikmalaya'])
        filtered_df = df[df['Wilayah Jawa Barat'].isin(selected_regions)]

    with col_filter_year:
        # Filter by year
        selected_year = st.selectbox('Select Year', filtered_df['Tahun'].unique(), index=6)
        filtered_df = filtered_df[['Wilayah Jawa Barat', 'Tahun', 'Tingkat Angkatan Kerja (%)', 'Tingkat Pengangguran (%)']]
        filtered_df = filtered_df[filtered_df['Tahun'] == selected_year]
                
    radar_data = filtered_df.drop(columns=['Tahun'])
    # Convert data to list of dictionaries
    radar_data = radar_data.to_dict(orient='records')
    
    col_radar_chart, col_expl = st.columns(2)
    
    with col_radar_chart:
        with elements("nivo_charts"):
            with mui.Box(sx={"height": 500}):
                nivo.Radar(
                    data=radar_data,
                    keys=filtered_df.iloc[:,2:].columns.tolist(),
                    indexBy="Wilayah Jawa Barat",
                    valueFormat=">-.2f",
                    margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
                    borderColor={ "from": "color" },
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={ "theme": "background" },
                    dotBorderWidth=2,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemHeight": 20,
                            "itemTextColor": "#FFFFFF", 
                            "symbolSize": 12,
                            "itemTextSize": 14,  
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#999"
                                    }
                                }
                            ]
                        }
                    ],
                    theme={
                        "background": "#0E1117",
                        "textColor": "#FFFFFF",
                        "tooltip": {
                            "container": {
                                "background": "#0E1117",
                                "color": "#FFFFFF",
                            }
                        }
                    },
                )        
            
    with col_expl:
        with st.expander('Insight', expanded=True):
            st.write("""
                    Berdasarkan perbandingan Top 3 (Kota Bekasi, Kota Depok, dan Kota Bandung) dan Bottom 3 (Subang, Indramayu, dan Cianjur) pada indeks pendidikan, 
                    persentase tingkat pengangguran tertinggi pada tahun 2023 terdapat di Kota Bandung 8.83%, Kota Bekasi 7.90%, dan Cianjur 7.71%.      
                    """)
            horizontal_line()
            st.write("""
                     Pada 2023, Kota Bandung memiliki persentase tingkat pengangguran yang cukup tinggi yakni 8.83%, sedangkan pada tahun 2021, :orange[persentase ini menurun ketika terjadi pandemi Covid-19 yang mencapai 11.46%]. 
                     Kota Bandung tidak memiliki sumber daya alam. Bandung hanya memiliki Sumber Daya Manusia (SDM) sehingga pendapatannya bergantung pada bisnis fashion, wisata, kuliner, perdagangan, desain, dan lain-lain. 
                     :orange[Dengan terbatasnya sumber daya, maka tingkat inflasi harga barang di Bandung akan lebih tinggi ketimbang daerah lainnya. Hal inilah yang akan berkaitan erat dengan persentase tingkat pengangguran di Kota Bandung]
                     """)
            st.write('Referensi: https://bandungbergerak.id/article/detail/159126/membaca-klaim-penurunan-angka-pengangguran-kota-bandung-di-tengah-marak-pencari-kerja')
    # Proporsi Jenis Pekerja Berdasarkan Jenis Kelamin
    
    df_jk = pd.read_csv(r'data/csv/Proporsi_JK_Pekerja_Formal_Informal_2018_2023.csv')
    df_tipe_daerah = pd.read_csv(r'data/csv/Proporsi_Daerah_Pekerja_Formal_Informal_2018_2023.csv')

    col_title, col_filter_year = st.columns([2,1])
    
    enter(); enter()
    
    with col_title:
        colored_header(
            label="Proporsi Jenis Pekerja Berdasarkan Jenis Kelamin",
            description="",
          
            color_name="orange-70",
        )
    with col_filter_year:
        selected_year = st.selectbox('Select Year', df_jk['Tahun'].unique(), index=5)
    
    enter()
    
    filtered_df_jk = df_jk[df_jk['Tahun'] == selected_year]
    filtered_df_tipe_daerah = df_tipe_daerah[df_tipe_daerah['Tahun'] == selected_year]
    
    col_pie_jk, col_pie_tipe_daerah = st.columns(2)

    with col_pie_jk:
        
        formal_pria_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Laki-laki']['Proporsi Formal (%)'].values[0]
        informal_pria_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Laki-laki']['Proporsi Informal (%)'].values[0]
        formal_perempuan_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Perempuan']['Proporsi Formal (%)'].values[0]
        informal_perempuan_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Perempuan']['Proporsi Informal (%)'].values[0]
        
        option_pie_jk = {
            'backgroundColor': '#0E1117',
            'title': {
                'text': 'Proporsi Pekerja berdasarkan Jenis Kelamin',
                'left': 'center',
                'top': 20,
                'textStyle': {
                    'color': '#ccc'
                }
            },
            'tooltip': {
                'trigger': 'item'
            },
            'visualMap': {
                'show': False,
                'min': 80,
                'max': 600,
                # 'inRange': {
                #     'colorLightness': [0, 1]
                # }
            },
            'series': [
                {
                    'name': 'Persentase',
                    'type': 'pie',
                    'radius': '55%',
                    'center': ['50%', '50%'],
                    'data': [
                        {'value': formal_pria_value, 'name': 'Pria (Formal)', 'itemStyle': {'color': '#5470C6'}},
                        {'value': formal_perempuan_value, 'name': 'Wanita (Formal)', 'itemStyle': {'color': '#EE6666'}},
                        {'value': informal_pria_value, 'name': 'Pria (Informal)', 'itemStyle': {'color': '#5470C6'}},
                        {'value': informal_perempuan_value, 'name': 'Wanita (Informal)', 'itemStyle': {'color': '#EE6666'}},
                    ],
                    'roseType': 'radius',
                    'label': {
                        'color': 'rgba(255, 255, 255, 0.3)',
                        'textStyle': { 
                            'fontSize': 16  
                        }
                    },
                    'labelLine': {
                        'lineStyle': {
                            'color': 'rgba(255, 255, 255, 0.3)'
                        },
                        'smooth': 0.2,
                        'length': 10,
                        'length2': 20
                    },
                    'itemStyle': {
                        'shadowBlur': 200,
                        'shadowColor': 'rgba(0, 0, 0, 0.5)'
                    },
                    'animationType': 'scale',
                    'animationEasing': 'elasticOut',
                    'animationDelay': 200  
                }
            ]
        }

        st_echarts(
            options=option_pie_jk, height="500px",
        )
        
        with st.expander('Insights', expanded=True):
            st.write("""
                     Pada tahun 2023, persentase pekerja informal wanita cenderung lebih tinggi dibandingkan pria hal ini dikarenakan tingkat kepuasan terhadap kinerja, 
                     beberapa faktor yang menjelaskan perbedaan kepuasan kerja antar gender tersebut: 
                     
                    - Perempuan memiliki harapan yang lebih rendah dibandingkan laki-laki
                    - Perempuan fokus pada perannya sebagai ibu rumah tangga dan pengasuh anak 
                    - Pendapatan bukan menjadi ukuran kepuasan kerja perempuan, melainkan relasi sosial, dan lain sebagainya.
                     """)
            
            st.write('Referensi: https://unair.ac.id/banyak-wanita-indonesia-bekerja-di-sektor-informal-apakah-mereka-puas-dengan-pekerjaan-ini/')
            
    with col_pie_tipe_daerah:
        
        formal_perkotaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perkotaan']['Proporsi Formal (%)'].values[0]
        informal_perkotaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perkotaan']['Proporsi Informal (%)'].values[0]
        formal_perdesaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perdesaan']['Proporsi Formal (%)'].values[0]
        informal_perdesaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perdesaan']['Proporsi Informal (%)'].values[0]
        
        option_pie_jk = {
            'backgroundColor': '#0E1117',
            'title': {
                'text': 'Proporsi Pekerja berdasarkan Daerah Tempat Tinggal',
                'left': 'center',
                'top': 20,
                'textStyle': {
                    'color': '#ccc'
                }
            },
            'tooltip': {
                'trigger': 'item'
            },
            'visualMap': {
                'show': False,
                'min': 80,
                'max': 600,
                # 'inRange': {
                #     'colorLightness': [0, 1]
                # }
            },
            'series': [
                {
                    'name': 'Persentase',
                    'type': 'pie',
                    'radius': '55%',
                    'center': ['50%', '50%'],
                    'data': [
                        {"value": formal_perkotaan_value, "name": "Perkotaan (Formal)"},
                        {"value": formal_perdesaan_value, "name": "Perdesaan (Formal)", 'itemStyle': {'color': '#712622'}},
                        {"value": informal_perkotaan_value, "name": "Perkotaan (Informal)"},
                        {"value": informal_perdesaan_value, "name": "Perdesaan (Informal)", 'itemStyle': {'color': '#712622'}},
                    ],
                    'roseType': 'radius',
                    'label': {
                        'color': 'rgba(255, 255, 255, 0.3)',
                        'textStyle': {   
                            'fontSize': 16 
                        }
                    },
                    'labelLine': {
                        'lineStyle': {
                            'color': 'rgba(255, 255, 255, 0.3)'
                        },
                        'smooth': 0.2,
                        'length': 10,
                        'length2': 20
                    },
                    'itemStyle': {
                        'shadowBlur': 200,
                        'shadowColor': 'rgba(0, 0, 0, 0.5)'
                    },
                    'animationType': 'scale',
                    'animationEasing': 'elasticOut',
                    'animationDelay': 200 
                }
            ]
        }

        st_echarts(
            options=option_pie_jk, height="500px",
        )
        
        with st.expander('Insights', expanded=True):
            st.write("""
                     Pada tahun 2023, :orange[74.59% proporsi pekerja di pedesaan berada pada sektor informal]. Membengkaknya proporsi pekerja di sektor informal disebabkan karena terbatasnya daya serap sektor modern atau formal terhadap angkatan kerja. 
                     :orange[Terbatasnya daya serap sektor formal atau modern ini karena tenaga kerja yang dibutuhkan adalah mereka yang mempunyai pendidikan dan keterampilan yang tinggi, padahal di lain pihak sebagian besar tenaga kerja Indonesia masih mempunyai pendidikan yang rendah.] 
                     Akibatnya tenaga kerja yang tidak terserap di sektor formal terpaksa masuk ke sektor informal yang tidak membutuhkan persyaratan apa-apa seperti di sektor formal.
                     """)
            
            st.write('Referensi: https://lib.ui.ac.id/m/detail.jsp?id=78268&lokasi=lokal')
        