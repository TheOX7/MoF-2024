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
            Kemiskinan Jawa Barat <br> 2017-2023
            </b>
        </div>
    """, unsafe_allow_html=True)
    
    enter()

    logo_link('', r'img/logo-jabar.png', 125)
    enter()
    horizontal_line()

    selected = option_menu(menu_title=None, 
                          options=["Home", 'IPM', 'Trend IHK', 'Radar Chart (Nivo)'], 
                          icons=['house'], 
                          menu_icon="cast", default_index=0
                        )
    
    horizontal_line()
    
    st.header('Popux Box (Information)')

    
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
        idx_before = df[df['Tahun'] == 2021]['Jumlah Penduduk Miskin'].mean()
        idx_latest = df[df['Tahun'] == 2022]['Jumlah Penduduk Miskin'].mean()
        delta_idx = idx_latest - idx_before
        metric_idx_penduduk.metric(label="Jumlah Penduduk Miskin (Ribu)", value=round(idx_latest, 2), delta=round(delta_idx, 2))

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
            <b>Judul ... </b>
        </div>
    """, unsafe_allow_html=True)   
    horizontal_line()
              
    # Load dataset
    df = pd.read_csv(r'data/csv/metrics.csv')

    _, col_filter_wilayah, col_filter_features, _ = st.columns([1, 7, 7, 1])

    with col_filter_wilayah:
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique())
        filtered_df = df[df['Wilayah Jawa Barat'].isin(selected_regions)]
        filtered_df = filtered_df[~filtered_df['Tahun'].isin([2015, 2016, 2023])]

    # Calculate "Jumlah Penduduk Miskin" mean for selected regions
    mean_penduduk_miskin = [round(value, 2) for value in filtered_df.groupby('Tahun')['Jumlah Penduduk Miskin'].mean().tolist()]

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
                "max": 500,
                "interval": 100,
                "axisLabel": {"formatter": "{value} Jiwa", "color": "white"},
                "nameTextStyle": {
                    "color": "white",
                    "fontWeight": "bolder",
                    "align": "right"
                },
                "axisTick": {
                    "alignWithLabel": True
                },
                "splitLine": {"show": True}
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
                "data": mean_penduduk_miskin,
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
            <b>Judul ... </b>
        </div>
    """, unsafe_allow_html=True)   
    horizontal_line()

    
    df = pd.read_csv(r'data/csv/metrics.csv')  
    df.drop(['Tingkat Angkatan Kerja (%)', 'Tingkat Pengangguran (%)', 'Jumlah Penduduk Miskin'], inplace=True, axis=1)
    df.columns = df.columns.str.replace(' ', '_')
    df = df[df['Tahun'] == 2022]
        
    cellStyle = JsCode(
        r"""
        function(params) {
            var style = {};
            if (params.colDef.field == 'Indeks_Pendidikan') {
                if (params.value > 80) {
                    style['background-color'] = 'green';
                } else if (params.value < 60) {
                    style['background-color'] = 'red';
                }
            } else if (params.colDef.field == 'Indeks_Kesehatan') {
                if (params.value > 80) {
                    style['background-color'] = 'green';
                } else if (params.value < 50) {
                    style['background-color'] = 'red';
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
    
    enter()
        
if selected == 'IPM':  
    # colored_header(
    #     label="My New Pretty Colored Header",
    #     description="",
    #     color_name="violet-70",
    # )
    
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:30px'>
            <b>IPM per Komponen (2017 - 2023)</b>
        </div>
    """, unsafe_allow_html=True)  
    horizontal_line()
    
       
    df = pd.read_csv('data/csv/IPM_Menurut_Komponen_2015_2023.csv')
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
                  
if selected == 'Radar Chart (Nivo)':
    df = pd.read_csv(r"data/csv/df_merge_idx.csv")
    df_jk = pd.read_csv(r'data/csv/Proporsi_JK_Pekerja_Formal_Informal_2018_2023.csv')
    df_tipe_daerah = pd.read_csv(r'data/csv/Proporsi_Daerah_Pekerja_Formal_Informal_2018_2023.csv')

    colored_header(
        label="Regions Index Value per Year (Radar Chart)",
        description="",
        color_name="orange-70",
    )
    
    enter()
    
    col_filter_wilayah, col_filter_year = st.columns(2)
    
    with col_filter_wilayah:
        # Filter by region
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique(), default=['Bandung', 'Garut', 'Tasikmalaya'])
        filtered_df = df[df['Wilayah Jawa Barat'].isin(selected_regions)]

    with col_filter_year:
        # Filter by year
        selected_year = st.selectbox('Select Year', filtered_df['Tahun'].unique(), index=1)
        filtered_df = filtered_df[filtered_df['Tahun'] == selected_year]
        filtered_df_jk = df_jk[df_jk['Tahun'] == selected_year]
        filtered_df_tipe_daerah = df_tipe_daerah[df_tipe_daerah['Tahun'] == selected_year]
        
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
        with st.expander('Explanation', expanded=True):
            st.subheader('_Streamlit_ is :blue[cool]')
        
        # st.write(f"This is :blue[{selected_year}]")    
        # st.write(f"This is :blue[test]")    


    colored_header(
        label="Proposi Jenis Pekerja Berdasarkan Jenis Kelamin",
        description="",
        color_name="orange-70",
    )
    
    enter()
    
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
        
        with st.expander('Insights'):
            st.write('')
            
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
        
        with st.expander('Insights'):
            st.write('')
        
# if selected == 'Data Preview':        
#     option = {
#         "title": {
#             "text": "Male and female height and weight distribution",
#             "subtext": "Data from: Heinz 2003"
#         },
#         "grid": {
#             "left": "3%",
#             "right": "7%",
#             "bottom": "7%",
#             "containLabel": True
#         },
#         "tooltip": {
#             "showDelay": 0,
#             "formatter": 
#                 streamlit_echarts.JsCode(
#                 "function (params) {if (params.value.length > 1) {return (params.seriesName +' :<br/>' + params.value[0] + 'cm ' + params.value[1] + 'kg ');} else { return (params.seriesName +' :<br/>' + params.name + ' : ' + params.value +'kg ');}}"     
#                 ).js_code,
#             "axisPointer": {
#                 "show": True,
#                 "type": "cross",
#                 "lineStyle": {
#                     "type": "dashed",
#                     "width": 1
#                 }
#             }
#         },
#         "toolbox": {
#             "feature": {
#                 "dataZoom": {},
#                 "brush": {
#                     "type": ["rect", "polygon", "clear"]
#                 }
#             }
#         },
#         "brush": {},
#         "legend": {
#             "data": ["Female", "Male"],
#             "left": "center",
#             "bottom": 10
#         },
#         "xAxis": [
#             {
#                 "type": "value",
#                 "scale": True,
#                 "axisLabel": {
#                     "formatter": "{value} cm"
#                 },
#                 "splitLine": {
#                     "show": False
#                 }
#             }
#         ],
#         "yAxis": [
#             {
#                 "type": "value",
#                 "scale": True,
#                 "axisLabel": {
#                     "formatter": "{value} kg"
#                 },
#                 "splitLine": {
#                     "show": False
#                 }
#             }
#         ],
#         "series": [
#             {
#                 "name": "Female",
#                 "type": "scatter",
#                 "emphasis": {
#                     "focus": "series"
#                 },
#                 "data": [
#                     [161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6],
#                     [170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2],
#                     [172.5, 55.2], [170.9, 54.2], [172.9, 62.5], [153.4, 42.0], [160.0, 50.0],
#                     [147.2, 49.8], [168.2, 49.2], [175.0, 73.2], [157.0, 47.8], [167.6, 68.8],
#                     [159.5, 50.6], [175.0, 82.5], [166.8, 57.2], [176.5, 87.8], [170.2, 72.8],
#                     [174.0, 54.5], [173.0, 59.8], [179.9, 67.3], [170.5, 67.8], [160.0, 47.0],
#                 ],
#                 "markArea": {
#                     "silent": True,
#                     "itemStyle": {
#                         "color": "transparent",
#                         "borderWidth": 1,
#                         "borderType": "dashed"
#                     },
#                     "data": [
#                         [
#                             {
#                                 "name": "Female Data Range",
#                                 "xAxis": "min",
#                                 "yAxis": "min"
#                             },
#                             {
#                                 "xAxis": "max",
#                                 "yAxis": "max"
#                             }
#                         ]
#                     ]
#                 },
#                 "markPoint": {
#                     "data": [
#                         {"type": "max", "name": "Max"},
#                         {"type": "min", "name": "Min"}
#                     ]
#                 },
#                 "markLine": {
#                     "lineStyle": {
#                         "type": "solid"
#                     },
#                     "data": [{"type": "average", "name": "AVG"}, {"xAxis": 160}]
#                 }
#             },
#             {
#                 "name": "Male",
#                 "type": "scatter",
#                 "emphasis": {
#                     "focus": "series"
#                 },
#                 "data": [
#                     [174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6], [187.2, 78.8],
#                     [181.5, 74.8], [184.0, 86.4], [184.5, 78.4], [175.0, 62.0], [184.0, 81.6],
#                     [180.0, 76.6], [177.8, 83.6], [192.0, 90.0], [176.0, 74.6], [174.0, 71.0],
#                     [184.0, 79.6], [192.7, 93.8], [171.5, 70.0], [173.0, 72.4], [176.0, 85.9],
#                     [176.0, 78.8], [180.5, 77.8], [172.7, 66.2], [176.0, 86.4], [173.5, 81.8],
#                     [178.0, 89.6], [180.3, 82.8], [180.3, 76.4], [164.5, 63.2], [173.0, 60.9],
#                 ],
#                 "markArea": {
#                     "silent": True,
#                     "itemStyle": {
#                         "color": "transparent",
#                         "borderWidth": 1,
#                         "borderType": "dashed"
#                     },
#                     "data": [
#                         [
#                             {
#                                 "name": "Male Data Range",
#                                 "xAxis": "min",
#                                 "yAxis": "min"
#                             },
#                             {
#                                 "xAxis": "max",
#                                 "yAxis": "max"
#                             }
#                         ]
#                     ]
#                 },
#                 "markPoint": {
#                     "data": [
#                         {"type": "max", "name": "Max"},
#                         {"type": "min", "name": "Min"}
#                     ]
#                 },
#                 "markLine": {
#                     "lineStyle": {
#                         "type": "solid"
#                     },
#                     "data": [{"type": "average", "name": "Average"}, {"xAxis": 170}]
#                 }
#             }
#         ]
#     }
    
#     st_echarts(options=option, height="600px")
        
#     enter()
