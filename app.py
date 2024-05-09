import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header
from streamlit_elements import elements, mui, nivo
from streamlit_echarts import st_echarts
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

    # logo_link('', r'img\logo-jabar.png', 125)
    enter()
    horizontal_line()

    selected = option_menu(menu_title=None, 
                          options=["Home", 'IPM per Kategori', 'Trend IHK Kategori', 'Radar Chart (Nivo)', 'Data Preview'], 
                          icons=['house'], 
                          menu_icon="cast", default_index=0
                        )
    
    horizontal_line()
    
    st.header('Popux Box (Information)')

    
if selected == 'Home':
    colored_header(
        label="Kemiskinan di Jawa Barat (General)",
        description="",
        color_name="orange-70",
    )
    
    enter()
    
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b> Metrics Year 2022 vs 2021</b>
        </div>
    """, unsafe_allow_html=True)   
    
    enter()
     
    df = pd.read_csv(r'data\csv\df_metrics.csv')
    
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
    
    horizontal_line()
    
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b>
            Judul ...
            </b>
        </div>
    """, unsafe_allow_html=True)   
    
    enter()
     
    _, col_filter_wilayah, col_filter_features, _ = st.columns([1,3,3,1])
    
    with col_filter_wilayah:
        selected_regions = st.multiselect('Select Regions', df['Wilayah Jawa Barat'].unique(), default=['Kota Bandung', 'Bandung'])
        filtered_df = df[df['Wilayah Jawa Barat'].isin(selected_regions)]

    # with col_filter_year:
    #     selected_year = st.slider("Select a range of years",
    #                        2017, 2022, (2017, 2022))
    #     filtered_df = filtered_df[(df['Tahun'] >= selected_year[0]) & (df['Tahun'] <= selected_year[1])]
    
    with col_filter_features:
        selected_features_columns = st.multiselect('Select features for line chart', 
                                            ['Indeks Kesehatan', 'Indeks Pembangunan Manusia','Indeks Pendidikan', 'Indeks Pengeluaran', 'Indeks Kedalaman Kemiskinan', 'Indeks Keparahan Kemiskinan'], 
                                            default=['Indeks Kesehatan', 'Indeks Pembangunan Manusia','Indeks Pendidikan', 'Indeks Pengeluaran',])

    # Filter year from 2017 to 2023
    filtered_df = filtered_df[~filtered_df['Tahun'].isin([2015,2016,2023])]
    
    # Remove duplicate values from 'Tahun' column
    filtered_df = filtered_df.drop_duplicates(subset=['Tahun'])
    x_axis_data = filtered_df['Tahun'].tolist()

    # Generate series for line chart
    line_series = []
    for column in selected_features_columns:
        series_data = {
            "name": column,
            "type": "line",
            "yAxisIndex": 1,
            "data": filtered_df[column].values.tolist(),
            "lineStyle": {"width": 4},
            "symbolSize": 8,
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
            "data": ["Jumlah Penduduk Miskin", "Indeks Kesehatan", "Indeks Pembangunan Manusia", "Indeks Pendidikan", "Indeks Pengeluaran", "Indeks Kedalaman Kemiskinan", "Indeks Keparahan Kemiskinan"],
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
                "max": 300,
                "interval": 50,
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
                "data": filtered_df['Jumlah Penduduk Miskin'].values.tolist(),
            },
            *line_series  # Menambahkan series untuk line chart
        ],
    }

    st_echarts(options, height="400px")    
    
    horizontal_line()
    enter() 
    
    st.header('Judul ...')
    
    df = pd.read_csv(r'data\csv\df_metrics.csv')  
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
    
    
    
if selected == 'IPM per Kategori':  
    colored_header(
        label="My New Pretty Colored Header",
        description="",
        color_name="violet-70",
    )
               
if selected == 'Trend IHK Kategori':
    
    df = pd.read_csv(r'data\csv\Merged_IHK_Kelompok_Pengeluaran_2017_2024.csv')
    df['Bulan_Tahun'] = pd.to_datetime(df['Bulan_Tahun'], format='%B-%Y')
    df = df.sort_values('Bulan_Tahun', ascending=True).reset_index(drop=True)
    
    # Convert 'Bulan_Tahun' to datetime
    df['Bulan_Tahun'] = pd.to_datetime(df['Bulan_Tahun'])

    # Extract year from 'Bulan_Tahun'
    df['Year'] = df['Bulan_Tahun'].dt.year.astype(str)

    # Preprocess data
    xAxis_data = df['Year'].unique().tolist()
    series_data = []
    for kelompok in df['Kelompok Pengeluaran IHK'].unique():
        series_data.append({
            "name": kelompok,
            "type": "line",
            "data": df[df['Kelompok Pengeluaran IHK'] == kelompok].groupby('Year')['IHK Value'].mean().tolist()
        })

    # ECharts option
    option = {
        "title": {"text": "IHK Value by Year"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": df['Kelompok Pengeluaran IHK'].unique().tolist()},
        "xAxis": {"type": "category", "boundaryGap": False, "data": xAxis_data},
        "yAxis": {"type": "value"},
        "series": series_data
    }

    # Render ECharts
    st_echarts(options=option, height="500px")   
     
if selected == 'Radar Chart (Nivo)':
    df = pd.read_csv(r"data\csv\df_merge_idx.csv")
    df_jk = pd.read_csv(r'data\csv\Proporsi_JK_Pekerja_Formal_Informal_2018_2023.csv')
    df_tipe_daerah = pd.read_csv(r'data\csv\Proporsi_Daerah_Pekerja_Formal_Informal_2018_2023.csv')

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
    
    
    col_pie_jk, col_pie_tipe_daerah = st.columns(2)
    
    with col_pie_jk:
        
        formal_pria_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Laki-laki']['Proporsi Formal (%)'].values[0]
        informal_pria_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Laki-laki']['Proporsi Informal (%)'].values[0]
        formal_perempuan_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Perempuan']['Proporsi Formal (%)'].values[0]
        informal_perempuan_value = filtered_df_jk[filtered_df_jk['Jenis Kelamin'] == 'Perempuan']['Proporsi Informal (%)'].values[0]
        
        options_pie_jk = {
            "tooltip": {"trigger": "item"},
            "legend": {"top": "5%", "left": "center"},
            "series": [
                    {
                        "name": "Jenis Kelamin",
                        "type": "pie",
                        "radius": ["40%", "70%"],
                        "avoidLabelOverlap": False,
                        "itemStyle": {
                            "borderRadius": 10,
                            "borderColor": "#fff",
                            "borderWidth": 2,
                        },
                        "label": {"show": False, "position": "center"},
                        "emphasis": {
                            "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
                        },
                        "labelLine": {"show": False},
                        "data": [
                            {"value": formal_pria_value, "name": "Formal Pria"},
                            {"value": informal_pria_value, "name": "Informal Pria"},
                            {"value": formal_perempuan_value, "name": "Formal Wanita"},
                            {"value": informal_perempuan_value, "name": "Informal Wanita"},
                        ],
                    }
                ],
            }
        
        st_echarts(
            options=options_pie_jk, height="500px",
        )
        
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
            
    with col_pie_tipe_daerah:
        
        formal_perkotaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perkotaan']['Proporsi Formal (%)'].values[0]
        informal_perkotaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perkotaan']['Proporsi Informal (%)'].values[0]
        formal_perdesaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perdesaan']['Proporsi Formal (%)'].values[0]
        informal_perdesaan_value = filtered_df_tipe_daerah[filtered_df_tipe_daerah['Tipe Daerah'] == 'Perdesaan']['Proporsi Informal (%)'].values[0]

        options_pie_jk = {
            "tooltip": {"trigger": "item"},
            "legend": {"top": "5%", "left": "center"},
            "series": [
                    {
                        "name": "Jenis Kelamin",
                        "type": "pie",
                        "radius": ["40%", "70%"],
                        "avoidLabelOverlap": False,
                        "itemStyle": {
                            "borderRadius": 10,
                            "borderColor": "#fff",
                            "borderWidth": 2,
                        },
                        "label": {"show": False, "position": "center"},
                        "emphasis": {
                            "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
                        },
                        "labelLine": {"show": False},
                        "data": [
                            {"value": formal_perkotaan_value, "name": "Perkotaan (Formal)"},
                            {"value": informal_perkotaan_value, "name": "Perkotaan (Informal)"},
                            {"value": formal_perdesaan_value, "name": "Pedesaan (Formal)", 'itemStyle': {'color': '#712622'}},
                            {"value": informal_perdesaan_value, "name": "Pedesaan (Informal)", 'itemStyle': {'color': '#712622'}},
                        ],
                    }
                ],
            }
        
        st_echarts(
            options=options_pie_jk, height="500px",
        )
        
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
        
if selected == 'Data Preview':
    
    df = pd.read_csv(r'data\csv\Merged_IHK_Kelompok_Pengeluaran_2017_2024.csv')  

                
    # option = {
    #     "title": {
    #         "text": "Male and female height and weight distribution",
    #         "subtext": "Data from: Heinz 2003",
    #     },
    #     "grid": {
    #         "left": "3%",
    #         "right": "7%",
    #         "bottom": "7%",
    #         "containLabel": True,
    #     },
    #     "tooltip": {
    #         "trigger": "axis",
    #         "showDelay": 0,
            
    #     },
    #     "toolbox": {
    #         "feature": {
    #             "dataZoom": {},
    #             "brush": {"type": ["rect", "polygon", "clear"]},
    #         }
    #     },
    #     "brush": {},
    #     "legend": {"data": ["Female", "Male"], "left": "center", "bottom": 10},
    #     "xAxis": [
    #         {
    #             "type": "value",
    #             "scale": True,
    #             "axisLabel": {"formatter": "{value} cm"},
    #             "splitLine": {"show": False},
    #         }
    #     ],
    #     "yAxis": [
    #         {
    #             "type": "value",
    #             "scale": True,
    #             "axisLabel": {"formatter": "{value} kg"},
    #             "splitLine": {"show": False},
    #         }
    #     ],
    #     "series": [
    #         {
    #             "name": "Female",
    #             "type": "scatter",
    #             "emphasis": {"focus": "series"},
    #             "data": [
    #                 [161.2, 51.6],
    #                 [167.5, 59.0],
    #                 # Add more data points here...
    #             ],
    #             "markArea": {
    #                 "silent": True,
    #                 "itemStyle": {
    #                     "color": "transparent",
    #                     "borderWidth": 1,
    #                     "borderType": "dashed",
    #                 },
    #                 "data": [
    #                     [
    #                         {"name": "Female Data Range", "xAxis": "min", "yAxis": "min"},
    #                         {"xAxis": "max", "yAxis": "max"},
    #                     ]
    #                 ],
    #             },
    #             "markPoint": {"data": [{"type": "max", "name": "Max"}, {"type": "min", "name": "Min"}]},
    #             "markLine": {"lineStyle": {"type": "solid"}, "data": [{"type": "average", "name": "AVG"}, {"xAxis": 160}]},
    #         },
    #         {
    #             "name": "Male",
    #             "type": "scatter",
    #             "emphasis": {"focus": "series"},
    #             "data": [
    #                 [174.0, 65.6],
    #                 [175.3, 71.8],
    #                 # Add more data points here...
    #             ],
    #             "markArea": {
    #                 "silent": True,
    #                 "itemStyle": {
    #                     "color": "transparent",
    #                     "borderWidth": 1,
    #                     "borderType": "dashed",
    #                 },
    #                 "data": [
    #                     [
    #                         {"name": "Male Data Range", "xAxis": "min", "yAxis": "min"},
    #                         {"xAxis": "max", "yAxis": "max"},
    #                     ]
    #                 ],
    #             },
    #             "markPoint": {"data": [{"type": "max", "name": "Max"}, {"type": "min", "name": "Min"}]},
    #             "markLine": {"lineStyle": {"type": "solid"}, "data": [{"type": "average", "name": "Average"}, {"xAxis": 170}]},
    #         },
    #     ],
    # }

    # st_echarts(options=option)