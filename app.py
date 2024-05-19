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

# def horizontal_line(color='#808080'):
#     st.markdown(f'<hr style="border:2px solid {color};">', unsafe_allow_html=True)
def horizontal_line():
    st.markdown(f'<hr>', unsafe_allow_html=True)
    
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
    page_title='MoF - Tingkat Ekonomi Jawa Barat',
    layout='wide'
)

with st.sidebar:
    st.markdown("""
        <div style='text-align: center; font-size:24px'>
            <b>
            Tingkat Ekonomi <br> Jawa Barat <br>
            </b>
        </div>
    """, unsafe_allow_html=True)
    
    enter()

    logo_link('', r'img/logo-jabar.png', 100)
    enter()
    horizontal_line()

    selected = option_menu(menu_title=None, 
                          options=["Home", 'IPM', 'Trend IHK', 'Pekerja'], 
                          icons=['house'], 
                          menu_icon="cast", default_index=0
                        )
    
    horizontal_line()
        
    st.markdown("""
        <div style='text-align: center; font-size:20px'>
            <b>Created By</b> <br>
            <a href="https://www.linkedin.com/in/sherly-santiadi-2723a821a" style="text-decoration: none;">Sherly Santiadi</a>
            <br>
            <a href="https://linkedin.com/in/marselius-agus-dhion/" style="text-decoration: none;">Marselius Agus Dhion</a>
        </div>
    """, unsafe_allow_html=True)
    
    horizontal_line()
    
    st.markdown("""
        <div style='text-align: center; font-size:20px'>
            <b>Data Source</b> <br>
            <a href="https://jabar.bps.go.id" style="text-decoration: none;">BPS Jabar</a>
        </div>
    """, unsafe_allow_html=True)
    
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
        _, _, metric_idx_p1, metric_idx_penduduk, metric_idx_p2, _, _ = st.columns([2,2,4,4,4,2,2])                
        
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
        _, metric_idx_kesehatan, metric_ipm, metric_idx_pendidikan, metric_idx_pengeluaran, _ = st.columns([1,2,2,2,2,1])                
        
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
        <div style='text-align: center; font-size:28px'>
            <b>Perbandingan Tingkat Ekonomi <br> Kota/Kab. di Jawa Barat (2017-2023) </b>
        </div>
    """, unsafe_allow_html=True)   
    horizontal_line()
              
    # Load dataset
    df = pd.read_csv(r'data/csv/metrics.csv')

    _, col_filter_wilayah, col_filter_features, _ = st.columns([1, 7, 7, 1])
    enter()
    
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
    df = df[df['Tahun'] == 2022]
    df.drop(['Tahun', 'Tingkat Angkatan Kerja (%)', 'Tingkat Pengangguran (%)', 'Jumlah Penduduk Miskin'], inplace=True, axis=1)
    df.columns = df.columns.str.replace(' ', '_')
        
    rank_color_expl = """
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom:8px">
        <div style="display: flex; align-items: center;">
            <div style="width: 15px; height: 15px; background-color: green; margin-right: 5px;"></div>
            <div style="margin-right: 15px">Sangat Tinggi</div>
            <div style="width: 15px; height: 15px; background-color: #0D590D; margin-right: 5px;"></div>
            <div style="margin-right: 15px">Tinggi</div>
            <div style="width: 15px; height: 15px; background-color: #EA9800; margin-right: 5px;"></div>
            <div style="margin-right: 15px">Sedang</div>
            <div style="width: 15px; height: 15px; background-color: #D80000; margin-right: 5px;"></div>
            <div style="margin-right: 15px">Rendah</div>
        </div>
    </div>
    """
    st.markdown(rank_color_expl, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; font-size:16px; margin-bottom: 12px'>
            <a href="https://repository.its.ac.id/2807/1/1315201715-Master_Theses.pdf" style="text-decoration: none;">Referensi Legend (Hal 32)</a>
        </div>
    """, unsafe_allow_html=True)

            
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
                if (value >= 80 && value <= 100) {
                    style['background-color'] = 'green'; // sangat tinggi
                } else if (value >= 70 && value < 80) {
                    style['background-color'] = '#0D590D'; // tinggi
                } else if (value >= 60 && value < 70) {
                    style['background-color'] = '#EA9800'; // sedang
                } else if (value >= 0 && value < 60) {
                    style['background-color'] = '#D80000'; // rendah
                }
            } else if (field == 'Indeks_Kedalaman_Kemiskinan') {
                if (value <= """ + str(Q1_kemiskinan) + """) {
                    style['background-color'] = 'green';
                } else if (value >= """ + str(Q3_kemiskinan) + """) {
                    style['background-color'] = '#D80000';
                } else {
                    style['background-color'] = '#EA9800';
                }
            } else if (field == 'Indeks_Keparahan_Kemiskinan') {
                if (value <= """ + str(Q1_keparahan) + """) {
                    style['background-color'] = 'green';
                } else if (value >= """ + str(Q3_keparahan) + """) {
                    style['background-color'] = '#D80000';
                } else {
                    style['background-color'] = '#EA9800';
                }
            }
            
            // Tambahkan properti font-size di sini
            style['font-size'] = '14px'; // Misalnya, ukuran teks 14px
            return style;
        }
        """
    )

    # Mengatur GridOptions
    grid_options = GridOptionsBuilder.from_dataframe(df).build()
    grid_options['defaultColDef']['cellStyle'] = cellStyle
    grid_options['autoSizeColumns'] = True  # Mengatur lebar kolom berdasarkan teks pada nama kolom

    # Menampilkan tabel menggunakan AgGrid
    AgGrid(df, gridOptions=grid_options, allow_unsafe_jscode=True, key='grid1')
    
    legend_col, expl_matrix_col = st.columns([4,5])
    
    with legend_col:
            with st.expander('Legend Color', expanded=True):    
                legend_html = """
                - <b>Indeks Kesehatan, Pembangunan Manusia, Pendidikan & Pengeluaran</b>
                <div style="display: flex; align-items: center">
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: green; margin-right: 5px; margin-left: 30px"></div>
                        <div>80 <= Nilai <= 100</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: #0D590D; margin-right: 5px;"></div>
                        <div>70 <= Nilai < 80</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: #EA9800; margin-right: 5px;"></div>
                        <div>60 <= Nilai < 70</div>
                    </div>
                    <div style="display: flex; align-items: center;">
                        <div style="width: 15px; height: 15px; background-color: #D80000; margin-right: 5px;"></div>
                        <div>0 <= Nilai < 60</div>
                    </div>
                </div>
                """
                st.markdown(legend_html, unsafe_allow_html=True)

                
                enter()

                legend_html_kemiskinan = f"""
                - <b>Indeks Kedalaman Kemiskinan</b>
                <div style="display: flex; align-items: center">
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: green; margin-right: 5px; margin-left: 30px"></div>
                        <div style="margin-right: 4px">Nilai <= {Q1_kemiskinan:.2f} (Q1)</div>
                    </div>
                    <div style="display: flex; align-items: center;">
                        <div style="width: 15px; height: 15px; background-color: #EA9800; margin-right: 5px;"></div>
                        <div style="margin-right: 22px">Q1 < Nilai < Q3</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: #D80000; margin-right: 5px;"></div>
                        <div>Nilai >= {Q3_kemiskinan:.2f} (Q3)</div>
                    </div>
                </div>
                """

                st.markdown(legend_html_kemiskinan, unsafe_allow_html=True)

                enter()
                
                legend_html_keparahan = f"""
                - <b>Indeks Keparahan Kemiskinan</b>
                <div style="display: flex; align-items: center">
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: green; margin-right: 5px; margin-left: 30px"></div>
                        <div style="margin-right: 4px">Nilai <= {Q1_keparahan:.2f} (Q1)</div>
                    </div>
                    <div style="display: flex; align-items: center;">
                        <div style="width: 15px; height: 15px; background-color: #EA9800; margin-right: 5px;"></div>
                        <div style="margin-right: 22px">Q1 < Nilai < Q3</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-right: 20px;">
                        <div style="width: 15px; height: 15px; background-color: #D80000; margin-right: 5px;"></div>
                        <div>Nilai >= {Q3_keparahan:.2f} (Q3)</div>
                    </div>
                </div>
                """
                st.markdown(legend_html_keparahan, unsafe_allow_html=True)
                
                enter()

    with expl_matrix_col:
        with st.expander('Insight', expanded=True):
            st.write('aABC')
    
    
    enter();enter();enter() 
    
    def tooltip_html(color, text):
        return f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="width: 20px; height: 20px; background-color: {color}; margin-right: 5px;"></div>
            <div>{text}</div>
        </div>
        """
    
    col_header, col_filter_index = st.columns([3,1])
    
    with col_header:
        colored_header(
            label="Lima Kota/Kab. Teratas & Terbawah",
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
            if ((selected_feature == 'Indeks Kedalaman Kemiskinan') or (selected_feature == 'Indeks Keparahan Kemiskinan')):
                st.markdown("""
                    <div style='text-align: center; font-size:24px'>
                        <b>Lima Kota/Kab. Terbawah</b>
                    </div>
                """, unsafe_allow_html=True)   
                enter()
                
                df = pd.read_csv(r'data/csv/metrics.csv')  
                df = df[['Wilayah Jawa Barat', 'Tahun', selected_feature]]
                df_2022 = df[df['Tahun'] == 2022]
                df_sorted = df_2022.sort_values(by=selected_feature, ascending=True)   
                df_sorted = df_sorted.astype(str)
                bottom_5_df = df_sorted.head().reset_index(drop=True)
                st.dataframe(bottom_5_df)
            
            else:
                st.markdown("""
                    <div style='text-align: center; font-size:24px'>
                        <b>Lima Kota/Kab. Teratas</b>
                    </div>
                """, unsafe_allow_html=True)   
                enter()
            
                df = pd.read_csv(r'data/csv/metrics.csv')  
                df = df[['Wilayah Jawa Barat', 'Tahun', selected_feature]]
                df_2022 = df[df['Tahun'] == 2022]
                df_sorted = df_2022.sort_values(by=selected_feature, ascending=False)   
                df_sorted = df_sorted.astype(str)
                top_5_df = df_sorted.head().reset_index(drop=True)
                st.dataframe(top_5_df)
                   
    with col_bottom_5:
            if ((selected_feature == 'Indeks Kedalaman Kemiskinan') or (selected_feature == 'Indeks Keparahan Kemiskinan')):
                st.markdown("""
                    <div style='text-align: center; font-size:24px'>
                        <b>Lima Kota/Kab. Teratas</b>
                    </div>
                """, unsafe_allow_html=True)   
                enter()    
                 
                df = pd.read_csv(r'data/csv/metrics.csv')  
                df = df[['Wilayah Jawa Barat', 'Tahun', selected_feature]]
                df_2022 = df[df['Tahun'] == 2022]
                df_sorted = df_2022.sort_values(by=selected_feature, ascending=False)
                df_sorted = df_sorted.astype(str)
                top_5_df = df_sorted.tail().reset_index(drop=True)

                st.dataframe(top_5_df)
                
            else:
                st.markdown("""
                    <div style='text-align: center; font-size:24px'>
                        <b>Lima Kota/Kab. Terbawah</b>
                    </div>
                """, unsafe_allow_html=True)   
                enter()
                
                df = pd.read_csv(r'data/csv/metrics.csv')  
                df = df[['Wilayah Jawa Barat', 'Tahun', selected_feature]]
                df_2022 = df[df['Tahun'] == 2022]
                df_sorted = df_2022.sort_values(by=selected_feature, ascending=True)
                df_sorted = df_sorted.astype(str)
                bottom_5_df = df_sorted.tail().reset_index(drop=True)

                st.dataframe(bottom_5_df)
                
    with col_expl_index:
        if selected_feature == 'Indeks Kesehatan':
            with st.expander('Program yang dapat dilakukan bagi kota/kab. terbawah', expanded=True):                
                    st.markdown("""
                        <div style='font-size:16px'>
                            Berikut merupakan program-program yang telah direalisasikan pada tahun 2021 
                            dan berdampak pada peningkatan indeks kesehatan tahun 2022 pada Kota Bekasi:
                            <br>
                            <ul>
                                <li> Intervensi dan konvergensi tentang stunting. </li>
                                <li> Jaminan kesehatan masyarakat miskin melalui PBI, BPJS dan Jamkesda. </li>
                                <li> Peningkatan Puskesmas Pembantu menjadi Puskesmas. </li>
                                <li> Akreditasi Puskesmas </li>
                                <li> Peningkatan upaya kesehatan masyarakat melalui promotive, preventif dan kuratif ketenagakerjaan </li>  <br>                  
                            </ul>

                        Referensi: <a href='https://www.bekasikab.go.id/ini-dia-43-program-prioritas-kabupaten-bekasi-tahun-2021'>Program Prioritas Bekasi Tahun 2021</a> <br>
                        </div>
                    """, unsafe_allow_html=True)   
            
        if selected_feature == 'Indeks Pembangunan Manusia':
            with st.expander('Program yang dapat dilakukan bagi kota/kab. terbawah', expanded=True):                
                st.markdown("""
                    <div style='font-size:16px'>
                        Berikut adalah program-program yang telah direalisasikan pada tahun 2021. Sehingga berdampak
                        pada peningkatan IPM tahun 2022 pada Kota Bandung:
                        <br>
                        <ul>
                            <li> Menggelar semacam Musyawarah Perencanaan Pembangunan (MUSRENBANG) dalam rangka penyusunan Rencana Kerja Pemerintah Daerah (RKPD) </li>
                            <li> Memperbanyak pelatihan yang berorientasi pada pengembangan usaha </li>
                            <li> Memperbanyak job fair terutama untuk penyandang disabilitas </li>
                        </ul>

                    Referensi: 
                    - <a href='https://jabarprov.go.id/berita/serat-aspirasi-pemkot-bandung-gelar-musrenbang-rkpd-tahun-2025-12621'>Serat Aspirasi, Pemkot Bandung Gelar Musrenbang RKPD Tahun 2025</a> <br>
                    - <a href='https://www.bandung.go.id/news/read/7767/ipm-naik-angka-pengangguran-turun-pemkot-bandung-gaskan-musrenbang'>IPM Naik, Angka Pengangguran Turun, Pemkot Bandung "Gaskan" Musrenbang 2024</a> <br>
                    </div>
                """, unsafe_allow_html=True)
                enter()
                
        if selected_feature == 'Indeks Pendidikan':
            with st.expander('Program yang dapat dilakukan bagi kota/kab. terbawah', expanded=True):                
                st.markdown("""
                    <div style='font-size:16px'>
                        Berikut adalah program-program yang telah direalisasikan pada tahun 2021 dan berdampak
                        pada peningkatan indeks pendidikan tahun 2022 pada Kota Bandung:
                        <br>
                        <ul>
                            <li> Peningkatan Mutu Pendidikan melalui Akreditasi Sekolah/Lembaga Pendidikan </li>
                            <li> Peningkatan Mutu Sarana dan Prasarana Pendidikan melalui Perbaikan dan Penambahan Ruang Kelas Baru, Perpustakaan dan Laboratorium </li>
                            <li> Optimalisasi ICT sebagai Decision Support System dan Executive Support System dalam layanan Pendidikan yang berkualitas </li>
                        </ul>
                    <br>
                    Referensi: <a href='https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiQm8a_gZmGAxWge2wGHaEEA3AQFnoECDIQAQ&url=https%3A%2F%2Fdisdik.bekasikota.go.id%2Fdownload%2Ffile%2FRenstra_Disdik_2019.pdf&usg=AOvVaw0sbx6EM3NHPvLaKTtKYyVs&cshid=1716097817019113&opi=89978449'>Rencana Strategis Dinas Pendidikan Kota Bekasi Tahun 2018 - 2023</a> <br>
                    </div>
                """, unsafe_allow_html=True)
                enter()
                
        if selected_feature == 'Indeks Pengeluaran':
            with st.expander('Insight', expanded=True):                
                st.markdown("""
                    <div style='font-size:16px'>
                        Persentase angka kemiskinan Kabupaten/Kota Tasikmalaya sebenarnya telah menunjukkan penurunan dari tahun sebelumnya. <br>
                        Pada saat ini Kabupaten/ Kota Tasikmalaya merupakan Kabupaten/ Kota termiskin dari 27 kabupaten/kota se-Jawa Barat di urutan pertengahan. <br>
                        Namun hal yang bisa dilakukan agar keluar dari jurang kemiskinan salah satunya adalah peran penting para pemuda agar jangan sampai menjadi penyumbang pengangguran tetapi harus mau berwirausaha <br> <br>
                    
                    Referensi: <a href='https://radartasik.id/kemiskinan-kabupaten-tasikmalaya-tembus-1073-persen/'>Biaya Hidup di Bekasi Capai Rp 14,34 Juta</a> <br>
                    </div>
                """, unsafe_allow_html=True)
                enter()
                
        if ((selected_feature == 'Indeks Kedalaman Kemiskinan') or (selected_feature == 'Indeks Keparahan Kemiskinan')):
            with st.expander('Insight', expanded=True):                
                st.markdown("""
                    <div style='font-size:16px'>
                        Indeks pengeluaran di Kota Bekasi tahun 2022 merupakan indeks tertinggi di Provinsi Jawa Barat. <br>
                        Pada tahun 2022, UMK Kabupaten Bekasi ditetapkan sebesar Rp4.791.844. <br>
                        Deputi Bidang Statistik Distribusi dan Jasa BPS menyatakan bahwa nilai konsumsi SBH (Survei Biaya Hidup) di Kota Bekasi sebesar Rp 14,34 juta per bulan.  <br>
                        Hal tersebut terjadi, karena biaya hidup pada Kota Bekasi yang tinggi dan menjadikannya sebagai kota dengan nilai konsumsi/pengeluaran tertinggi di Jawa Barat <br> <br>

                    Referensi: <a href='https://katadata.co.id/finansial/makro/6578ed58b1347/biaya-hidup-di-bekasi-capai-rp-14-34-juta-termahal-setelah-jakarta'>Biaya Hidup di Bekasi Capai Rp 14,34 Juta</a> <br>
                    </div>
                """, unsafe_allow_html=True)
                enter()
                
                        
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

    # Agregasi mean untuk nilai sesuai kategori dan tahun
    df = df.groupby(['Kategori', 'Tahun'])['Value'].mean().round(2).reset_index()

    df_bar = df[df['Kategori'] == 'Usia Harapan Hidup']

    df_line = df[(df['Kategori'] == 'Rata Rata Lama Sekolah') | (df['Kategori'] == 'Harapan Lama Sekolah')]

    data_series = []

    data_series.append({
        "name": 'Usia Harapan Hidup',
        "type": "bar",
        "barGap": 0,
        "data": list(df_bar['Value']),
        "yAxisIndex": 0,
        "emphasis": {"focus": "series"},
        "label": {"show": False},
        "barWidth": 100,
    })

    for kategori, group in df_line.groupby('Kategori'):
        data_series.append({
            "name": kategori,
            "type": "line",
            "data": list(group['Value']),
            "yAxisIndex": 1,
            "emphasis": {"focus": "series"},
            "lineStyle": {"width": 4},
            "label": {"show": False},
            "symbolSize": 8,
        })

    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "xAxis": [{"type": "category", "axisTick": {"show": False}, "data": df_line['Tahun'].unique().tolist(),
                "axisLabel": {"fontSize": 14, "color": "white"}}],
        "yAxis": [
            {"type": "value", "name": "Usia Harapan Hidup", "position": "left",
            "axisLabel": {"fontSize": 14, "color": "white"}, "max": 100, "interval":25,
            "nameTextStyle": {"color": "white"}},
            {"type": "value", "name": "Lama Sekolah", "position": "right",
            "axisLabel": {"fontSize": 14, "color": "white"}, "max":20, "interval":5,
            "nameTextStyle": {"color": "white"}}
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
                <b>Trend & Jumlah IHK (2020-2024)</b>
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
            df['Bulan_Tahun'] = pd.to_datetime(df['Bulan_Tahun'], format='%B-%Y')

            # Mengurutkan DataFrame berdasarkan Bulan_Tahun
            df = df.sort_values(by='Bulan_Tahun')

            # Mengubah Bulan_Tahun kembali menjadi string
            df['Bulan_Tahun'] = df['Bulan_Tahun'].dt.strftime('%Y-%m-%d')

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
                        "max": 130,
                        "min": 95,
                        "axisLabel": {"fontSize": 12, "color": "white"}
                        },
                "series": [],
            }

            # data series untuk setiap kategori
            for category in categories:
                category_data = grouped_data.get_group(category)
                # Menghitung rata-rata nilai IHK untuk setiap bulan
                category_data_mean = category_data.groupby('Bulan_Tahun')['IHK Value'].mean().round(2).reset_index()
                series_data = {"name": category, "type": "line", "data": category_data_mean['IHK Value'].tolist(), "smooth": True}
                echart_config["series"].append(series_data)

            st_echarts(echart_config, height="600px")
            
        with st.expander('Insight', expanded=True):
            st.markdown("""
                <div style='font-size:16px'>
                    <ul>
                        <li>
                            Pada dashboard grafik sebelah kiri, terdapat salah satu hal yang menarik untuk dibahas yaitu terdapat <span style='color: #FFBD32;'>penurunan tajam trend IHK yaitu pada rentang waktu sekitar Desember 2023.</span> <br>
                            Hal ini ada kaitannya dengan hasil pemantauan BPS di tujuh kota di Jabar pada Desember 2023 terjadi inflasi yoy sebesar 2.48% atau 
                            <span style='color: #FFBD32;'>terjadi kenaikan Indeks Harga Konsumen (IHK) dari 115.11 pada Desember 2022 menjadi 117.96 di Desember 2023 </span>.
                        </li>
                        <li>
                            Jika dilihat berdasar kelompok pengeluarannya, 
                            <span style='color: #FFBD32;'>penyumbang inflasi secara tahunan terbesar adalah makanan, minuman dan tembakau yang mengalami inflasi sebesar 6.47%</span> dan 
                            <span style='color: #FFBD32;'>memberi andil sebesar 1.6% pada inflasi tahunan</span>, 
                            dengan komoditas yang memberikan andil terbesar pada kelompok ini adalah 
                            <span style='color: #FFBD32;'>beras (0.49%), cabai merah (0.28%), dan rokok kretek, filter, (0.17%)</span>.
                        </li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
                  
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
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique(), default=['Bandung', 'Bekasi', 'Cianjur'])
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
                    maxValue=100,  # Set maximum value for the radar chart axes
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
                     Pendapatan Kota Bandung bergantung pada bisnis fashion, wisata, kuliner, perdagangan, desain, dan lain-lain. 
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
                        'color': '#CCCCCC',
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
                        'color': '#CCCCCC',
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
        